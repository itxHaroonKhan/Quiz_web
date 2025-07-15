```python
import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 67 questions covering specified JavaScript topics
quiz = [
    # Topic 20: for loops nested
    {
        "question": "What does the following nested loop output?\n```javascript\nfor (let i = 1; i <= 2; i++) {\n  for (let j = 1; j <= 2; j++) {\n    console.log(i, j);\n  }\n}\n```",
        "options": [
            "1 1, 1 2, 2 1, 2 2",
            "1 1, 2 2",
            "1 2, 2 1",
            "1 1, 1 1, 2 2, 2 2"
        ],
        "answer": "1 1, 1 2, 2 1, 2 2",
        "difficulty": "Medium",
        "explanation": "The outer loop runs for i=1 and i=2. For each i, the inner loop runs for j=1 and j=2, printing each combination."
    },
    {
        "question": "How many times will 'Hello' be printed in this nested loop?\n```javascript\nfor (let i = 0; i < 3; i++) {\n  for (let j = 0; j < 2; j++) {\n    console.log('Hello');\n  }\n}\n```",
        "options": ["3", "5", "6", "2"],
        "answer": "6",
        "difficulty": "Easy",
        "explanation": "The outer loop runs 3 times, and for each iteration, the inner loop runs 2 times, resulting in 3 * 2 = 6 prints."
    },
    {
        "question": "What is the purpose of a nested for loop in JavaScript?",
        "options": [
            "To repeat a single task multiple times",
            "To iterate over multi-dimensional arrays or perform repeated tasks for each iteration",
            "To replace a while loop",
            "To execute asynchronous code"
        ],
        "answer": "To iterate over multi-dimensional arrays or perform repeated tasks for each iteration",
        "difficulty": "Easy",
        "explanation": "Nested for loops are used to handle multi-dimensional data structures or to perform tasks for each combination of indices."
    },
    # Topic 21: Changing case
    {
        "question": "How do you convert a string to uppercase in JavaScript?",
        "options": [
            "str.toUpperCase()",
            "str.upperCase()",
            "str.toUpper()",
            "str.makeUpperCase()"
        ],
        "answer": "str.toUpperCase()",
        "difficulty": "Easy",
        "explanation": "The `toUpperCase()` method converts all characters in a string to uppercase."
    },
    {
        "question": "What does `str.toLowerCase()` do in JavaScript?",
        "options": [
            "Converts a string to lowercase",
            "Converts a string to uppercase",
            "Removes spaces from a string",
            "Reverses a string"
        ],
        "answer": "Converts a string to lowercase",
        "difficulty": "Easy",
        "explanation": "The `toLowerCase()` method converts all characters in a string to lowercase."
    },
    {
        "question": "What will `'Hello World'.toUpperCase()` return?",
        "options": ["hello world", "HELLO WORLD", "Hello World", "hELLO wORLD"],
        "answer": "HELLO WORLD",
        "difficulty": "Easy",
        "explanation": "`toUpperCase()` converts all characters to uppercase, so 'Hello World' becomes 'HELLO WORLD'."
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
        "question": "What does `'Hello'.slice(1, 3)` return?",
        "options": ["He", "el", "ell", "lo"],
        "answer": "el",
        "difficulty": "Medium",
        "explanation": "The `slice(start, end)` method extracts characters from index `start` to `end-1`. Here, `slice(1, 3)` returns characters at indices 1 and 2, which are 'e' and 'l'."
    },
    {
        "question": "How do you extract the first 3 characters of a string 'JavaScript'?",
        "options": [
            "'JavaScript'.substring(0, 3)",
            "'JavaScript'.slice(3, 0)",
            "'JavaScript'.substr(0, 3)",
            "Both A and C"
        ],
        "answer": "Both A and C",
        "difficulty": "Medium",
        "explanation": "Both `substring(0, 3)` and `substr(0, 3)` extract characters from index 0 to 2, returning 'Jav'."
    },
    # Topic 23: Strings: finding segments
    {
        "question": "What does `'Hello World'.indexOf('World')` return?",
        "options": ["5", "6", "-1", "0"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "The `indexOf()` method returns the starting index of the first occurrence of 'World', which is at index 6 (after 'Hello ')."
    },
    {
        "question": "What happens if `'test'.indexOf('x')` is called?",
        "options": [
            "Returns -1",
            "Returns 0",
            "Throws an error",
            "Returns the length of the string"
        ],
        "answer": "Returns -1",
        "difficulty": "Easy",
        "explanation": "If the substring is not found, `indexOf()` returns -1."
    },
    {
        "question": "Which method checks if a string contains a substring?",
        "options": ["includes()", "contains()", "has()", "search()"],
        "answer": "includes()",
        "difficulty": "Easy",
        "explanation": "The `includes()` method returns `true` if the string contains the specified substring, otherwise `false`."
    },
    # Topic 24: Strings: finding a character at a location
    {
        "question": "How do you find the character at index 2 in 'Hello'?",
        "options": ["'Hello'[2]", "'Hello'.charAt(2)", "Both A and B", "'Hello'.getChar(2)"],
        "answer": "Both A and B",
        "difficulty": "Easy",
        "explanation": "Both bracket notation (`[2]`) and `charAt(2)` return the character at index 2, which is 'l'."
    },
    {
        "question": "What does `'JavaScript'.charAt(4)` return?",
        "options": ["S", "c", "r", "i"],
        "answer": "S",
        "difficulty": "Easy",
        "explanation": "The `charAt(4)` method returns the character at index 4, which is 'S' in 'JavaScript'."
    },
    {
        "question": "What happens if you call `'test'.charAt(10)`?",
        "options": [
            "Returns an empty string",
            "Throws an error",
            "Returns undefined",
            "Returns the last character"
        ],
        "answer": "Returns an empty string",
        "difficulty": "Medium",
        "explanation": "If the index is out of range, `charAt()` returns an empty string."
    },
    # Topic 25: Strings: replacing characters
    {
        "question": "How do you replace 'cat' with 'dog' in 'I have a cat'?",
        "options": [
            "'I have a cat'.replace('cat', 'dog')",
            "'I have a cat'.replaceAll('cat', 'dog')",
            "Both A and B",
            "'I have a cat'.sub('cat', 'dog')"
        ],
        "answer": "Both A and B",
        "difficulty": "Medium",
        "explanation": "`replace('cat', 'dog')` replaces the first occurrence, while `replaceAll('cat', 'dog')` replaces all occurrences. Both work here since there's only one 'cat'."
    },
    {
        "question": "What does `'hello hello'.replace('hello', 'hi')` return?",
        "options": ["hi hi", "hi hello", "hello hi", "hello hello"],
        "answer": "hi hello",
        "difficulty": "Medium",
        "explanation": "The `replace()` method only replaces the first occurrence of 'hello' with 'hi'."
    },
    {
        "question": "What does `'hello hello'.replaceAll('hello', 'hi')` return?",
        "options": ["hi hi", "hi hello", "hello hi", "hello hello"],
        "answer": "hi hi",
        "difficulty": "Medium",
        "explanation": "The `replaceAll()` method replaces all occurrences of 'hello' with 'hi'."
    },
    # Topic 26: Rounding numbers
    {
        "question": "How do you round 3.6 to the nearest integer?",
        "options": ["Math.round(3.6)", "Math.floor(3.6)", "Math.ceil(3.6)", "Math.trunc(3.6)"],
        "answer": "Math.round(3.6)",
        "difficulty": "Easy",
        "explanation": "`Math.round()` rounds to the nearest integer, so 3.6 becomes 4."
    },
    {
        "question": "What does `Math.floor(5.9)` return?",
        "options": ["5", "6", "5.9", "0"],
        "answer": "5",
        "difficulty": "Easy",
        "explanation": "`Math.floor()` rounds down to the nearest integer."
    },
    {
        "question": "What does `Math.ceil(4.1)` return?",
        "options": ["4", "5", "4.1", "0"],
        "answer": "5",
        "difficulty": "Easy",
        "explanation": "`Math.ceil()` rounds up to the nearest integer."
    },
    # Topic 27: Generating random numbers
    {
        "question": "How do you generate a random number between 0 and 1 in JavaScript?",
        "options": ["Math.random()", "Math.rand()", "Random.next()", "Math.floor()"],
        "answer": "Math.random()",
        "difficulty": "Easy",
        "explanation": "`Math.random()` generates a random floating-point number between 0 (inclusive) and 1 (exclusive)."
    },
    {
        "question": "How do you generate a random integer between 1 and 10?",
        "options": [
            "Math.floor(Math.random() * 10) + 1",
            "Math.random() * 10",
            "Math.ceil(Math.random() * 10)",
            "Math.round(Math.random() * 10)"
        ],
        "answer": "Math.floor(Math.random() * 10) + 1",
        "difficulty": "Medium",
        "explanation": "`Math.random() * 10` gives a number between 0 and 10, `Math.floor()` rounds it down, and `+ 1` shifts the range to 1–10."
    },
    {
        "question": "What is the range of `Math.random()`?",
        "options": ["0 to 1", "0 to 100", "1 to 10", "-1 to 1"],
        "answer": "0 to 1",
        "difficulty": "Easy",
        "explanation": "`Math.random()` returns a value between 0 (inclusive) and 1 (exclusive)."
    },
    # Topic 28: Converting strings to integers and decimals
    {
        "question": "How do you convert the string '123' to an integer?",
        "options": ["parseInt('123')", "parseFloat('123')", "Number('123')", "Both A and C"],
        "answer": "Both A and C",
        "difficulty": "Medium",
        "explanation": "`parseInt('123')` and `Number('123')` both convert the string '123' to the integer 123."
    },
    {
        "question": "What does `parseFloat('12.34')` return?",
        "options": ["12", "12.34", "12.3", "1234"],
        "answer": "12.34",
        "difficulty": "Easy",
        "explanation": "`parseFloat()` converts a string to a floating-point number."
    },
    {
        "question": "What happens if you call `parseInt('abc')`?",
        "options": ["NaN", "0", "undefined", "Throws an error"],
        "answer": "NaN",
        "difficulty": "Medium",
        "explanation": "`parseInt()` returns `NaN` if the string cannot be converted to an integer."
    },
    # Topic 29: Converting strings to numbers, numbers to strings
    {
        "question": "How do you convert the number 42 to a string?",
        "options": ["42.toString()", "String(42)", "Both A and B", "'42'"],
        "answer": "Both A and B",
        "difficulty": "Easy",
        "explanation": "Both `toString()` and `String()` convert a number to a string."
    },
    {
        "question": "What does `Number('56')` return?",
        "options": ["56", "'56'", "NaN", "undefined"],
        "answer": "56",
        "difficulty": "Easy",
        "explanation": "`Number()` converts a string to a number if possible."
    },
    {
        "question": "What is the result of `'123' + 1`?",
        "options": ["124", "'1231'", "NaN", "1231"],
        "answer": "'1231'",
        "difficulty": "Medium",
        "explanation": "The `+` operator concatenates a string with a number, converting the number to a string."
    },
    # Topic 30: Controlling the length of decimals
    {
        "question": "How do you format 3.14159 to two decimal places?",
        "options": ["3.14159.toFixed(2)", "3.14159.toPrecision(2)", "Math.round(3.14159, 2)", "3.14159.format(2)"],
        "answer": "3.14159.toFixed(2)",
        "difficulty": "Medium",
        "explanation": "`toFixed(2)` formats a number to 2 decimal places, returning '3.14' as a string."
    },
    {
        "question": "What does `5.6789.toFixed(1)` return?",
        "options": ["'5.7'", "5.7", "'5.6'", "6"],
        "answer": "'5.7'",
        "difficulty": "Medium",
        "explanation": "`toFixed(1)` rounds to one decimal place and returns a string."
    },
    {
        "question": "What does `3.14159.toPrecision(3)` return?",
        "options": ["'3.14'", "'3.141'", "3.14", "3.1"],
        "answer": "'3.14'",
        "difficulty": "Medium",
        "explanation": "`toPrecision(3)` formats the number to 3 significant digits, returning a string."
    },
    # Topic 31: Getting the current date and time
    {
        "question": "How do you get the current date and time in JavaScript?",
        "options": ["new Date()", "Date.now()", "new Date().toString()", "Date.getCurrent()"],
        "answer": "new Date()",
        "difficulty": "Easy",
        "explanation": "`new Date()` creates a Date object with the current date and time."
    },
    {
        "question": "What does `Date.now()` return?",
        "options": [
            "A timestamp in milliseconds",
            "A Date object",
            "A string representation of the date",
            "The current year"
        ],
        "answer": "A timestamp in milliseconds",
        "difficulty": "Easy",
        "explanation": "`Date.now()` returns the number of milliseconds since January 1, 1970."
    },
    {
        "question": "How do you get the current year using a Date object?",
        "options": [
            "new Date().getFullYear()",
            "new Date().getYear()",
            "new Date().year()",
            "new Date().getCurrentYear()"
        ],
        "answer": "new Date().getFullYear()",
        "difficulty": "Easy",
        "explanation": "`getFullYear()` returns the four-digit year of the current date."
    },
    # Topic 32: Extracting parts of the date and time
    {
        "question": "How do you get the current month from a Date object?",
        "options": ["getMonth()", "getDate()", "getDay()", "getYear()"],
        "answer": "getMonth()",
        "difficulty": "Easy",
        "explanation": "`getMonth()` returns the month (0–11) of a Date object."
    },
    {
        "question": "What does `new Date().getDay()` return?",
        "options": [
            "The day of the week (0–6)",
            "The day of the month",
            "The month",
            "The year"
        ],
        "answer": "The day of the week (0–6)",
        "difficulty": "Easy",
        "explanation": "`getDay()` returns the day of the week (0 for Sunday, 6 for Saturday)."
    },
    {
        "question": "What does `new Date().getHours()` return?",
        "options": ["0–23", "0–59", "1–12", "0–11"],
        "answer": "0–23",
        "difficulty": "Easy",
        "explanation": "`getHours()` returns the hour of the day in 24-hour format (0–23)."
    },
    # Topic 33: Specifying a date and time
    {
        "question": "How do you create a Date object for January 1, 2023?",
        "options": [
            "new Date(2023, 0, 1)",
            "new Date(2023, 1, 1)",
            "new Date('2023/1/1')",
            "Both A and C"
        ],
        "answer": "Both A and C",
        "difficulty": "Medium",
        "explanation": "`new Date(2023, 0, 1)` uses month index 0 for January, and `new Date('2023/1/1')` parses the string."
    },
    {
        "question": "What does `new Date('2023-01-01')` represent?",
        "options": [
            "January 1, 2023",
            "January 1, 2022",
            "December 1, 2023",
            "Invalid date"
        ],
        "answer": "January 1, 2023",
        "difficulty": "Easy",
        "explanation": "The string '2023-01-01' is parsed as January 1, 2023 in ISO format."
    },
    {
        "question": "What is the month index for March in `new Date(year, month, day)`?",
        "options": ["2", "3", "1", "0"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "Months are 0-based in JavaScript, so March is index 2."
    },
    # Topic 34: Changing elements of a date and time
    {
        "question": "How do you set the year of a Date object to 2025?",
        "options": [
            "date.setFullYear(2025)",
            "date.setYear(2025)",
            "date.year = 2025",
            "date.setDate(2025)"
        ],
        "answer": "date.setFullYear(2025)",
        "difficulty": "Easy",
        "explanation": "`setFullYear()` sets the year of a Date object."
    },
    {
        "question": "What does `date.setHours(15)` do?",
        "options": [
            "Sets the hour to 3 PM",
            "Sets the hour to 3 AM",
            "Sets the minutes to 15",
            "Throws an error"
        ],
        "answer": "Sets the hour to 3 PM",
        "difficulty": "Easy",
        "explanation": "`setHours(15)` sets the hour to 15:00 (3 PM) in 24-hour format."
    },
    {
        "question": "How do you set the month to June in a Date object?",
        "options": ["date.setMonth(5)", "date.setMonth(6)", "date.month = 6", "date.setMonth(0, 6)"],
        "answer": "date.setMonth(5)",
        "difficulty": "Medium",
        "explanation": "June is month index 5 (0-based) in `setMonth()`."
    },
    # Topic 35: Functions
    {
        "question": "How do you define a function in JavaScript?",
        "options": [
            "function myFunc() {}",
            "def myFunc() {}",
            "func myFunc() {}",
            "myFunc() => {}"
        ],
        "answer": "function myFunc() {}",
        "difficulty": "Easy",
        "explanation": "A function is defined using the `function` keyword, followed by the name and parentheses."
    },
    {
        "question": "What is an arrow function in JavaScript?",
        "options": [
            "() => {}",
            "function() {}",
            "=> function() {}",
            "arrow() {}"
        ],
        "answer": "() => {}",
        "difficulty": "Medium",
        "explanation": "An arrow function is defined using the `=>` syntax, introduced in ES6."
    },
    {
        "question": "What does a function without a `return` statement return?",
        "options": ["undefined", "null", "0", "false"],
        "answer": "undefined",
        "difficulty": "Easy",
        "explanation": "If no `return` statement is used, a function returns `undefined` by default."
    },
    # Topic 36: Functions: passing them data
    {
        "question": "How do you pass a parameter to a function?",
        "options": [
            "function myFunc(x) {}",
            "function myFunc = x {}",
            "function myFunc[x] {}",
            "myFunc(x) => {}"
        ],
        "answer": "function myFunc(x) {}",
        "difficulty": "Easy",
        "explanation": "Parameters are defined in the parentheses of a function declaration."
    },
    {
        "question": "What does `myFunc(5)` do in this code?\n```javascript\nfunction myFunc(num) { return num * 2; }\n```",
        "options": ["Returns 10", "Returns 5", "Throws an error", "Returns undefined"],
        "answer": "Returns 10",
        "difficulty": "Easy",
        "explanation": "The function doubles the input parameter, so `myFunc(5)` returns 5 * 2 = 10."
    },
    {
        "question": "How many arguments can a function accept?",
        "options": [
            "Any number",
            "Only one",
            "Up to three",
            "Depends on the function type"
        ],
        "answer": "Any number",
        "difficulty": "Easy",
        "explanation": "JavaScript functions can accept any number of arguments, accessible via the `arguments` object or defined parameters."
    },
    # Topic 37: Functions: passing data back from them
    {
        "question": "How do you return a value from a function?",
        "options": ["return value;", "output value;", "send value;", "value;"],
        "answer": "return value;",
        "difficulty": "Easy",
        "explanation": "The `return` statement sends a value back from a function and stops its execution."
    },
    {
        "question": "What does this function return?\n```javascript\nfunction add(a, b) { return a + b; }\n```",
        "options": ["a + b", "The sum of a and b", "undefined", "null"],
        "answer": "The sum of a and b",
        "difficulty": "Easy",
        "explanation": "The function returns the result of `a + b`."
    },
    {
        "question": "What happens if a function has multiple `return` statements?",
        "options": [
            "Only the first executed `return` runs",
            "All `return` statements run",
            "The last `return` statement runs",
            "It causes an error"
        ],
        "answer": "Only the first executed `return` runs",
        "difficulty": "Medium",
        "explanation": "A function exits as soon as a `return` statement is executed, so only the first one encountered runs."
    },
    # Topic 38: Functions: local vs. global variables
    {
        "question": "What is a local variable in a function?",
        "options": [
            "A variable declared inside the function",
            "A variable declared outside the function",
            "A variable passed as an argument",
            "A variable in the global object"
        ],
        "answer": "A variable declared inside the function",
        "difficulty": "Easy",
        "explanation": "Local variables are declared within a function and are only accessible within that function's scope."
    },
    {
        "question": "What happens if you access a global variable inside a function?",
        "options": [
            "The global variable is accessible",
            "It throws an error",
            "The variable becomes local",
            "It returns undefined"
        ],
        "answer": "The global variable is accessible",
        "difficulty": "Easy",
        "explanation": "Global variables are accessible inside functions unless shadowed by a local variable."
    },
    {
        "question": "What is the output of this code?\n```javascript\nlet x = 10;\nfunction test() { let x = 20; console.log(x); }\ntest();\n```",
        "options": ["20", "10", "undefined", "Error"],
        "answer": "20",
        "difficulty": "Medium",
        "explanation": "The local variable `x` inside the function shadows the global `x`, so `20` is printed."
    },
    # Topic 39: switch statements: how to start them
    {
        "question": "How do you start a switch statement in JavaScript?",
        "options": [
            "switch (expression) {",
            "case (expression):",
            "switch: expression {",
            "if (expression) {"
        ],
        "answer": "switch (expression) {",
        "difficulty": "Easy",
        "explanation": "A switch statement begins with `switch (expression) {`, followed by case clauses."
    },
    {
        "question": "What does the `switch` keyword evaluate?",
        "options": [
            "An expression",
            "A boolean",
            "A function",
            "A loop"
        ],
        "answer": "An expression",
        "difficulty": "Easy",
        "explanation": "The `switch` statement evaluates an expression and matches it against case values."
    },
    {
        "question": "What is the role of the `case` keyword in a switch statement?",
        "options": [
            "Defines possible values to match",
            "Ends the switch statement",
            "Declares a variable",
            "Loops through values"
        ],
        "answer": "Defines possible values to match",
        "difficulty": "Easy",
        "explanation": "The `case` keyword specifies a value to compare against the switch expression."
    },
    # Topic 40: switch statements: how to complete them
    {
        "question": "How do you prevent fall-through in a switch statement?",
        "options": ["Use break;", "Use return;", "Use continue;", "Use exit;"],
        "answer": "Use break;",
        "difficulty": "Easy",
        "explanation": "The `break` statement exits the switch block, preventing execution of subsequent cases."
    },
    {
        "question": "What is the purpose of the `default` case in a switch statement?",
        "options": [
            "Executes if no case matches",
            "Executes first",
            "Declares a variable",
            "Loops through cases"
        ],
        "answer": "Executes if no case matches",
        "difficulty": "Easy",
        "explanation": "The `default` case runs if none of the case values match the switch expression."
    },
    {
        "question": "What is the output of this switch statement?\n```javascript\nlet x = 2;\nswitch (x) {\n  case 1: console.log('One'); break;\n  case 2: console.log('Two'); break;\n  default: console.log('None');\n}\n```",
        "options": ["Two", "One", "None", "Error"],
        "answer": "Two",
        "difficulty": "Medium",
        "explanation": "The value `x = 2` matches `case 2`, so 'Two' is printed, and `break` prevents further execution."
    }
]

# Cache shuffled quiz (remove cache for testing)
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
    if not quiz:
        st.error("Quiz list is empty!")
    st.session_state.update({
        "quiz_data": shuffle_quiz(quiz) if quiz else [],
        "score": 0,
        "current_q": 0,
        "start_time": datetime.now(),
        "answers": [None] * len(quiz) if quiz else [],
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 1800,  # 30 minutes
        "theme": "dark",
        "streak": 0,
        "started": False,
        "max_streak": 0  # Added max_streak
    })
    # Debug: Check quiz_data length
    st.write(f"Initialized quiz with {len(st.session_state.quiz_data)} questions")

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
        "max_streak": 0,
        "started": False
    })
    st.rerun()

# CSS for enhanced UI
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

# Main UI
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 JavaScript Mastery Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript Expertise!</p>', unsafe_allow_html=True)

# Theme toggle button
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen
if not st.session_state.started:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: var(--text-color); font-size: 18px;">Test your JavaScript skills with 67 comprehensive questions!</p>
        <p style="color: #b0b0d0;">30 minutes, 2 points per correct answer. Ready?</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Quiz", key="start_quiz"):
        st.session_state.started = True
        st.session_state.start_time = datetime.now()
        st.write(f"Quiz started with {len(st.session_state.quiz_data)} questions")
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
        <div style="color: var(--text-color); font-size: 13px; text-align: center;">
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
                        key=f"q{i}_{st.session_state.current_q}",  # Unique key per question
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
                            st.session_state.score += 2
                            st.session_state.streak += 1
                            if st.session_state.streak > st.session_state.max_streak:
                                st.session_state.max_streak = st.session_state.streak
                            if st.session_state.streak >= 3:
                                st.session_state.score += 0.5
                        else:
                            st.session_state.streak = 0
                        # Move to next question or show results
                        if st.session_state.current_q < len(st.session_state.quiz_data) - 1:
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
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 1800)
            total_possible_score = len(quiz) * 2
            accuracy = (st.session_state.score / total_possible_score) * 100 if total_possible_score > 0 else 0
            st.markdown('<div class="question-container">', unsafe_allow_html=True)
            st.markdown(f'<h2 style="color: #34c759; text-align: center;">🏆 Score: {st.session_state.score}/{total_possible_score}</h2>', unsafe_allow_html=True)
            st.markdown(f"""
            <h3>📊 Results</h3>
            <div style="color: var(--text-color); font-size: 15px;">
                - ⏱️ Time: {int(time_taken) // 60}m {int(time_taken) % 60}s<br>
                - 🎯 Accuracy: {accuracy:.1f}%<br>
                - ✅ Correct: {sum(1 for ans in st.session_state.answers if ans and ans["is_correct"])}<br>
                - ❌ Incorrect: {sum(1 for ans in st.session_state.answers if ans and not ans["is_correct"])}<br>
                - 🔥 Max Streak: {st.session_state.max_streak}
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
            st.markdown('<h3>📝 Review Your Answers</h3>', unsafe_allow_html=True)
            for i, ans in enumerate(st.session_state.answers):
                if ans:
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})"
                    st.markdown(f"""
                    <div style="color: var(--text-color); margin-bottom: 10px;">
                        Question {i+1}: {ans["question"]}<br>
                        Your Answer: {ans["user_answer"]}<br>
                        {status}<br>
                        Explanation: {quiz[i]["explanation"]}
                    </div>
                    """, unsafe_allow_html=True)

            # Play Again button
            if st.button("🔄 Play Again", key="play_again"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
```
