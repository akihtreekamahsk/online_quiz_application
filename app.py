import streamlit as st
import sqlite3
import hashlib
import secrets
import os
import random
import uuid
import time
import io
import html
import pandas as pd
import matplotlib.pyplot as plt

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from streamlit_autorefresh import st_autorefresh

from quiz_data import QUIZ_DATA


# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Online Quiz Application",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Online Quiz Application")
st.markdown(
    "<h4 style='text-align:center; color:gray;'>Welcome to your Quiz Dashboard!</h4>",
    unsafe_allow_html=True
)
st.divider()
st.caption("Test your knowledge and improve your skills!")


# ---------------- DATABASE ----------------

os.makedirs("data", exist_ok=True)
DB_PATH = "data/quiz.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            subject TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            percentage REAL NOT NULL,
            date TEXT NOT NULL
        )
    """)

    con.commit()
    con.close()


initialize_database()


# ---------------- PASSWORD SECURITY ----------------

def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        200000
    ).hex()

    return salt + "$" + password_hash


def verify_password(password, stored_password):
    try:
        salt, saved_hash = stored_password.split("$")

        entered_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            salt.encode(),
            200000
        ).hex()

        return secrets.compare_digest(
            entered_hash,
            saved_hash
        )
    except ValueError:
        return False


# ---------------- SESSION STATE ----------------

defaults = {
    "logged_in": False,
    "username": "",
    "quiz_active": False,
    "quiz_questions": [],
    "quiz_answers": {},
    "quiz_subject": "",
    "quiz_difficulty": "",
    "quiz_id": "",
    "quiz_end_time": 0,
    "quiz_result": None,
    "result_saved": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ---------------- REGISTRATION ----------------

def register_user(username, password):
    con = get_connection()

    try:
        con.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hash_password(password))
        )
        con.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        con.close()


# ---------------- LOGIN ----------------

def login_user(username, password):
    con = get_connection()

    row = con.execute(
        "SELECT password FROM users WHERE username = ?",
        (username,)
    ).fetchone()

    con.close()

    if row and verify_password(password, row[0]):
        st.session_state.logged_in = True
        st.session_state.username = username
        return True

    return False


# ---------------- SAVE QUIZ RESULT ----------------

def save_result(score, total):
    percentage = (score / total) * 100 if total else 0

    con = get_connection()

    con.execute("""
        INSERT INTO results
        (username, subject, difficulty, score, total, percentage, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        st.session_state.username,
        st.session_state.quiz_subject,
        st.session_state.quiz_difficulty,
        score,
        total,
        percentage,
        time.strftime("%Y-%m-%d %H:%M")
    ))

    con.commit()
    con.close()


# ---------------- FINISH QUIZ ----------------

def finish_quiz():
    if st.session_state.result_saved:
        return

    questions = st.session_state.quiz_questions
    answers = st.session_state.quiz_answers

    score = 0

    for i, question in enumerate(questions):
        if answers.get(i) == question["answer"]:
            score += 1

    total = len(questions)
    percentage = (score / total) * 100 if total else 0

    st.session_state.quiz_result = {
        "score": score,
        "total": total,
        "percentage": percentage
    }

    save_result(score, total)

    st.session_state.result_saved = True
    st.session_state.quiz_active = False


# ---------------- PDF REPORT ----------------

def create_pdf():
    result = st.session_state.quiz_result

    buffer = io.BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4
    )

    styles = getSampleStyleSheet()
    content = []

    content.append(
        Paragraph("Online Quiz Application - Result", styles["Title"])
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Student: " + html.escape(st.session_state.username),
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "Subject: " + html.escape(st.session_state.quiz_subject),
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "Difficulty: " + html.escape(st.session_state.quiz_difficulty),
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            f"Score: {result['score']} / {result['total']}",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Percentage: {result['percentage']:.2f}%",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            "Thank you for attending the quiz!",
            styles["Normal"]
        )
    )

    document.build(content)

    buffer.seek(0)
    return buffer


# ---------------- LOGIN AND REGISTER PAGE ----------------

