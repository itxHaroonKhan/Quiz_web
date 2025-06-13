import streamlit as st
import random
from datetime import datetime
import uuid

quiz = [
    
    {
        "question": "What is the output of `alert('Welcome!');` in JavaScript?",
        "options": ["Logs 'Welcome!' to console", "Shows a pop-up with 'Welcome!'", "Returns 'Welcome!'", "Nothing happens"],
        "answer": "Shows a pop-up with 'Welcome!'",
        "difficulty": "Easy",
        "explanation": "The `alert()` function displays a pop-up with the message 'Welcome!' in the browser.",
        "hint": "Think about browser pop-ups."
    },
    {
        "question": "What is the correct way to declare a string variable?",
        "options": ["let str = 'Hello';", "string str = 'Hello';", "let str = Hello;", "var str = Hello;"],
        "answer": "let str = 'Hello';",
        "difficulty": "Easy",
        "explanation": "Strings must be enclosed in quotes, and `let` is a valid variable declaration.",
        "hint": "Strings need quotes."
    },
    {
        "question": "What is the value of `let num = 3.14;` after execution?",
        "options": ["'3.14'", "3.14", "undefined", "null"],
        "answer": "3.14",
        "difficulty": "Easy",
        "explanation": "The variable `num` is assigned the numeric value `3.14`.",
        "hint": "Think about number assignment."
    },
    {
        "question": "Which variable name is illegal?",
        "options": ["let userName;", "let $price;", "let 1stPlace;", "let _score;"],
        "answer": "let 1stPlace;",
        "difficulty": "Medium",
        "explanation": "Variable names cannot start with a number, making `1stPlace` illegal.",
        "hint": "Check naming rules."
    },
    {
        "question": "What is the output of `console.log(4 + 2 * 3);`?",
        "options": ["18", "10", "12", "9"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "Multiplication has higher precedence, so `2 * 3 = 6`, then `4 + 6 = 10`.",
        "hint": "Consider operator precedence."
    },
    {
        "question": "What is the output of `console.log(8 ** 2);`?",
        "options": ["16", "64", "10", "4"],
        "answer": "64",
        "difficulty": "Medium",
        "explanation": "The `**` operator raises 8 to the power of 2, resulting in `64`.",
        "hint": "Think about exponentiation."
    },
    {
        "question": "What is the output of `console.log((5 + 3) * 2);`?",
        "options": ["16", "10", "13", "20"],
        "answer": "16",
        "difficulty": "Medium",
        "explanation": "Parentheses ensure `5 + 3 = 8` is evaluated first, then `8 * 2 = 16`.",
        "hint": "Parentheses control order."
    },
    {
        "question": "What is the output of `console.log('Hi' + ' ' + 'there');`?",
        "options": ["Hi there", "Hithere", "Hi + there", "Hi, there"],
        "answer": "Hi there",
        "difficulty": "Easy",
        "explanation": "The `+` operator concatenates strings, including the space, resulting in `'Hi there'`.",
        "hint": "Think about joining strings."
    },
    {
        "question": "What does `let input = prompt('Enter a number');` do?",
        "options": ["Logs a message", "Asks for user input and stores it", "Shows an alert", "Declares a number"],
        "answer": "Asks for user input and stores it",
        "difficulty": "Easy",
        "explanation": "`prompt()` displays a dialog for user input, storing the result in `input`.",
        "hint": "Think about user input dialogs."
    },
    {
        "question": "What is the output of `if (10 > 5) { console.log('Yes'); }`?",
        "options": ["Yes", "No", "undefined", "Nothing"],
        "answer": "Yes",
        "difficulty": "Easy",
        "explanation": "Since `10 > 5` is true, the `if` block logs `'Yes'`.",
        "hint": "Evaluate the condition."
    },
    {
        "question": "What is the output of `console.log(3 === '3');`?",
        "options": ["true", "false", "3", "undefined"],
        "answer": "false",
        "difficulty": "Medium",
        "explanation": "The `===` operator checks value and type, so `3` (number) is not equal to `'3'` (string).",
        "hint": "Consider type comparison."
    },
    {
        "question": "What is the output of `let x = 8; if (x > 10) { console.log('High'); } else if (x > 5) { console.log('Medium'); }`?",
        "options": ["High", "Medium", "Nothing", "Low"],
        "answer": "Medium",
        "difficulty": "Medium",
        "explanation": "Since `x > 10` is false but `x > 5` is true, the `else if` block logs `'Medium'`.",
        "hint": "Check conditions in order."
    },
    {
        "question": "What is the output of `if (x > 5 && x < 10) { console.log('Valid'); }` when `x = 7`?",
        "options": ["Valid", "Invalid", "Nothing", "undefined"],
        "answer": "Valid",
        "difficulty": "Medium",
        "explanation": "Both conditions (`x > 5` and `x < 10`) are true for `x = 7`, so `'Valid'` is logged.",
        "hint": "Evaluate logical AND."
    },
    {
        "question": "What is the output of `if (x > 5) { if (x < 10) { console.log('Range'); } }` when `x = 8`?",
        "options": ["Range", "Nothing", "Out of range", "undefined"],
        "answer": "Range",
        "difficulty": "Medium",
        "explanation": "Both outer (`x > 5`) and inner (`x < 10`) conditions are true, so `'Range'` is logged.",
        "hint": "Check nested conditions."
    },
    {
        "question": "What is the output of `let arr = [1, 2, 3]; console.log(arr[0]);`?",
        "options": ["1", "2", "3", "undefined"],
        "answer": "1",
        "difficulty": "Easy",
        "explanation": "Square brackets access array elements by index, so `arr[0]` returns the first element, `1`.",
        "hint": "Remember array indices start at 0."
    },
    {
        "question": "What is the output of `let arr = [1, 2]; arr.push(3); console.log(arr);`?",
        "options": ["[1, 2]", "[1, 2, 3]", "[3, 2, 1]", "[3]"],
        "answer": "[1, 2, 3]",
        "difficulty": "Medium",
        "explanation": "`push()` adds `3` to the end of the array, resulting in `[1, 2, 3]`.",
        "hint": "Think about adding to an array."
    },
    {
        "question": "What is the output of `let arr = [1, 2, 3]; arr.splice(1, 1); console.log(arr);`?",
        "options": ["[1, 2, 3]", "[1, 3]", "[2, 3]", "[1, 2]"],
        "answer": "[1, 3]",
        "difficulty": "Medium",
        "explanation": "`splice(1, 1)` removes 1 element at index 1, resulting in `[1, 3]`.",
        "hint": "Think about removing from an array."
    },
    {
        "question": "What is the output of `for (let i = 0; i < 2; i++) { console.log(i); }`?",
        "options": ["0, 1", "1, 2", "0, 1, 2", "Nothing"],
        "answer": "0, 1",
        "difficulty": "Easy",
        "explanation": "The loop runs from `i = 0` to `i < 2`, logging `0` and `1`.",
        "hint": "Count the loop iterations."
    },
    {
        "question": "What is the output of `let found = false; for (let i = 0; i < 3; i++) { if (i === 2) { found = true; break; } } console.log(found);`?",
        "options": ["true", "false", "2", "undefined"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "When `i === 2`, `found` is set to `true`, and `break` exits the loop, so `'true'` is logged.",
        "hint": "Think about flags and breaking loops."
    },
    {
        "question": "What is the output of `for (let i = 1; i <= 2; i++) { for (let j = 1; j <= 2; j++) { console.log(i * j); } }`?",
        "options": ["1, 2, 2, 4", "1, 2, 3, 4", "1, 2", "1, 4"],
        "answer": "1, 2, 2, 4",
        "difficulty": "Medium",
        "explanation": "The outer loop runs for `i = 1, 2`, and the inner loop for `j = 1, 2`, logging `1*1=1`, `1*2=2`, `2*1=2`, `2*2=4`.",
        "hint": "Trace nested loop multiplication."
    },
    {
        "question": "What is the output of `console.log('hello'.toUpperCase());`?",
        "options": ["HELLO", "hello", "Hello", "undefined"],
        "answer": "HELLO",
        "difficulty": "Easy",
        "explanation": "`toUpperCase()` converts `'hello'` to `'HELLO'`.",
        "hint": "Think about case conversion."
    },
    {
        "question": "What is the output of `let str = 'hello'; console.log(str.length);`?",
        "options": ["4", "5", "6", "undefined"],
        "answer": "5",
        "difficulty": "Easy",
        "explanation": "The `length` property returns the number of characters in `'hello'`, which is `5`.",
        "hint": "Count the letters in 'hello'."
    },
    {
        "question": "What is the output of `console.log('hello'.indexOf('lo'));`?",
        "options": ["0", "3", "4", "-1"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "`indexOf('lo')` returns the starting index of `'lo'` in `'hello'`, which is `3`.",
        "hint": "Find where 'lo' starts in 'hello'."
    },
    {
        "question": "What is the output of `let str = 'hello'; console.log(str.replace('l', 'p'));`?",
        "options": ["heppo", "hello", "peppo", "helpo"],
        "answer": "heppo",
        "difficulty": "Medium",
        "explanation": "`replace('l', 'p')` replaces the first `'l'` with `'p'`, resulting in `'heppo'`.",
        "hint": "Think about replacing one character."
    },
    {
        "question": "What is the output of `let i = 0; do { console.log(i); i++; } while (i < 2);`?",
        "options": ["0, 1", "1, 2", "0", "Nothing"],
        "answer": "0, 1",
        "difficulty": "Medium",
        "explanation": "The `do...while` loop runs at least once, logging `0` and `1` as `i` increments until `i < 2` is false.",
        "hint": "Consider the guaranteed first iteration."
    },
    {
        "question": "What is the purpose of an alert in JavaScript?",
        "options": ["To display a message in the console", "To show a pop-up message to the user", "To redirect to a new page", "To log errors"],
        "answer": "To show a pop-up message to the user",
        "difficulty": "Easy",
        "explanation": "The `alert()` function displays a simple pop-up message to the user in the browser.",
        "hint": "Think about what happens when you see a pop-up message in a browser."
    },
    {
        "question": "What is a string variable in JavaScript?",
        "options": ["A variable storing numbers", "A variable storing text", "A variable storing objects", "A variable storing functions"],
        "answer": "A variable storing text",
        "difficulty": "Easy",
        "explanation": "A string variable stores text data, enclosed in single or double quotes, e.g., `let name = 'Alice';`.",
        "hint": "Consider what type of data is stored in quotes."
    },
    {
        "question": "What type of data is stored in a number variable in JavaScript?",
        "options": ["Text", "Numeric values", "Boolean values", "Arrays"],
        "answer": "Numeric values",
        "difficulty": "Easy",
        "explanation": "Number variables store integers or decimals, e.g., `let num = 42;`.",
        "hint": "Think about numbers like 42 or 3.14."
    },
    {
        "question": "Which of the following is an illegal variable name in JavaScript?",
        "options": ["myVar", "2ndVar", "_var", "varName"],
        "answer": "2ndVar",
        "difficulty": "Medium",
        "explanation": "Variable names cannot start with a number, making `2ndVar` illegal.",
        "hint": "Check JavaScript’s variable naming rules."
    },
    {
        "question": "Which operator performs multiplication in JavaScript?",
        "options": ["+", "-", "*", "/"],
        "answer": "*",
        "difficulty": "Easy",
        "explanation": "The `*` operator is used for multiplication, e.g., `5 * 2 = 10`.",
        "hint": "Think about basic math operators."
    },
    {
        "question": "What does the exponentiation operator (**) do in JavaScript?",
        "options": ["Divides numbers", "Raises a number to a power", "Returns the remainder", "Adds numbers"],
        "answer": "Raises a number to a power",
        "difficulty": "Medium",
        "explanation": "The `**` operator raises the first number to the power of the second, e.g., `2 ** 3 = 8`.",
        "hint": "Consider an operator for powers."
    },
    {
        "question": "How do you eliminate ambiguity in math expressions in JavaScript?",
        "options": ["Using variables", "Using parentheses", "Using comments", "Using strings"],
        "answer": "Using parentheses",
        "difficulty": "Medium",
        "explanation": "Parentheses `()` control the order of operations, ensuring expressions are evaluated as intended.",
        "hint": "Think about grouping in math."
    },
    {
        "question": "What is string concatenation in JavaScript?",
        "options": ["Splitting strings", "Joining strings", "Reversing strings", "Comparing strings"],
        "answer": "Joining strings",
        "difficulty": "Easy",
        "explanation": "String concatenation combines strings using the `+` operator, e.g., `'Hello' + 'World'` yields `'HelloWorld'`.",
        "hint": "Think about combining text."
    },
    {
        "question": "What is the purpose of the `prompt()` function in JavaScript?",
        "options": ["Logs to the console", "Asks for user input", "Displays an alert", "Redirects to a URL"],
        "answer": "Asks for user input",
        "difficulty": "Easy",
        "explanation": "The `prompt()` function displays a dialog box for user input, returning the entered value.",
        "hint": "Consider user interaction dialogs."
    },
    {
        "question": "What does an `if` statement do in JavaScript?",
        "options": ["Loops through code", "Executes code conditionally", "Declares variables", "Defines functions"],
        "answer": "Executes code conditionally",
        "difficulty": "Easy",
        "explanation": "An `if` statement runs code only if its condition is true, e.g., `if (x > 5)`.",
        "hint": "Think about decision-making."
    },
    {
        "question": "Which operator checks for strict equality in JavaScript?",
        "options": ["==", "===", "!=", "!=="],
        "answer": "===",
        "difficulty": "Medium",
        "explanation": "The `===` operator checks for both value and type equality, e.g., `5 === '5'` is false.",
        "hint": "Consider strict comparison."
    },
    {
        "question": "What is the role of an `else if` statement in JavaScript?",
        "options": ["Runs if the first condition is true", "Checks another condition if prior ones are false", "Always runs", "Declares variables"],
        "answer": "Checks another condition if prior ones are false",
        "difficulty": "Medium",
        "explanation": "`else if` tests additional conditions if previous `if` or `else if` conditions fail.",
        "hint": "Think about multiple conditions."
    },
    {
        "question": "How can multiple conditions be combined in an `if` statement?",
        "options": ["Using commas", "Using && or || operators", "Using switch", "Using loops"],
        "answer": "Using && or || operators",
        "difficulty": "Medium",
        "explanation": "Logical operators `&&` (AND) and `||` (OR) combine conditions in an `if` statement.",
        "hint": "Consider logical operators."
    },
    {
        "question": "What is a nested `if` statement in JavaScript?",
        "options": ["An if statement inside another if statement", "Multiple if statements in a row", "An if statement with no condition", "An if statement in a loop"],
        "answer": "An if statement inside another if statement",
        "difficulty": "Medium",
        "explanation": "A nested `if` statement is an `if` block inside another `if` block for layered conditions.",
        "hint": "Think about conditions within conditions."
    },
    {
        "question": "What is an array in JavaScript?",
        "options": ["A single value", "A collection of values", "A function", "A string"],
        "answer": "A collection of values",
        "difficulty": "Easy",
        "explanation": "An array is a data structure that stores multiple values in a single variable, e.g., `[1, 2, 3]`.",
        "hint": "Think about lists of items."
    },
    {
        "question": "Which method adds an element to the end of an array?",
        "options": ["pop()", "push()", "shift()", "unshift()"],
        "answer": "push()",
        "difficulty": "Medium",
        "explanation": "The `push()` method adds elements to the end of an array, e.g., `arr.push(4)`.",
        "hint": "Consider adding to the end of a list."
    },
    {
        "question": "What does the `splice()` method do in JavaScript arrays?",
        "options": ["Copies elements", "Removes or replaces elements", "Sorts elements", "Joins arrays"],
        "answer": "Removes or replaces elements",
        "difficulty": "Medium",
        "explanation": "`splice()` removes or replaces elements at a specific index, e.g., `arr.splice(1, 1)` removes one element at index 1.",
        "hint": "Think about modifying arrays."
    },
    {
        "question": "What is the purpose of a `for` loop in JavaScript?",
        "options": ["To execute code once", "To repeat code a specific number of times", "To declare variables", "To define functions"],
        "answer": "To repeat code a specific number of times",
        "difficulty": "Easy",
        "explanation": "A `for` loop repeats code based on a counter, e.g., `for (let i = 0; i < 5; i++)`.",
        "hint": "Think about repeating tasks."
    },
    {
        "question": "What is a flag in a `for` loop?",
        "options": ["A counter variable", "A Boolean to control the loop", "An array index", "A loop condition"],
        "answer": "A Boolean to control the loop",
        "difficulty": "Medium",
        "explanation": "A flag is a Boolean variable used to signal when a condition is met in a loop.",
        "hint": "Think about signaling in loops."
    },
    {
        "question": "What is a nested `for` loop?",
        "options": ["A loop inside another loop", "Multiple loops in sequence", "A loop with no condition", "A loop in a function"],
        "answer": "A loop inside another loop",
        "difficulty": "Medium",
        "explanation": "A nested `for` loop is a `for` loop inside another, often used for multi-dimensional data.",
        "hint": "Think about loops within loops."
    },
    {
        "question": "What are `()` called in JavaScript?",
        "options": ["Curly braces", "Square brackets", "Parentheses", "Angle brackets"],
        "answer": "Parentheses",
        "difficulty": "Easy",
        "explanation": "`()` are called parentheses and are used for function calls, grouping expressions, and conditions.",
        "hint": "Think about round symbols in functions."
    },
    {
        "question": "What are `{}` used for in JavaScript?",
        "options": ["Defining arrays", "Defining code blocks or objects", "Calling functions", "Accessing elements"],
        "answer": "Defining code blocks or objects",
        "difficulty": "Medium",
        "explanation": "Curly braces `{}` define code blocks (e.g., in loops) or object literals (e.g., `{ key: value }`).",
        "hint": "Consider objects or loop bodies."
    },
    {
        "question": "What are `[]` used for in JavaScript?",
        "options": ["Defining functions", "Defining arrays or accessing elements", "Creating objects", "Setting conditions"],
        "answer": "Defining arrays or accessing elements",
        "difficulty": "Medium",
        "explanation": "Square brackets `[]` are used to define arrays (e.g., `[1, 2]`) or access elements (e.g., `arr[0]`).",
        "hint": "Think about lists or indexing."
    },
    {
        "question": "When was JavaScript first created?",
        "options": ["1990", "1995", "2000", "2005"],
        "answer": "1995",
        "difficulty": "Easy",
        "explanation": "JavaScript was created in 1995 by Brendan Eich at Netscape.",
        "hint": "Think about the mid-90s internet era."
    },
    {
        "question": "Which is a popular alternative to JavaScript for web development?",
        "options": ["Python", "TypeScript", "C++", "Java"],
        "answer": "TypeScript",
        "difficulty": "Medium",
        "explanation": "TypeScript is a superset of JavaScript with static typing, often used for web development.",
        "hint": "Consider a language that compiles to JavaScript."
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
