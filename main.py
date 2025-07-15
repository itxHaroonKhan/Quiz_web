import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data (67 questions on nested loops, strings, numbers, dates, functions, switch statements)
quiz = [
    {
        "question": "How do you write a nested for loop to iterate over a 2D array in JavaScript?\n```javascript\nfor (let i = 0; i < array.length; i++) { for (let j = 0; j < array[i].length; j++) { } }\n```",
        "options": [
            "for (let i = 0; i < array.length; i++) { for (let j = 0; j < array[i].length; j++) { } }",
            "for (let i = 0; i < array; i++) { for (let j = 0; j < array[i]; j++) { } }",
            "for (let i in array) { for (let j in array[i]) { } }",
            "for (let i of array) { for (let j of array) { } }"
        ],
        "answer": "for (let i = 0; i < array.length; i++) { for (let j = 0; j < array[i].length; j++) { } }",
        "difficulty": "Medium",
        "explanation": "A nested for loop uses two indices: `i` for rows and `j` for columns, accessing each element as `array[i][j]`."
    },
    {
        "question": "What is the purpose of a nested for loop in JavaScript?",
        "options": [
            "To iterate over multi-dimensional data",
            "To repeat a single loop multiple times",
            "To create a function inside another function",
            "To replace a while loop"
        ],
        "answer": "To iterate over multi-dimensional data",
        "difficulty": "Easy",
        "explanation": "Nested for loops are used to process multi-dimensional data, such as 2D arrays, by iterating over each dimension."
    },
    {
        "question": "How many iterations does the inner loop perform in this code?\n```javascript\nfor (let i = 0; i < 4; i++) { for (let j = 0; j < 3; j++) { } }\n```",
        "options": [
            "12",
            "4",
            "3",
            "7"
        ],
        "answer": "12",
        "difficulty": "Medium",
        "explanation": "The outer loop runs 4 times, and the inner loop runs 3 times per outer iteration, so 4 * 3 = 12 total iterations."
    },
    {
        "question": "What does the `toUpperCase()` method do in JavaScript?",
        "options": [
            "Converts a string to uppercase",
            "Converts a string to lowercase",
            "Capitalizes the first letter",
            "Removes spaces from a string"
        ],
        "answer": "Converts a string to uppercase",
        "difficulty": "Easy",
        "explanation": "`toUpperCase()` converts all characters in a string to uppercase, e.g., 'hello' becomes 'HELLO'."
    },
    {
        "question": "How do you convert a string to lowercase in JavaScript?",
        "options": [
            "string.toLowerCase()",
            "string.toUpperCase()",
            "string.lower()",
            "string.toLowCase()"
        ],
        "answer": "string.toLowerCase()",
        "difficulty": "Easy",
        "explanation": "`toLowerCase()` converts all characters in a string to lowercase, e.g., 'HELLO' becomes 'hello'."
    },
    {
        "question": "How do you capitalize the first letter of a string in JavaScript?",
        "options": [
            "string.charAt(0).toUpperCase() + string.slice(1)",
            "string[0].toUpperCase() + string.slice(1)",
            "string.capitalizeFirst()",
            "string.toUpperCase(0)"
        ],
        "answer": "string.charAt(0).toUpperCase() + string.slice(1)",
        "difficulty": "Medium",
        "explanation": "Use `charAt(0).toUpperCase()` for the first character and `slice(1)` for the rest of the string."
    },
    {
        "question": "What is the length of the string `'JavaScript'`?",
        "options": [
            "10",
            "9",
            "11",
            "8"
        ],
        "answer": "10",
        "difficulty": "Easy",
        "explanation": "The `length` property returns the number of characters in a string, so `'JavaScript'.length` is 10."
    },
    {
        "question": "How do you extract characters from index 2 to 5 in a string?",
        "options": [
            "string.slice(2, 6)",
            "string.substring(2, 5)",
            "string.substr(2, 4)",
            "string.extract(2, 5)"
        ],
        "answer": "string.slice(2, 6)",
        "difficulty": "Medium",
        "explanation": "`slice(2, 6)` extracts characters from index 2 up to (but not including) index 6."
    },
    {
        "question": "What does `string.substr(1, 3)` return for the string `'hello'`?",
        "options": [
            "ell",
            "hel",
            "llo",
            "lo"
        ],
        "answer": "ell",
        "difficulty": "Medium",
        "explanation": "`substr(1, 3)` extracts 3 characters starting from index 1, so `hello` becomes `ell`. Note: `substr` is deprecated."
    },
    {
        "question": "Which method checks if a string contains 'code'?",
        "options": [
            "string.includes('code')",
            "string.contains('code')",
            "string.has('code')",
            "string.find('code')"
        ],
        "answer": "string.includes('code')",
        "difficulty": "Easy",
        "explanation": "`includes('code')` returns `true` if the string contains 'code', otherwise `false`."
    },
    {
        "question": "What does `string.indexOf('test')` return if 'test' is not found?",
        "options": [
            "-1",
            "0",
            "null",
            "undefined"
        ],
        "answer": "-1",
        "difficulty": "Medium",
        "explanation": "`indexOf('test')` returns -1 if the substring 'test' is not found in the string."
    },
    {
        "question": "How do you find the character at index 4 in a string?",
        "options": [
            "string.charAt(4)",
            "string.getChar(4)",
            "string.char(4)",
            "string.atIndex(4)"
        ],
        "answer": "string.charAt(4)",
        "difficulty": "Easy",
        "explanation": "`charAt(4)` returns the character at index 4. `string[4]` is also valid."
    },
    {
        "question": "What does `string.at(2)` return for the string `'hello'`?",
        "options": [
            "l",
            "h",
            "e",
            "o"
        ],
        "answer": "l",
        "difficulty": "Medium",
        "explanation": "`at(2)` returns the character at index 2, which is 'l' in 'hello'. It supports negative indices."
    },
    {
        "question": "How do you replace the first 'a' with 'b' in a string?",
        "options": [
            "string.replace('a', 'b')",
            "string.replaceAll('a', 'b')",
            "string.swap('a', 'b')",
            "string.change('a', 'b')"
        ],
        "answer": "string.replace('a', 'b')",
        "difficulty": "Medium",
        "explanation": "`replace('a', 'b')` replaces only the first occurrence of 'a' with 'b'."
    },
    {
        "question": "How do you replace all 'x' with 'y' in a string?",
        "options": [
            "string.replaceAll('x', 'y')",
            "string.replace('x', 'y')",
            "string.update('x', 'y')",
            "string.modify('x', 'y')"
        ],
        "answer": "string.replaceAll('x', 'y')",
        "difficulty": "Medium",
        "explanation": "`replaceAll('x', 'y')` replaces all occurrences of 'x' with 'y'."
    },
    {
        "question": "What does `Math.round(4.6)` return?",
        "options": [
            "5",
            "4",
            "4.6",
            "5.0"
        ],
        "answer": "5",
        "difficulty": "Easy",
        "explanation": "`Math.round(4.6)` rounds 4.6 to the nearest integer, which is 5."
    },
    {
        "question": "How do you round a number down to the nearest integer?",
        "options": [
            "Math.floor(number)",
            "Math.round(number)",
            "Math.ceil(number)",
            "Math.trunc(number)"
        ],
        "answer": "Math.floor(number)",
        "difficulty": "Easy",
        "explanation": "`Math.floor(number)` rounds a number down to the nearest integer, e.g., 4.9 becomes 4."
    },
    {
        "question": "What does `Math.ceil(3.1)` return?",
        "options": [
            "4",
            "3",
            "3.1",
            "4.0"
        ],
        "answer": "4",
        "difficulty": "Easy",
        "explanation": "`Math.ceil(3.1)` rounds 3.1 up to the nearest integer, which is 4."
    },
    {
        "question": "What is the range of numbers returned by `Math.random()`?",
        "options": [
            "0 to 1 (exclusive)",
            "0 to 1 (inclusive)",
            "1 to 10",
            "0 to 100"
        ],
        "answer": "0 to 1 (exclusive)",
        "difficulty": "Easy",
        "explanation": "`Math.random()` returns a random number from 0 (inclusive) to 1 (exclusive)."
    },
    {
        "question": "How do you generate a random integer between 1 and 5?",
        "options": [
            "Math.floor(Math.random() * 5) + 1",
            "Math.random() * 5",
            "Math.round(Math.random() * 5)",
            "Math.floor(Math.random() * 5)"
        ],
        "answer": "Math.floor(Math.random() * 5) + 1",
        "difficulty": "Medium",
        "explanation": "`Math.random() * 5` gives 0 to 4.999..., `Math.floor` rounds down, and `+ 1` shifts to 1–5."
    },
    {
        "question": "How do you convert the string '789' to an integer?",
        "options": [
            "parseInt('789')",
            "parseFloat('789')",
            "toInt('789')",
            "String.toNumber('789')"
        ],
        "answer": "parseInt('789')",
        "difficulty": "Medium",
        "explanation": "`parseInt('789')` converts the string '789' to the integer 789."
    },
    {
        "question": "What does `parseFloat('12.34')` return?",
        "options": [
            "12.34",
            "12",
            "12.34.0",
            "13"
        ],
        "answer": "12.34",
        "difficulty": "Medium",
        "explanation": "`parseFloat('12.34')` converts the string '12.34' to the floating-point number 12.34."
    },
    {
        "question": "How do you convert a number to a string in JavaScript?",
        "options": [
            "number.toString()",
            "number.toStr()",
            "convertToString(number)",
            "number.string()"
        ],
        "answer": "number.toString()",
        "difficulty": "Easy",
        "explanation": "`toString()` converts a number to a string, e.g., 123 becomes '123'."
    },
    {
        "question": "How do you convert a string to a number using the Number constructor?",
        "options": [
            "Number(string)",
            "string.toNumber()",
            "parseNumber(string)",
            "toNumber(string)"
        ],
        "answer": "Number(string)",
        "difficulty": "Medium",
        "explanation": "`Number(string)` converts a string to a number, e.g., `Number('123')` returns 123."
    },
    {
        "question": "How do you limit a number to 2 decimal places?",
        "options": [
            "number.toFixed(2)",
            "number.toPrecision(2)",
            "number.round(2)",
            "number.limit(2)"
        ],
        "answer": "number.toFixed(2)",
        "difficulty": "Medium",
        "explanation": "`toFixed(2)` formats a number to 2 decimal places, returning a string, e.g., 3.14159 becomes '3.14'."
    },
    {
        "question": "What does `number.toPrecision(3)` do?",
        "options": [
            "Formats a number to 3 significant digits",
            "Formats a number to 3 decimal places",
            "Rounds a number to 3 integers",
            "Converts a number to a 3-character string"
        ],
        "answer": "Formats a number to 3 significant digits",
        "difficulty": "Medium",
        "explanation": "`toPrecision(3)` formats a number to 3 significant digits, e.g., 123.456 becomes '123'."
    },
    {
        "question": "How do you get the current date and time in JavaScript?",
        "options": [
            "new Date()",
            "Date.now()",
            "Date.getCurrent()",
            "new DateTime()"
        ],
        "answer": "new Date()",
        "difficulty": "Easy",
        "explanation": "`new Date()` creates a Date object representing the current date and time."
    },
    {
        "question": "What does `Date.now()` return?",
        "options": [
            "A timestamp in milliseconds",
            "A Date object",
            "The current date as a string",
            "The current time in seconds"
        ],
        "answer": "A timestamp in milliseconds",
        "difficulty": "Medium",
        "explanation": "`Date.now()` returns the milliseconds since January 1, 1970 (Unix epoch)."
    },
    {
        "question": "How do you extract the year from a Date object?",
        "options": [
            "date.getFullYear()",
            "date.getYear()",
            "date.year()",
            "date.getDate()"
        ],
        "answer": "date.getFullYear()",
        "difficulty": "Medium",
        "explanation": "`getFullYear()` returns the four-digit year of a Date object, e.g., 2025."
    },
    {
        "question": "How do you get the month from a Date object?",
        "options": [
            "date.getMonth()",
            "date.getDate()",
            "date.month()",
            "date.getMonthNumber()"
        ],
        "answer": "date.getMonth()",
        "difficulty": "Medium",
        "explanation": "`getMonth()` returns the month (0–11), where 0 is January."
    },
    {
        "question": "How do you create a Date object for February 20, 2024?",
        "options": [
            "new Date(2024, 1, 20)",
            "new Date(2024, 2, 20)",
            "new Date('2024-02-20')",
            "new Date('February 20, 2024')"
        ],
        "answer": "new Date(2024, 1, 20)",
        "difficulty": "Medium",
        "explanation": "`new Date(2024, 1, 20)` creates a Date for February 20, 2024, as months are 0-based."
    },
    {
        "question": "How do you specify a Date object for 10:30 AM on July 15, 2025?",
        "options": [
            "new Date(2025, 6, 15, 10, 30)",
            "new Date(2025, 7, 15, 10, 30)",
            "new Date('2025-07-15 10:30')",
            "new Date('July 15, 2025 10:30')"
        ],
        "answer": "new Date(2025, 6, 15, 10, 30)",
        "difficulty": "Medium",
        "explanation": "`new Date(2025, 6, 15, 10, 30)` creates a Date for July 15, 2025, at 10:30 AM."
    },
    {
        "question": "How do you set the year of a Date object to 2026?",
        "options": [
            "date.setFullYear(2026)",
            "date.setYear(2026)",
            "date.updateYear(2026)",
            "date.changeYear(2026)"
        ],
        "answer": "date.setFullYear(2026)",
        "difficulty": "Medium",
        "explanation": "`setFullYear(2026)` sets the year of a Date object to 2026."
    },
    {
        "question": "How do you add 2 days to a Date object?",
        "options": [
            "date.setDate(date.getDate() + 2)",
            "date.addDays(2)",
            "date.setDay(date.getDay() + 2)",
            "date.updateDate(2)"
        ],
        "answer": "date.setDate(date.getDate() + 2)",
        "difficulty": "Medium",
        "explanation": "`setDate(date.getDate() + 2)` increments the day of the month by 2."
    },
    {
        "question": "How do you define a named function in JavaScript?",
        "options": [
            "function myFunc() {}",
            "def myFunc() {}",
            "func myFunc() {}",
            "myFunc() => {}"
        ],
        "answer": "function myFunc() {}",
        "difficulty": "Easy",
        "explanation": "A named function is defined using the `function` keyword, a name, parentheses, and curly braces."
    },
    {
        "question": "What is an arrow function in JavaScript?",
        "options": [
            "A concise function syntax using =>",
            "A function with a return statement",
            "A function inside a loop",
            "A function with no parameters"
        ],
        "answer": "A concise function syntax using =>",
        "difficulty": "Medium",
        "explanation": "Arrow functions use the `=>` syntax, e.g., `const myFunc = () => {}`."
    },
    {
        "question": "How do you pass a parameter to a function?",
        "options": [
            "function myFunc(param) {}",
            "function myFunc: param {}",
            "function myFunc[param] {}",
            "function myFunc { param }"
        ],
        "answer": "function myFunc(param) {}",
        "difficulty": "Easy",
        "explanation": "Parameters are defined inside the parentheses of a function, e.g., `myFunc(param)`."
    },
    {
        "question": "How do you pass multiple parameters to a function?",
        "options": [
            "function myFunc(a, b) {}",
            "function myFunc(a; b) {}",
            "function myFunc[a, b] {}",
            "function myFunc {a, b}"
        ],
        "answer": "function myFunc(a, b) {}",
        "difficulty": "Easy",
        "explanation": "Multiple parameters are separated by commas in the function definition."
    },
    {
        "question": "What does a function return if it lacks a `return` statement?",
        "options": [
            "undefined",
            "null",
            "0",
            "false"
        ],
        "answer": "undefined",
        "difficulty": "Medium",
        "explanation": "A function without a `return` statement implicitly returns `undefined`."
    },
    {
        "question": "How do you return a value from a function?",
        "options": [
            "return value",
            "output value",
            "send value",
            "give value"
        ],
        "answer": "return value",
        "difficulty": "Easy",
        "explanation": "The `return` statement sends a value back and stops function execution."
    },
    {
        "question": "What is a local variable in a function?",
        "options": [
            "A variable declared inside a function",
            "A variable declared outside a function",
            "A variable shared across functions",
            "A variable with a fixed value"
        ],
        "answer": "A variable declared inside a function",
        "difficulty": "Medium",
        "explanation": "Local variables are declared inside a function and are only accessible within it."
    },
    {
        "question": "What is a global variable in JavaScript?",
        "options": [
            "A variable declared outside any function",
            "A variable inside a function",
            "A variable passed to a function",
            "A variable with block scope"
        ],
        "answer": "A variable declared outside any function",
        "difficulty": "Medium",
        "explanation": "Global variables are declared outside functions and are accessible throughout the code."
    },
    {
        "question": "What happens if a local variable shadows a global variable?",
        "options": [
            "The local variable is used inside the function",
            "The global variable is used",
            "An error occurs",
            "The variables merge"
        ],
        "answer": "The local variable is used inside the function",
        "difficulty": "Medium",
        "explanation": "A local variable with the same name as a global variable takes precedence inside the function."
    },
    {
        "question": "How do you start a switch statement in JavaScript?",
        "options": [
            "switch (expression) {",
            "case (expression) {",
            "if (expression) {",
            "match (expression) {"
        ],
        "answer": "switch (expression) {",
        "difficulty": "Easy",
        "explanation": "A `switch` statement starts with `switch (expression) {`, followed by case clauses."
    },
    {
        "question": "What is the purpose of a `case` clause in a switch statement?",
        "options": [
            "To specify a value to match",
            "To start the switch",
            "To end the switch",
            "To loop through values"
        ],
        "answer": "To specify a value to match",
        "difficulty": "Easy",
        "explanation": "A `case` clause specifies a value to compare against the switch expression."
    },
    {
        "question": "How do you complete a switch statement?",
        "options": [
            "Add a `default` case and close with `}`",
            "Add a `break` and close with `}`",
            "Add a `return` and close with `}`",
            "Add an `end` keyword"
        ],
        "answer": "Add a `default` case and close with `}`",
        "difficulty": "Medium",
        "explanation": "A `switch` statement typically includes a `default` case for unmatched values and ends with `}`."
    },
    {
        "question": "What does the `break` statement do in a switch case?",
        "options": [
            "Exits the current case",
            "Skips to the next case",
            "Returns a value",
            "Stops the entire program"
        ],
        "answer": "Exits the current case",
        "difficulty": "Medium",
        "explanation": "The `break` statement exits the current case, preventing fall-through to the next case."
    },
    {
        "question": "What happens if you omit `break` in a switch case?",
        "options": [
            "Execution continues to the next case",
            "The switch stops",
            "An error occurs",
            "The function returns"
        ],
        "answer": "Execution continues to the next case",
        "difficulty": "Medium",
        "explanation": "Without `break`, execution falls through to the next case."
    },
    {
        "question": "How do you handle multiple cases with the same action in a switch statement?",
        "options": [
            "case 'a': case 'b': code;",
            "case 'a', 'b': code;",
            "case 'a' || 'b': code;",
            "case 'a' && 'b': code;"
        ],
        "answer": "case 'a': case 'b': code;",
        "difficulty": "Medium",
        "explanation": "Multiple `case` labels without `break` share the same code block (fall-through)."
    },
    {
        "question": "What does `'hello'.slice(-2)` return?",
        "options": [
            "lo",
            "he",
            "ll",
            "el"
        ],
        "answer": "lo",
        "difficulty": "Medium",
        "explanation": "`slice(-2)` extracts the last 2 characters of 'hello', which is 'lo'."
    },
    {
        "question": "What does `Math.trunc(7.8)` return?",
        "options": [
            "7",
            "8",
            "7.8",
            "8.0"
        ],
        "answer": "7",
        "difficulty": "Easy",
        "explanation": "`Math.trunc(7.8)` removes the decimal part, returning 7."
    },
    {
        "question": "How do you generate a random integer between 0 and 9?",
        "options": [
            "Math.floor(Math.random() * 10)",
            "Math.random() * 10",
            "Math.round(Math.random() * 10)",
            "Math.floor(Math.random() * 9)"
        ],
        "answer": "Math.floor(Math.random() * 10)",
        "difficulty": "Medium",
        "explanation": "`Math.random() * 10` generates 0 to 9.999..., and `Math.floor` rounds down to 0–9."
    },
    {
        "question": "How do you convert a string to a number using the unary plus operator?",
        "options": [
            "+string",
            "string++",
            "++string",
            "-string"
        ],
        "answer": "+string",
        "difficulty": "Medium",
        "explanation": "The unary plus operator `+` converts a string to a number, e.g., +'123' returns 123."
    },
    {
        "question": "How do you get the current minutes from a Date object?",
        "options": [
            "date.getMinutes()",
            "date.getMinute()",
            "date.minutes()",
            "date.getTime().minutes"
        ],
        "answer": "date.getMinutes()",
        "difficulty": "Medium",
        "explanation": "`getMinutes()` returns the minutes (0–59) of a Date object."
    },
    {
        "question": "How do you set the minutes of a Date object to 45?",
        "options": [
            "date.setMinutes(45)",
            "date.setMinute(45)",
            "date.updateMinutes(45)",
            "date.changeMinutes(45)"
        ],
        "answer": "date.setMinutes(45)",
        "difficulty": "Medium",
        "explanation": "`setMinutes(45)` sets the minutes of a Date object to 45."
    },
    {
        "question": "What is a function expression in JavaScript?",
        "options": [
            "A function assigned to a variable",
            "A named function declaration",
            "A function inside a loop",
            "A function with no return value"
        ],
        "answer": "A function assigned to a variable",
        "difficulty": "Medium",
        "explanation": "A function expression assigns an anonymous function to a variable, e.g., `const myFunc = function() {}`."
    },
    {
        "question": "What is the scope of a variable declared with `const` inside a function?",
        "options": [
            "Block scope",
            "Global scope",
            "Function scope",
            "Module scope"
        ],
        "answer": "Block scope",
        "difficulty": "Medium",
        "explanation": "Variables declared with `const` inside a function have block scope, limited to the block they are defined in."
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

# CSS styling
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
        --correct: #34c759;
        --wrong: #ff3b30;
        --text-light: #b0b0d0;
        --card-bg: #2c2c54;
    }
    [data-theme="light"] {
        --bg-gradient: linear-gradient(180deg, #e0e7ff, #f3e8ff);
        --bg-container: #ffffff;
        --text-color: #1f2937;
        --button-bg: linear-gradient(45deg, #4f46e5, #7c3aed);
        --button-hover: linear-gradient(45deg, #6366f1, #a78bfa);
        --code-bg: #f1f5f9;
        --shadow: rgba(0,0,0,0.1);
        --correct: #34c759;
        --wrong: #ff3b30;
        --text-light: #6b7280;
        --card-bg: #ffffff;
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
        background: var(--correct) !important;
        transform: scale(1.05);
    }
    .selected-wrong {
        background: var(--wrong) !important;
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
        color: var(--correct);
        font-weight: 600;
        font-size: 18px;
        margin: 15px 0;
        animation: fadeIn 0.5s ease;
    }
    .feedback-wrong {
        color: var(--wrong);
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
        color: var(--text-light);
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
        color: var(--text-light);
        margin-bottom: 10px;
    }
    .score-display {
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        color: var(--text-color);
        margin-bottom: 1rem;
    }
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        text-align: center;
    }
    .stat-item {
        background: rgba(168, 85, 247, 0.05);
        padding: 1rem;
        border-radius: 12px;
    }
    .stat-value {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--text-color);
    }
    .stat-label {
        font-size: 0.9rem;
        color: var(--text-light);
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
        white-space: pre-wrap;
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
        .stats-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
""", unsafe_allow_html=True)

# Main UI
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 JavaScript Fundamentals Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Test Your JavaScript Skills!</p>', unsafe_allow_html=True)

# Theme toggle button
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen
if not st.session_state.started:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: var(--text-color); font-size: 18px;">Test your JavaScript skills with 67 questions on loops, strings, numbers, dates, functions, and switch statements!</p>
        <p style="color: var(--text-light);">60 minutes, 2 points per correct answer, 0.5 bonus for streaks of 3+ correct answers. Ready?</p>
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
                    parts = q["question"].split("```javascript
                    question_text = parts[0].strip()
                    code_snippet = parts[1].split("```")[0].strip() if len(parts) > 1 else ""
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{question_text}**")
                    if code_snippet:
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
                        key=f"q{i}_{q['id']}",
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
                        # Move to next question or show results
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

            # Confetti for high score
            if accuracy > 80:
                st.markdown("""
                <script>
                    confetti({
                        particleCount: 100,
                        spread: 70,
                        origin: { y: 0.6 }
                    });
                </script>
                """, unsafe_allow_html=True)

            # Review Answers
            st.markdown('<h3 style="color: var(--text-color); margin-bottom: 1rem;">📝 Review Your Answers</h3>', unsafe_allow_html=True)
            for i, ans in enumerate(st.session_state.answers):
                if ans:
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})"
                    question_text = ans["question"].split("```javascript
                    st.markdown(f"""
                    <div style="background: var(--card-bg); padding: 1rem; border-radius: 12px; margin-bottom: 1rem; box-shadow: var(--shadow);">
                        <div style="font-weight: 600; color: var(--text-color); margin-bottom: 0.5rem;">Question {i+1}: {question_text}</div>
                        <div style="margin-bottom: 0.25rem;">Your Answer: {ans["user_answer"]}</div>
                        <div style="margin-bottom: 0.5rem; color: {'var(--correct)' if ans["is_correct"] else 'var(--wrong)'}">{status}</div>
                        <div style="font-size: 0.9rem; color: var(--text-light); padding: 0.75rem; background: rgba(168, 85, 247, 0.05); border-radius: 8px;">
                            Explanation: {quiz[i]["explanation"]}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

            # Play Again button
            if st.button("🔄 Play Again", key="play_again"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
