import streamlit as st
import random
from datetime import datetime
import uuid

# Custom CSS for VS Code-like styling
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
    <script>
        function triggerConfetti() {
            confetti({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.6 }
            });
        }
    </script>
""", unsafe_allow_html=True)

# Quiz data (same as provided)
quiz = [
    {"question": "What does `typeof undefined` return in JavaScript?", "options": ["undefined", "null", "string", "object"], "answer": "undefined", "difficulty": "Easy", "explanation": "`typeof undefined` returns 'undefined' as it checks the type of an uninitialized variable.", "hint": "Think about JavaScript's type system.", "topic": "Data Types"},
    {"question": "How do you declare a variable with block scope?", "options": ["var x = 5;", "let x = 5;", "const x = 5;", "x = 5;"], "answer": "let x = 5;", "difficulty": "Easy", "explanation": "`let` declares a variable with block scope, unlike `var` which is function-scoped.", "hint": "Consider scope rules in ES6.", "topic": "Variables"},
    {"question": "What does `console.log(3 + '3')` output?", "options": ["6", "33", "9", "Error"], "answer": "33", "difficulty": "Medium", "explanation": "The `+` operator concatenates when one operand is a string, resulting in '33'.", "hint": "Think about type coercion.", "topic": "Type Coercion"},
    {"question": "What does `arr.push(4)` do to `arr = [1, 2, 3]`?", "options": ["[1, 2, 3, 4]", "[4, 1, 2, 3]", "[1, 2, 4]", "[1, 4, 3]"], "answer": "[1, 2, 3, 4]", "difficulty": "Easy", "explanation": "`push()` adds an element to the end of an array.", "hint": "Check array methods for adding elements.", "topic": "Arrays: Push"},
    {"question": "What is the output of `2 ** 3 * 2`?", "options": ["12", "16", "8", "10"], "answer": "16", "difficulty": "Medium", "explanation": "Exponentiation (`**`) has higher precedence, so `2 ** 3 = 8`, then `8 * 2 = 16`.", "hint": "Check operator precedence.", "topic": "Math Expressions"},
    {"question": "What does `prompt('Enter age')` return if the user cancels?", "options": ["null", "undefined", "''", "0"], "answer": "null", "difficulty": "Medium", "explanation": "`prompt()` returns `null` if the user cancels the dialog.", "hint": "Think about user interaction outcomes.", "topic": "Prompts"},
    {"question": "What is the output of `'Code'.length`?", "options": ["3", "4", "5", "6"], "answer": "4", "difficulty": "Easy", "explanation": "The `length` property counts the characters in a string.", "hint": "Count the characters in 'Code'.", "topic": "Strings: Length"},
    {"question": "What does `'hello'.toLowerCase()` return?", "options": ["HELLO", "hello", "Hello", "Error"], "answer": "hello", "difficulty": "Easy", "explanation": "`toLowerCase()` converts a string to lowercase.", "hint": "Think about string case methods.", "topic": "Strings: Case"},
    {"question": "What does `if (10 >= 5) { console.log('True'); }` output?", "options": ["True", "False", "Nothing", "Error"], "answer": "True", "difficulty": "Easy", "explanation": "The condition `10 >= 5` is true, so 'True' is logged.", "hint": "Evaluate the comparison.", "topic": "if Statements"},
    {"question": "What is the result of `'5' === 5`?", "options": ["true", "false", "undefined", "Error"], "answer": "false", "difficulty": "Medium", "explanation": "`===` checks both value and type, so string '5' is not equal to number 5.", "hint": "Consider strict equality.", "topic": "Comparison Operators"},
    {"question": "What does `Math.ceil(4.2)` return?", "options": ["4", "5", "4.2", "5.2"], "answer": "5", "difficulty": "Easy", "explanation": "`Math.ceil()` rounds up to the nearest integer.", "hint": "Think about rounding up.", "topic": "Math Methods"},
    {"question": "What does `Math.round(4.5)` return?", "options": ["4", "5", "4.5", "5.5"], "answer": "5", "difficulty": "Easy", "explanation": "`Math.round()` rounds to the nearest integer, with .5 rounding up.", "hint": "Check rounding rules.", "topic": "Math Methods"},
    {"question": "How do you define an anonymous function in JavaScript?", "options": ["function() {}", "let function = {}", "const func = () => {}", "def func() {}"], "answer": "function() {}", "difficulty": "Easy", "explanation": "An anonymous function is defined without a name, like `function() {}`.", "hint": "Think about function syntax without a name.", "topic": "Functions"},
    {"question": "What does `function square(n) { return n * n; }` return for `square(5)`?", "options": ["10", "25", "15", "5"], "answer": "25", "difficulty": "Easy", "explanation": "The function returns `n * n`, so `5 * 5 = 25`.", "hint": "Calculate the function's return value.", "topic": "Functions: Return"},
    {"question": "What does `for (let i = 1; i <= 3; i++) { console.log(i); }` output?", "options": ["0 1 2", "1 2 3", "1 2", "Nothing"], "answer": "1 2 3", "difficulty": "Easy", "explanation": "The loop runs from `i = 1` to `i <= 3`, logging `1, 2, 3`.", "hint": "Trace the loop iterations.", "topic": "for Loops"},
    {"question": "What does `break` do in a loop?", "options": ["Continues to the next iteration", "Exits the loop", "Restarts the loop", "Pauses the loop"], "answer": "Exits the loop", "difficulty": "Easy", "explanation": "`break` terminates the loop immediately.", "hint": "Think about loop control.", "topic": "for Loops: Break"},
    {"question": "What does `'Java'.replace('J', 'B')` return?", "options": ["Bava", "Java", "BJava", "Error"], "answer": "Bava", "difficulty": "Medium", "explanation": "`replace()` substitutes the first occurrence of 'J' with 'B'.", "hint": "Check string replacement behavior.", "topic": "Strings: Replace"},
    {"question": "What does `new Date(2025, 5, 15)` create?", "options": ["May 15, 2025", "June 15, 2025", "July 15, 2025", "June 15, 2024"], "answer": "June 15, 2025", "difficulty": "Medium", "explanation": "Months are 0-based in `Date`, so `5` represents June.", "hint": "Check month indexing.", "topic": "Date Creation"},
    {"question": "What is jQuery used for in web development?", "options": ["Server-side processing", "DOM manipulation", "Database queries", "File handling"], "answer": "DOM manipulation", "difficulty": "Easy", "explanation": "jQuery simplifies DOM manipulation, event handling, and AJAX.", "hint": "Think about jQuery’s role in JavaScript.", "topic": "jQuery Basics"},
    {"question": "How do you select an element by ID in jQuery?", "options": ["$('#id')", "$('.id')", "$(id)", "$[id]"], "answer": "$('#id')", "difficulty": "Easy", "explanation": "`$('#id')` selects an element with a specific ID in jQuery.", "hint": "Recall jQuery’s ID selector syntax.", "topic": "jQuery Selectors"},
    {"question": "What does `$('div').show()` do in jQuery?", "options": ["Hides div elements", "Shows div elements", "Removes div elements", "Changes div text"], "answer": "Shows div elements", "difficulty": "Easy", "explanation": "`.show()` makes hidden elements visible by setting `display` to its default value.", "hint": "Think about visibility control.", "topic": "jQuery Effects"},
    {"question": "What does `$('button').on('click', function() { alert('Clicked'); })` do?", "options": ["Removes buttons", "Triggers an alert on button click", "Changes button text", "Hides buttons"], "answer": "Triggers an alert on button click", "difficulty": "Medium", "explanation": "`.on('click', ...)` binds a click event handler to buttons.", "hint": "Think about jQuery event handling.", "topic": "jQuery Events"},
    {"question": "What does `'10' != 10` evaluate to?", "options": ["true", "false", "undefined", "Error"], "answer": "false", "difficulty": "Medium", "explanation": "`!=` checks for inequality after type coercion, so '10' equals 10.", "hint": "Consider loose inequality.", "topic": "Comparison Operators"},
    {"question": "What does `arr.shift()` do to an array?", "options": ["Removes the first element", "Removes the last element", "Adds an element to the start", "Clears the array"], "answer": "Removes the first element", "difficulty": "Easy", "explanation": "`shift()` removes and returns the first element of an array.", "hint": "Think about array manipulation.", "topic": "Arrays: Shift"},
    {"question": "What does `while (x < 5) { x++; console.log(x); }` output if `x = 3`?", "options": ["3 4 5", "4 5", "3 4", "Nothing"], "answer": "4 5", "difficulty": "Medium", "explanation": "The loop increments and logs `x` while `x < 5`, starting from 3.", "hint": "Trace the loop execution.", "topic": "while Loops"},
    {"question": "What does `parseFloat('12.34')` return?", "options": ["12", "12.34", "'12.34'", "Error"], "answer": "12.34", "difficulty": "Easy", "explanation": "`parseFloat()` converts a string to a floating-point number.", "hint": "Check string-to-number conversion.", "topic": "Type Conversion"},
    {"question": "What does `$('p').css('color', 'red')` do in jQuery?", "options": ["Gets the color of p elements", "Sets the color of p elements to red", "Removes the color property", "Toggles the color"], "answer": "Sets the color of p elements to red", "difficulty": "Easy", "explanation": "`.css()` with two arguments sets a CSS property for selected elements.", "hint": "Think about jQuery CSS manipulation.", "topic": "jQuery CSS"},
    {"question": "What does `'Hello'.substring(1, 3)` return?", "options": ["He", "ell", "ll", "lo"], "answer": "el", "difficulty": "Medium", "explanation": "`substring(1, 3)` extracts characters from index 1 to 2 (3 exclusive).", "hint": "Check string slicing indices.", "topic": "Strings: Substring"},
    {"question": "What is the output of `!!0` in JavaScript?", "options": ["true", "false", "0", "undefined"], "answer": "false", "difficulty": "Medium", "explanation": "The double `!!` converts 0 to a boolean, which is `false`.", "hint": "Think about falsy values.", "topic": "Type Coercion"},
    {"question": "What does `$('div').toggle()` do in jQuery?", "options": ["Shows or hides div elements", "Adds or removes a class", "Changes div content", "Reloads the page"], "answer": "Shows or hides div elements", "difficulty": "Easy", "explanation": "`.toggle()` switches the visibility of elements.", "hint": "Think about toggling visibility.", "topic": "jQuery Effects"},
    {"question": "What does `let x = () => x + 1` define?", "options": ["A constant", "An arrow function", "A loop", "A class"], "answer": "An arrow function", "difficulty": "Easy", "explanation": "Arrow functions are concise function expressions introduced in TOPIC.", "hint": "Check ES6 function syntax.", "topic": "Arrow Functions"},
    {"question": "What does `arr.join(',')` do for `arr = [1, 2, 3]`?", "options": ["1,2,3", "[1,2,3]", "123", "Error"], "answer": "1,2,3", "difficulty": "Easy", "explanation": "`join(',')` combines array elements into a string with commas.", "hint": "Think about array-to-string conversion.", "topic": "Arrays: Join"},
    {"question": "What does `if (x >= 5 && x <= 10) { console.log('Range'); }` output if `x = 7`?", "options": ["Range", "Nothing", "Error", "True"], "answer": "Range", "difficulty": "Medium", "explanation": "Both conditions are true for `x = 7`, so 'Range' is logged.", "hint": "Evaluate the logical AND.", "topic": "Logical Operators"},
    {"question": "What does `$('p').html('<b>Bold</b>')` do in jQuery?", "options": ["Gets HTML content", "Sets HTML content to <b>Bold</b>", "Appends HTML content", "Removes HTML content"], "answer": "Sets HTML content to <b>Bold</b>", "difficulty": "Easy", "explanation": "`.html()` sets the HTML content of selected elements.", "hint": "Think about HTML manipulation.", "topic": "jQuery HTML Manipulation"},
    {"question": "What does `typeof function(){}` return?", "options": ["object", "function", "undefined", "string"], "answer": "function", "difficulty": "Easy", "explanation": "`typeof` identifies a function expression as 'function'.", "hint": "Check JavaScript type checking.", "topic": "Data Types"},
    {"question": "What does `'abc'.charAt(0)` return?", "options": ["a", "b", "c", "Error"], "answer": "a", "difficulty": "Easy", "explanation": "`charAt(0)` returns the character at index 0, which is 'a'.", "hint": "Check string indexing.", "topic": "Strings: charAt"},
    {"question": "What does `new Date().getMonth()` return in July 2025?", "options": ["6", "7", "8", "5"], "answer": "6", "difficulty": "Medium", "explanation": "Months are 0-based, so July is 6.", "hint": "Check month indexing.", "topic": "Date Methods"},
    {"question": "What does `$('input').val('test')` do in jQuery?", "options": ["Gets the input value", "Sets the input value to 'test'", "Clears the input", "Disables the input"], "answer": "Sets the input value to 'test'", "difficulty": "Easy", "explanation": "`.val('test')` sets the value of input elements.", "hint": "Think about form handling in jQuery.", "topic": "jQuery Form Handling"},
    {"question": "What does `let x = 5; x *= 3;` result in?", "options": ["15", "8", "5", "Error"], "answer": "15", "difficulty": "Easy", "explanation": "`*=` multiplies `x` by 3, so `5 * 3 = 15`.", "hint": "Check assignment operators.", "topic": "Assignment Operators"},
    {"question": "What does `arr.concat([4, 5])` do to `arr = [1, 2, 3]`?", "options": ["[1, 2, 3, 4, 5]", "[4, 5, 1, 2, 3]", "[1, 2, 3]", "[4, 5]"], "answer": "[1, 2, 3, 4, 5]", "difficulty": "Easy", "explanation": "`concat()` creates a new array by combining `arr` with `[4, 5]`.", "hint": "Think about array merging.", "topic": "Arrays: Concat"},
    {"question": "What does `$('div').fadeOut()` do in jQuery?", "options": ["Fades in div elements", "Hides div elements with a fade effect", "Removes div elements", "Changes div text"], "answer": "Hides div elements with a fade effect", "difficulty": "Easy", "explanation": "`.fadeOut()` gradually hides elements by reducing opacity.", "hint": "Think about jQuery animations.", "topic": "jQuery Effects"},
    {"question": "What is the output of `typeof NaN`?", "options": ["number", "undefined", "null", "string"], "answer": "number", "difficulty": "Medium", "explanation": "`NaN` is considered a number type in JavaScript.", "hint": "Check JavaScript’s type system.", "topic": "Data Types"},
    {"question": "What does `for (let i = 0; i < 2; i++) { console.log(i * 2); }` output?", "options": ["0 2", "0 1", "2 4", "Nothing"], "answer": "0 2", "difficulty": "Easy", "explanation": "The loop logs `i * 2` for `i = 0` and `1`, resulting in `0, 2`.", "hint": "Calculate the loop output.", "topic": "for Loops"},
    {"question": "What does `$('p').remove()` do in jQuery?", "options": ["Hides p elements", "Removes p elements from the DOM", "Changes p text", "Toggles p visibility"], "answer": "Removes p elements from the DOM", "difficulty": "Easy", "explanation": "`.remove()` deletes the selected elements from the DOM.", "hint": "Think about DOM manipulation.", "topic": "jQuery DOM Manipulation"},
    {"question": "What does `'123'.slice(0, 2)` return?", "options": ["12", "23", "123", "1"], "answer": "12", "difficulty": "Medium", "explanation": "`slice(0, 2)` extracts characters from index 0 to 1.", "hint": "Check string slicing indices.", "topic": "Strings: Slice"},
    {"question": "What is a JavaScript closure?", "options": ["A loop construct", "A function with access to outer scope variables", "A variable type", "An event handler"], "answer": "A function with access to outer scope variables", "difficulty": "Medium", "explanation": "A closure retains access to its outer function’s variables after execution.", "hint": "Think about function scope.", "topic": "Closures"},
    {"question": "$('p').each(function() { $(this).text('Hi'); })` does what?", "options": ["Sets text of each p element to 'Hi'", "Gets text of each p element", "Hides each p element", "Removes each p element"], "answer": "Sets text of each p element to 'Hi'", "difficulty": "Medium", "explanation": "`.each()` iterates over elements, and `$(this).text('Hi')` sets their text.", "hint": "Think about jQuery iteration.", "topic": "jQuery Iteration"},
    {"question": "What does `Number('12.34')` return?", "options": ["12", "12.34", "'12.34'", "Error"], "answer": "12.34", "difficulty": "Easy", "explanation": "`Number()` converts a string to a number, including decimals.", "hint": "Check type conversion.", "topic": "Type Conversion"}
]

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

# Main UI
st.set_page_config(page_title="JavaScript Quiz Pro", page_icon=":rocket:", layout="centered")
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 JavaScript Quiz Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Test Your JavaScript & jQuery Mastery!</p>', unsafe_allow_html=True)

# Theme Toggle
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()

# Welcome Screen
if not st.session_state.started:
    st.markdown("""
        <div style="text-align: center;">
            <p style="color: var(--text-color); font-size: 16px;">Challenge yourself with 50 JavaScript & jQuery questions!</p>
            <p style="color: #8b8b8b;">30 minutes, 1-3 points per correct answer based on difficulty. Ready to code?</p>
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
                parts = q["question"].split("```javascript")
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
                            st.session_state.score += 1  # Bonus point for streak
                    else:
                        st.session_state.streak = 0
                    st.rerun()

            # Feedback
            if st.session_state.feedback:
                if st.session_state.feedback["is_correct"]:
                    st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                    st.markdown('<script>triggerConfetti();</script>', unsafe_allow_html=True)
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
        st.markdown('<script>triggerConfetti();</script>', unsafe_allow_html=True)
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
