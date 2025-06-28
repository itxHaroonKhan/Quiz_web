
import streamlit as st
import random
from datetime import datetime
import uuid


quiz = [
    {
        question: "What is the output of `typeof null` in JavaScript?",
        options: ["null", "object", "undefined", "string"],
        answer: "object",
        difficulty: "Medium",
        explanation: "`typeof null` returns 'object' due to a historical bug in JavaScript.",
        hint: "Think about JavaScript's quirks with null.",
        topic: "Data Types"
    },
    {
        question: "How do you declare a constant variable in JavaScript?",
        options: ["let x = 10;", "var x = 10;", "const x = 10;", "constant x = 10;"],
        answer: "const x = 10;",
        difficulty: "Easy",
        explanation: "`const` declares a variable that cannot be reassigned after initialization.",
        hint: "Check variable declaration keywords.",
        topic: "Variables"
    },
    {
        question: "What does `alert('Hello')` do in JavaScript?",
        options: ["Logs to console", "Shows a pop-up", "Changes text", "Nothing"],
        answer: "Shows a pop-up",
        difficulty: "Easy",
        explanation: "`alert()` displays a dialog box with a message and an OK button.",
        hint: "Think about browser interactions.",
        topic: "Alerts"
    },
    {
        question: "What is the result of `5 + '5'` in JavaScript?",
        options: ["10", "55", "5", "Error"],
        answer: "55",
        difficulty: "Medium",
        explanation: "The `+` operator concatenates when one operand is a string, resulting in '55'.",
        hint: "Consider type coercion.",
        topic: "Type Coercion"
    },
    {
        question: "Which is a valid way to create an array?",
        options: ["let arr = [];", "let arr = {};", "let arr = '';", "arr = ();"],
        answer: "let arr = [];",
        difficulty: "Easy",
        explanation: "Arrays are created using square brackets `[]`.",
        hint: "Check array syntax.",
        topic: "Arrays"
    },
    {
        question: "What does `arr.pop()` do to an array `arr`?",
        options: ["Adds an element", "Removes the last element", "Removes the first element", "Clears the array"],
        answer: "Removes the last element",
        difficulty: "Easy",
        explanation: "`pop()` removes and returns the last element of an array.",
        hint: "Think about array modification.",
        topic: "Arrays: Methods"
    },
    {
        question: "What is the output of `3 * 2 ** 2`?",
        options: ["12", "36", "18", "9"],
        answer: "12",
        difficulty: "Medium",
        explanation: "Exponentiation (`**`) has higher precedence, so `2 ** 2 = 4`, then `3 * 4 = 12`.",
        hint: "Check operator precedence.",
        topic: "Math Expressions"
    },
    {
        question: "What does `prompt('Enter name')` do?",
        options: ["Logs to console", "Shows an input dialog", "Changes text", "Nothing"],
        answer: "Shows an input dialog",
        difficulty: "Easy",
        explanation: "`prompt()` displays a dialog box for user input with a text field.",
        hint: "Think about user interaction.",
        topic: "Prompts"
    },
    {
        question: "What is the output of `'Hello'.length`?",
        options: ["4", "5", "6", "7"],
        answer: "5",
        difficulty: "Easy",
        explanation: "The `length` property returns the number of characters in a string.",
        hint: "Count the characters.",
        topic: "Strings: Length"
    },
    {
        question: "What does `'JavaScript'.toUpperCase()` return?",
        options: ["javascript", "JAVASCRIPT", "JavaScript", "Error"],
        answer: "JAVASCRIPT",
        difficulty: "Easy",
        explanation: "`toUpperCase()` converts a string to uppercase.",
        hint: "Think about string case conversion.",
        topic: "Strings: Case"
    },
    {
        question: "What does `if (5 > 3) { console.log('True'); }` output?",
        options: ["True", "False", "Nothing", "Error"],
        answer: "True",
        difficulty: "Easy",
        explanation: "The condition `5 > 3` is true, so 'True' is logged.",
        hint: "Evaluate the condition.",
        topic: "if Statements"
    },
    {
        question: "What is the result of `'10' == 10`?",
        options: ["true", "false", "undefined", "Error"],
        answer: "true",
        difficulty: "Medium",
        explanation: "The `==` operator performs type coercion, so string '10' equals number 10.",
        hint: "Think about loose equality.",
        topic: "Comparison Operators"
    },
    {
        question: "What does `Math.floor(7.9)` return?",
        options: ["7", "8", "7.9", "9"],
        answer: "7",
        difficulty: "Easy",
        explanation: "`Math.floor()` rounds down to the nearest integer.",
        hint: "Think about rounding down.",
        topic: "Math Methods"
    },
    {
        question: "What does `Math.random()` generate?",
        options: ["0 to 100", "0 to 1", "1 to 10", "1 to 100"],
        answer: "0 to 1",
        difficulty: "Easy",
        explanation: "`Math.random()` generates a float between 0 (inclusive) and 1 (exclusive).",
        hint: "Check random number range.",
        topic: "Random Numbers"
    },
    {
        question: "How do you define a function named `add`?",
        options: ["function add() {}", "add = function {}", "def add() {}", "function = add()"],
        answer: "function add() {}",
        difficulty: "Easy",
        explanation: "Functions are defined with the `function` keyword, name, and body.",
        hint: "Check function syntax.",
        topic: "Functions"
    },
    {
        question: "What does `function multiply(x, y) { return x * y; }` return for `multiply(2, 3)`?",
        options: ["5", "6", "8", "Error"],
        answer: "6",
        difficulty: "Easy",
        explanation: "The function returns `x * y`, so `2 * 3 = 6`.",
        hint: "Focus on the return value.",
        topic: "Functions: Return"
    },
    {
        question: "What does `for (let i = 0; i < 3; i++) { console.log(i); }` output?",
        options: ["0 1 2", "1 2 3", "0 1", "Nothing"],
        answer: "0 1 2",
        difficulty: "Easy",
        explanation: "The loop runs from `i = 0` to `i = 2`, logging each value.",
        hint: "Trace loop iterations.",
        topic: "for Loops"
    },
    {
        question: "What stops a loop in `for (let i = 0; i < 5; i++) { if (i === 3) break; }`?",
        options: ["stop;", "break;", "exit;", "return;"],
        answer: "break;",
        difficulty: "Medium",
        explanation: "`break` exits the loop when `i === 3`.",
        hint: "Think about loop termination.",
        topic: "for Loops: Break"
    },
    {
        question: "What does `'Test'.replace('T', 'B')` return?",
        options: ["Best", "Test", "BTest", "Error"],
        answer: "Best",
        difficulty: "Medium",
        explanation: "`replace()` substitutes the first 'T' with 'B', resulting in 'Best'.",
        hint: "Think about string replacement.",
        topic: "Strings: Replace"
    },
    {
        question: "What does `new Date().getFullYear()` return on June 28, 2025?",
        options: ["2024", "2025", "25", "6"],
        answer: "2025",
        difficulty: "Medium",
        explanation: "`getFullYear()` returns the current year, which is 2025.",
        hint: "Check date methods.",
        topic: "Date Methods"
    },
    {
        question: "What is jQuery primarily used for?",
        options: ["Server-side scripting", "DOM manipulation", "Database queries", "File handling"],
        answer: "DOM manipulation",
        difficulty: "Easy",
        explanation: "jQuery simplifies DOM manipulation, event handling, and AJAX in JavaScript.",
        hint: "Think about jQuery’s purpose in web development.",
        topic: "jQuery Basics"
    },
    {
        question: "How do you include jQuery in an HTML file?",
        options: [
            "<script src='jquery.min.js'></script>",
            "<link href='jquery.min.js'>",
            "<script include='jquery.js'>",
            "<jquery src='jquery.js'>"
        ],
        answer: "<script src='jquery.min.js'></script>",
        difficulty: "Easy",
        explanation: "jQuery is included using a `<script>` tag with the `src` attribute.",
        hint: "Check HTML script inclusion.",
        topic: "jQuery Setup"
    },
    {
        question: "What does `$(document).ready()` do in jQuery?",
        options: [
            "Reloads the page",
            "Executes code when DOM is loaded",
            "Submits a form",
            "Hides elements"
        ],
        answer: "Executes code when DOM is loaded",
        difficulty: "Easy",
        explanation: "`$(document).ready()` runs code after the DOM is fully loaded.",
        hint: "Think about when jQuery code executes.",
        topic: "jQuery Document Ready"
    },
    {
        question: "Which jQuery selector targets elements by class?",
        options: ["#class", ".class", "class()", "[class]"],
        answer: ".class",
        difficulty: "Easy",
        explanation: "The `.class` selector targets elements with the specified class.",
        hint: "Recall CSS selector syntax in jQuery.",
        topic: "jQuery Selectors"
    },
    {
        question: "What does `$('p').hide()` do in jQuery?",
        options: [
            "Shows p elements",
            "Hides p elements",
            "Removes p elements",
            "Changes p text"
        ],
        answer: "Hides p elements",
        difficulty: "Easy",
        explanation: "`.hide()` sets `display: none` for selected elements.",
        hint: "Think about visibility in jQuery.",
        topic: "jQuery Effects"
    },
    {
        question: "What does `$('button').click(function() { alert('Hi'); })` do?",
        options: [
            "Removes buttons",
            "Adds a click event to buttons",
            "Changes button text",
            "Hides buttons"
        ],
        answer: "Adds a click event to buttons",
        difficulty: "Medium",
        explanation: "`.click()` binds a click event handler to buttons, showing an alert.",
        hint: "Think about jQuery event handling.",
        topic: "jQuery Events"
    },
    {
        question: "What is the result of `'20' !== 20` in JavaScript?",
        options: ["true", "false", "undefined", "Error"],
        answer: "true",
        difficulty: "Medium",
        explanation: "`!==` checks value and type, so string '20' is not equal to number 20.",
        hint: "Consider strict inequality.",
        topic: "Comparison Operators"
    },
    {
        question: "What does `arr.slice(1, 3)` do for `arr = [1, 2, 3, 4]`?",
        options: ["Returns [2, 3]", "Returns [1, 2]", "Removes [2, 3]", "Returns [3, 4]"],
        answer: "Returns [2, 3]",
        difficulty: "Medium",
        explanation: "`slice(1, 3)` extracts elements from index 1 to 2 (3 exclusive).",
        hint: "Check array extraction methods.",
        topic: "Arrays: Slice"
    },
    {
        question: "What does `while (x < 3) { console.log(x); x++; }` output if `x = 1`?",
        options: ["1 2", "1 2 3", "0 1 2", "Nothing"],
        answer: "1 2",
        difficulty: "Medium",
        explanation: "The loop runs while `x < 3`, logging `1` and `2`.",
        hint: "Trace the loop condition.",
        topic: "while Loops"
    },
    {
        question: "What does `do { console.log(x); x++; } while (x < 2);` do if `x = 1`?",
        options: ["Logs 1", "Logs 1 2", "Nothing", "Infinite loop"],
        answer: "Logs 1",
        difficulty: "Medium",
        explanation: "The `do...while` loop runs once, logging `1`, then stops as `x < 2` is false.",
        hint: "Check minimum loop runs.",
        topic: "do...while Loops"
    },
    {
        question: "What does `$('div').addClass('active')` do in jQuery?",
        options: [
            "Removes a class",
            "Adds the 'active' class to divs",
            "Toggles a class",
            "Changes div content"
        ],
        answer: "Adds the 'active' class to divs",
        difficulty: "Easy",
        explanation: "`.addClass()` adds the specified class to selected elements.",
        hint: "Think about class manipulation in jQuery.",
        topic: "jQuery Class Manipulation"
    },
    {
        question: "What does `'Hello World'.indexOf('World')` return?",
        options: ["5", "6", "-1", "7"],
        answer: "6",
        difficulty: "Medium",
        explanation: "`indexOf()` returns the starting index of 'World', which is 6 (after the space).",
        hint: "Check substring position.",
        topic: "Strings: IndexOf"
    },
    {
        question: "What does `parseInt('123')` return?",
        options: ["123", "'123'", "12.3", "Error"],
        answer: "123",
        difficulty: "Easy",
        explanation: "`parseInt()` converts a string to an integer.",
        hint: "Think about string-to-number conversion.",
        topic: "Type Conversion"
    },
    {
        question: "What does `(4.567).toFixed(2)` return?",
        options: ["4.56", "4.57", "4.6", "4.567"],
        answer: "4.57",
        difficulty: "Medium",
        explanation: "`toFixed(2)` rounds to 2 decimal places, returning '4.57' as a string.",
        hint: "Check decimal precision.",
        topic: "Number Formatting"
    },
    {
        question: "What does `new Date(2025, 0, 1)` create?",
        options: [
            "January 1, 2025",
            "February 1, 2025",
            "January 1, 2026",
            "December 1, 2024"
        ],
        answer: "January 1, 2025",
        difficulty: "Medium",
        explanation: "Months are 0-based, so `0` is January.",
        hint: "Check month indexing in Date.",
        topic: "Date Creation"
    },
    {
        question: "What is a closure in JavaScript?",
        options: [
            "A loop construct",
            "A function with access to its outer scope",
            "A type of variable",
            "A jQuery method"
        ],
        answer: "A function with access to its outer scope",
        difficulty: "Medium",
        explanation: "A closure is a function that retains access to its outer scope’s variables even after the outer function has executed.",
        hint: "Think about scope and functions.",
        topic: "Closures"
    },
    {
        question: "What does `$('p').text()` do in jQuery?",
        options: [
            "Sets text of p elements",
            "Gets text of the first p element",
            "Removes p elements",
            "Hides p elements"
        ],
        answer: "Gets text of the first p element",
        difficulty: "Medium",
        explanation: "`.text()` without arguments retrieves the text of the first selected element.",
        hint: "Check jQuery text methods.",
        topic: "jQuery Text Manipulation"
    },
    {
        question: "What does `let x = 10; x += 5;` result in?",
        options: ["10", "15", "5", "Error"],
        answer: "15",
        difficulty: "Easy",
        explanation: "`+=` adds 5 to `x`, so `x` becomes 15.",
        hint: "Think about assignment operators.",
        topic: "Assignment Operators"
    },
    {
        question: "What does `arr.push(5)` do to `arr = [1, 2, 3]`?",
        options: ["[1, 2, 3, 5]", "[5, 1, 2, 3]", "[1, 2, 5]", "[1, 5, 3]"],
        answer: "[1, 2, 3, 5]",
        difficulty: "Easy",
        explanation: "`push()` adds an element to the end of the array.",
        hint: "Check array modification methods.",
        topic: "Arrays: Push"
    },
    {
        question: "What does `switch(x) { case 1: console.log('One'); break; }` do if `x = 1`?",
        options: ["Logs 'One'", "Logs nothing", "Logs 'x'", "Error"],
        answer: "Logs 'One'",
        difficulty: "Easy",
        explanation: "The `switch` statement executes the case where `x` matches, logging 'One'.",
        hint: "Think about switch case execution.",
        topic: "switch Statements"
    },
    {
        question: "What does `$('div').css('color', 'blue')` do?",
        options: [
            "Gets the color",
            "Sets the color to blue",
            "Removes the color",
            "Toggles the color"
        ],
        answer: "Sets the color to blue",
        difficulty: "Easy",
        explanation: "`.css()` with two arguments sets the CSS property for selected elements.",
        hint: "Think about jQuery CSS manipulation.",
        topic: "jQuery CSS"
    },
    {
        question: "What does `'abc'.charAt(1)` return?",
        options: ["a", "b", "c", "Error"],
        answer: "b",
        difficulty: "Easy",
        explanation: "`charAt(1)` returns the character at index 1, which is 'b'.",
        hint: "Check string indexing.",
        topic: "Strings: charAt"
    },
    {
        question: "What is the output of `console.log(!!'hello')`?",
        options: ["true", "false", "'hello'", "undefined"],
        answer: "true",
        difficulty: "Medium",
        explanation: "The double `!!` converts a truthy value ('hello') to `true`.",
        hint: "Think about boolean conversion.",
        topic: "Type Coercion"
    },
    {
        question: "What does `$('p').append('!')` do in jQuery?",
        options: [
            "Removes p elements",
            "Adds '!' to the end of p content",
            "Replaces p content with '!'",
            "Hides p elements"
        ],
        answer: "Adds '!' to the end of p content",
        difficulty: "Easy",
        explanation: "`.append()` adds content to the end of selected elements’ content.",
        hint: "Think about adding content in jQuery.",
        topic: "jQuery DOM Manipulation"
    },
    {
        question: "What does `let x; console.log(x);` output?",
        options: ["null", "undefined", "0", "Error"],
        answer: "undefined",
        difficulty: "Easy",
        explanation: "A declared but uninitialized variable is `undefined`.",
        hint: "Check variable initialization.",
        topic: "Variables"
    },
    {
        question: "What does `arr.splice(1, 1, 'x')` do to `arr = [1, 2, 3]`?",
        options: ["[1, 'x', 3]", "[1, 2, 'x']", "['x', 2, 3]", "[1, 2, 3, 'x']"],
        answer: "[1, 'x', 3]",
        difficulty: "Medium",
        explanation: "`splice(1, 1, 'x')` removes 1 element at index 1 and inserts 'x'.",
        hint: "Check splice parameters.",
        topic: "Arrays: Splice"
    },
    {
        question: "What does `$.ajax()` do in jQuery?",
        options: [
            "Animates elements",
            "Makes an HTTP request",
            "Selects elements",
            "Changes the URL"
        ],
        answer: "Makes an HTTP request",
        difficulty: "Medium",
        explanation: "`$.ajax()` performs asynchronous HTTP requests for server communication.",
        hint: "Think about jQuery’s server interaction.",
        topic: "jQuery AJAX"
    },
    {
        question: "What does `for (let i = 0; i < 2; i++) { for (let j = 0; j < 2; j++) { console.log(i + j); } }` output?",
        options: ["0 1 1 2", "0 1 2 3", "0 0 1 1", "Nothing"],
        answer: "0 1 1 2",
        difficulty: "Medium",
        explanation: "The nested loops log sums: `0+0, 0+1, 1+0, 1+1`.",
        hint: "Trace nested loop outputs.",
        topic: "Nested Loops"
    },
    {
        question: "What does `$('p').first().text('Start')` do?",
        options: [
            "Sets text of all p elements",
            "Sets text of the first p element",
            "Gets text of the first p",
            "Hides the first p"
        ],
        answer: "Sets text of the first p element",
        difficulty: "Medium",
        explanation: "`.first()` selects the first element, and `.text('Start')` sets its text.",
        hint: "Check jQuery traversal methods.",
        topic: "jQuery Traversal"
    },
    {
        question: "What is the output of `Number('123')`?",
        options: ["123", "'123'", "Error", "undefined"],
        answer: "123",
        difficulty: "Easy",
        explanation: "`Number()` converts a string to a number.",
        hint: "Think about type conversion.",
        topic: "Type Conversion"
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

