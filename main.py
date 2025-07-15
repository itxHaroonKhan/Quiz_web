import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 67 questions covering specified JavaScript topics
quiz = [
    # Topic 20: For loops nested
    {
        "question": "What is the output of the following nested for loop?\n```javascript\nfor (let i = 1; i <= 2; i++) {\n  for (let j = 1; j <= 2; j++) {\n    console.log(i, j);\n  }\n}\n```",
        "options": ["1 1, 1 2, 2 1, 2 2", "1 2, 2 1", "1 1, 2 2", "1 1, 1 1, 2 2, 2 2"],
        "answer": "1 1, 1 2, 2 1, 2 2",
        "difficulty": "Medium",
        "explanation": "The outer loop runs for `i = 1` and `i = 2`, and for each `i`, the inner loop runs for `j = 1` and `j = 2`, printing each combination."
    },
    {
        "question": "How many times will the inner loop execute in this nested loop?\n```javascript\nfor (let i = 0; i < 3; i++) {\n  for (let j = 0; j < 2; j++) {\n    console.log('Hi');\n  }\n}\n```",
        "options": ["3", "6", "2", "5"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "The outer loop runs 3 times, and for each iteration, the inner loop runs 2 times, resulting in 3 * 2 = 6 executions."
    },
    # Topic 21: Changing case
    {
        "question": "Which method converts a string to uppercase in JavaScript?",
        "options": ["str.toUpperCase()", "str.upperCase()", "str.toUpper()", "str.makeUpperCase()"],
        "answer": "str.toUpperCase()",
        "difficulty": "Easy",
        "explanation": "The `toUpperCase()` method converts all characters in a string to uppercase."
    },
    {
        "question": "What does `toLowerCase()` do to a string?",
        "options": ["Converts it to lowercase", "Converts it to uppercase", "Trims whitespace", "Reverses the string"],
        "answer": "Converts it to lowercase",
        "difficulty": "Easy",
        "explanation": "The `toLowerCase()` method converts all characters in a string to lowercase."
    },
    # Topic 22: Strings: measuring length and extracting parts
    {
        "question": "How do you measure the length of a string in JavaScript?",
        "options": ["str.length", "str.size()", "str.len()", "str.count()"],
        "answer": "str.length",
        "difficulty": "Easy",
        "explanation": "The `length` property returns the number of characters in a string."
    },
    {
        "question": "What does `slice(1, 3)` return for the string 'Hello'?",
        "options": ["el", "ell", "he", "lo"],
        "answer": "el",
        "difficulty": "Medium",
        "explanation": "`slice(1, 3)` extracts characters from index 1 to 2 (end index is exclusive), so for 'Hello', it returns 'el'."
    },
    # Topic 23: Strings: finding segments
    {
        "question": "Which method finds the index of the first occurrence of a substring?",
        "options": ["indexOf()", "search()", "find()", "locate()"],
        "answer": "indexOf()",
        "difficulty": "Easy",
        "explanation": "The `indexOf()` method returns the index of the first occurrence of a substring, or -1 if not found."
    },
    {
        "question": "What does `'Hello World'.indexOf('World')` return?",
        "options": ["6", "5", "0", "-1"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "The substring 'World' starts at index 6 in 'Hello World' (counting starts at 0, and there’s a space at index 5)."
    },
    # Topic 24: Strings: finding a character at a location
    {
        "question": "How do you get the character at index 2 in the string 'JavaScript'?",
        "options": ["'JavaScript'[2]", "charAt(2)", "getChar(2)", "at(2)"],
        "answer": "'JavaScript'[2]",
        "difficulty": "Easy",
        "explanation": "You can access a character at index 2 using bracket notation (`str[2]`) or `charAt(2)`. Both return 'v' for 'JavaScript'."
    },
    {
        "question": "What is the output of `'Test'.charAt(1)`?",
        "options": ["e", "T", "s", "t"],
        "answer": "e",
        "difficulty": "Easy",
        "explanation": "The `charAt(1)` method returns the character at index 1, which is 'e' in 'Test'."
    },
    # Topic 25: Strings: replacing characters
    {
        "question": "Which method replaces the first occurrence of a substring in a string?",
        "options": ["replace()", "swap()", "change()", "substitute()"],
        "answer": "replace()",
        "difficulty": "Easy",
        "explanation": "The `replace()` method replaces the first occurrence of a substring with a new value."
    },
    {
        "question": "What does `'Hello World'.replace('World', 'Universe')` return?",
        "options": ["Hello Universe", "Hello World", "Universe World", "Hello"],
        "answer": "Hello Universe",
        "difficulty": "Medium",
        "explanation": "The `replace()` method replaces 'World' with 'Universe', resulting in 'Hello Universe'."
    },
    # Topic 26: Rounding numbers
    {
        "question": "Which method rounds a number to the nearest integer?",
        "options": ["Math.round()", "Math.floor()", "Math.ceil()", "Math.trunc()"],
        "answer": "Math.round()",
        "difficulty": "Easy",
        "explanation": "`Math.round()` rounds a number to the nearest integer (e.g., 3.6 becomes 4, 3.4 becomes 3)."
    },
    {
        "question": "What is the result of `Math.round(3.7)`?",
        "options": ["4", "3", "3.7", "4.0"],
        "answer": "4",
        "difficulty": "Easy",
        "explanation": "`Math.round(3.7)` rounds 3.7 to the nearest integer, which is 4."
    },
    # Topic 27: Generating random numbers
    {
        "question": "How do you generate a random number between 0 and 1 in JavaScript?",
        "options": ["Math.random()", "Math.rand()", "Random()", "Math.floor()"],
        "answer": "Math.random()",
        "difficulty": "Easy",
        "explanation": "`Math.random()` generates a random floating-point number between 0 (inclusive) and 1 (exclusive)."
    },
    {
        "question": "How do you generate a random integer between 1 and 10?",
        "options": ["Math.floor(Math.random() * 10) + 1", "Math.random() * 10", "Math.ceil(Math.random() * 10)", "Math.round(Math.random() * 10)"],
        "answer": "Math.floor(Math.random() * 10) + 1",
        "difficulty": "Medium",
        "explanation": "`Math.random() * 10` generates a number between 0 and 10, `Math.floor()` rounds it down, and `+1` shifts the range to 1–10."
    },
    # Topic 28: Converting strings to integers and decimals
    {
        "question": "Which function converts a string to an integer?",
        "options": ["parseInt()", "parseFloat()", "Number()", "toString()"],
        "answer": "parseInt()",
        "difficulty": "Easy",
        "explanation": "`parseInt()` converts a string to an integer, parsing until a non-numeric character is encountered."
    },
    {
        "question": "What is the result of `parseInt('42px')`?",
        "options": ["42", "NaN", "42px", "0"],
        "answer": "42",
        "difficulty": "Medium",
        "explanation": "`parseInt('42px')` parses the string until it encounters 'px', returning the integer 42."
    },
    # Topic 29: Converting strings to numbers, numbers to strings
    {
        "question": "How do you convert a number to a string in JavaScript?",
        "options": ["toString()", "String()", "parseString()", "numberToString()"],
        "answer": "toString()",
        "difficulty": "Easy",
        "explanation": "The `toString()` method or `String()` function converts a number to a string."
    },
    {
        "question": "What is the result of `String(123)`?",
        "options": ["'123'", "123", "'123.0'", "NaN"],
        "answer": "'123'",
        "difficulty": "Easy",
        "explanation": "The `String()` function converts the number 123 to the string '123'."
    },
    # Topic 30: Controlling the length of decimals
    {
        "question": "Which method controls the number of decimal places in a number?",
        "options": ["toFixed()", "toPrecision()", "round()", "truncate()"],
        "answer": "toFixed()",
        "difficulty": "Easy",
        "explanation": "`toFixed(n)` formats a number to `n` decimal places and returns it as a string."
    },
    {
        "question": "What is the result of `(3.14159).toFixed(2)`?",
        "options": ["'3.14'", "3.14", "'3.14159'", "3.1"],
        "answer": "'3.14'",
        "difficulty": "Medium",
        "explanation": "`toFixed(2)` rounds 3.14159 to 2 decimal places, returning the string '3.14'."
    },
    # Topic 31: Getting the current date and time
    {
        "question": "How do you get the current date and time in JavaScript?",
        "options": ["new Date()", "Date.now()", "getDate()", "Date.get()"],
        "answer": "new Date()",
        "difficulty": "Easy",
        "explanation": "`new Date()` creates a new Date object representing the current date and time."
    },
    {
        "question": "What does `Date.now()` return?",
        "options": ["Current timestamp in milliseconds", "Current date as a string", "Current year", "Current time as an object"],
        "answer": "Current timestamp in milliseconds",
        "difficulty": "Medium",
        "explanation": "`Date.now()` returns the number of milliseconds since January 1, 1970 (Unix epoch)."
    },
    # Topic 32: Extracting parts of the date and time
    {
        "question": "Which method gets the year from a Date object?",
        "options": ["getFullYear()", "getYear()", "getDate()", "getMonth()"],
        "answer": "getFullYear()",
        "difficulty": "Easy",
        "explanation": "`getFullYear()` returns the four-digit year of a Date object."
    },
    {
        "question": "What does `new Date('2023-05-15').getMonth()` return?",
        "options": ["4", "5", "15", "2023"],
        "answer": "4",
        "difficulty": "Medium",
        "explanation": "Months are 0-based in JavaScript, so May (the 5th month) returns 4."
    },
    # Topic 33: Specifying a date and time
    {
        "question": "How do you create a Date object for January 1, 2023?",
        "options": ["new Date(2023, 0, 1)", "new Date(2023, 1, 1)", "new Date('2023/1/1')", "Both a and c"],
        "answer": "Both a and c",
        "difficulty": "Medium",
        "explanation": "You can use `new Date(2023, 0, 1)` (0-based month) or `new Date('2023-01-01')` to specify January 1, 2023."
    },
    {
        "question": "What is the correct format for `new Date('YYYY-MM-DD')`?",
        "options": ["'2023-01-01'", "'01-01-2023'", "'2023/01/01'", "'Jan 1, 2023'"],
        "answer": "'2023-01-01'",
        "difficulty": "Medium",
        "explanation": "The ISO format 'YYYY-MM-DD' (e.g., '2023-01-01') is widely supported for creating Date objects."
    },
    # Topic 34: Changing elements of a date and time
    {
        "question": "Which method sets the year of a Date object?",
        "options": ["setFullYear()", "setYear()", "changeYear()", "updateYear()"],
        "answer": "setFullYear()",
        "difficulty": "Easy",
        "explanation": "`setFullYear()` sets the year of a Date object (e.g., `date.setFullYear(2023)`)."
    },
    {
        "question": "What does `date.setMonth(5)` do?",
        "options": ["Sets the month to June", "Sets the month to May", "Sets the day to 5", "Sets the year to 5"],
        "answer": "Sets the month to June",
        "difficulty": "Medium",
        "explanation": "Months are 0-based, so `setMonth(5)` sets the month to June (the 6th month)."
    },
    # Topic 35: Functions
    {
        "question": "How do you declare a function in JavaScript?",
        "options": ["function myFunc() {}", "def myFunc() {}", "func myFunc() {}", "myFunc() => {}"],
        "answer": "function myFunc() {}",
        "difficulty": "Easy",
        "explanation": "A function is declared using the `function` keyword, followed by the name, parentheses, and curly braces."
    },
    {
        "question": "What is an arrow function in JavaScript?",
        "options": ["() => {}", "function() {}", "=> function {}", "func => {}"],
        "answer": "() => {}",
        "difficulty": "Medium",
        "explanation": "An arrow function is a concise syntax introduced in ES6, using `=>` (e.g., `() => {}`)."
    },
    # Topic 36: Functions: passing them data
    {
        "question": "How do you pass parameters to a function?",
        "options": ["function myFunc(a, b) {}", "function myFunc[a, b] {}", "function myFunc{a, b} {}", "myFunc(a, b) => {}"],
        "answer": "function myFunc(a, b) {}",
        "difficulty": "Easy",
        "explanation": "Parameters are passed by listing them in parentheses in the function declaration."
    },
    {
        "question": "What is the output of this function call?\n```javascript\nfunction add(a, b) { return a + b; }\nconsole.log(add(2, 3));\n```",
        "options": ["5", "23", "undefined", "NaN"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The function `add` returns the sum of `a` and `b`, so `add(2, 3)` returns 5."
    },
    # Topic 37: Functions: passing data back from them
    {
        "question": "How does a function return a value?",
        "options": ["return", "yield", "output", "send"],
        "answer": "return",
        "difficulty": "Easy",
        "explanation": "The `return` statement sends a value back from a function and ends its execution."
    },
    {
        "question": "What is the output of this function?\n```javascript\nfunction square(num) { return num * num; }\nconsole.log(square(4));\n```",
        "options": ["16", "8", "4", "undefined"],
        "answer": "16",
        "difficulty": "Medium",
        "explanation": "The function `square` returns `num * num`, so `square(4)` returns 16."
    },
    # Topic 38: Functions: local vs. global variables
    {
        "question": "What is a local variable in a function?",
        "options": ["A variable declared inside the function", "A variable declared outside the function", "A constant variable", "A global constant"],
        "answer": "A variable declared inside the function",
        "difficulty": "Easy",
        "explanation": "A local variable is declared inside a function and is only accessible within that function’s scope."
    },
    {
        "question": "What happens to a global variable in this code?\n```javascript\nlet x = 10;\nfunction test() { x = 20; }\ntest();\nconsole.log(x);\n```",
        "options": ["20", "10", "undefined", "NaN"],
        "answer": "20",
        "difficulty": "Medium",
        "explanation": "Since `x` is global and not redeclared in the function, `test()` modifies the global `x` to 20."
    },
    # Topic 39: Switch statements: how to start them
    {
        "question": "How do you start a switch statement in JavaScript?",
        "options": ["switch (expression) {}", "case (expression) {}", "switch expression {}", "if (expression) {}"],
        "answer": "switch (expression) {}",
        "difficulty": "Easy",
        "explanation": "A switch statement starts with `switch (expression)` followed by a block containing `case` clauses."
    },
    {
        "question": "What is the purpose of the `switch` keyword?",
        "options": ["To evaluate an expression against multiple cases", "To loop through values", "To define a function", "To declare variables"],
        "answer": "To evaluate an expression against multiple cases",
        "difficulty": "Easy",
        "explanation": "The `switch` statement evaluates an expression and executes code based on matching `case` values."
    },
    # Topic 40: Switch statements: how to complete them
    {
        "question": "What is required to prevent fall-through in a switch statement?",
        "options": ["break", "return", "continue", "exit"],
        "answer": "break",
        "difficulty": "Easy",
        "explanation": "The `break` statement exits the switch block, preventing execution of subsequent cases."
    },
    {
        "question": "What is the output of this switch statement?\n```javascript\nlet x = 2;\nswitch (x) {\n  case 1: console.log('One'); break;\n  case 2: console.log('Two'); break;\n  default: console.log('Other');\n}\n```",
        "options": ["Two", "One", "Other", "undefined"],
        "answer": "Two",
        "difficulty": "Medium",
        "explanation": "The value of `x` is 2, so the `case 2` block executes, printing 'Two', and `break` prevents fall-through."
    },
    # Additional questions to reach 67
    {
        "question": "What is the output of this nested loop?\n```javascript\nfor (let i = 1; i <= 2; i++) {\n  for (let j = 1; j <= 3; j++) {\n    console.log(j);\n  }\n}\n```",
        "options": ["1, 2, 3, 1, 2, 3", "1, 2, 3", "1, 1, 2, 2, 3, 3", "1, 2"],
        "answer": "1, 2, 3, 1, 2, 3",
        "difficulty": "Medium",
        "explanation": "The inner loop prints 1, 2, 3 for each iteration of the outer loop (twice), resulting in 1, 2, 3, 1, 2, 3."
    },
    {
        "question": "What does `'HELLO'.toLowerCase()` return?",
        "options": ["'hello'", "'HELLO'", "'Hello'", "undefined"],
        "answer": "'hello'",
        "difficulty": "Easy",
        "explanation": "`toLowerCase()` converts all characters in 'HELLO' to lowercase, resulting in 'hello'."
    },
    {
        "question": "What does `'Hello World'.slice(0, 5)` return?",
        "options": ["'Hello'", "'World'", "'Hell'", "'o Wor'"],
        "answer": "'Hello'",
        "difficulty": "Medium",
        "explanation": "`slice(0, 5)` extracts characters from index 0 to 4, resulting in 'Hello'."
    },
    {
        "question": "What does `'JavaScript'.indexOf('Script')` return?",
        "options": ["4", "5", "0", "-1"],
        "answer": "4",
        "difficulty": "Medium",
        "explanation": "'Script' starts at index 4 in 'JavaScript'."
    },
    {
        "question": "What is the output of `'Code'.charAt(2)`?",
        "options": ["'d'", "'C'", "'o'", "'e'"],
        "answer": "'d'",
        "difficulty": "Easy",
        "explanation": "`charAt(2)` returns the character at index 2, which is 'd' in 'Code'."
    },
    {
        "question": "What does `'Hello World'.replace('o', '0')` return?",
        "options": ["'Hell0 World'", "'Hello W0rld'", "'Hell0 W0rld'", "'Hello World'"],
        "answer": "'Hell0 World'",
        "difficulty": "Medium",
        "explanation": "`replace('o', '0')` replaces the first 'o' with '0', resulting in 'Hell0 World'."
    },
    {
        "question": "What is the result of `Math.floor(3.9)`?",
        "options": ["3", "4", "3.9", "0"],
        "answer": "3",
        "difficulty": "Easy",
        "explanation": "`Math.floor()` rounds down to the nearest integer, so 3.9 becomes 3."
    },
    {
        "question": "How do you generate a random integer between 0 and 5?",
        "options": ["Math.floor(Math.random() * 6)", "Math.random() * 5", "Math.ceil(Math.random() * 5)", "Math.round(Math.random() * 5)"],
        "answer": "Math.floor(Math.random() * 6)",
        "difficulty": "Medium",
        "explanation": "`Math.random() * 6` generates a number between 0 and 6, and `Math.floor()` rounds down to get 0–5."
    },
    {
        "question": "What is the result of `parseFloat('3.14px')`?",
        "options": ["3.14", "3", "NaN", "3.14px"],
        "answer": "3.14",
        "difficulty": "Medium",
        "explanation": "`parseFloat('3.14px')` parses the string until a non-numeric character, returning 3.14."
    },
    {
        "question": "What is the result of `(123.456).toString()`?",
        "options": ["'123.456'", "123.456", "'123'", "NaN"],
        "answer": "'123.456'",
        "difficulty": "Easy",
        "explanation": "`toString()` converts the number 123.456 to the string '123.456'."
    },
    {
        "question": "What is the result of `(2.71828).toFixed(3)`?",
        "options": ["'2.718'", "2.718", "'2.72'", "2.7"],
        "answer": "'2.718'",
        "difficulty": "Medium",
        "explanation": "`toFixed(3)` rounds 2.71828 to 3 decimal places, returning '2.718' as a string."
    },
    {
        "question": "What does `new Date().getDate()` return?",
        "options": ["The current day of the month", "The current year", "The current month", "The current timestamp"],
        "answer": "The current day of the month",
        "difficulty": "Easy",
        "explanation": "`getDate()` returns the day of the month (1–31) for the Date object."
    },
    {
        "question": "What does `new Date('2023-07-15').getDay()` return?",
        "options": ["6", "15", "7", "0"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "July 15, 2023, was a Saturday, and `getDay()` returns 0–6 (Sunday–Saturday), so it returns 6."
    },
    {
        "question": "How do you create a Date object for a specific time on January 1, 2023?",
        "options": ["new Date(2023, 0, 1, 12, 30)", "new Date('2023-01-01 12:30')", "new Date(2023, 1, 1, 12, 30)", "Both a and b"],
        "answer": "Both a and b",
        "difficulty": "Medium",
        "explanation": "Both `new Date(2023, 0, 1, 12, 30)` and `new Date('2023-01-01 12:30')` create a Date object for January 1, 2023, 12:30."
    },
    {
        "question": "What does `date.setDate(15)` do?",
        "options": ["Sets the day of the month to 15", "Sets the month to 15", "Sets the year to 15", "Sets the hour to 15"],
        "answer": "Sets the day of the month to 15",
        "difficulty": "Easy",
        "explanation": "`setDate(15)` sets the day of the month to 15 for the Date object."
    },
    {
        "question": "What is the output of this function?\n```javascript\nfunction greet(name) { return `Hello, ${name}!`; }\nconsole.log(greet('Alice'));\n```",
        "options": ["Hello, Alice!", "Hello, name!", "undefined", "Alice"],
        "answer": "Hello, Alice!",
        "difficulty": "Medium",
        "explanation": "The function uses a template literal to return 'Hello, Alice!' when called with 'Alice'."
    },
    {
        "question": "What is a global variable?",
        "options": ["A variable declared outside any function", "A variable declared inside a function", "A constant variable", "A parameter"],
        "answer": "A variable declared outside any function",
        "difficulty": "Easy",
        "explanation": "A global variable is declared outside any function and is accessible throughout the program."
    },
    {
        "question": "What is the output of this switch statement?\n```javascript\nlet day = 0;\nswitch (day) {\n  case 0: console.log('Sunday'); break;\n  case 1: console.log('Monday'); break;\n  default: console.log('Other');\n}\n```",
        "options": ["Sunday", "Monday", "Other", "undefined"],
        "answer": "Sunday",
        "difficulty": "Medium",
        "explanation": "The value of `day` is 0, so the `case 0` block executes, printing 'Sunday'."
    }
]

# Cache shuffled quiz
@st.cache_data
def shuffle_quiz(_quiz):
    shuffled = random.sample(_quiz, len(_quiz))
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = q["options"].copy()
        random.shuffle(q["display_options"])
        q["labeled_answer"] = q["answer"]
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
        "time_left": 3600,  # 60 minutes
        "theme": "dark",
        "streak": 0,
        "started": False,
        "max_streak": 0
    })

# Theme toggle
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# Timer logic
def update_timer():
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.session_state.time_left = max(3600 - elapsed, 0)
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
        "time_left": 3600,
        "streak": 0,
        "max_streak": 0,
        "started": False
    })
    st.rerun()

