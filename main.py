
import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data (50 JavaScript MCQs)
quiz = [
    {
        "question": "What does the `alert()` function do in a browser environment?",
        "options": ["Logs a message to the console", "Displays a pop-up dialog", "Redirects to a new page", "Throws an error"],
        "answer": "Displays a pop-up dialog",
        "difficulty": "Medium",
        "explanation": "The `alert()` function creates a pop-up dialog box in the browser to display a message and waits for the user to click 'OK'.",
        "hint": "Think about user-facing notifications in browsers."
    },
    {
        "question": "What is the result of `let str = 'Hello'; str = str + ' World'; console.log(str);`?",
        "options": ["Hello", "World", "Hello World", "Error"],
        "answer": "Hello World",
        "difficulty": "Medium",
        "explanation": "The `+` operator concatenates 'Hello' and ' World' to form 'Hello World'.",
        "hint": "Consider how strings are combined."
    },
    {
        "question": "What is the value of `x` after `let x = 8; x += 2;`?",
        "options": ["6", "8", "10", "12"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "The `+=` operator adds 2 to `x`, so `8 + 2 = 10`.",
        "hint": "Recall compound assignment operators."
    },
    {
        "question": "Which variable name is illegal in JavaScript?",
        "options": ["myVar", "_count", "user_name", "1stVar"],
        "answer": "1stVar",
        "difficulty": "Medium",
        "explanation": "Variable names cannot start with a digit; they must begin with a letter, underscore, or dollar sign.",
        "hint": "Check JavaScript naming conventions."
    },
    {
        "question": "What is the result of `6 + 4 * 2` in JavaScript?",
        "options": ["20", "14", "10", "12"],
        "answer": "14",
        "difficulty": "Medium",
        "explanation": "Following PEMDAS, multiplication is done first: `4 * 2 = 8`, then addition: `6 + 8 = 14`.",
        "hint": "Remember the order of operations."
    },
    {
        "question": "What does the `**` operator do in JavaScript?",
        "options": ["Multiplies two numbers", "Raises a number to a power", "Performs division", "Increments a number"],
        "answer": "Raises a number to a power",
        "difficulty": "Medium",
        "explanation": "The `**` operator performs exponentiation, e.g., `2 ** 3 = 8`.",
        "hint": "Think about mathematical powers."
    },
    {
        "question": "How do you ensure `5 + 3 * 4` evaluates to `32` instead of `17`?",
        "options": ["(5 + 3) * 4", "5 + (3 * 4)", "5 * (3 + 4)", "No change needed"],
        "answer": "(5 + 3) * 4",
        "difficulty": "Medium",
        "explanation": "Parentheses ensure `5 + 3 = 8` is calculated first, then `8 * 4 = 32`.",
        "hint": "Use parentheses to control precedence."
    },
    {
        "question": "What is the result of `'Good' + ' ' + 'Day'`?",
        "options": ["GoodDay", "Good Day", "Good+Day", "Error"],
        "answer": "Good Day",
        "difficulty": "Medium",
        "explanation": "The `+` operator concatenates the strings, including the space, to form 'Good Day'.",
        "hint": "Spaces are important in concatenation."
    },
    {
        "question": "What does `prompt('Enter age')` return if the user enters '25'?",
        "options": ["25", "'25'", "null", "undefined"],
        "answer": "'25'",
        "difficulty": "Medium",
        "explanation": "`prompt()` returns user input as a string, so '25' is returned as `'25'`.",
        "hint": "Consider the data type of user input."
    },
    {
        "question": "What will `if (7 > 4) { console.log('True'); }` output?",
        "options": ["True", "False", "Nothing", "Error"],
        "answer": "True",
        "difficulty": "Medium",
        "explanation": "The condition `7 > 4` is true, so 'True' is logged.",
        "hint": "Evaluate the `if` condition."
    },
    {
        "question": "What is the result of `'10' == 10` in JavaScript?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The `==` operator performs type coercion, so `'10'` is converted to the number 10, making the comparison true.",
        "hint": "Compare loose equality behavior."
    },
    {
        "question": "What will be output: `let x = 15; if (x < 10) { console.log('Small'); } else if (x < 20) { console.log('Medium'); } else { console.log('Large'); }`?",
        "options": ["Small", "Medium", "Large", "Nothing"],
        "answer": "Medium",
        "difficulty": "Medium",
        "explanation": "Since `x = 15` is less than 20 but not less than 10, 'Medium' is logged.",
        "hint": "Check which condition matches."
    },
    {
        "question": "What is the result of `if (4 > 2 && 3 < 5) { console.log('Yes'); }`?",
        "options": ["Yes", "No", "Nothing", "Error"],
        "answer": "Yes",
        "difficulty": "Medium",
        "explanation": "Both `4 > 2` and `3 < 5` are true, so the `&&` operator evaluates to true, logging 'Yes'.",
        "hint": "Evaluate the logical operator."
    },
    {
        "question": "What will be output: `let x = 7; if (x > 5) { if (x < 10) { console.log('In Range'); } }`?",
        "options": ["In Range", "Out of Range", "Nothing", "Error"],
        "answer": "In Range",
        "difficulty": "Medium",
        "explanation": "Both conditions (`x > 5` and `x < 10`) are true for `x = 7`, so 'In Range' is logged.",
        "hint": "Trace nested conditions."
    },
    {
        "question": "Which creates an array in JavaScript?",
        "options": ["let arr = {};", "let arr = [];", "let arr = '';", "let arr = null;"],
        "answer": "let arr = [];",
        "difficulty": "Medium",
        "explanation": "Arrays are created with square brackets `[]`. Curly braces `{}` create objects.",
        "hint": "Recall array syntax."
    },
    {
        "question": "What does `arr.push(4)` do to `arr = [1, 2, 3]`?",
        "options": ["[1, 2, 3, 4]", "[4, 1, 2, 3]", "[1, 2, 4]", "[4]"],
        "answer": "[1, 2, 3, 4]",
        "difficulty": "Medium",
        "explanation": "`push(4)` adds 4 to the end of the array, resulting in `[1, 2, 3, 4]`.",
        "hint": "Think about adding to the end of an array."
    },
    {
        "question": "What does `arr.splice(1, 1)` do to `arr = [1, 2, 3]`?",
        "options": ["Removes 1", "Removes 2", "Removes 3", "Clears the array"],
        "answer": "Removes 2",
        "difficulty": "Medium",
        "explanation": "`splice(1, 1)` removes 1 element at index 1, so `2` is removed, leaving `[1, 3]`.",
        "hint": "Check `splice()` parameters."
    },
    {
        "question": "What will `for (let i = 0; i < 3; i++) { console.log(i); }` output?",
        "options": ["0, 1, 2", "1, 2, 3", "0, 1", "Nothing"],
        "answer": "0, 1, 2",
        "difficulty": "Medium",
        "explanation": "The loop runs from `i = 0` to `i < 3`, logging `0`, `1`, and `2`.",
        "hint": "Trace the loop counter."
    },
    {
        "question": "What will be output: `let arr = [1, 2, 3]; for (let i = 0; i < arr.length; i++) { if (arr[i] === 2) break; console.log(arr[i]); }`?",
        "options": ["1", "1, 2", "1, 2, 3", "Nothing"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "The loop stops at `arr[i] === 2` due to `break`, so only `1` is logged.",
        "hint": "Consider the `break` statement."
    },
    {
        "question": "What will be output: `for (let i = 1; i <= 2; i++) { for (let j = 1; j <= 2; j++) { console.log(i * j); } }`?",
        "options": ["1, 2, 2, 4", "1, 2, 3, 4", "1, 1, 2, 2", "Nothing"],
        "answer": "1, 2, 2, 4",
        "difficulty": "Medium",
        "explanation": "The loop outputs products: `1*1=1`, `1*2=2`, `2*1=2`, `2*2=4`.",
        "hint": "Trace nested loop iterations."
    },
    {
        "question": "What is the result of `'hello'.toUpperCase()`?",
        "options": ["HELLO", "hello", "Hello", "hELLO"],
        "answer": "HELLO",
        "difficulty": "Medium",
        "explanation": "`toUpperCase()` converts all characters to uppercase, resulting in 'HELLO'.",
        "hint": "Think about case transformation."
    },
    {
        "question": "What is the result of `'JavaScript'.substring(0, 4)`?",
        "options": ["Java", "Scri", "JavaS", "Script"],
        "answer": "Java",
        "difficulty": "Medium",
        "explanation": "`substring(0, 4)` extracts characters from index 0 to 3, resulting in 'Java'.",
        "hint": "Check `substring()` indices."
    },
    {
        "question": "What does `'Hello World'.indexOf('World')` return?",
        "options": ["0", "5", "6", "-1"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "`indexOf('World')` returns the starting index of 'World', which is 6 (after 'Hello ').",
        "hint": "Locate 'World' in the string."
    },
    {
        "question": "What does `'Test'.charAt(1)` return?",
        "options": ["T", "e", "s", "t"],
        "answer": "e",
        "difficulty": "Medium",
        "explanation": "`charAt(1)` returns the character at index 1, which is 'e' in 'Test'.",
        "hint": "Count characters from index 0."
    },
    {
        "question": "What is the result of `'Hello All'.replace('All', 'Everyone')`?",
        "options": ["Hello Everyone", "Hello All", "Everyone All", "Hello"],
        "answer": "Hello Everyone",
        "difficulty": "Medium",
        "explanation": "`replace()` substitutes 'All' with 'Everyone', resulting in 'Hello Everyone'.",
        "hint": "Think about string replacement."
    },
    {
        "question": "What is the result of `Math.round(5.8)`?",
        "options": ["5", "6", "5.5", "7"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "`Math.round()` rounds to the nearest integer. Since 5.8 is closer to 6, it returns 6.",
        "hint": "Consider rounding rules."
    },
    {
        "question": "How do you generate a random integer from 1 to 10?",
        "options": ["Math.random() * 10", "Math.floor(Math.random() * 10) + 1", "Math.round(Math.random() * 10)", "Math.random(1, 10)"],
        "answer": "Math.floor(Math.random() * 10) + 1",
        "difficulty": "Medium",
        "explanation": "`Math.random() * 10` gives 0 to 9.999..., `Math.floor()` rounds down to 0–9, and `+1` shifts to 1–10.",
        "hint": "Scale and shift a random number."
    },
    {
        "question": "What does `parseInt('123.45')` return?",
        "options": ["123.45", "123", "124", "NaN"],
        "answer": "123",
        "difficulty": "Medium",
        "explanation": "`parseInt()` converts a string to an integer, stopping at the decimal, so '123.45' becomes 123.",
        "hint": "Think about integer conversion."
    },
    {
        "question": "How do you convert the number 42 to a string?",
        "options": ["42.toString()", "String(42)", "parseInt(42)", "Both 42.toString() and String(42)"],
        "answer": "Both 42.toString() and String(42)",
        "difficulty": "Medium",
        "explanation": "Both `42.toString()` and `String(42)` convert 42 to the string '42'.",
        "hint": "Consider number-to-string methods."
    },
    {
        "question": "What does `3.14159.toFixed(2)` return?",
        "options": ["3.14", "3.141", "3.15", "3.14159"],
        "answer": "3.14",
        "difficulty": "Medium",
        "explanation": "`toFixed(2)` rounds to 2 decimal places, returning '3.14' as a string.",
        "hint": "Check decimal formatting."
    },
    {
        "question": "What does `new Date()` return?",
        "options": ["A string", "A Date object", "A timestamp", "A formatted date"],
        "answer": "A Date object",
        "difficulty": "Medium",
        "explanation": "`new Date()` creates a Date object for the current date and time.",
        "hint": "Think about the Date constructor."
    },
    {
        "question": "What does `new Date().getFullYear()` return in 2025?",
        "options": ["2024", "2025", "25", "2026"],
        "answer": "2025",
        "difficulty": "Medium",
        "explanation": "`getFullYear()` returns the four-digit year, e.g., 2025.",
        "hint": "Consider Date object methods."
    },
    {
        "question": "Which creates a Date object for April 1, 2025?",
        "options": ["new Date(2025, 4, 1)", "new Date(2025, 3, 1)", "new Date('2025-04-01')", "Both new Date(2025, 3, 1) and new Date('2025-04-01')"],
        "answer": "Both new Date(2025, 3, 1) and new Date('2025-04-01')",
        "difficulty": "Medium",
        "explanation": "April is month 3 (0-based), and '2025-04-01' is a valid string format.",
        "hint": "Check month indexing."
    },
    {
        "question": "What does `date.setFullYear(2026)` do to a Date object?",
        "options": ["Sets the month to 2026", "Sets the year to 2026", "Sets the day to 2026", "Sets the timestamp"],
        "answer": "Sets the year to 2026",
        "difficulty": "Medium",
        "explanation": "`setFullYear(2026)` updates the year of the Date object to 2026.",
        "hint": "Think about Date modification."
    },
    {
        "question": "What is the correct function declaration syntax?",
        "options": ["function myFunc() {}", "myFunc() {}", "func myFunc() {}", "function = myFunc() {}"],
        "answer": "function myFunc() {}",
        "difficulty": "Medium",
        "explanation": "Functions are declared with the `function` keyword, a name, and a body.",
        "hint": "Recall function syntax."
    },
    {
        "question": "What will `function add(a, b) { console.log(a + b); } add(2, 3);` output?",
        "options": ["5", "23", "Nothing", "Error"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The function adds `2 + 3` and logs 5.",
        "hint": "Trace the function parameters."
    },
    {
        "question": "What does `function square(n) { return n * n; } square(3);` return?",
        "options": ["6", "9", "3", "Nothing"],
        "answer": "9",
        "difficulty": "Medium",
        "explanation": "The function returns `3 * 3 = 9`.",
        "hint": "Focus on the `return` statement."
    },
    {
        "question": "What is the scope of `let x` inside a function?",
        "options": ["Global", "Local to the function", "Browser scope", "Global and local"],
        "answer": "Local to the function",
        "difficulty": "Medium",
        "explanation": "`let` variables inside a function are local and not accessible outside.",
        "hint": "Think about variable scope."
    },
    {
        "question": "What is the correct `switch` statement syntax?",
        "options": ["switch (x) {}", "switch x {}", "case (x) {}", "switch { x }"],
        "answer": "switch (x) {}",
        "difficulty": "Medium",
        "explanation": "A `switch` statement starts with `switch (expression) {}`.",
        "hint": "Recall `switch` structure."
    },
    {
        "question": "What happens if `break` is omitted in a `switch` case?",
        "options": ["Skips the case", "Executes the next case", "Throws an error", "Exits the switch"],
        "answer": "Executes the next case",
        "difficulty": "Medium",
        "explanation": "Without `break`, execution falls through to the next case.",
        "hint": "Think about fall-through behavior."
    },
    {
        "question": "What will `let i = 0; while (i < 2) { console.log(i); i++; }` output?",
        "options": ["0, 1", "1, 2", "0, 1, 2", "Nothing"],
        "answer": "0, 1",
        "difficulty": "Medium",
        "explanation": "The loop runs while `i < 2`, logging `0` and `1`.",
        "hint": "Trace the loop condition."
    },
    {
        "question": "What will `let i = 3; do { console.log(i); i++; } while (i < 3);` output?",
        "options": ["Nothing", "3", "3, 4", "2, 3"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "The `do...while` loop runs once, logging `3`, then stops since `i < 3` is false.",
        "hint": "Recall `do...while` behavior."
    },
    {
        "question": "What happens if `alert('Test')` is called in Node.js?",
        "options": ["Shows a pop-up", "Logs to console", "Throws an error", "Nothing"],
        "answer": "Throws an error",
        "difficulty": "Medium",
        "explanation": "`alert()` is browser-specific and undefined in Node.js, causing an error.",
        "hint": "Consider environment differences."
    },
    {
        "question": "What is the result of `let str = 'Hi'; str += '!'; console.log(str);`?",
        "options": ["Hi", "Hi!", "!Hi", "Error"],
        "answer": "Hi!",
        "difficulty": "Medium",
        "explanation": "The `+=` operator concatenates '!' to 'Hi', resulting in 'Hi!'.",
        "hint": "Think about string modification."
    },
    {
        "question": "What is the value of `x` after `let x = 12; x -= 5;`?",
        "options": ["7", "17", "5", "12"],
        "answer": "7",
        "difficulty": "Medium",
        "explanation": "The `-=` operator subtracts 5 from `x`, so `12 - 5 = 7`.",
        "hint": "Check compound operators."
    },
    {
        "question": "What is the result of `15 % 4` in JavaScript?",
        "options": ["3", "4", "2", "0"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "The `%` operator returns the remainder, so `15 % 4 = 3`.",
        "hint": "Think about division remainders."
    },
    {
        "question": "What is the result of `let x = '3'; let y = 4; console.log(x + y);`?",
        "options": ["7", "34", "12", "Error"],
        "answer": "34",
        "difficulty": "Medium",
        "explanation": "The `+` operator concatenates the string '3' with the number 4 (converted to '4'), resulting in '34'.",
        "hint": "Consider type coercion."
    },
    {
        "question": "What does `arr.pop()` do to `arr = [1, 2, 3]`?",
        "options": ["Removes 1", "Removes 3", "Removes 2", "Clears the array"],
        "answer": "Removes 3",
        "difficulty": "Medium",
        "explanation": "`pop()` removes and returns the last element, so `3` is removed, leaving `[1, 2]`.",
        "hint": "Think about the end of an array."
    },
    {
        "question": "What will `for (let i = 0; i < 4; i += 2) { console.log(i); }` output?",
        "options": ["0, 1, 2, 3", "0, 2", "1, 3", "0, 1, 2"],
        "answer": "0, 2",
        "difficulty": "Medium",
        "explanation": "The loop increments `i` by 2, logging `0` and `2`.",
        "hint": "Check the increment step."
    },
    {
        "question": "What does `function divide(a, b) { return a / b; } divide(10, 2);` return?",
        "options": ["5", "20", "2", "Nothing"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The function returns `10 / 2 = 5`.",
        "hint": "Focus on the `return` value."
    }
]

# Cache shuffled quiz
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

# Initialize session state
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

# Theme toggle
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# Timer logic
def update_timer():
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.session_state.time_left = max(1800 - elapsed, 0)
    if st.session_state.time_left <= 0:
        st.session_state.show_results = True
        st.rerun()

# Reset quiz
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

# Progress snapshot function
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

# CSS for VS Code-like styling
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

# Theme toggle button
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen
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
else:
    # Timer
    if not st.session_state.show_results:
        update_timer()
        minutes = int(st.session_state.time_left // 60)
        seconds = int(st.session_state.time_left % 60)
        st.markdown(f'<div class="timer">⏰ Time Left: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

    if not st.session_state.quiz_data:
        st.error("No quiz questions available.")
    else:
        # Progress bar
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

        if not st.session_state.show_results:
            with st.container():
                st.markdown('<div class="question-container">', unsafe_allow_html=True)
                q = st.session_state.quiz_data[st.session_state.current_q]

                # Display difficulty and streak
                st.markdown(f'<div class="difficulty">Difficulty: {q["difficulty"]} | Streak: 🔥 {st.session_state.streak}</div>', unsafe_allow_html=True)

                # Split question into text and code
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

                # Option buttons
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

                # Feedback
                if st.session_state.feedback:
                    if st.session_state.feedback["is_correct"]:
                        st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="color: var(--text-color); font-size: 13px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                # Hint button
                if st.button("💡 Show Hint", key="hint", disabled=st.session_state.show_hint or st.session_state.selected_option is not None):
                    st.session_state.show_hint = True
                    st.session_state.score = max(0, st.session_state.score - 0.5)
                    st.rerun()
                if st.session_state.show_hint:
                    st.markdown(f'<div style="color: #facc15; font-size: 13px;">Hint: {q["hint"]}</div>', unsafe_allow_html=True)

                # Navigation and progress snapshot
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

                # Reset quiz button
                if st.button("🔄 Reset Quiz", key="reset"):
                    reset_quiz()

                st.markdown("</div>", unsafe_allow_html=True)

        # Results screen
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
                        <strong>Difficulty:</strong> {ans['difficulty']}
                    </div>
                    """, unsafe_allow_html=True)

            if st.button("🔄 Try Again", key="try_again"):
                reset_quiz()

st.markdown("</div>", unsafe_allow_html=True)
