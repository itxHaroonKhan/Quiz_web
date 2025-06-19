
import streamlit as st
import random
from datetime import datetime
import uuid

quiz = [
    {
        "question": "What will `if (7 > 4) { console.log('True'); }` output?",
        "options": ["True", "False", "Nothing", "Error"],
        "answer": "True",
        "difficulty": "Medium",
        "explanation": "The condition `7 > 4` is true, so 'True' is logged.",
        "hint": "Evaluate the `if` condition.",
        "topic": "if statements"
    },
    {
        "question": "What is the result of `'10' == 10` in JavaScript?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The `==` operator performs type coercion, so `'10'` is converted to the number 10, making the comparison true.",
        "hint": "Compare loose equality behavior.",
        "topic": "Comparison operators"
    },
    {
        "question": "What will be output: `let x = 15; if (x < 10) { console.log('Small'); } else if (x < 20) { console.log('Medium'); } else { console.log('Large'); }`?",
        "options": ["Small", "Medium", "Large", "Nothing"],
        "answer": "Medium",
        "difficulty": "Medium",
        "explanation": "Since `x = 15` is less than 20 but not less than 10, 'Medium' is logged.",
        "hint": "Check which condition matches.",
        "topic": "if...else and else if statements"
    },
    {
        "question": "What is the result of `if (4 > 2 && 3 < 5) { console.log('Yes'); }`?",
        "options": ["Yes", "No", "Nothing", "Error"],
        "answer": "Yes",
        "difficulty": "Medium",
        "explanation": "Both `4 > 2` and `3 < 5` are true, so the `&&` operator evaluates to true, logging 'Yes'.",
        "hint": "Evaluate the logical operator.",
        "topic": "Testing sets of conditions"
    },
    {
        "question": "What will be output: `let x = 7; if (x > 5) { if (x < 10) { console.log('In Range'); } }`?",
        "options": ["In Range", "Out of Range", "Nothing", "Error"],
        "answer": "In Range",
        "difficulty": "Medium",
        "explanation": "Both conditions (`x > 5` and `x < 10`) are true for `x = 7`, so 'In Range' is logged.",
        "hint": "Trace nested conditions.",
        "topic": "if statements nested"
    },
    {
        "question": "Which creates an array in JavaScript?",
        "options": ["let arr = {};", "let arr = [];", "let arr = '';", "let arr = null;"],
        "answer": "let arr = [];",
        "difficulty": "Medium",
        "explanation": "Arrays are created with square brackets `[]`. Curly braces `{}` create objects.",
        "hint": "Recall array syntax.",
        "topic": "Arrays"
    },
    {
        "question": "What does `arr.push(4)` do to `arr = [1, 2, 3]`?",
        "options": ["[1, 2, 3, 4]", "[4, 1, 2, 3]", "[1, 2, 4]", "[4]"],
        "answer": "[1, 2, 3, 4]",
        "difficulty": "Medium",
        "explanation": "`push(4)` adds 4 to the end of the array, resulting in `[1, 2, 3, 4]`.",
        "hint": "Think about adding to the end of an array.",
        "topic": "Arrays: adding and removing elements"
    },
    {
        "question": "What does `arr.splice(1, 1)` do to `arr = [1, 2, 3]`?",
        "options": ["Removes 1", "Removes 2", "Removes 3", "Clears the array"],
        "answer": "Removes 2",
        "difficulty": "Medium",
        "explanation": "`splice(1, 1)` removes 1 element at index 1, so `2` is removed, leaving `[1, 3]`.",
        "hint": "Check `splice()` parameters.",
        "topic": "Arrays: removing, inserting, and extracting elements"
    },
    {
        "question": "What will `for (let i = 0; i < 3; i++) { console.log(i); }` output?",
        "options": ["0, 1, 2", "1, 2, 3", "0, 1", "Nothing"],
        "answer": "0, 1, 2",
        "difficulty": "Medium",
        "explanation": "The loop runs from `i = 0` to `i < 3`, logging `0`, `1`, and `2`.",
        "hint": "Trace the loop counter.",
        "topic": "for loops"
    },
    {
        "question": "What will be output: `let arr = [1, 2, 3]; for (let i = 0; i < arr.length; i++) { if (arr[i] === 2) break; console.log(arr[i]); }`?",
        "options": ["1", "1, 2", "1, 2, 3", "Nothing"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "The loop stops at `arr[i] === 2` due to `break`, so only `1` is logged.",
        "hint": "Consider the `break` statement.",
        "topic": "for loops: flags, Booleans, array length, and breaks"
    },
    {
        "question": "What will be output: `for (let i = 1; i <= 2; i++) { for (let j = 1; j <= 2; j++) { console.log(i * j); } }`?",
        "options": ["1, 2, 2, 4", "1, 2, 3, 4", "1, 1, 2, 2", "Nothing"],
        "answer": "1, 2, 2, 4",
        "difficulty": "Medium",
        "explanation": "The loop outputs products: `1*1=1`, `1*2=2`, `2*1=2`, `2*2=4`.",
        "hint": "Trace nested loop iterations.",
        "topic": "for loops nested"
    },
    {
        "question": "What is the result of `'hello'.toUpperCase()`?",
        "options": ["HELLO", "hello", "Hello", "hELLO"],
        "answer": "HELLO",
        "difficulty": "Medium",
        "explanation": "`toUpperCase()` converts moje characters to uppercase, resulting in 'HELLO'.",
        "hint": "Think about case transformation.",
        "topic": "Changing case"
    },
    {
        "question": "What is the result of `'JavaScript'.substring(0, 4)`?",
        "options": ["Java", "Scri", "JavaS", "Script"],
        "answer": "Java",
        "difficulty": "Medium",
        "explanation": "`substring(0, 4)` extracts characters from index 0 to 3, resulting in 'Java'.",
        "hint": "Check `substring()` indices.",
        "topic": "Strings: measuring length and extracting parts"
    },
    {
        "question": "What does `'Hello World'.indexOf('World')` return?",
        "options": ["0", "5", "6", "-1"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "`indexOf('World')` returns the starting index of 'World', which is 6 (after 'Hello ').",
        "hint": "Locate 'World' in the string.",
        "topic": "Strings: finding segments"
    },
    {
        "question": "What does `'Test'.charAt(1)` return?",
        "options": ["T", "e", "s", "t"],
        "answer": "e",
        "difficulty": "Medium",
        "explanation": "`charAt(1)` returns the character at index 1, which is 'e' in 'Test'.",
        "hint": "Count characters from index 0.",
        "topic": "Strings: finding a character at a location"
    },
    {
        "question": "What is the result of `'Hello moje'.replace('moje', 'Everyone')`?",
        "options": ["Hello Everyone", "Hello moje", "Everyone moje", "Hello"],
        "answer": "Hello Everyone",
        "difficulty": "Medium",
        "explanation": "`replace()` substitutes 'moje' with 'Everyone', resulting in 'Hello Everyone'.",
        "hint": "Think about string replacement.",
        "topic": "Strings: replacing characters"
    },
    {
        "question": "What is the result of `Math.round(5.8)`?",
        "options": ["5", "6", "5.5", "7"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "`Math.round()` rounds to the nearest integer. Since 5.8 is closer to 6, it returns 6.",
        "hint": "Consider rounding rules.",
        "topic": "Rounding numbers"
    },
    {
        "question": "How do you generate a random integer from 1 to 10?",
        "options": ["Math.random() * 10", "Math.floor(Math.random() * 10) + 1", "Math.round(Math.random() * 10)", "Math.random(1, 10)"],
        "answer": "Math.floor(Math.random() * 10) + 1",
        "difficulty": "Medium",
        "explanation": "`Math.random() * 10` gives 0 to 9.999..., `Math.floor()` rounds down to 0–9, and `+1` shifts to 1–10.",
        "hint": "Scale and shift a random number.",
        "topic": "Generating random numbers"
    },
    {
        "question": "What does `parseInt('123.45')` return?",
        "options": ["123.45", "123", "124", "NaN"],
        "answer": "123",
        "difficulty": "Medium",
        "explanation": "`parseInt()` converts a string to an integer, stopping at the decimal, so '123.45' becomes 123.",
        "hint": "Think about integer conversion.",
        "topic": "Converting strings to integers and decimals"
    },
    {
        "question": "How do you convert the number 42 to a string?",
        "options": ["42.toString()", "String(42)", "parseInt(42)", "Both 42.toString() and String(42)"],
        "answer": "Both 42.toString() and String(42)",
        "difficulty": "Medium",
        "explanation": "Both `42.toString()` and `String(42)` convert 42 to the string '42'.",
        "hint": "Consider number-to-string methods.",
        "topic": "Converting strings to numbers, numbers to strings"
    },
    {
        "question": "What does `3.14159.toFixed(2)` return?",
        "options": ["3.14", "3.141", "3.15", "3.14159"],
        "answer": "3.14",
        "difficulty": "Medium",
        "explanation": "`toFixed(2)` rounds to 2 decimal places, returning '3.14' as a string.",
        "hint": "Check decimal formatting.",
        "topic": "Controlling the length of decimals"
    },
    {
        "question": "What does `new Date()` return?",
        "options": ["A string", "A Date object", "A timestamp", "A formatted date"],
        "answer": "A Date object",
        "difficulty": "Medium",
        "explanation": "`new Date()` creates a Date object for the current date and time.",
        "hint": "Think about the Date constructor.",
        "topic": "Getting the current date and time"
    },
    {
        "question": "What does `new Date().getFullYear()` return in 2025?",
        "options": ["2024", "2025", "25", "2026"],
        "answer": "2025",
        "difficulty": "Medium",
        "explanation": "`getFullYear()` returns the four-digit year, e.g., 2025.",
        "hint": "Consider Date object methods.",
        "topic": "Extracting parts of the date and time"
    },
    {
        "question": "Which creates a Date object for April 1, 2025?",
        "options": ["new Date(2025, 4, 1)", "new Date(2025, 3, 1)", "new Date('2025-04-01')", "Both new Date(2025, 3, 1) and new Date('2025-04-01')"],
        "answer": "Both new Date(2025, 3, 1) and new Date('2025-04-01')",
        "difficulty": "Medium",
        "explanation": "April is month 3 (0-based), and '2025-04-01' is a valid string format.",
        "hint": "Check month indexing.",
        "topic": "Specifying a date and time"
    },
    {
        "question": "What does `date.setFullYear(2026)` do to a Date object?",
        "options": ["Sets the month to 2026", "Sets the year to 2026", "Sets the day to 2026", "Sets the timestamp"],
        "answer": "Sets the year to 2026",
        "difficulty": "Medium",
        "explanation": "`setFullYear(2026)` updates the year of the Date object to 2026.",
        "hint": "Think about Date modification.",
        "topic": "Changing elements of a date and time"
    },
    {
        "question": "What is the correct function declaration syntax?",
        "options": ["function myFunc() {}", "myFunc() {}", "func myFunc() {}", "function = myFunc() {}"],
        "answer": "function myFunc() {}",
        "difficulty": "Medium",
        "explanation": "Functions are declared with the `function` keyword, a name, and a body.",
        "hint": "Recall function syntax.",
        "topic": "Functions"
    },
    {
        "question": "What will `function add(a, b) { console.log(a + b); } add(2, 3);` output?",
        "options": ["5", "23", "Nothing", "Error"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The function adds `2 + 3` and logs 5.",
        "hint": "Trace the function parameters.",
        "topic": "Functions: passing them data"
    },
    {
        "question": "What does `function square(n) { return n * n; } square(3);` return?",
        "options": ["6", "9", "3", "Nothing"],
        "answer": "9",
        "difficulty": "Medium",
        "explanation": "The function returns `3 * 3 = 9`.",
        "hint": "Focus on the `return` statement.",
        "topic": "Functions: passing data back from them"
    },
    {
        "question": "What is the scope of `let x` inside a function?",
        "options": ["Global", "Local to the function", "Browser scope", "Global and local"],
        "answer": "Local to the function",
        "difficulty": "Medium",
        "explanation": "`let` variables inside a function are local and not accessible outside.",
        "hint": "Think about variable scope.",
        "topic": "Functions: local vs. global variables"
    },
    {
        "question": "What is the correct `switch` statement syntax?",
        "options": ["switch (x) {}", "switch x {}", "case (x) {}", "switch { x }"],
        "answer": "switch (x) {}",
        "difficulty": "Medium",
        "explanation": "A `switch` statement starts with `switch (expression) {}`.",
        "hint": "Recall `switch` structure.",
        "topic": "switch statements: how to start them"
    },
    {
        "question": "What happens if `break` is omitted in a `switch` case?",
        "options": ["Skips the case", "Executes the next case", "Throws an error", "Exits the switch"],
        "answer": "Executes the next case",
        "difficulty": "Medium",
        "explanation": "Without `break`, execution falls through to the next case.",
        "hint": "Think about fall-through behavior.",
        "topic": "switch statements: how to complete them"
    },
    {
        "question": "What will `let i = 0; while (i < 2) { console.log(i); i++; }` output?",
        "options": ["0, 1", "1, 2", "0, 1, 2", "Nothing"],
        "answer": "0, 1",
        "difficulty": "Medium",
        "explanation": "The loop runs while `i < 2`, logging `0` and `1`.",
        "hint": "Trace the loop condition.",
        "topic": "while loops"
    },
    {
        "question": "What will `let i = 3; do { console.log(i); i++; } while (i < 3);` output?",
        "options": ["Nothing", "3", "3, 4", "2, 3"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "The `do...while` loop runs once, logging `3`, then stops since `i < 3` is false.",
        "hint": "Recall `do...while` behavior.",
        "topic": "do...while loops"
    },
    {
        "question": "Where should a `<script>` tag be placed in an HTML document to ensure it loads after the DOM is fully parsed?",
        "options": ["At the start of `<head>`", "At the end of `<body>`", "In the `<footer>`", "Before the `<html>` tag"],
        "answer": "At the end of `<body>`",
        "difficulty": "Medium",
        "explanation": "Placing the `<script>` tag at the end of `<body>` ensures the DOM is fully parsed before the JavaScript executes, preventing errors from accessing unrendered elements.",
        "hint": "Consider when the DOM is ready for JavaScript to access.",
        "topic": "Placing scripts"
    },
    {
        "question": "Which of the following is a valid single-line comment in JavaScript?",
        "options": ["// This is a comment", "# This is a comment", "<!-- This is a comment -->", "/* This is a comment */"],
        "answer": "// This is a comment",
        "difficulty": "Medium",
        "explanation": "In JavaScript, single-line comments start with `//`. `/* */` is for multi-line comments, `<!-- -->` is for HTML, and `#` is not used for comments.",
        "hint": "Look for the syntax used in JavaScript for inline notes.",
        "topic": "Commenting"
    },
    {
        "question": "How do you add a click event listener to an HTML `<a>` link element in JavaScript?",
        "options": ["link.onclick = function() {}", "link.addEvent('click', function() {})", "link.on('click', function() {})", "link.click(function() {})"],
        "answer": "link.onclick = function() {}",
        "difficulty": "Medium",
        "explanation": "The `onclick` property or `addEventListener('click', function() {})` can be used to handle click events on a link. The first option is a valid and common approach.",
        "hint": "Think about how to handle user clicks on a hyperlink.",
        "topic": "Events: link"
    },
    {
        "question": "What is the correct way to attach a click event to a button element with ID 'myButton' in JavaScript?",
        "options": ["document.getElementById('myButton').addEventListener('click', function() {})", "button.onClick('myButton', function() {})", "document.getElementById('myButton').click = function() {}", "document.querySelector('myButton').onclick(function() {})"],
        "answer": "document.getElementById('myButton').addEventListener('click', function() {})",
        "difficulty": "Medium",
        "explanation": "`addEventListener('click', function() {})` is the standard way to attach a click event to a button, allowing multiple listeners and better control.",
        "hint": "Consider modern JavaScript event handling for buttons.",
        "topic": "Events: button"
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