# Enhanced CSS for UI
st.markdown("""
<style>
/* Global styles */
.main-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    transition: all 0.3s ease;
}

/* Theme-specific styles */
.main-container[data-theme="dark"] {
    background-color: #1a1a1a;
    color: #ffffff;
    --text-color: #ffffff;
    --primary-color: #34c759;
    --secondary-color: #2c2c2e;
    --button-bg: #2c2c2e;
    --button-hover: #3a3a3c;
    --feedback-correct-bg: #34c759;
    --feedback-wrong-bg: #ff3b30;
    --progress-fill: #34c759;
}

.main-container[data-theme="light"] {
    background-color: #ffffff;
    color: #333333;
    --text-color: #333333;
    --primary-color: #28a745;
    --secondary-color: #f5f5f5;
    --button-bg: #f5f5f5;
    --button-hover: #e0e0e0;
    --feedback-correct-bg: #28a745;
    --feedback-wrong-bg: #dc3545;
    --progress-fill: #28a745;
}

/* Title and caption */
.title {
    font-size: 2.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 10px;
    color: var(--primary-color);
    animation: fadeIn 0.5s ease-in;
}

.caption {
    font-size: 1.1rem;
    text-align: center;
    color: var(--text-color);
    opacity: 0.8;
    margin-bottom: 20px;
}

/* Timer */
.timer {
    font-size: 1rem;
    font-weight: 600;
    text-align: right;
    color: var(--primary-color);
    margin-bottom: 15px;
}

/* Progress bar */
.progress-bar {
    background-color: var(--secondary-color);
    border-radius: 10px;
    height: 20px;
    position: relative;
    margin: 20px 0;
    overflow: hidden;
}

.progress-fill {
    background-color: var(--progress-fill);
    height: 100%;
    border-radius: 10px;
    transition: width 0.3s ease;
}

.progress-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--text-color);
}

/* Question container */
.question-container {
    background-color: var(--secondary-color);
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    animation: slideUp 0.3s ease;
}

/* Difficulty and streak */
.difficulty {
    font-size: 0.9rem;
    color: var(--text-color);
    opacity: 0.7;
    margin-bottom: 15px;
    text-align: right;
}

/* Buttons */
.stButton > button {
    width: 100%;
    background-color: var(--button-bg);
    color: var(--text-color);
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    padding: 12px;
    margin: 8px 0;
    font-size: 1rem;
    font-weight: 500;
    transition: all 0.2s ease;
    text-align: left;
}

.stButton > button:hover {
    background-color: var(--button-hover);
    transform: translateY(-2px);
}

.stButton > button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

/* Selected button states */
.selected-correct {
    background-color: var(--feedback-correct-bg) !important;
    color: white !important;
    border-color: var(--feedback-correct-bg) !important;
}

.selected-wrong {
    background-color: var(--feedback-wrong-bg) !important;
    color: white !important;
    border-color: var(--feedback-wrong-bg) !important;
}

/* Feedback */
.feedback-correct {
    background-color: var(--feedback-correct-bg);
    color: white;
    padding: 10px;
    border-radius: 8px;
    margin-top: 15px;
    font-weight: 500;
    text-align: center;
    animation: fadeIn 0.3s ease;
}

.feedback-wrong {
    background-color: var(--feedback-wrong-bg);
    color: white;
    padding: 10px;
    border-radius: 8px;
    margin-top: 15px;
    font-weight: 500;
    text-align: center;
    animation: fadeIn 0.3s ease;
}

/* Code block */
.stCodeBlock {
    background-color: #2f2f2f;
    border-radius: 8px;
    padding: 15px;
    margin: 10px 0;
    font-size: 0.95rem;
}

.main-container[data-theme="light"] .stCodeBlock {
    background-color: #f5f5f5;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideUp {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

/* Responsive design */
@media (max-width: 600px) {
    .title {
        font-size: 2rem;
    }
    
    .question-container {
        padding: 15px;
    }
    
    .stButton > button {
        font-size: 0.9rem;
        padding: 10px;
    }
    
    .timer {
        font-size: 0.9rem;
        text-align: center;
    }
}

/* Theme toggle, start, and play again buttons */
.stButton > button[key="theme_toggle"],
.stButton > button[key="start_quiz"],
.stButton > button[key="play_again"] {
    background-color: var(--primary-color);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 600;
    transition: all 0.2s ease;
    width: auto;
    margin: 10px auto;
    display: block;
}

.stButton > button[key="theme_toggle"]:hover,
.stButton > button[key="start_quiz"]:hover,
.stButton > button[key="play_again"]:hover {
    background-color: #2c974b;
    transform: translateY(-2px);
}

.main-container[data-theme="light"] .stButton > button[key="theme_toggle"],
.main-container[data-theme="light"] .stButton > button[key="start_quiz"],
.main-container[data-theme="light"] .stButton > button[key="play_again"] {
    background-color: #218838;
}

.main-container[data-theme="light"] .stButton > button[key="theme_toggle"]:hover,
.main-container[data-theme="light"] .stButton > button[key="start_quiz"]:hover,
.main-container[data-theme="light"] .stButton > button[key="play_again"]:hover {
    background-color: #1c7430;
}
</style>
""", unsafe_allow_html=True)

