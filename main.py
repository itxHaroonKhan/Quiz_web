
import streamlit as st
import random
from datetime import datetime
import uuid

quiz = [
    {
        "question": "What is logged to the console when the user clicks 'Cancel'?\n```javascript\nlet result = prompt('Enter name');\nconsole.log(result);\n```",
        "options": ["null", "undefined", "'Cancel'", "''"],
        "answer": "null",
        "difficulty": "Medium",
        "explanation": "The `prompt()` function returns `null` when the user clicks 'Cancel'. This value is assigned to `result` and logged to the console.",
        "hint": "Consider what `prompt()` returns when no input is provided."
    },
    {
        "question": "What does `alert('Hello!')` do in JavaScript?\n```javascript\nalert('Hello!');\n```",
        "options": ["Logs 'Hello!' to the console", "Displays a popup with 'Hello!'", "Returns 'Hello!'", "Nothing"],
        "answer": "Displays a popup with 'Hello!'",
        "difficulty": "Easy",
        "explanation": "The `alert()` function displays a simple popup dialog with the message 'Hello!' in the browser.",
        "hint": "Think about the role of `alert()` in user interaction."
    },
    {
        "question": "What is the value of `str` after this code runs?\n```javascript\nlet str = 'Hello';\nstr = str + ' World';\n```",
        "options": ["'HelloWorld'", "'Hello World'", "'Hello'", "'World'"],
        "answer": "'Hello World'",
        "difficulty": "Easy",
        "explanation": "The `+` operator concatenates the string 'Hello' with ' World', resulting in 'Hello World'.",
        "hint": "Consider how strings are combined using the `+` operator."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = '20';\nx = parseInt(x) * 2;\n```",
        "options": ["40", "'40'", "20", "NaN"],
        "answer": "40",
        "difficulty": "Medium",
        "explanation": "The `parseInt()` function converts the string '20' to the number 20. Multiplying by 2 gives 40.",
        "hint": "Check how `parseInt()` affects the string before multiplication."
    },
    {
        "question": "Which variable name is illegal in JavaScript?\n```javascript\nlet 1stPlace = 'Winner';\nlet firstPlace = 'Winner';\nlet $place = 'Winner';\nlet _place = 'Winner';\n```",
        "options": ["1stPlace", "firstPlace", "$place", "_place"],
        "answer": "1stPlace",
        "difficulty": "Easy",
        "explanation": "Variable names cannot start with a number, making `1stPlace` illegal. The others are valid.",
        "hint": "Recall the rules for valid JavaScript variable names."
    },
    {
        "question": "What does this expression evaluate to?\n```javascript\n15 % 4\n```",
        "options": ["3", "4", "1", "0"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "The modulo operator `%` returns the remainder of 15 divided by 4, which is 3 (15 = 4 * 3 + 3).",
        "hint": "Perform the division and focus on the remainder."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet num = 8;\nif (num > 5 && num < 10) {\n  console.log('In range');\n} else {\n  console.log('Out of range');\n}\n```",
        "options": ["In range", "Out of range", "Nothing", "Error"],
        "answer": "In range",
        "difficulty": "Medium",
        "explanation": "The condition `num > 5 && num < 10` is true for `num = 8`, so 'In range' is logged.",
        "hint": "Evaluate both parts of the `&&` condition."
    },
    {
        "question": "What is the value of `arr` after this code runs?\n```javascript\nlet arr = [1, 2, 3];\narr.push(4);\n```",
        "options": ["[1, 2, 3, 4]", "[1, 2, 3]", "[4, 1, 2, 3]", "[1, 2, 4, 3]"],
        "answer": "[1, 2, 3, 4]",
        "difficulty": "Easy",
        "explanation": "The `push()` method adds the element 4 to the end of the array.",
        "hint": "Consider what `push()` does to an array."
    },
    {
        "question": "What is logged to the console?\n```javascript\nfor (let i = 0; i < 3; i++) {\n  console.log(i);\n}\n```",
        "options": ["0, 1, 2", "1, 2, 3", "0, 1, 2, 3", "Nothing"],
        "answer": "0, 1, 2",
        "difficulty": "Medium",
        "explanation": "The `for` loop iterates from `i = 0` to `i = 2` (since `i < 3`), logging each value of `i`.",
        "hint": "Trace the loop iterations and check the condition."
    },
    {
        "question": "What is the value of `str` after this code runs?\n```javascript\nlet str = 'JavaScript';\nstr = str.toUpperCase();\n```",
        "options": ["'javascript'", "'JAVASCRIPT'", "'JavaScript'", "'JAVAscript'"],
        "answer": "'JAVASCRIPT'",
        "difficulty": "Easy",
        "explanation": "The `toUpperCase()` method converts all characters in the string to uppercase.",
        "hint": "Think about what `toUpperCase()` does to a string."
    },
    {
        "question": "What does this code return?\n```javascript\nfunction getSquare(num) {\n  return num * num;\n}\nconsole.log(getSquare(5));\n```",
        "options": ["25", "10", "5", "Error"],
        "answer": "25",
        "difficulty": "Medium",
        "explanation": "The function `getSquare` multiplies `num` by itself. For `num = 5`, it returns `5 * 5 = 25`.",
        "hint": "Evaluate the function's return value for the input 5."
    },
    {
        "question": "What is the value of `num` after this code runs?\n```javascript\nlet num = Math.round(7.6);\n```",
        "options": ["7", "8", "7.6", "8.0"],
        "answer": "8",
        "difficulty": "Medium",
        "explanation": "The `Math.round()` function rounds 7.6 to the nearest integer, which is 8.",
        "hint": "Consider how `Math.round()` handles decimal numbers."
    },
    {
        "question": "What is the result of this expression?\n```javascript\n'5' + 5\n```",
        "options": ["10", "'55'", "55", "NaN"],
        "answer": "'55'",
        "difficulty": "Medium",
        "explanation": "The `+` operator concatenates the string '5' with the number 5, resulting in the string '55'.",
        "hint": "Check how JavaScript handles `+` with a string and a number."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 10;\nif (x === '10') {\n  console.log('Equal');\n} else {\n  console.log('Not equal');\n}\n```",
        "options": ["Equal", "Not equal", "Nothing", "Error"],
        "answer": "Not equal",
        "difficulty": "Medium",
        "explanation": "The `===` operator checks for strict equality (value and type). Since `x` is a number and '10' is a string, they are not equal.",
        "hint": "Consider the difference between `==` and `===`."
    },
    {
        "question": "What is the value of `arr` after this code runs?\n```javascript\nlet arr = [1, 2, 3];\narr.splice(1, 1, 4);\n```",
        "options": ["[1, 4, 3]", "[1, 2, 4]", "[4, 2, 3]", "[1, 2, 3, 4]"],
        "answer": "[1, 4, 3]",
        "difficulty": "Medium",
        "explanation": "The `splice(1, 1, 4)` method removes 1 element at index 1 (the number 2) and inserts 4, resulting in `[1, 4, 3]`.",
        "hint": "Understand the parameters of the `splice()` method."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet str = 'Hello World';\nconsole.log(str.length);\n```",
        "options": ["10", "11", "12", "9"],
        "answer": "11",
        "difficulty": "Easy",
        "explanation": "The `length` property returns the number of characters in the string, including the space, so 'Hello World' has 11 characters.",
        "hint": "Count the characters, including spaces."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = Math.floor(9.8);\n```",
        "options": ["9", "10", "9.8", "8"],
        "answer": "9",
        "difficulty": "Medium",
        "explanation": "The `Math.floor()` function rounds down to the nearest integer, so 9.8 becomes 9.",
        "hint": "Consider how `Math.floor()` handles decimals."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet arr = [1, 2, 3];\nfor (let i = 0; i < arr.length; i++) {\n  if (arr[i] === 2) {\n    break;\n  }\n  console.log(arr[i]);\n}\n```",
        "options": ["1", "1, 2", "1, 2, 3", "Nothing"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "The loop logs elements until `arr[i] === 2`, where it breaks, so only `1` is logged.",
        "hint": "Check the effect of the `break` statement in the loop."
    },
    {
        "question": "What is the value of `str` after this code runs?\n```javascript\nlet str = 'hello';\nstr = str.replace('h', 'H');\n```",
        "options": ["'Hello'", "'hello'", "'Helloo'", "'Hhello'"],
        "answer": "'Hello'",
        "difficulty": "Medium",
        "explanation": "The `replace()` method replaces the first 'h' with 'H', resulting in 'Hello'.",
        "hint": "Consider what `replace()` does with its first occurrence."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet num = 5;\nif (num > 3) {\n  if (num < 7) {\n    console.log('Nested');\n  }\n}\n```",
        "options": ["Nested", "Nothing", "Error", "5"],
        "answer": "Nested",
        "difficulty": "Medium",
        "explanation": "The outer condition `num > 3` is true for `num = 5`, and the inner condition `num < 7` is also true, so 'Nested' is logged.",
        "hint": "Evaluate both conditions in the nested `if` statements."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = parseFloat('3.14');\n```",
        "options": ["3.14", "'3.14'", "3", "NaN"],
        "answer": "3.14",
        "difficulty": "Medium",
        "explanation": "The `parseFloat()` function converts the string '3.14' to the number 3.14.",
        "hint": "Check the purpose of `parseFloat()`."
    },
    {
        "question": "What is logged to Math.random()?\n```javascript\nconsole.log(Math.random());\n```",
        "options": ["A number between 0 and 1", "A number between 1 and 10", "A whole number", "Nothing"],
        "answer": "A number between 0 and 1",
        "difficulty": "Easy",
        "explanation": "The `Math.random()` function returns a random number between 0 (inclusive) and 1 (exclusive).",
        "hint": "Consider the range of values `Math.random()` generates."
    },
    {
        "question": "What is the value of `str` after this code runs?\n```javascript\nlet str = 'JavaScript';\nstr = str.substring(0, 4);\n```",
        "options": ["'Java'", "'JavaS'", "'Script'", "'JavaScript'"],
        "answer": "'Java'",
        "difficulty": "Medium",
        "explanation": "The `substring(0, 4)` method extracts characters from index 0 to 3, resulting in 'Java'.",
        "hint": "Check the indices used in `substring()`."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 10;\nif (x > 5 || x < 0) {\n  console.log('True');\n} else {\n  console.log('False');\n}\n```",
        "options": ["True", "False", "Nothing", "Error"],
        "answer": "True",
        "difficulty": "Medium",
        "explanation": "The condition `x > 5 || x < 0` is true because `x = 10` satisfies `x > 5`.",
        "hint": "Evaluate the logical OR condition."
    },
    {
        "question": "What is the value of `arr` after this code runs?\n```javascript\nlet arr = [1, 2, 3];\narr.pop();\n```",
        "options": ["[1, 2]", "[1, 3]", "[2, 3]", "[1, 2, 3]"],
        "answer": "[1, 2]",
        "difficulty": "Easy",
        "explanation": "The `pop()` method removes the last element from the array, resulting in `[1, 2]`.",
        "hint": "Consider what `pop()` does to an array."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = (2 + 3) * 4;\n```",
        "options": ["20", "14", "10", "24"],
        "answer": "20",
        "difficulty": "Easy",
        "explanation": "Parentheses ensure `2 + 3` is evaluated first, giving 5, then `5 * 4 = 20`.",
        "hint": "Check the order of operations with parentheses."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet str = 'Hello';\nconsole.log(str.indexOf('l'));\n```",
        "options": ["2", "1", "3", "-1"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "The `indexOf('l')` method returns the index of the first 'l' in 'Hello', which is at index 2.",
        "hint": "Count the position of the first occurrence of 'l'."
    },
    {
        "question": "What is the value of `num` after this code runs?\n```javascript\nlet num = Number('123');\n```",
        "options": ["123", "'123'", "NaN", "Error"],
        "answer": "123",
        "difficulty": "Medium",
        "explanation": "The `Number()` function converts the string '123' to the number 123.",
        "hint": "Check how `Number()` handles string conversion."
    },
    {
        "question": "What is logged to the console?\n```javascript\nfor (let i = 1; i <= 3; i++) {\n  for (let j = 1; j <= 2; j++) {\n    console.log(i);\n  }\n}\n```",
        "options": ["1, 1, 2, 2, 3, 3", "1, 2, 3", "1, 2, 3, 1, 2, 3", "Nothing"],
        "answer": "1, 1, 2, 2, 3, 3",
        "difficulty": "Hard",
        "explanation": "The inner loop runs twice for each iteration of the outer loop, logging `i` (1, 1, 2, 2, 3, 3).",
        "hint": "Trace the nested loop iterations."
    },
    {
        "question": "What is the value of `str` after this code runs?\n```javascript\nlet str = 'Hello';\nstr = str.toLowerCase();\n```",
        "options": ["'HELLO'", "'hello'", "'Hello'", "'hELLO'"],
        "answer": "'hello'",
        "difficulty": "Easy",
        "explanation": "The `toLowerCase()` method converts all characters in the string to lowercase.",
        "hint": "Think about what `toLowerCase()` does to a string."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet date = new Date('2025-06-28');\nconsole.log(date.getFullYear());\n```",
        "options": ["2025", "6", "28", "Error"],
        "answer": "2025",
        "difficulty": "Medium",
        "explanation": "The `getFullYear()` method returns the year of the date, which is 2025.",
        "hint": "Check what `getFullYear()` extracts from a Date object."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = 3.14159;\nx = x.toFixed(2);\n```",
        "options": ["'3.14'", "3.14", "'3.14159'", "3"],
        "answer": "'3.14'",
        "difficulty": "Medium",
        "explanation": "The `toFixed(2)` method formats the number to 2 decimal places and returns it as a string, '3.14'.",
        "hint": "Check the return type of `toFixed()`."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 5;\nif (x !== '5') {\n  console.log('Not equal');\n}\n```",
        "options": ["Not equal", "Equal", "Nothing", "Error"],
        "answer": "Not equal",
        "difficulty": "Medium",
        "explanation": "The `!==` operator checks for strict inequality. Since `x` is a number and '5' is a string, they are not equal.",
        "hint": "Consider strict inequality with different types."
    },
    {
        "question": "What is the value of `arr` after this code runs?\n```javascript\nlet arr = [1, 2, 3];\narr.shift();\n```",
        "options": ["[2, 3]", "[1, 2]", "[1, 3]", "[1, 2, 3]"],
        "answer": "[2, 3]",
        "difficulty": "Medium",
        "explanation": "The `shift()` method removes the first element from the array, resulting in `[2, 3]`.",
        "hint": "Consider what `shift()` does to an array."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet str = 'JavaScript';\nconsole.log(str.charAt(4));\n```",
        "options": ["'S'", "'s'", "'c'", "''"],
        "answer": "'S'",
        "difficulty": "Medium",
        "explanation": "The `charAt(4)` method returns the character at index 4, which is 'S' in 'JavaScript'.",
        "hint": "Check the character at index 4 in the string."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = 10 / 2 + 3;\n```",
        "options": ["8", "13", "5", "15"],
        "answer": "8",
        "difficulty": "Easy",
        "explanation": "Division has higher precedence than addition, so `10 / 2 = 5`, then `5 + 3 = 8`.",
        "hint": "Check the order of operations."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = true;\nif (x) {\n  console.log('True');\n} else {\n  console.log('False');\n}\n```",
        "options": ["True", "False", "Nothing", "Error"],
        "answer": "True",
        "difficulty": "Easy",
        "explanation": "The condition `x` is true, so 'True' is logged.",
        "hint": "Evaluate the boolean condition."
    },
    {
        "question": "What is the value of `num` after this code runs?\n```javascript\nlet num = Math.ceil(4.1);\n```",
        "options": ["4", "5", "4.1", "5.0"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The `Math.ceil()` function rounds up to the nearest integer, so 4.1 becomes 5.",
        "hint": "Consider how `Math.ceil()` handles decimals."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet str = 'Hello World';\nconsole.log(str.includes('World'));\n```",
        "options": ["true", "false", "'World'", "Error"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The `includes()` method checks if 'World' is a substring, returning `true`.",
        "hint": "Check what `includes()` returns for substrings."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = 5;\nx += 3;\n```",
        "options": ["8", "5", "3", "15"],
        "answer": "8",
        "difficulty": "Easy",
        "explanation": "The `+=` operator adds 3 to `x`, so `5 + 3 = 8`.",
        "hint": "Consider the effect of the `+=` operator."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet arr = [1, 2, 3];\nconsole.log(arr[1]);\n```",
        "options": ["1", "2", "3", "Error"],
        "answer": "2",
        "difficulty": "Easy",
        "explanation": "The array index `1` accesses the second element, which is 2.",
        "hint": "Check the element at index 1."
    },
    {
        "question": "What is the value of `str` after this code runs?\n```javascript\nlet str = '123';\nstr = Number(str).toString();\n```",
        "options": ["'123'", "123", "'NaN'", "Error"],
        "answer": "'123'",
        "difficulty": "Medium",
        "explanation": "The `Number()` function converts '123' to 123, and `toString()` converts it back to '123'.",
        "hint": "Trace the conversion from string to number and back."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet date = new Date('2025-06-28');\nconsole.log(date.getMonth());\n```",
        "options": ["5", "6", "28", "2025"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The `getMonth()` method returns the month (0-11), so June is 5.",
        "hint": "Remember that months are zero-based in JavaScript."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = 2;\nfunction double(num) {\n  return num * 2;\n}\nx = double(x);\n```",
        "options": ["4", "2", "8", "Error"],
        "answer": "4",
        "difficulty": "Medium",
        "explanation": "The `double` function returns `2 * 2 = 4`, which is assigned to `x`.",
        "hint": "Evaluate the function call and its return value."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 10;\nif (x > 5) {\n  console.log('Big');\n} else if (x > 0) {\n  console.log('Small');\n}\n```",
        "options": ["Big", "Small", "Nothing", "Error"],
        "answer": "Big",
        "difficulty": "Medium",
        "explanation": "The condition `x > 5` is true for `x = 10`, so 'Big' is logged, and the `else if` is skipped.",
        "hint": "Check which condition is evaluated first."
    },
    {
        "question": "What is the value of `arr` after this code runs?\n```javascript\nlet arr = [1, 2, 3];\narr[1] = 5;\n```",
        "options": ["[1, 5, 3]", "[1, 2, 3]", "[5, 2, 3]", "[1, 5, 5]"],
        "answer": "[1, 5, 3]",
        "difficulty": "Easy",
        "explanation": "The assignment `arr[1] = 5` replaces the element at index 1 with 5.",
        "hint": "Consider how array indexing works."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet str = 'JavaScript';\nconsole.log(str.slice(4, 10));\n```",
        "options": ["'Script'", "'Java'", "'JavaScript'", "'Scrip'"],
        "answer": "'Script'",
        "difficulty": "Medium",
        "explanation": "The `slice(4, 10)` method extracts characters from index 4 to 9, resulting in 'Script'.",
        "hint": "Check the indices used in `slice()`."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = 7;\nx *= 2;\n```",
        "options": ["14", "7", "49", "21"],
        "answer": "14",
        "difficulty": "Easy",
        "explanation": "The `*=` operator multiplies `x` by 2, so `7 * 2 = 14`.",
        "hint": "Consider the effect of the `*=` operator."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet date = new Date('2025-06-28');\ndate.setFullYear(2026);\nconsole.log(date.getFullYear());\n```",
        "options": ["2025", "2026", "6", "28"],
        "answer": "2026",
        "difficulty": "Medium",
        "explanation": "The `setFullYear(2026)` method changes the year to 2026, and `getFullYear()` returns it.",
        "hint": "Check how `setFullYear()` affects the date."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = '10.5';\nx = parseFloat(x) + 0.5;\n```",
        "options": ["11", "'11'", "10.5", "11.0"],
        "answer": "11",
        "difficulty": "Medium",
        "explanation": "The `parseFloat()` function converts '10.5' to 10.5, and adding 0.5 gives 11.",
        "hint": "Trace the conversion and addition."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet flag = false;\nfor (let i = 0; i < 5; i++) {\n  if (i === 3) {\n    flag = true;\n    break;\n  }\n}\nconsole.log(flag);\n```",
        "options": ["true", "false", "3", "Nothing"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The loop sets `flag` to `true` when `i === 3` and breaks, so `true` is logged.",
        "hint": "Check the effect of `break` after setting the flag."
    },
    {
        "question": "What is the value of `str` after this code runs?\n```javascript\nlet str = 'Hello World';\nstr = str.replace('World', 'JavaScript');\n```",
        "options": ["'Hello JavaScript'", "'Hello World'", "'World JavaScript'", "'Hello'"],
        "answer": "'Hello JavaScript'",
        "difficulty": "Medium",
        "explanation": "The `replace()` method replaces 'World' with 'JavaScript', resulting in 'Hello JavaScript'.",
        "hint": "Consider what `replace()` does with the first occurrence of a substring."
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

# Skip question
def skip_question():
    st.session_state.answers[st.session_state.current_q] = {
        "question": st.session_state.quiz_data[st.session_state.current_q]["question"],
        "user_answer": "Skipped",
        "correct_answer": st.session_state.quiz_data[st.session_state.current_q]["labeled_answer"],
        "is_correct": False,
        "difficulty": st.session_state.quiz_data[st.session_state.current_q]["difficulty"]
    }
    st.session_state.score = max(0, st.session_state.score - 1)
    st.session_state.streak = 0
    if st.session_state.current_q < len(quiz) - 1:
        st.session_state.current_q += 1
    else:
        st.session_state.show_results = True
    st.session_state.selected_option = None
    st.session_state.feedback = None
    st.session_state.show_hint = False
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
st.markdown('<h1 class="title">🚀 JavaScript Quiz Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript Skills!</p>', unsafe_allow_html=True)

# Theme toggle button
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen
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
                        st.markdown(f'<div style="color: var(--text-color); font-size: 14px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                # Hint button
                if st.button("💡 Show Hint", key="hint", disabled=st.session_state.show_hint or st.session_state.selected_option is not None):
                    st.session_state.show_hint = True
                    st.session_state.score = max(0, st.session_state.score - 0.5)
                    st.rerun()
                if st.session_state.show_hint:
                    st.markdown(f'<div style="color: #facc15; font-size: 14px;">Hint: {q["hint"]}</div>', unsafe_allow_html=True)

                # Navigation
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("⬅ Previous", disabled=st.session_state.current_q == 0):
                        if st.session_state.current_q > 0 and st.session_state.answers[st.session_state.current_q] and st.session_state.answers[st.session_state.current_q]["is_correct"]:
                            points = {"Easy": 1, "Medium": 2, "Hard": 3}[st.session_state.answers[st.session_state.current_q]["difficulty"]]
                            st.session_state.score -= points
                            if st.session_state.streak >= 3:
                                st.session_state.score -= 1
                        st.session_state.current_q -= 1
                        st.session_state.selected_option = None
                        st.session_state.feedback = None
                        st.session_state.show_hint = False
                        st.rerun()
                with col2:
                    if st.button("⏭️ Skip", key="skip"):
                        skip_question()
                with col3:
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

        else:
            # Results
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 1800)
            total_possible_score = sum({"Easy": 1, "Medium": 2, "Hard": 3}[q["difficulty"]] for q in quiz)
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
                - ⏭️ Skipped: {sum(1 for ans in st.session_state.answers if ans and ans["user_answer"] == "Skipped")}<br>
                - 🔥 Max Streak: {st.session_state.streak}
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

            # Leaderboard
            leaderboard = [
                {"name": "Alice", "score": 45, "time": 600},
                {"name": "Sam", "score": 40, "time": 700},
                {"name": "You", "score": st.session_state.score, "time": int(time_taken)}
            ]
            leaderboard.sort(key=lambda x: (-x["score"], x["time"]))
            st.markdown('<h3>🏅 Leaderboard</h3>', unsafe_allow_html=True)
            for i, entry in enumerate(leaderboard[:5], 1):
                st.markdown(f'<div style="color: var(--text-color);">{i}. <b>{entry["name"]}</b>: {entry["score"]}/{total_possible_score} (Time: {entry["time"]//60}m {entry["time"]%60}s)</div>', unsafe_allow_html=True)

            # Review Answers
            st.markdown('<h3>📝 Review Your Answers</h3>', unsafe_allow_html=True)
            for i, ans in enumerate(st.session_state.answers):
                if ans:
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})" if ans["user_answer"] != "Skipped" else "⏭️ Skipped"
                    st.markdown(f'<div style="color: var(--text-color);">Question {i+1}: {ans["question"]}<br>Your Answer: {ans["user_answer"]}<br>{status}<br>Explanation: {quiz[i]["explanation"]}</div>', unsafe_allow_html=True)

            # Reset button
            if st.button("🔄 Play Again", key="play_again"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