if not st.session_state.logged_in:

    st.subheader("Welcome!")

    login_tab, register_tab = st.tabs(
        ["Login", "Register"]
    )

    with login_tab:
        st.subheader("Student Login")

        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input(
                "Password",
                type="password"
            )

            login_button = st.form_submit_button(
                "Login",
                use_container_width=True
            )

        if login_button:
            if login_user(username.strip(), password):
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

    with register_tab:
        st.subheader("Create an Account")

        with st.form("register_form"):
            new_username = st.text_input("Choose a username")
            new_password = st.text_input(
                "Choose a password",
                type="password"
            )
            confirm_password = st.text_input(
                "Confirm password",
                type="password"
            )

            register_button = st.form_submit_button(
                "Register",
                use_container_width=True
            )

        if register_button:
            if not new_username.strip() or not new_password:
                st.warning("Please fill in all fields.")

            elif len(new_password) < 6:
                st.warning("Password must contain at least 6 characters.")

            elif new_password != confirm_password:
                st.error("Passwords do not match.")

            elif register_user(new_username.strip(), new_password):
                st.success("Registration successful! Please log in.")

            else:
                st.error("Username already exists. Choose another.")

    st.stop()


# ---------------- SIDEBAR NAVIGATION ----------------

st.sidebar.title("🎓 Student Dashboard")

st.sidebar.write(
    "Welcome, " + st.session_state.username
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Start Quiz",
        "My Results",
        "Leaderboard"
    ]
)

if st.sidebar.button("Logout", use_container_width=True):
    for key in defaults:
        st.session_state[key] = defaults[key]

    st.rerun()


# ---------------- HOME PAGE ----------------

