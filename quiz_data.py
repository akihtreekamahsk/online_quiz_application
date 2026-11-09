# Complete question bank for Online Quiz Application

def make_question(question, options, answer):
    return {
        "question": question,
        "options": options,
        "answer": answer
    }


QUIZ_DATA = {
    "Python": {
        "Easy": [
            make_question("Which symbol starts a comment in Python?", ["//", "#", "/*", "--"], "#"),
            make_question("Which function displays output?", ["input()", "print()", "show()", "display()"], "print()"),
            make_question("Which data type stores True or False?", ["int", "str", "bool", "list"], "bool"),
            make_question("Which keyword defines a function?", ["function", "define", "def", "fun"], "def"),
            make_question("Which brackets create a list?", ["()", "{}", "[]", "<>"], "[]"),
            make_question("What is the result of 3 ** 2?", ["6", "8", "9", "5"], "9"),
            make_question("Which method adds an item to a list?", ["append()", "add_end()", "insert_last()", "push()"], "append()"),
            make_question("Which function reads user input?", ["scan()", "read()", "input()", "get()"], "input()"),
            make_question("Which value represents no value in Python?", ["0", "None", "False", "Empty"], "None"),
            make_question("Which extension is used for Python files?", [".pt", ".py", ".python", ".p"], ".py")
        ],

        "Medium": [
            make_question("What is the output of len('Python')?", ["5", "6", "7", "8"], "6"),
            make_question("Which collection does not allow duplicate values?", ["list", "tuple", "set", "string"], "set"),
            make_question("What does range(4) produce?", ["1 to 4", "0 to 4", "0 to 3", "1 to 3"], "0 to 3"),
            make_question("Which keyword handles an exception?", ["catch", "except", "error", "handle"], "except"),
            make_question("What is the result of 10 // 3?", ["3.33", "3", "1", "4"], "3"),
            make_question("Which method converts a string to lowercase?", ["lower()", "small()", "casefolding()", "down()"], "lower()"),
            make_question("What does a dictionary store?", ["Only values", "Key-value pairs", "Only keys", "Sorted numbers"], "Key-value pairs"),
            make_question("Which keyword is used to create a class?", ["object", "struct", "class", "type"], "class"),
            make_question("What is the output of bool([])?", ["True", "False", "None", "Error"], "False"),
            make_question("Which statement skips the current loop iteration?", ["stop", "exit", "continue", "pass"], "continue")
        ],

        "Hard": [
            make_question("What is the purpose of __init__ in a class?", ["Destroy an object", "Initialize an object", "Import a module", "Print an object"], "Initialize an object"),
            make_question("Which feature allows a function to call itself?", ["Iteration", "Recursion", "Inheritance", "Encapsulation"], "Recursion"),
            make_question("What does a decorator commonly do?", ["Deletes a function", "Modifies or extends function behavior", "Converts code to HTML", "Stops a loop"], "Modifies or extends function behavior"),
            make_question("Which keyword creates a generator value?", ["return", "yield", "generate", "next"], "yield"),
            make_question("What is the average lookup time of a dictionary by key?", ["O(1)", "O(n)", "O(n log n)", "O(n²)"], "O(1)"),
            make_question("What does the with statement commonly manage?", ["Conditional branches", "Context-managed resources", "Class inheritance", "Loops"], "Context-managed resources"),
            make_question("Which module supports regular expressions?", ["math", "re", "random", "sys"], "re"),
            make_question("What is method overriding?", ["Defining a method again in a subclass", "Deleting a method", "Calling a method twice", "Making a method private"], "Defining a method again in a subclass"),
            make_question("Which collection is immutable?", ["list", "set", "tuple", "dictionary"], "tuple"),
            make_question("What does the GIL in CPython primarily control?", ["Garbage collection", "Access to Python bytecode execution by threads", "Database access", "File permissions"], "Access to Python bytecode execution by threads")
        ]
    },

    "Computer Science": {
        "Easy": [
            make_question("What does CPU stand for?", ["Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Processing User"], "Central Processing Unit"),
            make_question("Which device is used to enter text?", ["Monitor", "Keyboard", "Speaker", "Printer"], "Keyboard"),
            make_question("Which is an operating system?", ["Python", "Linux", "HTML", "SQL"], "Linux"),
            make_question("What is the binary number system base?", ["2", "8", "10", "16"], "2"),
            make_question("Which memory is volatile?", ["ROM", "Hard disk", "RAM", "DVD"], "RAM"),
            make_question("What does URL stand for?", ["Uniform Resource Locator", "Universal Record Link", "User Reference Location", "Unified Resource Line"], "Uniform Resource Locator"),
            make_question("Which is an output device?", ["Mouse", "Scanner", "Monitor", "Keyboard"], "Monitor"),
            make_question("What does LAN stand for?", ["Local Area Network", "Large Access Node", "Long Area Number", "Linked Application Network"], "Local Area Network"),
            make_question("Which language is mainly used to structure web pages?", ["HTML", "SQL", "C", "Bash"], "HTML"),
            make_question("What is the full form of USB?", ["Universal Serial Bus", "United System Board", "Universal Storage Box", "User Service Bus"], "Universal Serial Bus")
        ],

        "Medium": [
            make_question("Which data structure follows FIFO?", ["Stack", "Queue", "Tree", "Graph"], "Queue"),
            make_question("Which data structure follows LIFO?", ["Queue", "Array", "Stack", "Linked list"], "Stack"),
            make_question("What is the time complexity of binary search on a sorted array?", ["O(n)", "O(log n)", "O(n²)", "O(1)"], "O(log n)"),
            make_question("Which SQL command retrieves records?", ["INSERT", "UPDATE", "SELECT", "DELETE"], "SELECT"),
            make_question("Which normal form removes partial dependency?", ["1NF", "2NF", "3NF", "BCNF"], "2NF"),
            make_question("Which protocol is commonly used for secure web browsing?", ["HTTP", "FTP", "HTTPS", "SMTP"], "HTTPS"),
            make_question("What is a primary key?", ["A duplicate field", "A field that uniquely identifies a row", "A nullable description", "A backup table"], "A field that uniquely identifies a row"),
            make_question("Which algorithm design technique solves overlapping subproblems?", ["Dynamic programming", "Bubble sort", "Linear search", "Hashing"], "Dynamic programming"),
            make_question("Which layer of the OSI model handles routing?", ["Physical", "Data Link", "Network", "Presentation"], "Network"),
            make_question("What is a deadlock in an operating system?", ["A process finishes", "Processes wait indefinitely for resources", "A file is deleted", "The CPU speeds up"], "Processes wait indefinitely for resources")
        ],

        "Hard": [
            make_question("What is the worst-case time complexity of quicksort?", ["O(log n)", "O(n)", "O(n log n)", "O(n²)"], "O(n²)"),
            make_question("Which CAP property means every read receives the most recent write?", ["Consistency", "Availability", "Partition tolerance", "Durability"], "Consistency"),
            make_question("Which scheduling algorithm may cause starvation?", ["Round Robin", "First Come First Served", "Priority Scheduling", "FIFO queue"], "Priority Scheduling"),
            make_question("What is the purpose of a database index?", ["Encrypt all rows", "Speed up data retrieval", "Delete duplicate tables", "Replace primary keys"], "Speed up data retrieval"),
            make_question("Which graph algorithm finds shortest paths from one source with non-negative edge weights?", ["Dijkstra's algorithm", "Kruskal's algorithm", "DFS", "Prim's algorithm"], "Dijkstra's algorithm"),
            make_question("What does ACID atomicity guarantee?", ["All transaction operations happen or none do", "Transactions always run in parallel", "Data is compressed", "Queries are sorted"], "All transaction operations happen or none do"),
            make_question("Which technique prevents multiple threads from entering a critical section simultaneously?", ["Caching", "Mutual exclusion", "Paging", "Spooling"], "Mutual exclusion"),
            make_question("What is the space complexity of an adjacency matrix for V vertices?", ["O(V)", "O(E)", "O(V²)", "O(V + E)"], "O(V²)"),
            make_question("Which protocol provides reliable, ordered byte-stream delivery?", ["UDP", "IP", "TCP", "ARP"], "TCP"),
            make_question("In compiler design, what does a parser typically build?", ["Syntax tree", "Machine monitor", "Network packet", "Database index"], "Syntax tree")
        ]
    },

    "AIML": {
        "Easy": [
            make_question("What does AI stand for?", ["Artificial Intelligence", "Automatic Internet", "Advanced Input", "Applied Interface"], "Artificial Intelligence"),
            make_question("What does ML stand for?", ["Machine Learning", "Multiple Logic", "Memory Language", "Machine Linking"], "Machine Learning"),
            make_question("Which is an example of AI?", ["Voice assistant", "Plain notebook", "Desk lamp", "Paper clip"], "Voice assistant"),
            make_question("What is a dataset?", ["Collection of data", "Computer cable", "Programming loop", "Operating system"], "Collection of data"),
            make_question("Which language is widely used in AI?", ["Python", "HTML", "CSS", "XML"], "Python"),
            make_question("Which task predicts a category or class?", ["Classification", "Regression", "Compression", "Formatting"], "Classification"),
            make_question("What does NLP stand for?", ["Natural Language Processing", "Network Link Program", "Numeric Logic Processing", "New Language Protocol"], "Natural Language Processing"),
            make_question("Which is a common AI application?", ["Image recognition", "Manual stapling", "Paper folding", "Mechanical pencil"], "Image recognition"),
            make_question("What is a chatbot designed to do?", ["Interact through conversation", "Cool a processor", "Store electricity", "Print circuit boards"], "Interact through conversation"),
            make_question("What is a robot?", ["A programmable machine", "A database table", "A web browser", "A text editor"], "A programmable machine")
        ],

        "Medium": [
            make_question("Which learning uses labeled training data?", ["Supervised learning", "Unsupervised learning", "Reinforcement learning", "Random learning"], "Supervised learning"),
            make_question("Which learning method groups similar data without labels?", ["Supervised learning", "Unsupervised learning", "Transfer learning", "Rule-based learning"], "Unsupervised learning"),
            make_question("What is the purpose of a test dataset?", ["Train model weights", "Evaluate performance on unseen data", "Increase the number of labels", "Remove all features"], "Evaluate performance on unseen data"),
            make_question("Which metric is the fraction of correct predictions?", ["Precision", "Recall", "Accuracy", "Specificity"], "Accuracy"),
            make_question("What is overfitting?", ["Model performs well on training data but poorly on new data", "Model cannot learn training data", "Dataset has no rows", "Training stops immediately"], "Model performs well on training data but poorly on new data"),
            make_question("Which algorithm is commonly used for classification?", ["K-nearest neighbors", "K-means only", "Apriori", "PageRank"], "K-nearest neighbors"),
            make_question("What does a confusion matrix summarize?", ["Predicted versus actual classes", "Training time only", "Number of model layers", "Image dimensions"], "Predicted versus actual classes"),
            make_question("Which technique helps reduce overfitting in neural networks?", ["Dropout", "Increasing label noise deliberately", "Removing the test set", "Using only one example"], "Dropout"),
            make_question("What is regression used to predict?", ["Continuous numerical values", "Only image labels", "Clusters without labels", "Text tokens only"], "Continuous numerical values"),
            make_question("What is a feature in machine learning?", ["An input variable used by a model", "The final report", "A type of processor", "A programming language"], "An input variable used by a model")
        ],

        "Hard": [
            make_question("What does gradient descent update during training?", ["Model parameters", "Class names", "Dataset filenames", "CPU instructions"], "Model parameters"),
            make_question("What is the main purpose of regularization?", ["Reduce overfitting", "Increase training labels", "Guarantee zero training error", "Remove the loss function"], "Reduce overfitting"),
            make_question("In a neural network, what does an activation function introduce?", ["Non-linearity", "Database indexing", "File compression", "Sorting"], "Non-linearity"),
            make_question("Which optimizer uses estimates of first and second moments of gradients?", ["Adam", "K-means", "Naive Bayes", "PCA"], "Adam"),
            make_question("What does PCA primarily do?", ["Reduce dimensionality", "Generate class labels", "Translate languages", "Increase sample count"], "Reduce dimensionality"),
            make_question("What is the vanishing gradient problem?", ["Gradients become very small in earlier layers", "Training data disappears", "The loss becomes an image", "The model has too many labels"], "Gradients become very small in earlier layers"),
            make_question("Which architecture is especially suited to sequential data?", ["Recurrent neural network", "Decision stump", "K-means", "Linear search"], "Recurrent neural network"),
            make_question("What does the attention mechanism help a model do?", ["Weight the importance of different input elements", "Delete all input tokens", "Sort training files", "Convert labels into pixels"], "Weight the importance of different input elements"),
            make_question("What is the purpose of cross-validation?", ["Estimate model generalization across data splits", "Increase the number of model parameters", "Replace feature engineering", "Guarantee perfect accuracy"], "Estimate model generalization across data splits"),
            make_question("In reinforcement learning, what guides an agent's learning from the environment?", ["Rewards", "Primary keys", "HTML tags", "Compiler tokens"], "Rewards")
        ]
    }
}