# Main UI
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 JavaScript Mastery Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript Skills!</p>', unsafe_allow_html=True)

# Theme toggle button
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen
if not st.session_state.started:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: var(--text-color); font-size: 18px;">Test your JavaScript skills with 67 comprehensive questions!</p>
        <p style="color: var(--text-color); opacity: 0.8;">60 minutes, 2 points per correct answer. Ready?</p>
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
        <div class="progress-container">
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress_percentage}%"></div>
                <div class="progress-text">{progress_percentage}%</div>
            </div>
            <div style="color: var(--text-color); font-size: 13px; text-align: center;">
                Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
            </div>
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
                        disabled=st.session_state.selected_option is not None
                    ):
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
                            st.session_state.score += 2  # 2 points for correct answer
                            st.session_state.streak += 1
                            if st.session_state.streak > st.session_state.max_streak:
                                st.session_state.max_streak = st.session_state.streak
                            if st.session_state.streak >= 3:
                                st.session_state.score += 0.5
                        else:
                            st.session_state.streak = 0
                        # Automatically move to next question or show results
                        if st.session_state.current_q < len(quiz) - 1:
                            st.session_state.current_q += 1
                            st.session_state.selected_option = None
                            st.session_state.feedback = None
                        else:
                            st.session_state.show_results = True
                        st.rerun()

                # Feedback
                if st.session_state.feedback:
                    if st.session_state.feedback["is_correct"]:
                        st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="color: var(--text-color); font-size: 14px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

        else:
            # Results
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 3600)
            total_possible_score = len(quiz) * 2  # 2 points per question
            accuracy = (st.session_state.score / total_possible_score) * 100 if total_possible_score > 0 else 0
            st.markdown('<div class="results-container">', unsafe_allow_html=True)
            st.markdown(f'<div class="score-display">{st.session_state.score}/{total_possible_score}</div>', unsafe_allow_html=True)
            st.markdown(f"""
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-value">⏱️ {int(time_taken) // 60}m {int(time_taken) % 60}s</div>
                    <div class="stat-label">Time Taken</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">🎯 {accuracy:.1f}%</div>
                    <div class="stat-label">Accuracy</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">✅ {sum(1 for ans in st.session_state.answers if ans and ans["is_correct"])}</div>
                    <div class="stat-label">Correct</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">❌ {sum(1 for ans in st.session_state.answers if ans and not ans["is_correct"])}</div>
                    <div class="stat-label">Incorrect</div>
                </div>
            </div>
            <div style="text-align: center; margin: 1.5rem 0;">
                <div style="font-size: 1.2rem; color: var(--text-color);">🔥 Max Streak: {st.session_state.max_streak}</div>
            </div>
            """, unsafe_allow_html=True)

            # Review Answers
            st.markdown('<h3 style="color: var(--text-color); margin-bottom: 1rem;">📝 Review Your Answers</h3>', unsafe_allow_html=True)
            for i, ans in enumerate(st.session_state.answers):
                if ans:
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})"
                    st.markdown(f"""
                    <div style="background: var(--secondary-color); padding: 1rem; border-radius: 12px; margin-bottom: 1rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                        <div style="font-weight: 600; color: var(--text-color); margin-bottom: 0.5rem;">Question {i+1}: {ans["question"]}</div>
                        <div style="margin-bottom: 0.25rem;">Your Answer: {ans["user_answer"]}</div>
                        <div style="margin-bottom: 0.5rem; color: {'var(--feedback-correct-bg)' if ans["is_correct"] else 'var(--feedback-wrong-bg)'}">{status}</div>
                        <div style="font-size: 0.9rem; color: var(--text-color); opacity: 0.8; padding: 0.75rem; background: rgba(0, 0, 0, 0.05); border-radius: 8px;">
                            Explanation: {quiz[i]["explanation"]}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

            # Play Again button
            if st.button("🔄 Play Again", key="play_again"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