if page == "Home":

    st.header("Welcome to your Quiz Dashboard")

    st.write(
        "Choose a subject, select your difficulty level, "
        "and test your knowledge."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Subjects", "3")
    col2.metric("Difficulty Levels", "3")
    col3.metric("Question Types", "MCQ")

    st.divider()

    st.subheader("Available Subjects")

    col1, col2, col3 = st.columns(3)

    col1.info("🐍 Python")
    col2.info("💻 Computer Science")
    col3.info("🤖 AIML")

    st.subheader("How to use the application")

    st.write("""
    1. Open Start Quiz.
    2. Select your subject.
    3. Select your difficulty level.
    4. Answer the questions before time runs out.
    5. Submit and view your result.
    6. Download your PDF report.
    """)


# ---------------- START QUIZ PAGE ----------------

elif page == "Start Quiz":

    st.header("Start Your Quiz")

    if not st.session_state.quiz_active and st.session_state.quiz_result is None:

        subject = st.selectbox(
            "Select Subject",
            list(QUIZ_DATA.keys())
        )

        difficulty = st.selectbox(
            "Select Difficulty",
            ["Easy", "Medium", "Hard"]
        )

        available_questions = QUIZ_DATA[subject][difficulty]

        st.write(
            f"Available questions: {len(available_questions)}"
        )

        if st.button("Start Quiz", type="primary"):

            questions = random.sample(
                available_questions,
                k=min(10, len(available_questions))
            )

            st.session_state.quiz_questions = questions
            st.session_state.quiz_answers = {}
            st.session_state.quiz_subject = subject
            st.session_state.quiz_difficulty = difficulty
            st.session_state.quiz_id = str(uuid.uuid4())
            st.session_state.quiz_end_time = time.time() + 900
            st.session_state.quiz_active = True
            st.session_state.quiz_result = None
            st.session_state.result_saved = False

            st.rerun()

    # -------- ACTIVE QUIZ --------

    if st.session_state.quiz_active:

        st_autorefresh(
            interval=1000,
            key="quiz_timer_" + st.session_state.quiz_id
        )

        remaining = max(
            0,
            int(st.session_state.quiz_end_time - time.time())
        )

        minutes, seconds = divmod(remaining, 60)

        st.warning(
            f"⏳ Time remaining: {minutes:02d}:{seconds:02d}"
        )

        if remaining <= 0:
            finish_quiz()
            st.warning("Time is up! Your quiz has been submitted.")
            st.rerun()

        questions = st.session_state.quiz_questions

        st.write(
            f"Subject: {st.session_state.quiz_subject}"
        )

        st.write(
            f"Difficulty: {st.session_state.quiz_difficulty}"
        )

        st.progress(
            len(st.session_state.quiz_answers) / len(questions)
        )

        for i, question in enumerate(questions):

            st.subheader(
                f"Question {i + 1}: {question['question']}"
            )

            selected = st.radio(
                "Choose your answer:",
                question["options"],
                index=None,
                key=f"answer_{st.session_state.quiz_id}_{i}"
            )

            if selected is not None:
                st.session_state.quiz_answers[i] = selected

            st.divider()

        if st.button("Submit Quiz", type="primary"):

            finish_quiz()
            st.rerun()


# ---------------- RESULT PAGE ----------------

    if st.session_state.quiz_result is not None:

        result = st.session_state.quiz_result

        st.success("Quiz completed successfully!")

        st.subheader("Your Quiz Result")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Score",
            f"{result['score']} / {result['total']}"
        )

        col2.metric(
            "Percentage",
            f"{result['percentage']:.2f}%"
        )

        col3.metric(
            "Correct Answers",
            result["score"]
        )

        st.subheader("Performance Analysis")

        correct = result["score"]
        incorrect = result["total"] - correct

        fig, ax = plt.subplots()

        ax.pie(
            [correct, incorrect],
            labels=["Correct", "Incorrect"],
            autopct="%1.1f%%",
            startangle=90
        )

        ax.set_title("Quiz Performance")

        st.pyplot(fig)
        plt.close(fig)

        st.subheader("Answer Review")

        for i, question in enumerate(st.session_state.quiz_questions):

            selected = st.session_state.quiz_answers.get(i)

            st.write(
                f"**Question {i + 1}: {question['question']}**"
            )

            st.write(
                "Your answer: " + (selected if selected else "Not answered")
            )

            st.write(
                "Correct answer: " + question["answer"]
            )

            if selected == question["answer"]:
                st.success("Correct answer!")
            else:
                st.error("Incorrect answer.")

            st.divider()

        pdf_file = create_pdf()

        st.download_button(
            "📄 Download PDF Result",
            data=pdf_file,
            file_name="Quiz_Result.pdf",
            mime="application/pdf"
        )

        if st.button("Take Another Quiz"):
            st.session_state.quiz_active = False
            st.session_state.quiz_result = None
            st.session_state.quiz_questions = []
            st.session_state.quiz_answers = {}
            st.session_state.result_saved = False
            st.rerun()


# ---------------- MY RESULTS PAGE ----------------

elif page == "My Results":

    st.header("My Quiz History")

    con = get_connection()

    history = pd.read_sql_query(
        """
        SELECT subject, difficulty, score, total,
               percentage, date
        FROM results
        WHERE username = ?
        ORDER BY id DESC
        """,
        con,
        params=(st.session_state.username,)
    )

    con.close()

    if history.empty:
        st.info("You have not completed any quizzes yet.")

    else:
        st.dataframe(
            history,
            use_container_width=True,
            hide_index=True
        )

        average = history["percentage"].mean()

        st.metric(
            "Average Performance",
            f"{average:.2f}%"
        )


# ---------------- LEADERBOARD PAGE ----------------

elif page == "Leaderboard":

    st.header("🏆 Student Leaderboard")

    con = get_connection()

    leaderboard = pd.read_sql_query(
        """
        SELECT username,
               COUNT(*) AS quizzes,
               MAX(percentage) AS best_percentage
        FROM results
        GROUP BY username
        ORDER BY best_percentage DESC, quizzes DESC
        """,
        con
    )

    con.close()

    if leaderboard.empty:
        st.info("No quiz results available yet.")

    else:
        leaderboard.index += 1

        st.dataframe(
            leaderboard,
            use_container_width=True
        )