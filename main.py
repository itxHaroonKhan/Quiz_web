import streamlit as st
import random
from datetime import datetime
import uuid

quiz = [
    {
        "question": "What is the purpose of an alert in JavaScript?",
        "options": ["To display a message in the console", "To show a pop-up message to the user", "To redirect to a new page", "To log errors"],
        "answer": "To show a pop-up message to the user",
        "difficulty": "Easy",
        "explanation": "The `alert()` function displays a simple pop-up message to the user in the browser.",
        "hint": "Think about what happens when you see a pop-up message in a browser."
    },
    {
        "question": "Which of the following is a valid string variable declaration?",
        "options": ["let name = 'John';", "string name = 'John';", "var name = John;", "let name = John;"],
        "answer": "let name = 'John';",
        "difficulty": "Easy",
        "explanation": "String variables in JavaScript must have their values enclosed in quotes. `let name = 'John';` is the correct syntax.",
        "hint": "Strings need quotes around their values."
    },
    {
        "question": "What is the correct way to declare a number variable?",
        "options": ["let num = '123';", "let num = 123;", "var num = '123';", "number num = 123;"],
        "answer": "let num = 123;",
        "difficulty": "Easy",
        "explanation": "Number variables in JavaScript are declared without quotes, e.g., `let num = 123;`.",
        "hint": "Numbers don’t use quotes."
    },
    {
        "question": "Which variable name is illegal in JavaScript?",
        "options": ["myVar", "2ndVar", "_count", "$price"],
        "answer": "2ndVar",
        "difficulty": "Medium",
        "explanation": "Variable names in JavaScript cannot start with a number, making `2ndVar` illegal.",
        "hint": "Check the rules for valid variable names."
    },
    {
        "question": "What does the `+` operator do in a math expression?",
        "options": ["Multiplies two numbers", "Adds two numbers", "Divides two numbers", "Subtracts two numbers"],
        "answer": "Adds two numbers",
        "difficulty": "Easy",
        "explanation": "The `+` operator is used for addition in mathematical expressions.",
        "hint": "Think of basic arithmetic operations."
    },
    {
        "question": "What is the result of the expression `5 % 2`?",
        "options": ["2", "1", "3", "0"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "The `%` operator returns the remainder of division, so `5 % 2` equals `1`.",
        "hint": "What does the modulus operator do?"
    },
    {
        "question": "How do you eliminate ambiguity in the expression `5 + 3 * 2`?",
        "options": ["Use parentheses", "Use a comma", "Use a semicolon", "Use curly braces"],
        "answer": "Use parentheses",
        "difficulty": "Medium",
        "explanation": "Parentheses `()` ensure the order of operations, e.g., `(5 + 3) * 2`.",
        "hint": "How can you control the order of operations?"
    },
    {
        "question": "How do you concatenate two strings in JavaScript?",
        "options": ["Using `&&`", "Using `+`", "Using `*`", "Using `/`"],
        "answer": "Using `+`",
        "difficulty": "Easy",
        "explanation": "The `+` operator concatenates strings, e.g., `'Hello' + 'World'` results in `'HelloWorld'`.",
        "hint": "Which operator joins text?"
    },
    {
        "question": "What does the `prompt()` function do?",
        "options": ["Displays a message", "Asks for user input", "Logs to the console", "Redirects the page"],
        "answer": "Asks for user input",
        "difficulty": "Easy",
        "explanation": "The `prompt()` function displays a dialog box that asks the user for input.",
        "hint": "What function asks the user to type something?"
    },
    {
        "question": "What is the purpose of an `if` statement?",
        "options": ["To loop through an array", "To execute code conditionally", "To define a function", "To declare a variable"],
        "answer": "To execute code conditionally",
        "difficulty": "Easy",
        "explanation": "`if` statements execute code only if a condition is true.",
        "hint": "Think about decision-making in code."
    },
    {
        "question": "Which operator checks for equality without type coercion?",
        "options": ["==", "===", "!=", "!=="],
        "answer": "===",
        "difficulty": "Medium",
        "explanation": "The `===` operator checks for both value and type equality.",
        "hint": "Which operator is strict about types?"
    },
    {
        "question": "What does an `else if` statement do?",
        "options": ["Repeats a block of code", "Checks another condition if the first is false", "Defines a function", "Ends a loop"],
        "answer": "Checks another condition if the first is false",
        "difficulty": "Medium",
        "explanation": "`else if` allows testing additional conditions if the previous `if` or `else if` is false.",
        "hint": "What happens after an `if` condition fails?"
    },
    {
        "question": "How do you test multiple conditions in a single `if` statement?",
        "options": ["Use `&&` or `||`", "Use `+`", "Use `;`", "Use `,`"],
        "answer": "Use `&&` or `||`",
        "difficulty": "Medium",
        "explanation": "`&&` (and) and `||` (or) operators combine multiple conditions in an `if` statement.",
        "hint": "Think about logical operators."
    },
    {
        "question": "What is a nested `if` statement?",
        "options": ["An `if` statement inside another `if` statement", "An `if` statement with multiple conditions", "An `if` statement in a loop", "An `if` statement with no condition"],
        "answer": "An `if` statement inside another `if` statement",
        "difficulty": "Medium",
        "explanation": "A nested `if` statement is an `if` statement placed inside another `if` block.",
        "hint": "Think about `if` statements within `if` statements."
    },
    {
        "question": "What is an array in JavaScript?",
        "options": ["A single value", "A collection of values", "A function", "A loop"],
        "answer": "A collection of values",
        "difficulty": "Easy",
        "explanation": "An array is a data structure that holds a collection of values, e.g., `[1, 2, 3]`.",
        "hint": "What stores multiple values in one variable?"
    },
    {
        "question": "How do you add an element to the end of an array?",
        "options": ["array.add()", "array.push()", "array.append()", "array.insert()"],
        "answer": "array.push()",
        "difficulty": "Medium",
        "explanation": "The `push()` method adds an element to the end of an array.",
        "hint": "Which method adds to the end?"
    },
    {
        "question": "How do you remove the first element from an array?",
        "options": ["array.pop()", "array.shift()", "array.splice()", "array.delete()"],
        "answer": "array.shift()",
        "difficulty": "Medium",
        "explanation": "The `shift()` method removes the first element from an array.",
        "hint": "Which method removes from the start?"
    },
    {
        "question": "What is the purpose of a `for` loop?",
        "options": ["To execute code once", "To repeat code a specific number of times", "To define a function", "To check a condition"],
        "answer": "To repeat code a specific number of times",
        "difficulty": "Easy",
        "explanation": "A `for` loop repeats a block of code for a specified number of iterations.",
        "hint": "What loop is used for a known number of iterations?"
    },
    {
        "question": "What does the `break` statement do in a `for` loop?",
        "options": ["Pauses the loop", "Exits the loop", "Skips one iteration", "Restarts the loop"],
        "answer": "Exits the loop",
        "difficulty": "Medium",
        "explanation": "The `break` statement terminates the loop immediately.",
        "hint": "What stops a loop completely?"
    },
    {
        "question": "What is a nested `for` loop?",
        "options": ["A loop inside another loop", "A loop with multiple conditions", "A loop with no condition", "A loop that runs once"],
        "answer": "A loop inside another loop",
        "difficulty": "Medium",
        "explanation": "A nested `for` loop is a `for` loop inside another `for` loop, often used for multi-dimensional arrays.",
        "hint": "Think about loops within loops."
    },
    {
        "question": "How do you convert a string to uppercase?",
        "options": ["string.toLowerCase()", "string.toUpperCase()", "string.upper()", "string.capitalize()"],
        "answer": "string.toUpperCase()",
        "difficulty": "Easy",
        "explanation": "The `toUpperCase()` method converts a string to uppercase letters.",
        "hint": "Which method changes text to all caps?"
    },
    {
        "question": "How do you find the length of a string?",
        "options": ["string.size", "string.length", "string.count", "string.len"],
        "answer": "string.length",
        "difficulty": "Easy",
        "explanation": "The `length` property returns the number of characters in a string.",
        "hint": "What property counts characters?"
    },
    {
        "question": "How do you find a substring in a string?",
        "options": ["string.includes()", "string.indexOf()", "string.search()", "All of the above"],
        "answer": "All of the above",
        "difficulty": "Medium",
        "explanation": "`includes()`, `indexOf()`, and `search()` can all be used to find substrings, with slight differences in their behavior.",
        "hint": "Which methods check for parts of a string?"
    },
    {
        "question": "How do you find a character at a specific index in a string?",
        "options": ["string.charAt()", "string.at()", "string.getChar()", "Both a and b"],
        "answer": "Both a and b",
        "difficulty": "Medium",
        "explanation": "Both `charAt()` and `at()` return the character at a specified index in a string.",
        "hint": "Which methods get a single character?"
    },
    {
        "question": "How do you replace all occurrences of a substring in a string?",
        "options": ["string.replace()", "string.replaceAll()", "string.substitute()", "string.change()"],
        "answer": "string.replaceAll()",
        "difficulty": "Medium",
        "explanation": "`replaceAll()` replaces all occurrences of a substring, while `replace()` only replaces the first.",
        "hint": "Which method replaces all matches?"
    },
    {
        "question": "What is logged?\n```javascript\nlet num = 9.8765;\nconsole.log(num.toFixed(3));\n```",
        "options": ["9.877", "9.876", "9.88", "9.8765"],
        "answer": "9.877",
        "difficulty": "Medium",
        "explanation": "`toFixed(3)` rounds to 3 decimal places, so 9.8765 becomes '9.877' (as a string).",
        "hint": "How many decimal places does `toFixed(3)` keep?"
    },
    {
        "question": "What is logged?\n```javascript\nconsole.log(Math.floor(Math.random() * 10));\n```",
        "options": ["A random integer from 0 to 10", "A random integer from 0 to 9", "A random float from 0 to 10", "A random float from 0 to 9"],
        "answer": "A random integer from 0 to 9",
        "difficulty": "Medium",
        "explanation": "`Math.random() * 10` generates a float from 0 to 9.999..., and `Math.floor()` rounds it down to an integer from 0 to 9.",
        "hint": "What range does `Math.random() * 10` produce?"
    },
    {
        "question": "What is logged?\n```javascript\nlet str = '123';\nconsole.log(parseInt(str));\n```",
        "options": ["'123'", "123", "12.3", "NaN"],
        "answer": "123",
        "difficulty": "Medium",
        "explanation": "`parseInt(str)` converts the string '123' to the integer 123.",
        "hint": "What does `parseInt()` do to a string?"
    },
    {
        "question": "What is logged?\n```javascript\nlet num = 123;\nconsole.log(String(num));\n```",
        "options": ["123", "'123'", "NaN", "undefined"],
        "answer": "'123'",
        "difficulty": "Medium",
        "explanation": "`String(num)` converts the number 123 to the string '123'.",
        "hint": "What does `String()` do to a number?"
    },
    {
        "question": "What is logged?\n```javascript\nlet num = 5.56789;\nconsole.log(num.toFixed(2));\n```",
        "options": ["5.57", "5.56", "5.6", "5.567"],
        "answer": "5.57",
        "difficulty": "Medium",
        "explanation": "`toFixed(2)` rounds to 2 decimal places, so 5.56789 becomes '5.57' (as a string).",
        "hint": "How does `toFixed(2)` round numbers?"
    },
    {
        "question": "What is logged?\n```javascript\nlet date = new Date();\nconsole.log(date.getFullYear());\n```",
        "options": ["The current month", "The current year", "The current day", "The current time"],
        "answer": "The current year",
        "difficulty": "Medium",
        "explanation": "`getFullYear()` returns the current year from a Date object.",
        "hint": "What does `getFullYear()` extract?"
    },
    {
        "question": "What is logged?\n```javascript\nlet date = new Date('2023-01-01');\nconsole.log(date.getMonth());\n```",
        "options": ["0", "1", "12", "2023"],
        "answer": "0",
        "difficulty": "Medium",
        "explanation": "`getMonth()` returns the month (0-based), so January is 0.",
        "hint": "Is January represented as 0 or 1?"
    },
    {
        "question": "What is logged?\n```javascript\nlet date = new Date();\ndate.setFullYear(2025);\nconsole.log(date.getFullYear());\n```",
        "options": ["2024", "2025", "2023", "undefined"],
        "answer": "2025",
        "difficulty": "Medium",
        "explanation": "`setFullYear(2025)` sets the year to 2025, and `getFullYear()` returns it.",
        "hint": "What does `setFullYear()` change?"
    },
    {
        "question": "What is logged?\n```javascript\nfunction greet() {\n  return 'Hello';\n}\nconsole.log(greet());\n```",
        "options": ["undefined", "Hello", "greet", "null"],
        "answer": "Hello",
        "difficulty": "Easy",
        "explanation": "The `greet()` function returns the string 'Hello', which is logged.",
        "hint": "What does the function return?"
    },
    {
        "question": "What is logged?\n```javascript\nfunction add(a, b) {\n  return a + b;\n}\nconsole.log(add(2, 3));\n```",
        "options": ["5", "23", "undefined", "NaN"],
        "answer": "5",
        "difficulty": "Easy",
        "explanation": "The `add` function takes two parameters and returns their sum, so `add(2, 3)` returns 5.",
        "hint": "What do the parameters `a` and `b` do?"
    },
    {
        "question": "What is logged?\n```javascript\nlet x = 10;\nfunction test() {\n  let x = 20;\n  return x;\n}\nconsole.log(test());\n```",
        "options": ["10", "20", "undefined", "null"],
        "answer": "20",
        "difficulty": "Medium",
        "explanation": "The local variable `x` inside the function shadows the global `x`, so `test()` returns 20.",
        "hint": "Which variable `x` is used inside the function?"
    },
    {
        "question": "What is logged?\n```javascript\nlet day = 3;\nswitch (day) {\n  case 1:\n    console.log('Monday');\n    break;\n  case 2:\n    console.log('Tuesday');\n    break;\n  default:\n    console.log('Other');\n}\n```",
        "options": ["Monday", "Tuesday", "Other", "undefined"],
        "answer": "Other",
        "difficulty": "Medium",
        "explanation": "Since `day` is 3 and no case matches, the `default` block executes, logging 'Other'.",
        "hint": "What happens when no case matches?"
    },
    {
        "question": "What is logged?\n```javascript\nlet i = 0;\nwhile (i < 2) {\n  console.log(i);\n  i++;\n}\n```",
        "options": ["0, 1", "1, 2", "0, 1, 2", "undefined"],
        "answer": "0, 1",
        "difficulty": "Medium",
        "explanation": "The `while` loop runs as long as `i < 2`, logging 0 and 1.",
        "hint": "How many times does the loop run?"
    },
    {
        "question": "What is logged?\n```javascript\nlet i = 0;\ndo {\n  console.log(i);\n  i++;\n} while (i < 2);\n```",
        "options": ["0, 1", "1, 2", "0, 1, 2", "undefined"],
        "answer": "0, 1",
        "difficulty": "Medium",
        "explanation": "The `do...while` loop runs at least once, logging 0 and 1 since the condition is `i < 2`.",
        "hint": "Does the loop run at least once?"
    },
    {
        "question": "What is logged?\n```javascript\nlet arr = [1, 2, 3];\narr.splice(1, 1);\nconsole.log(arr);\n```",
        "options": ["[1, 3]", "[1, 2]", "[2, 3]", "[1, 2, 3]"],
        "answer": "[1, 3]",
        "difficulty": "Medium",
        "explanation": "`splice(1, 1)` removes 1 element at index 1, so `[1, 2, 3]` becomes `[1, 3]`.",
        "hint": "What does `splice(1, 1)` remove?"
    },
    {
        "question": "What is logged?\n```javascript\nlet str = 'hello';\nconsole.log(str.slice(1, 3));\n```",
        "options": ["he", "el", "ll", "lo"],
        "answer": "el",
        "difficulty": "Medium",
        "explanation": "`slice(1, 3)` extracts characters from index 1 to 2, resulting in 'el'.",
        "hint": "What does `slice(1, 3)` include?"
    },
    {
        "question": "What is logged?\n```javascript\nlet str = 'JavaScript';\nconsole.log(str.indexOf('Script'));\n```",
        "options": ["4", "5", "6", "-1"],
        "answer": "4",
        "difficulty": "Medium",
        "explanation": "`indexOf('Script')` returns the starting index of 'Script', which is 4.",
        "hint": "Where does 'Script' start in 'JavaScript'?"
    },
    {
        "question": "What is logged?\n```javascript\nlet num = 3.14159;\nconsole.log(Math.round(num));\n```",
        "options": ["3", "4", "3.14", "3.142"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "`Math.round()` rounds to the nearest integer, so 3.14159 becomes 3.",
        "hint": "Does `Math.round()` round up or down?"
    },
    {
        "question": "What is logged?\n```javascript\nlet x = 5;\nif (x > 3 && x < 7) {\n  console.log('In range');\n} else {\n  console.log('Out of range');\n}\n```",
        "options": ["In range", "Out of range", "undefined", "null"],
        "answer": "In range",
        "difficulty": "Medium",
        "explanation": "The condition `x > 3 && x < 7` is true for `x = 5`, so 'In range' is logged.",
        "hint": "Evaluate the condition for `x = 5`."
    }
]

# Cache shuffled quiz (unchanged)
@st.cache_data
def shuffle_quiz(_quiz):
    shuffled = random.sample(_quiz, len(_quiz))
    for i in range(len(shuffled) - 1):
        if i < len(shuffled) - 1 and shuffled[i]["difficulty"] == shuffled[i + 1]["difficulty"]:
            for j in range(i + 2, len(shuffled)):
                if shuffled[j]["difficulty"] != shuffled[i]["difficulty"]:
                    shuffled[i + 1], shuffled[j] = shuffled[j], shuffled[i + 1]
                    break
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        labeled_options = list(zip(q["options"], ["A", "B", "C", "D"]))
        random.shuffle(labeled_options)
        q["display_options"] = [f"{label}: {option}" for option, label in labeled_options]
        for option, label in labeled_options:
            if option == q["answer"]:
                q["labeled_answer"] = f"{label}: {option}"
                break
    return shuffled

# Initialize session state (unchanged)
if "quiz_data" not in st.session_state:
    st.session_state.update({
        "quiz_data": shuffle_quiz(quiz) if quiz else [],
        "score": 0,
        "current_q": 0,
        "start_time": datetime.now(),
        "answers": [None] * len(quiz) if quiz else [],
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 1800,
        "theme": "dark",
        "streak": 0,
        "show_hint": False,
        "started": False
    })

# Theme toggle (unchanged)
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# Timer logic (unchanged)
def update_timer():
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.session_state.time_left = max(1800 - elapsed, 0)
    if st.session_state.time_left <= 0:
        st.session_state.show_results = True
        st.rerun()

# Reset quiz (unchanged)
def reset_quiz():
    st.session_state.update({
        "quiz_data": shuffle_quiz(quiz),
        "score": 0,
        "current_q": 0,
        "start_time": datetime.now(),
        "answers": [None] * len(quiz),
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 1800,
        "streak": 0,
        "show_hint": False,
        "started": False
    })
    st.rerun()

# NEW: Progress snapshot function
def show_progress_snapshot():
    answered = sum(1 for ans in st.session_state.answers if ans is not None)
    st.markdown("""
        <div style='background: var(--bg-container); padding: 15px; border-radius: 10px; box-shadow: 0 4px 12px var(--shadow); margin: 10px 0;'>
            <h4 style='color: var(--text-color);'>📊 Progress Snapshot</h4>
            <div style='color: var(--text-color); font-size: 14px;'>
                - 🏆 Current Score: {score}<br>
                - 🔥 Streak: {streak}<br>
                - ✅ Questions Answered: {answered}/{total}
            </div>
        </div>
    """.format(
        score=st.session_state.score,
        streak=st.session_state.streak,
        answered=answered,
        total=len(st.session_state.quiz_data)
    ), unsafe_allow_html=True)

# CSS (unchanged)
st.markdown("""
    <style>
    body {
        background: var(--bg-gradient);
        color: var(--text-color);
        font-family: 'Inter', 'Arial', sans-serif;
        transition: all 0.3s ease;
    }
    :root {
        --bg-gradient: linear-gradient(180deg, #1a1a3b, #2c2c54);
        --bg-container: #2c2c54;
        --text-color: #ffffff;
        --button-bg: linear-gradient(45deg, #6b21a8, #a855f7);
        --button-hover: linear-gradient(45deg, #8b5cf6, #c084fc);
        --code-bg: #1e1e1e;
        --shadow: rgba(0,0,0,0.3);
    }
    [data-theme="light"] {
        --bg-gradient: linear-gradient(180deg, #e0e7ff, #f3e8ff);
        --bg-container: #ffffff;
        --text-color: #1f2937;
        --button-bg: linear-gradient(45deg, #4f46e5, #7c3aed);
        --button-hover: linear-gradient(45deg, #6366f1, #a78bfa);
        --code-bg: #f1f5f9;
        --shadow: rgba(0,0,0,0.1);
    }
    .main-container {
        background: var(--bg-container);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 25px var(--shadow);
        max-width: 900px;
        margin: 20px auto;
    }
    .stButton>button {
        background: var(--button-bg);
        color: var(--text-color);
        border: none;
        border-radius: 10px;
        padding: 12px;
        width: 100%;
        font-size: 16px;
        font-weight: 600;
        margin: 6px 0;
        cursor: pointer;
        transition: all 0.3s ease;
        transform: scale(1);
    }
    .stButton>button:hover {
        background: var(--button-hover);
        transform: scale(1.05);
        box-shadow: 0 4px 12px var(--shadow);
    }
    .stButton>button:disabled {
        background: #6b7280;
        cursor: not-allowed;
        transform: scale(1);
    }
    .selected-correct {
        background: #34c759 !important;
        transform: scale(1.05);
    }
    .selected-wrong {
        background: #ff3b30 !important;
        transform: scale(1.05);
    }
    .question-container {
        background: var(--bg-container);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 12px var(--shadow);
        margin-bottom: 15px;
    }
    .feedback-correct {
        color: #34c759;
        font-weight: 600;
        font-size: 18px;
        margin: 15px 0;
        animation: fadeIn 0.5s ease;
    }
    .feedback-wrong {
        color: #ff3b30;
        font-weight: 600;
        font-size: 18px;
        margin: 15px 0;
        animation: fadeIn 0.5s ease;
    }
    .progress-bar {
        background: #4b4b6b;
        border-radius: 10px;
        height: 12px;
        margin: 10px 0;
        position: relative;
    }
    .progress-fill {
        background: var(--button-bg);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    .progress-text {
        position: absolute;
        top: -20px;
        right: 0;
        color: var(--text-color);
        font-size: 12px;
    }
    .title {
        font-size: 36px;
        text-align: center;
        margin-bottom: 8px;
        color: var(--text-color);
    }
    .caption {
        text-align: center;
        color: #b0b0d0;
        font-size: 16px;
        margin-bottom: 20px;
    }
    .timer {
        font-size: 16px;
        color: #ff6b6b;
        font-weight: 600;
        text-align: center;
        margin-top: 10px;
    }
    .difficulty {
        font-size: 14px;
        color: #b0b0d0;
        margin-bottom: 10px;
    }
    .stCodeBlock {
        background-color: var(--code-bg) !important;
        border-radius: 8px;
        padding: 15px;
        font-family: 'Consolas', 'Monaco', monospace;
        font-size: 14px;
        line-height: 1.5;
        border: 1px solid #4b4b6b;
    }
    .stCodeBlock pre, .stCodeBlock code {
        color: var(--text-color);
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @media (max-width: 600px) {
        .main-container {
            padding: 15px;
            margin: 10px;
        }
        .title {
            font-size: 28px;
        }
        .stButton>button {
            font-size: 14px;
            padding: 8px;
        }
    }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
""", unsafe_allow_html=True)

# Main UI (unchanged)
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 JavaScript Quiz Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript Skills!</p>', unsafe_allow_html=True)

# Theme toggle button (unchanged)
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen (unchanged)
if not st.session_state.started:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: var(--text-color); font-size: 18px;">Test your JavaScript knowledge with 50 exciting questions!</p>
        <p style="color: #b0b0d0;">30 minutes, 2 points per correct answer. Ready?</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Quiz", key="start_quiz"):
        st.session_state.started = True
        st.session_state.start_time = datetime.now()
        st.rerun()
else:
    # Timer (unchanged)
    if not st.session_state.show_results:
        update_timer()
        minutes = int(st.session_state.time_left // 60)
        seconds = int(st.session_state.time_left % 60)
        st.markdown(f'<div class="timer">⏰ Time Left: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

    if not st.session_state.quiz_data:
        st.error("No quiz questions available.")
    else:
        # Progress bar (unchanged)
        progress = st.session_state.current_q / len(st.session_state.quiz_data)
        progress_percentage = int(progress * 100)
        st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress_percentage}%"></div>
            <div class="progress-text">{progress_percentage}%</div>
        </div>
        <div style="color: var(--text-color); font-size: 13px; text-align: center;">
            Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
        </div>
        """, unsafe_allow_html=True)

        if not st.session_state.show_results:
            with st.container():
                st.markdown('<div class="question-container">', unsafe_allow_html=True)
                q = st.session_state.quiz_data[st.session_state.current_q]

                # Display difficulty and streak (unchanged)
                st.markdown(f'<div class="difficulty">Difficulty: {q["difficulty"]} | Streak: 🔥 {st.session_state.streak}</div>', unsafe_allow_html=True)

                # Split question into text and code (unchanged)
                if "```javascript" in q["question"]:
                    question_parts = q["question"].split("```javascript\n")
                    question_text = question_parts[0].strip()
                    code_snippet = question_parts[1].split("```")[0].strip()
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{question_text}**")
                    st.code(code_snippet, language="javascript")
                else:
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{q['question']}**")

                # Option buttons (unchanged)
                for i, option in enumerate(q["display_options"]):
                    button_class = ""
                    if st.session_state.selected_option == option:
                        button_class = "selected-correct" if option == q["labeled_answer"] else "selected-wrong"
                    if st.button(
                        option,
                        key=f"q{i}",
                        disabled=st.session_state.selected_option is not None,
                        help="Select this option"
                    ):
                        original_option = option[3:]
                        is_correct = option == q["labeled_answer"]
                        st.session_state.selected_option = option
                        st.session_state.feedback = {
                            "is_correct": is_correct,
                            "correct_answer": q["labeled_answer"],
                            "explanation": q["explanation"]
                        }
                        st.session_state.answers[st.session_state.current_q] = {
                            "question": q["question"],
                            "user_answer": option,
                            "correct_answer": q["labeled_answer"],
                            "is_correct": is_correct,
                            "difficulty": q["difficulty"]
                        }
                        if is_correct:
                            points = {"Easy": 1, "Medium": 2, "Hard": 3}[q["difficulty"]]
                            st.session_state.score += points
                            st.session_state.streak += 1
                            if st.session_state.streak >= 3:
                                st.session_state.score += 1
                        else:
                            st.session_state.streak = 0
                        st.rerun()

                # Feedback (unchanged)
                if st.session_state.feedback:
                    if st.session_state.feedback["is_correct"]:
                        st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="color: var(--text-color); font-size: 14px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                # Hint button (unchanged)
                if st.button("💡 Show Hint", key="hint", disabled=st.session_state.show_hint or st.session_state.selected_option is not None):
                    st.session_state.show_hint = True
                    st.session_state.score = max(0, st.session_state.score - 0.5)
                    st.rerun()
                if st.session_state.show_hint:
                    st.markdown(f'<div style="color: #facc15; font-size: 14px;">Hint: {q["hint"]}</div>', unsafe_allow_html=True)

                # CHANGED: Updated navigation (removed Previous and Skip, added Progress Snapshot)
                col1, col2 = st.columns(2)  # Now only two columns
                with col1:
                    if st.button("📊 Progress Snapshot", key="progress"):
                        show_progress_snapshot()
                with col2:
                    if st.session_state.current_q < len(quiz) - 1:
                        if st.button("➡️ Next", disabled=st.session_state.selected_option is None):
                            st.session_state.current_q += 1
                            st.session_state.selected_option = None
                            st.session_state.feedback = None
                            st.session_state.show_hint = False
                            st.rerun()
                    else:
                        if st.button("🏁 Finish", disabled=st.session_state.selected_option is None):
                            st.session_state.show_results = True
                            st.rerun()

                # Reset quiz button (unchanged)
                if st.button("🔄 Reset Quiz", key="reset"):
                    reset_quiz()

                st.markdown("</div>", unsafe_allow_html=True)
