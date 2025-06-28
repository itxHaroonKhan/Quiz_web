
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
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = '20';\nx = parseInt(x) * 2;\n```",
        "options": ["40", "'40'", "20", "NaN"],
        "answer": "40",
        "difficulty": "Medium",
        "explanation": "The `parseInt()` function converts the string '20' to the number 20. Multiplying by 2 gives 40, which is assigned to `x`.",
        "hint": "Check how `parseInt()` affects the string before multiplication."
    },
    {
        "question": "What does this expression evaluate to?\n```javascript\n15 % 4\n```",
        "options": ["3", "4", "1", "0"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "The modulo operator `%` returns the remainder of 15 divided by 4, which is 3 (since 15 = 4 * 3 + 3).",
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
        "question": "Which variable name is illegal?\n```javascript\nlet my_var = 1;\nlet 2var = 1;\nlet $var = 1;\nlet var_name = 1;\n```",
        "options": ["my_var", "2var", "$var", "var_name"],
        "answer": "2var",
        "difficulty": "Medium",
        "explanation": "Variable names cannot start with a number. `2var` is illegal, while `my_var`, `$var`, and `var_name` are valid.",
        "hint": "Review JavaScript naming rules for variables."
    },
    {
        "question": "What is the result of this expression?\n```javascript\n(10 - 4) * 2\n```",
        "options": ["12", "8", "14", "16"],
        "answer": "12",
        "difficulty": "Medium",
        "explanation": "Parentheses ensure `10 - 4` is evaluated first, giving 6. Then, `6 * 2 = 12`.",
        "hint": "Follow the order of operations with parentheses."
    },
    {
        "question": "What does this expression evaluate to?\n```javascript\n3 ** 2\n```",
        "options": ["9", "6", "8", "12"],
        "answer": "9",
        "difficulty": "Medium",
        "explanation": "The `**` operator performs exponentiation, so `3 ** 2` is 3 squared, which equals 9.",
        "hint": "The `**` operator raises the base to the power of the exponent."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet str = 'Hi';\nconsole.log(str + ' there!');\n```",
        "options": ["Hi there!", "Hithere!", "Hi", "there!"],
        "answer": "Hi there!",
        "difficulty": "Medium",
        "explanation": "The `+` operator concatenates the string 'Hi' with ' there!', resulting in 'Hi there!'.",
        "hint": "String concatenation combines strings with `+`."
    },
    {
        "question": "What is the value of `x`?\n```javascript\nlet x = confirm('Proceed?');\nif (x) {\n  x = 'Yes';\n} else {\n  x = 'No';\n}\n```",
        "options": ["Yes", "No", "true", "false"],
        "answer": "No",
        "difficulty": "Medium",
        "explanation": "The `confirm()` function returns `false` if 'Cancel' is clicked. The `else` block assigns 'No' to `x`.",
        "hint": "Assume the user clicks 'Cancel' on the confirm dialog."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet value = 15;\nif (value !== 10) {\n  console.log('Different');\n}\n```",
        "options": ["Different", "Nothing", "Error", "undefined"],
        "answer": "Different",
        "difficulty": "Medium",
        "explanation": "The `!==` operator checks for strict inequality. Since `15` is not equal to `10`, 'Different' is logged.",
        "hint": "The `!==` operator checks both value and type."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet score = 75;\nif (score >= 80) {\n  console.log('Pass');\n} else if (score >= 70) {\n  console.log('Borderline');\n} else {\n  console.log('Fail');\n}\n```",
        "options": ["Pass", "Borderline", "Fail", "Nothing"],
        "answer": "Borderline",
        "difficulty": "Medium",
        "explanation": "The condition `score >= 70` is true for `score = 75`, so 'Borderline' is logged after the first condition fails.",
        "hint": "Check the order of `else if` conditions."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 5;\nlet y = 10;\nif (x < 10 || y < 5) {\n  console.log('At least one true');\n}\n```",
        "options": ["At least one true", "Nothing", "Error", "undefined"],
        "answer": "At least one true",
        "difficulty": "Medium",
        "explanation": "The `||` operator returns true if at least one condition is true. Since `x < 10` is true, 'At least one true' is logged.",
        "hint": "Evaluate the `||` condition for both variables."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 7;\nif (x > 5) {\n  if (x < 10) {\n    console.log('In range');\n  }\n}\n```",
        "options": ["In range", "Nothing", "Error", "undefined"],
        "answer": "In range",
        "difficulty": "Medium",
        "explanation": "The outer condition `x > 5` is true for `x = 7`. The inner condition `x < 10` is also true, so 'In range' is logged.",
        "hint": "Trace the nested `if` statements."
    },
    {
        "question": "What is the value of `arr[2]`?\n```javascript\nlet arr = [4, 5, 6, 7];\n```",
        "options": ["6", "5", "7", "undefined"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "Arrays are zero-indexed. `arr[2]` accesses the third element, which is `6`.",
        "hint": "Count the index starting from 0."
    },
    {
        "question": "What is the value of `arr`?\n```javascript\nlet arr = [1, 2, 3];\narr.push(4);\n```",
        "options": ["[1, 2, 3, 4]", "[1, 2, 3]", "[4, 1, 2, 3]", "[1, 4]"],
        "answer": "[1, 2, 3, 4]",
        "difficulty": "Medium",
        "explanation": "The `push()` method adds `4` to the end of the array, resulting in `[1, 2, 3, 4]`.",
        "hint": "The `push()` method appends elements to the array’s end."
    },
    {
        "question": "What is the value of `arr`?\n```javascript\nlet arr = [1, 2, 3];\narr.splice(1, 1, 5);\n```",
        "options": ["[1, 5, 3]", "[1, 2, 5]", "[5, 2, 3]", "[1, 2, 3]"],
        "answer": "[1, 5, 3]",
        "difficulty": "Medium",
        "explanation": "The `splice(1, 1, 5)` method removes 1 element at index 1 (`2`) and inserts `5`, resulting in `[1, 5, 3]`.",
        "hint": "Understand the arguments of the `splice()` method."
    },
    {
        "question": "What is logged to the console?\n```javascript\nfor (let i = 1; i < 4; i++) {\n  console.log(i * 2);\n}\n```",
        "options": ["2, 4, 6", "1, 2, 3", "2, 4", "1, 3, 5"],
        "answer": "2, 4, 6",
        "difficulty": "Medium",
        "explanation": "The loop runs for `i = 1, 2, 3`, logging `i * 2` each time: `1*2=2`, `2*2=4`, `3*2=6`.",
        "hint": "Multiply the loop variable by 2 in each iteration."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet arr = [3, 4, 5];\nlet found = false;\nfor (let i = 0; i < arr.length; i++) {\n  if (arr[i] === 4) {\n    found = true;\n    break;\n  }\n}\nconsole.log(found);\n```",
        "options": ["true", "false", "4", "Nothing"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "When `arr[1] === 4`, `found` is set to `true`, and the `break` statement exits the loop. Then, `true` is logged.",
        "hint": "The `break` statement stops the loop when the condition is met."
    },
    {
        "question": "What is logged to the console?\n```javascript\nfor (let i = 1; i <= 2; i++) {\n  for (let j = 1; j <= 2; j++) {\n    console.log(i + j);\n  }\n}\n```",
        "options": ["2, 3, 3, 4", "1, 2, 3, 4", "2, 2, 3, 3", "1, 4"],
        "answer": "2, 3, 3, 4",
        "difficulty": "Medium",
        "explanation": "The outer loop runs for `i = 1, 2`, and the inner loop for `j = 1, 2`. The sums are `1+1=2`, `1+2=3`, `2+1=3`, `2+2=4`.",
        "hint": "Trace the nested loops and add `i` and `j`."
    },
    {
        "question": "What is the value of `str`?\n```javascript\nlet str = 'Hello';\nstr = str.toUpperCase();\n```",
        "options": ["HELLO", "hello", "Hello", "H"],
        "answer": "HELLO",
        "difficulty": "Medium",
        "explanation": "The `toUpperCase()` method converts all characters to uppercase, so 'Hello' becomes 'HELLO'.",
        "hint": "The `toUpperCase()` method affects the entire string."
    },
    {
        "question": "What is the value of `str.length`?\n```javascript\nlet str = 'Programming';\n```",
        "options": ["11", "10", "12", "9"],
        "answer": "11",
        "difficulty": "Medium",
        "explanation": "The `length` property counts the characters in 'Programming', which has 11 characters.",
        "hint": "Count each character, including all letters."
    },
    {
        "question": "What does this code return?\n```javascript\nlet str = 'JavaScript Code';\nstr.indexOf('Code');\n```",
        "options": ["10", "9", "0", "-1"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "The `indexOf()` method returns the starting index of 'Code' in 'JavaScript Code', which is 10 (after 'JavaScript ' including the space).",
        "hint": "Spaces count as characters in the index."
    },
    {
        "question": "What is the value of `str.charAt(2)`?\n```javascript\nlet str = 'Test';\n```",
        "options": ["T", "e", "s", "t"],
        "answer": "s",
        "difficulty": "Medium",
        "explanation": "The `charAt(2)` method returns the character at index 2 in 'Test', which is 's' (index 0 is 'T').",
        "hint": "Indexes start at 0, so find the third character."
    },
    {
        "question": "What is the value of `str`?\n```javascript\nlet str = 'Book';\nstr = str.replace('o', 'e');\n```",
        "options": ["Beek", "Book", "Boek", "Bok"],
        "answer": "Boek",
        "difficulty": "Medium",
        "explanation": "The `replace()` method replaces the first 'o' with 'e', so 'Book' becomes 'Boek'.",
        "hint": "The `replace()` method only changes the first occurrence."
    },
    {
        "question": "What is the value of `num`?\n```javascript\nlet num = 5.678;\nnum = Math.round(num);\n```",
        "options": ["6", "5", "5.7", "5.68"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "The `Math.round()` function rounds 5.678 to the nearest integer, which is 6.",
        "hint": "Check how `Math.round()` handles numbers above .5."
    },
    {
        "question": "What is a possible value of `num`?\n```javascript\nlet num = Math.floor(Math.random() * 10);\n```",
        "options": ["10", "9", "11", "-1"],
        "answer": "9",
        "difficulty": "Medium",
        "explanation": "The `Math.random() * 10` generates a number from 0 to <10. `Math.floor()` rounds down, so possible values are 0 to 9, including 9.",
        "hint": "The range of `Math.random()` is [0, 1), and `Math.floor()` gives integers."
    },
    {
        "question": "What is the value of `num`?\n```javascript\nlet num = parseInt('456.78');\n```",
        "options": ["456", "456.78", "NaN", "457"],
        "answer": "456",
        "difficulty": "Medium",
        "explanation": "The `parseInt()` function parses '456.78' and returns the integer 456, ignoring the decimal part.",
        "hint": "The `parseInt()` function stops at the decimal point."
    },
    {
        "question": "What is the value of `str`?\n```javascript\nlet num = 100;\nlet str = num.toString();\n```",
        "options": ["'100'", "100", "NaN", "undefined"],
        "answer": "'100'",
        "difficulty": "Medium",
        "explanation": "The `toString()` method converts the number 100 to the string '100'.",
        "hint": "The `toString()` method converts a number to a string."
    },
    {
        "question": "What is the value of `num`?\n```javascript\nlet num = 7.12345;\nnum = num.toFixed(2);\n```",
        "options": ["7.12", "7.12345", "7.13", "7"],
        "answer": "7.12",
        "difficulty": "Medium",
        "explanation": "The `toFixed(2)` method formats the number to 2 decimal places, returning '7.12' as a string.",
        "hint": "The `toFixed()` method rounds to the specified decimals."
    },
    {
        "question": "What does this code return?\n```javascript\nlet date = new Date('2025-06-06');\ndate.getMonth();\n```",
        "options": ["5", "6", "7", "0"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The `getMonth()` method returns the month (0-based), so June (6th month) is 5.",
        "hint": "JavaScript months are zero-based."
    },
    {
        "question": "What does this code return?\n```javascript\nlet date = new Date('2025-06-06');\ndate.getDay();\n```",
        "options": ["5", "6", "0", "1"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The `getDay()` method returns the day of the week (0-6, Sunday-Saturday). June 6, 2025, was a Friday, so it returns 5.",
        "hint": "Check the day of the week for June 6, 2025."
    },
    {
        "question": "What is the value of `date.getDate()`?\n```javascript\nlet date = new Date('2025-06-06');\ndate.setDate(15);\n```",
        "options": ["15", "6", "5", "16"],
        "answer": "15",
        "difficulty": "Medium",
        "explanation": "The `setDate(15)` method changes the day of the month to 15, so `getDate()` returns 15.",
        "hint": "The `setDate()` method modifies the day of the month."
    },
    {
        "question": "What is logged to the console?\n```javascript\nfunction square(num) {\n  return num * num;\n}\nconsole.log(square(4));\n```",
        "options": ["16", "8", "4", "undefined"],
        "answer": "16",
        "difficulty": "Medium",
        "explanation": "The `square` function returns `num * num`, so `square(4)` returns `4 * 4 = 16`.",
        "hint": "Calculate the result of the function for the input 4."
    },
    {
        "question": "What is logged to the console?\n```javascript\nfunction greet(name) {\n  return 'Hello, ' + name;\n}\nconsole.log(greet('Bob'));\n```",
        "options": ["Hello, Bob", "Bob", "Hello", "undefined"],
        "answer": "Hello, Bob",
        "difficulty": "Medium",
        "explanation": "The `greet` function concatenates 'Hello, ' with the parameter `name` ('Bob'), returning 'Hello, Bob'.",
        "hint": "Check how the parameter is used in the string concatenation."
    },
    {
        "question": "What is the value of `x`?\n```javascript\nlet x = '7' - 2;\n```",
        "options": ["5", "72", "NaN", "52"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The `-` operator converts the string '7' to a number and subtracts 2, resulting in `7 - 2 = 5`.",
        "hint": "The `-` operator triggers numeric conversion, unlike `+`."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = '10';\nif (x == 10) {\n  console.log('Equal');\n} else {\n  console.log('Not equal');\n}\n```",
        "options": ["Equal", "Not equal", "Nothing", "Error"],
        "answer": "Equal",
        "difficulty": "Medium",
        "explanation": "The `==` operator performs loose equality, converting '10' to the number 10, which equals 10, so 'Equal' is logged.",
        "hint": "The `==` operator converts types before comparing."
    },
    {
        "question": "What is the value of `arr.length`?\n```javascript\nlet arr = [1, 2, 3, 4];\narr.shift();\n```",
        "options": ["3", "4", "2", "1"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "The `shift()` method removes the first element, reducing `[1, 2, 3, 4]` to `[2, 3, 4]`, so `arr.length` is 3.",
        "hint": "The `shift()` method decreases the array length."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet arr = [2, 4, 6];\nfor (let i = 0; i < arr.length; i++) {\n  if (arr[i] % 2 === 0) {\n    console.log(arr[i]);\n  }\n}\n```",
        "options": ["2, 4, 6", "2, 4", "4, 6", "Nothing"],
        "answer": "2, 4, 6",
        "difficulty": "Medium",
        "explanation": "The loop checks each element. All elements (`2, 4, 6`) are even (`arr[i] % 2 === 0`), so all are logged.",
        "hint": "Check which elements satisfy the even number condition."
    },
    {
        "question": "What is the value of `str`?\n```javascript\nlet str = 'WORLD';\nstr = str.toLowerCase();\n```",
        "options": ["world", "WORLD", "World", "w"],
        "answer": "world",
        "difficulty": "Medium",
        "explanation": "The `toLowerCase()` method converts all characters to lowercase, so 'WORLD' becomes 'world'.",
        "hint": "The `toLowerCase()` method affects the entire string."
    },
    {
        "question": "What does this code return?\n```javascript\nlet str = 'JavaScript';\nstr.slice(4, 7);\n```",
        "options": ["Scri", "Java", "Scr", "ipt"],
        "answer": "Scr",
        "difficulty": "Medium",
        "explanation": "The `slice(4, 7)` method extracts characters from index 4 to 6, returning 'Scr' from 'JavaScript'.",
        "hint": "The `slice()` method’s second argument is exclusive."
    },
    {
        "question": "What does this code return?\n```javascript\nlet str = 'Hello World';\nstr.includes('World');\n```",
        "options": ["true", "false", "6", "-1"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The `includes()` method checks if 'World' is a substring of 'Hello World', returning `true`.",
        "hint": "The `includes()` method tests for substring presence."
    },
    {
        "question": "What is the value of `num`?\n```javascript\nlet num = parseFloat('9.99');\n```",
        "options": ["9.99", "9", "NaN", "10"],
        "answer": "9.99",
        "difficulty": "Medium",
        "explanation": "The `parseFloat()` function parses '9.99' and returns the floating-point number 9.99.",
        "hint": "The `parseFloat()` function includes decimals."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 12;\nif (x >= 10) {\n  if (x <= 15) {\n    console.log('Within bounds');\n  }\n}\n```",
        "options": ["Within bounds", "Nothing", "Error", "undefined"],
        "answer": "Within bounds",
        "difficulty": "Medium",
        "explanation": "Both conditions (`x >= 10` and `x <= 15`) are true for `x = 12`, so 'Within bounds' is logged.",
        "hint": "Check both nested conditions."
    },
    {
        "question": "What is the value of `arr`?\n```javascript\nlet arr = [1, 2, 3];\narr.pop();\n```",
        "options": ["[1, 2]", "[2, 3]", "[1, 3]", "[3]"],
        "answer": "[1, 2]",
        "difficulty": "Medium",
        "explanation": "The `pop()` method removes the last element, changing `[1, 2, 3]` to `[1, 2]`.",
        "hint": "The `pop()` method removes the last element."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet sum = 0;\nfor (let i = 1; i <= 4; i++) {\n  sum += i;\n}\nconsole.log(sum);\n```",
        "options": ["10", "6", "4", "15"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "The loop adds `1 + 2 + 3 + 4` to `sum`, resulting in 10.",
        "hint": "Add the numbers from 1 to 4."
    },
    {
        "question": "What is the value of `date.getFullYear()`?\n```javascript\nlet date = new Date('2025-06-06');\n```",
        "options": ["2025", "2024", "2026", "6"],
        "answer": "2025",
        "difficulty": "Medium",
        "explanation": "The `getFullYear()` method returns the year of the date, which is 2025.",
        "hint": "Check the year in the `Date` object."
    },
    {
        "question": "What is logged to the console?\n```javascript\nfunction divide(a, b = 2) {\n  return a / b;\n}\nconsole.log(divide(10));\n```",
        "options": ["5", "10", "2", "undefined"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The `divide` function has a default parameter `b = 2`. Calling `divide(10)` uses `b = 2`, so `10 / 2 = 5`.",
        "hint": "Check the default value of the parameter `b`."
    },
    {
        "question": "What is the value of `x`?\n```javascript\nlet x = '8' * '2';\n```",
        "options": ["16", "82", "NaN", "10"],
        "answer": "16",
        "difficulty": "Medium",
        "explanation": "The `*` operator converts both strings '8' and '2' to numbers, performing `8 * 2 = 16`.",
        "hint": "The `*` operator triggers numeric conversion for strings."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet arr = [1, 2, 3, 4];\nfor (let i = 0; i < arr.length; i++) {\n  if (arr[i] > 2) {\n    console.log(arr[i]);\n  }\n}\n```",
        "options": ["3, 4", "1, 2", "2, 3, 4", "Nothing"],
        "answer": "3, 4",
        "difficulty": "Medium",
        "explanation": "The loop logs elements where `arr[i] > 2`, which are `3` and `4`.",
        "hint": "Identify elements greater than 2 in the array."
    },
    {
        "question": "What does this code return?\n```javascript\nlet str = 'Hello World';\nstr.substring(6, 11);\n```",
        "options": ["World", "Hello", "rld", "lo Wo"],
        "answer": "World",
        "difficulty": "Medium",
        "explanation": "The `substring(6, 11)` method extracts characters from index 6 to 10, returning 'World'.",
        "hint": "The `substring()` method’s arguments define the start and end indices."
    },
    {
        "question": "What is the value of `num`?\n```javascript\nlet num = Math.floor(7.89);\n```",
        "options": ["7", "8", "7.89", "7.9"],
        "answer": "7",
        "difficulty": "Medium",
        "explanation": "The `Math.floor()` function rounds 7.89 down to the nearest integer, which is 7.",
        "hint": "The `Math.floor()` function rounds down."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 10;\nif (x > 5 && x < 15) {\n  console.log('Valid');\n} else {\n  console.log('Invalid');\n}\n```",
        "options": ["Valid", "Invalid", "Nothing", "Error"],
        "answer": "Valid",
        "difficulty": "Medium",
        "explanation": "The condition `x > 5 && x < 15` is true for `x = 10`, so 'Valid' is logged.",
        "hint": "Evaluate both conditions in the `&&` expression."
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
