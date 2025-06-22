
import streamlit as st
import random
from datetime import datetime
import uuid



quiz = [
    {
        "question": "What does `alert('Welcome!')` do in JavaScript?",
        "options": ["Logs to console", "Shows a pop-up", "Changes text", "Nothing"],
        "answer": "Shows a pop-up",
        "difficulty": "Easy",
        "explanation": "`alert()` displays a dialog box with a message and an OK button in the browser.",
        "hint": "Think about browser user interactions.",
        "topic": "Alerts"
    },
    {
        "question": "Which is a valid string variable declaration?",
        "options": ["let str = 'Hello';", "let str = Hello;", "str = 'Hello';", "string str = 'Hello';"],
        "answer": "let str = 'Hello';",
        "difficulty": "Easy",
        "explanation": "Strings are enclosed in quotes, and `let` is a proper way to declare variables.",
        "hint": "Check for quotes and valid declarations.",
        "topic": "Variables for Strings"
    },
    {
        "question": "How do you declare a number variable?",
        "options": ["let num = '10';", "let num = 10;", "let num = true;", "num = [10];"],
        "answer": "let num = 10;",
        "difficulty": "Easy",
        "explanation": "Numbers are declared without quotes, using `let` for variable declaration.",
        "hint": "Numbers don’t need quotes.",
        "topic": "Variables for Numbers"
    },
    {
        "question": "Which variable name is illegal?",
        "options": ["userName", "1stPlace", "_count", "total_sum"],
        "answer": "1stPlace",
        "difficulty": "Medium",
        "explanation": "Variable names cannot start with a number in JavaScript.",
        "hint": "Review variable naming rules.",
        "topic": "Variable Names Legal and Illegal"
    },
    {
        "question": "What is the result of `8 - 3 * 2`?",
        "options": ["10", "2", "5", "11"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "Multiplication has higher precedence than subtraction, so `3 * 2 = 6`, then `8 - 6 = 2`.",
        "hint": "Consider operator precedence.",
        "topic": "Math Expressions: familiar operators"
    },
    {
        "question": "What does `x **= 2` do if `x = 5`?",
        "options": ["x = 10", "x = 25", "x = 7", "x = 5"],
        "answer": "x = 25",
        "difficulty": "Medium",
        "explanation": "The `**=` operator raises `x` to the power of 2, so `5 ** 2 = 25`.",
        "hint": "Think about exponentiation.",
        "topic": "Math Expressions: unfamiliar operators"
    },
    {
        "question": "What is the result of `2 * (4 + 3)`?",
        "options": ["14", "10", "12", "8"],
        "answer": "14",
        "difficulty": "Easy",
        "explanation": "Parentheses ensure `4 + 3 = 7` is evaluated first, then `2 * 7 = 14`.",
        "hint": "Parentheses change order of operations.",
        "topic": "Math Expressions: eliminating ambiguity"
    },
    {
        "question": "What does `'Good' + ' ' + 'Morning'` produce?",
        "options": ["GoodMorning", "Good Morning", "Good+Morning", "Error"],
        "answer": "Good Morning",
        "difficulty": "Easy",
        "explanation": "The `+` operator concatenates strings, including the space.",
        "hint": "Think about combining strings.",
        "topic": "Concatenating text strings"
    },
    {
        "question": "What does `prompt('Your age?')` do?",
        "options": ["Logs to console", "Shows input dialog", "Changes text", "Nothing"],
        "answer": "Shows input dialog",
        "difficulty": "Easy",
        "explanation": "`prompt()` displays a dialog box for user input with a text field.",
        "hint": "It involves user interaction.",
        "topic": "Prompts"
    },
    {
        "question": "What will `if (10 > 7) { console.log('Greater'); }` output?",
        "options": ["Greater", "Nothing", "False", "Error"],
        "answer": "Greater",
        "difficulty": "Easy",
        "explanation": "The condition `10 > 7` is true, so 'Greater' is logged.",
        "hint": "Evaluate the `if` condition.",
        "topic": "if statements"
    },
    {
        "question": "What is the result of `'10' === 10`?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "false",
        "difficulty": "Medium",
        "explanation": "The `===` operator checks value and type, so string `'10'` is not equal to number `10`.",
        "hint": "Consider strict equality.",
        "topic": "Comparison operators"
    },
    {
        "question": "What outputs: `let x = 15; if (x < 10) { console.log('Small'); } else if (x < 20) { console.log('Medium'); } else { console.log('Large'); }`?",
        "options": ["Small", "Medium", "Large", "Nothing"],
        "answer": "Medium",
        "difficulty": "Medium",
        "explanation": "Since `x = 15` is less than 20 but not less than 10, 'Medium' is logged.",
        "hint": "Check condition sequence.",
        "topic": "if...else and else if statements"
    },
    {
        "question": "What is output if `x = 8` in `if (x > 5 && x < 10) { console.log('Yes'); }`?",
        "options": ["Yes", "No", "Nothing", "Error"],
        "answer": "Yes",
        "difficulty": "Medium",
        "explanation": "Both conditions `x > 5` and `x < 10` are true for `x = 8`, so 'Yes' is logged.",
        "hint": "Evaluate the `&&` operator.",
        "topic": "Testing sets of conditions"
    },
    {
        "question": "What outputs: `if (x > 10) { if (x < 15) { console.log('Range'); } }` when `x = 12`?",
        "options": ["Range", "Nothing", "Error", "False"],
        "answer": "Range",
        "difficulty": "Medium",
        "explanation": "Both outer (`x > 10`) and inner (`x < 15`) conditions are true, so 'Range' is logged.",
        "hint": "Trace nested conditions.",
        "topic": "if statements nested"
    },
    {
        "question": "How do you create an empty array?",
        "options": ["let arr = [];", "let arr = {};", "let arr = '';", "arr = ();"],
        "answer": "let arr = [];",
        "difficulty": "Easy",
        "explanation": "Arrays are created using square brackets `[]`.",
        "hint": "Check array syntax.",
        "topic": "Arrays"
    },
    {
        "question": "How do you remove the last element from an array `arr`?",
        "options": ["arr.pop();", "arr.push();", "arr.remove();", "arr.splice();"],
        "answer": "arr.pop();",
        "difficulty": "Easy",
        "explanation": "`pop()` removes and returns the last element of an array.",
        "hint": "Look for a method to remove from the end.",
        "topic": "Arrays: adding and removing elements"
    },
    {
        "question": "What method inserts 'item' at index 1 in `arr`?",
        "options": ["arr.splice(1, 0, 'item');", "arr.push(1, 'item');", "arr.insert(1, 'item');", "arr[1] = 'item';"],
        "answer": "arr.splice(1, 0, 'item');",
        "difficulty": "Medium",
        "explanation": "`splice(1, 0, 'item')` inserts 'item' at index 1 without removing elements.",
        "hint": "Check array insertion methods.",
        "topic": "Arrays: removing, inserting, and extracting elements"
    },
    {
        "question": "What does `for (let i = 0; i < 4; i++) { console.log(i); }` output?",
        "options": ["0 1 2 3", "1 2 3 4", "0 1 2", "Nothing"],
        "answer": "0 1 2 3",
        "difficulty": "Easy",
        "explanation": "The loop runs from `i = 0` to `i = 3`, logging each value.",
        "hint": "Trace loop iterations.",
        "topic": "for loops"
    },
    {
        "question": "What stops a loop if `arr[i] == 3` in a `for` loop?",
        "options": ["stop;", "break;", "exit;", "return;"],
        "answer": "break;",
        "difficulty": "Medium",
        "explanation": "`break` exits the loop immediately when the condition is met.",
        "hint": "Look for loop termination.",
        "topic": "for loops: flags, Booleans, array length, and breaks"
    },
    {
        "question": "What does `for (let i = 0; i < 2; i++) { for (let j = 0; j < 2; j++) { console.log(i + j); } }` output?",
        "options": ["0 1 1 2", "0 1 2 3", "0 0 1 1", "Nothing"],
        "answer": "0 1 1 2",
        "difficulty": "Medium",
        "explanation": "The inner loop runs for each outer loop iteration, logging sums: `0+0, 0+1, 1+0, 1+1`.",
        "hint": "Calculate nested loop outputs.",
        "topic": "for loops nested"
    },
    {
        "question": "What does `'javascript'.toLowerCase()` return?",
        "options": ["JAVASCRIPT", "javascript", "Javascript", "Error"],
        "answer": "javascript",
        "difficulty": "Easy",
        "explanation": "`toLowerCase()` converts a string to lowercase.",
        "hint": "Think about case conversion.",
        "topic": "Changing case"
    },
    {
        "question": "What is the length of `'coding'`?",
        "options": ["5", "6", "7", "8"],
        "answer": "6",
        "difficulty": "Easy",
        "explanation": "The `length` property counts the characters in the string.",
        "hint": "Count the characters.",
        "topic": "Strings: measuring length and extracting parts"
    },
    {
        "question": "What does `'Hello World'.indexOf('World')` return?",
        "options": ["5", "6", "-1", "7"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "`indexOf()` returns the starting index of 'World', which is 6 (after the space).",
        "hint": "Check substring position.",
        "topic": "Strings: finding segments"
    },
    {
        "question": "What does `'Code'.charAt(2)` return?",
        "options": ["C", "o", "d", "e"],
        "answer": "d",
        "difficulty": "Easy",
        "explanation": "`charAt(2)` returns the character at index 2, which is 'd'.",
        "hint": "Check index positions.",
        "topic": "Strings: finding a character at a location"
    },
    {
        "question": "What does `'Test'.replace('T', 'B')` return?",
        "options": ["Best", "Test", "BTest", "Error"],
        "answer": "Best",
        "difficulty": "Medium",
        "explanation": "`replace()` substitutes the first 'T' with 'B', resulting in 'Best'.",
        "hint": "Think about string replacement.",
        "topic": "Strings: replacing characters"
    },
    {
        "question": "What does `Math.round(7.8)` return?",
        "options": ["7", "8", "7.8", "9"],
        "answer": "8",
        "difficulty": "Easy",
        "explanation": "`Math.round()` rounds to the nearest integer, so 7.8 becomes 8.",
        "hint": "Check rounding rules.",
        "topic": "Rounding numbers"
    },
    {
        "question": "What range does `Math.random()` produce?",
        "options": ["0 to 100", "0 to 1", "1 to 10", "1 to 100"],
        "answer": "0 to 1",
        "difficulty": "Easy",
        "explanation": "`Math.random()` generates a float between 0 (inclusive) and 1 (exclusive).",
        "hint": "Think about random number range.",
        "topic": "Generating random numbers"
    },
    {
        "question": "What does `parseFloat('12.34')` return?",
        "options": ["12", "12.34", "'12.34'", "Error"],
        "answer": "12.34",
        "difficulty": "Easy",
        "explanation": "`parseFloat()` converts a string to a floating-point number.",
        "hint": "Check string-to-decimal conversion.",
        "topic": "Converting strings to integers and decimals"
    },
    {
        "question": "What does `Number('456')` return?",
        "options": ["456", "'456'", "Error", "undefined"],
        "answer": "456",
        "difficulty": "Easy",
        "explanation": "`Number()` converts a string to a number.",
        "hint": "Think about type conversion.",
        "topic": "Converting strings to numbers, numbers to strings"
    },
    {
        "question": "What does `(5.6789).toFixed(1)` return?",
        "options": ["5.7", "5.6", "5.67", "5.6789"],
        "answer": "5.7",
        "difficulty": "Medium",
        "explanation": "`toFixed(1)` rounds to 1 decimal place, returning '5.7' as a string.",
        "hint": "Check decimal precision.",
        "topic": "Controlling the length of decimals"
    },
    {
        "question": "How do you get the current date in JavaScript?",
        "options": ["new Date()", "getDate()", "Date.now()", "new Time()"],
        "answer": "new Date()",
        "difficulty": "Easy",
        "explanation": "`new Date()` creates a Date object with the current date and time.",
        "hint": "Think about date creation.",
        "topic": "Getting the current date and time"
    },
    {
        "question": "What does `new Date().getMonth()` return on June 22, 2025?",
        "options": ["5", "6", "7", "22"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "Months are 0-based, so June is 5.",
        "hint": "Check month indexing.",
        "topic": "Extracting parts of the date and time"
    },
    {
        "question": "How do you create a Date for March 15, 2025?",
        "options": ["new Date(2025, 3, 15)", "new Date(2025, 2, 15)", "new Date('2025-3-15')", "new Date(2025, 15, 3)"],
        "answer": "new Date(2025, 2, 15)",
        "difficulty": "Medium",
        "explanation": "Months are 0-based, so March is 2.",
        "hint": "Remember month indexing.",
        "topic": "Specifying a date and time"
    },
    {
        "question": "What does `date.setMonth(5)` do?",
        "options": ["Sets month to June", "Sets month to May", "Adds 5 months", "Nothing"],
        "answer": "Sets month to June",
        "difficulty": "Medium",
        "explanation": "`setMonth(5)` sets the month to June (0-based indexing).",
        "hint": "Check month modification.",
        "topic": "Changing elements of a date and time"
    },
    {
        "question": "How do you define a function named `greet`?",
        "options": ["function greet() {}", "greet = function {}", "def greet() {}", "function = greet()"],
        "answer": "function greet() {}",
        "difficulty": "Easy",
        "explanation": "Functions are defined with the `function` keyword, name, and body.",
        "hint": "Check function syntax.",
        "topic": "Functions"
    },
    {
        "question": "How do you pass two parameters to a function?",
        "options": ["function add(a, b) {}", "function add = a, b {}", "add(a, b) {}", "function add[a, b] {}"],
        "answer": "function add(a, b) {}",
        "difficulty": "Easy",
        "explanation": "Parameters are listed in parentheses in the function definition.",
        "hint": "Look at parameter syntax.",
        "topic": "Functions: passing them data"
    },
    {
        "question": "What does `function square(x) { return x * x; }` do when called with `square(4)`?",
        "options": ["Logs 16", "Returns 16", "Assigns 16", "Nothing"],
        "answer": "Returns 16",
        "difficulty": "Easy",
        "explanation": "`return x * x` sends back the square of the input, so `4 * 4 = 16`.",
        "hint": "Focus on the `return` statement.",
        "topic": "Functions: passing data back from them"
    },
    {
        "question": "What is a global variable?",
        "options": ["Declared inside a function", "Declared outside a function", "Only in loops", "Always constant"],
        "answer": "Declared outside a function",
        "difficulty": "Medium",
        "explanation": "Global variables are declared outside functions and are accessible everywhere.",
        "hint": "Think about variable scope.",
        "topic": "Functions: local vs. global variables"
    },
    {
        "question": "How do you start a `switch` statement for `day`?",
        "options": ["switch(day) {}", "case(day) {}", "switch day {}", "if(day) {}"],
        "answer": "switch(day) {}",
        "difficulty": "Easy",
        "explanation": "`switch` begins with the keyword and the expression in parentheses.",
        "hint": "Check switch syntax.",
        "topic": "switch statements: how to start them"
    },
    {
        "question": "What prevents fall-through in a `switch` case?",
        "options": ["break;", "return;", "end;", "stop;"],
        "answer": "break;",
        "difficulty": "Medium",
        "explanation": "`break` exits the `switch` statement, preventing the next case from executing.",
        "hint": "Think about case termination.",
        "topic": "switch statements: how to complete them"
    },
    {
        "question": "What does `while (x < 2) { console.log(x); x++; }` output if `x = 0`?",
        "options": ["0 1", "1 2", "0 1 2", "Nothing"],
        "answer": "0 1",
        "difficulty": "Medium",
        "explanation": "The loop runs while `x < 2`, logging `0` and `1`, then stops.",
        "hint": "Trace the loop condition.",
        "topic": "while loops"
    },
    {
        "question": "What does `do { console.log(x); x++; } while (x < 3);` do if `x = 2`?",
        "options": ["Logs 2", "Logs 2 3", "Nothing", "Infinite loop"],
        "answer": "Logs 2",
        "difficulty": "Medium",
        "explanation": "The `do...while` loop runs once, logging `2`, then stops since `x < 3` is false.",
        "hint": "Check minimum loop runs.",
        "topic": "do...while loops"
    },
    {
        "question": "Where is JavaScript code typically placed in HTML?",
        "options": ["<head>", "<body>", "<script>", "<div>"],
        "answer": "<script>",
        "difficulty": "Easy",
        "explanation": "JavaScript code goes inside `<script>` tags, often in `<head>` or `<body>`.",
        "hint": "Think about HTML tags for scripts.",
        "topic": "Placing scripts"
    },
    {
        "question": "How do you write a multi-line comment?",
        "options": ["// Comment", "/* Comment */", "<!-- Comment -->", "# Comment"],
        "answer": "/* Comment */",
        "difficulty": "Easy",
        "explanation": "`/* */` is used for multi-line comments in JavaScript.",
        "hint": "Check comment syntax.",
        "topic": "Commenting"
    },
    {
        "question": "What attribute triggers a function on clicking a link?",
        "options": ["onclick", "onhover", "onchange", "onlink"],
        "answer": "onclick",
        "difficulty": "Easy",
        "explanation": "`onclick` triggers a function when an element is clicked.",
        "hint": "Think about event attributes.",
        "topic": "Events: link"
    },
    {
        "question": "How do you add a click event to a button?",
        "options": ["<button onclick='func()'>", "<button onpress='func()'>", "<button click='func()'>", "<button event='click'>"],
        "answer": "<button onclick='func()'>",
        "difficulty": "Easy",
        "explanation": "`onclick` triggers a function when the button is clicked.",
        "hint": "Check button event syntax.",
        "topic": "Events: button"
    },
    
    {
        "question": "What does `'5' + 5` produce?",
        "options": ["10", "55", "5", "Error"],
        "answer": "55",
        "difficulty": "Medium",
        "explanation": "The `+` operator concatenates when one operand is a string, so `'5' + 5 = '55'`.",
        "hint": "Think about type coercion.",
        "topic": "Concatenating text strings"
    },
    {
        "question": "What is the result of `'20' !== 20`?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "`!==` checks value and type, so string `'20'` is not strictly equal to number `20`.",
        "hint": "Consider strict inequality.",
        "topic": "Comparison operators"
    },
    {
        "question": "What does `arr.slice(1, 3)` do for `arr = [1, 2, 3, 4]`?",
        "options": ["Returns [2, 3]", "Returns [1, 2]", "Removes [2, 3]", "Returns [3, 4]"],
        "answer": "Returns [2, 3]",
        "difficulty": "Medium",
        "explanation": "`slice(1, 3)` extracts elements from index 1 to 2 (3 exclusive).",
        "hint": "Check array extraction methods.",
        "topic": "Arrays: removing, inserting, and extracting elements"
    },
    {
        "question": "What does `Math.floor(9.7)` return?",
        "options": ["9", "10", "9.7", "8"],
        "answer": "9",
        "difficulty": "Easy",
        "explanation": "`Math.floor()` rounds down to the nearest integer.",
        "hint": "Think about rounding down.",
        "topic": "Rounding numbers"
    },
    {
        "question": "What does `function calc(x) { let y = x * 2; return y; }` return for `calc(3)`?",
        "options": ["6", "3", "Nothing", "Error"],
        "answer": "6",
        "difficulty": "Easy",
        "explanation": "The function returns `y`, which is `x * 2`, so `3 * 2 = 6`.",
        "hint": "Focus on the return value.",
        "topic": "Functions: passing data back from them"
    }
];
# Helper Functions
@st.cache_data
def shuffle_quiz(_quiz):
    """Shuffle quiz questions and options, ensuring varied difficulty sequence."""
    shuffled = random.sample(_quiz, len(_quiz))
    for i in range(len(shuffled) - 1):
        if shuffled[i]["difficulty"] == shuffled[i + 1]["difficulty"]:
            for j in range(i + 2, len(shuffled)):
                if shuffled[j]["difficulty"] != shuffled[i]["difficulty"]:
                    shuffled[i + 1], shuffled[j] = shuffled[j], shuffled[i + 1]
                    break
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        labeled_options = list(zip(q["options"], ["A", "B", "C", "D"]))
        random.shuffle(labeled_options)
        q["display_options"] = [f"{label}: {option}" for option, label in labeled_options]
        q["labeled_answer"] = next(f"{label}: {option}" for option, label in labeled_options if option == q["answer"])
    return shuffled

def toggle_theme():
    """Toggle between dark and light themes."""
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
    st.rerun()

def update_timer():
    """Update quiz timer and check for timeout."""
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.session_state.time_left = max(1800 - elapsed, 0)
    if st.session_state.time_left <= 0:
        st.session_state.show_results = True
        st.rerun()

def reset_quiz():
    """Reset quiz state to start a new session."""
    st.session_state.update({
        "quiz_data": shuffle_quiz(quiz) if quiz else [],
        "score": 0,
        "current_q": 0,
        "start_time": datetime.now(),
        "answers": [None] * len(quiz),
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 1800,
        "theme": "dark",
        "streak": 0,
        "show_hint": False,
        "started": False
    })
    st.rerun()

def show_progress_snapshot():
    """Display current quiz progress."""
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

# Initialize Session State
if "quiz_data" not in st.session_state:
    st.session_state.update({
        "quiz_data": shuffle_quiz(quiz) if quiz else [],
        "score": 0,
        "current_q": 0,
        "start_time": datetime.now(),
        "answers": [None] * len(quiz),
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 1800,
        "theme": "dark",
        "streak": 0,
        "show_hint": False,
        "started": False
    })

# VS Code-like CSS Styling
st.markdown("""
    <style>
    body {
        background: var(--bg-gradient);
        color: var(--text-color);
        font-family: 'Source Code Pro', 'Consolas', monospace;
        transition: all 0.3s ease;
    }
    :root {
        --bg-gradient: linear-gradient(180deg, #1e1e2e, #2e2e3e);
        --bg-container: #252526;
        --text-color: #d4d4d4;
        --button-bg: linear-gradient(45deg, #0078d4, #00b4ff);
        --button-hover: linear-gradient(45deg, #005a9e, #0088cc);
        --code-bg: #1e1e1e;
        --shadow: rgba(0,0,0,0.4);
        --accent: #0ea5e9;
        --correct: #2ea043;
        --wrong: #ef4444;
    }
    [data-theme="light"] {
        --bg-gradient: linear-gradient(180deg, #f5f5f5, #e5e5e5);
        --bg-container: #ffffff;
        --text-color: #1e1e1e;
        --button-bg: linear-gradient(45deg, #2563eb, #3b82f6);
        --button-hover: linear-gradient(45deg, #1e40af, #2563eb);
        --code-bg: #f5f5f5;
        --shadow: rgba(0,0,0,0.2);
        --accent: #2563eb;
        --correct: #15803d;
        --wrong: #dc2626;
    }
    .main-container {
        background: var(--bg-container);
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 16px var(--shadow);
        max-width: 800px;
        margin: 20px auto;
        border: 1px solid #3c3c3c;
    }
    .stButton>button {
        background: var(--button-bg);
        color: var(--text-color);
        border: none;
        border-radius: 6px;
        padding: 10px;
        width: 100%;
        font-size: 14px;
        font-family: 'Source Code Pro', 'Consolas', monospace;
        margin: 5px 0;
        cursor: pointer;
        transition: all 0.3s ease;
        transform: scale(1);
    }
    .stButton>button:hover {
        background: var(--button-hover);
        transform: scale(1.02);
        box-shadow: 0 2px 8px var(--shadow);
    }
    .stButton>button:disabled {
        background: #4b4b6b;
        cursor: not-allowed;
        transform: scale(1);
    }
    .selected-correct {
        background: var(--correct) !important;
        transform: scale(1.02);
    }
    .selected-wrong {
        background: var(--wrong) !important;
        transform: scale(1.02);
    }
    .question-container {
        background: var(--code-bg);
        padding: 15px;
        border-radius: 6px;
        border: 1px solid #3c3c3c;
        margin-bottom: 15px;
    }
    .feedback-correct {
        color: var(--correct);
        font-weight: 600;
        font-size: 16px;
        margin: 10px 0;
        animation: fadeIn 0.5s ease;
    }
    .feedback-wrong {
        color: var(--wrong);
        font-weight: 600;
        font-size: 16px;
        margin: 10px 0;
        animation: fadeIn 0.5s ease;
    }
    .progress-bar {
        background: #3c3c3c;
        border-radius: 6px;
        height: 10px;
        margin: 10px 0;
        position: relative;
    }
    .progress-fill {
        background: var(--accent);
        height: 100%;
        border-radius: 6px;
        transition: width 0.5s ease;
    }
    .progress-text {
        position: absolute;
        top: -18px;
        right: 0;
        color: var(--text-color);
        font-size: 12px;
    }
    .title {
        font-size: 28px;
        text-align: center;
        margin-bottom: 5px;
        color: var(--accent);
        font-family: 'Source Code Pro', 'Consolas', monospace;
    }
    .caption {
        text-align: center;
        color: #8b8b8b;
        font-size: 14px;
        margin-bottom: 15px;
    }
    .timer {
        font-size: 14px;
        color: var(--wrong);
        font-weight: 600;
        text-align: center;
        margin-top: 10px;
    }
    .difficulty {
        font-size: 12px;
        color: #8b8b8b;
        margin-bottom: 10px;
    }
    .stCodeBlock {
        background-color: var(--code-bg) !important;
        border-radius: 6px;
        padding: 10px;
        font-family: 'Source Code Pro', 'Consolas', monospace;
        font-size: 13px;
        line-height: 1.5;
        border: 1px solid #3c3c3c;
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
            padding: 10px;
            margin: 10px;
        }
        .title {
            font-size: 24px;
        }
        .stButton>button {
            font-size: 13px;
            padding: 8px;
        }
    }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
""", unsafe_allow_html=True)

# Main UI
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 JavaScript Quiz Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Test Your JavaScript Mastery!</p>', unsafe_allow_html=True)

# Theme Toggle
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()

# Welcome Screen
if not st.session_state.started:
    st.markdown("""
        <div style="text-align: center;">
            <p style="color: var(--text-color); font-size: 16px;">Challenge yourself with 50 JavaScript questions!</p>
            <p style="color: #8b8b8b;">30 minutes, 2 points per correct answer. Ready to code?</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Start Quiz", key="start_quiz"):
        st.session_state.started = True
        st.session_state.start_time = datetime.now()
        st.rerun()

# Quiz Logic
elif not st.session_state.quiz_data:
    st.error("No quiz questions available.")
else:
    # Timer
    if not st.session_state.show_results:
        update_timer()
        minutes, seconds = divmod(int(st.session_state.time_left), 60)
        st.markdown(f'<div class="timer">⏰ Time Left: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

    # Progress Bar
    progress = st.session_state.current_q / len(st.session_state.quiz_data)
    progress_percentage = int(progress * 100)
    st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress_percentage}%"></div>
            <div class="progress-text">{progress_percentage}%</div>
        </div>
        <div style="color: var(--text-color); font-size: 12px; text-align: center;">
            Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
        </div>
    """, unsafe_allow_html=True)

    # Question Display
    if not st.session_state.show_results:
        with st.container():
            st.markdown('<div class="question-container">', unsafe_allow_html=True)
            q = st.session_state.quiz_data[st.session_state.current_q]

            # Difficulty, Topic, and Streak
            st.markdown(f'<div class="difficulty">Difficulty: {q["difficulty"]} | Topic: {q["topic"]} | Streak: 🔥 {st.session_state.streak}</div>', unsafe_allow_html=True)

            # Display Question and Code Snippet
            if "```javascript" in q["question"]:
                parts = q["question"].split("```javascript\n")
                question_text = parts[0].strip()
                code_snippet = parts[1].split("```")[0].strip()
                st.markdown(f"### Question {st.session_state.current_q + 1}")
                st.markdown(f"**{question_text}**")
                st.code(code_snippet, language="javascript")
            else:
                st.markdown(f"### Question {st.session_state.current_q + 1}")
                st.markdown(f"**{q['question']}**")

            # Option Buttons
            for i, option in enumerate(q["display_options"]):
                button_class = "selected-correct" if st.session_state.selected_option == option and option == q["labeled_answer"] else \
                               "selected-wrong" if st.session_state.selected_option == option else ""
                if st.button(option, key=f"q{i}", disabled=st.session_state.selected_option is not None, help="Select this option"):
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
                        "difficulty": q["difficulty"],
                        "topic": q["topic"]
                    }
                    if is_correct:
                        points = {"Easy": 1, "Medium": 2, "Hard": 3}.get(q["difficulty"], 2)
                        st.session_state.score += points
                        st.session_state.streak += 1
                        if st.session_state.streak >= 3:
                            st.session_state.score += 1
                    else:
                        st.session_state.streak = 0
                    st.rerun()

            # Feedback
            if st.session_state.feedback:
                if st.session_state.feedback["is_correct"]:
                    st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div style="color: var(--text-color); font-size: 13px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

            # Hint
            if st.button("💡 Show Hint", key="hint", disabled=st.session_state.show_hint or st.session_state.selected_option is not None):
                st.session_state.show_hint = True
                st.session_state.score = max(0, st.session_state.score - 0.5)
                st.rerun()
            if st.session_state.show_hint:
                st.markdown(f'<div style="color: #facc15; font-size: 13px;">Hint: {q["hint"]}</div>', unsafe_allow_html=True)

            # Navigation
            col1, col2 = st.columns(2)
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

            # Reset Quiz
            if st.button("🔄 Reset Quiz", key="reset"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

    # Results Screen
    else:
        st.markdown('<h2 style="color: var(--accent); text-align: center;">🎉 Quiz Completed!</h2>', unsafe_allow_html=True)
        answered = sum(1 for ans in st.session_state.answers if ans is not None)
        correct = sum(1 for ans in st.session_state.answers if ans and ans["is_correct"])
        st.markdown(f"""
            <div style="text-align: center; color: var(--text-color);">
                <p><strong>Final Score:</strong> {st.session_state.score} points</p>
                <p><strong>Correct Answers:</strong> {correct}/{answered}</p>
                <p><strong>Accuracy:</strong> {int((correct / answered) * 100) if answered > 0 else 0}%</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("### Review Your Answers")
        for i, ans in enumerate(st.session_state.answers):
            if ans:
                status = "✅ Correct" if ans["is_correct"] else "❌ Incorrect"
                color = "var(--correct)" if ans["is_correct"] else "var(--wrong)"
                st.markdown(f"""
                    <div style="background: var(--code-bg); padding: 10px; border-radius: 6px; margin: 5px 0; border: 1px solid #3c3c3c;">
                        <strong>Question {i + 1}:</strong> {ans['question']}<br>
                        <strong>Your Answer:</strong> {ans['user_answer']}<br>
                        <strong>Correct Answer:</strong> {ans['correct_answer']}<br>
                        <strong>Status:</strong> <span style="color: {color};">{status}</span><br>
                        <strong>Difficulty:</strong> {ans['difficulty']}<br>
                        <strong>Topic:</strong> {ans['topic']}
                    </div>
                """, unsafe_allow_html=True)

        if st.button("🔄 Try Again", key="try_again"):
            reset_quiz()

st.markdown("</div>", unsafe_allow_html=True)

