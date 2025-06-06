import streamlit as st
import random
from datetime import datetime

# Quiz data with fixed syntax error in question 43 and corrected question 14
quiz = [
    {
        "question": "What happens if the user clicks 'Cancel' in this alert code?\n```javascript\nlet result = alert('Confirm action');\nconsole.log(result);\n```",
        "options": ["'OK'", "undefined", "null", "'Cancel'"],
        "answer": "undefined",
        "difficulty": "Medium",
        "explanation": "The alert() function displays a dialog box and always returns undefined, regardless of whether the user clicks 'OK' or 'Cancel'."
    },
    {
        "question": "What is the output of this string variable operation?\n```javascript\nlet str = 'Hello';\nstr += ' World';\nconsole.log(str);\n```",
        "options": ["HelloWorld", "Hello World", "Hello", "Error"],
        "answer": "Hello World",
        "difficulty": "Medium",
        "explanation": "The += operator concatenates ' World' to the string 'Hello', resulting in 'Hello World'."
    },
    {
        "question": "What is the result of this number variable operation?\n```javascript\nlet x = 20;\nx -= 7;\nconsole.log(x);\n```",
        "options": ["27", "13", "7", "Error"],
        "answer": "13",
        "difficulty": "Medium",
        "explanation": "The -= operator subtracts 7 from x (20), so x becomes 13."
    },
    {
        "question": "Which variable name follows JavaScript naming rules?\n```javascript\nlet user_name_1 = 'Ali';\n```",
        "options": ["1user", "user-name", "user_name_1", "user name"],
        "answer": "user_name_1",
        "difficulty": "Medium",
        "explanation": "Variable names can include letters, digits, underscores, or dollar signs but cannot start with a digit, use spaces, or include hyphens. 'user_name_1' is valid."
    },
    {
        "question": "What is the output of this math expression?\n```javascript\nconsole.log(15 / 3 + 2);\n```",
        "options": ["7", "10", "5", "17"],
        "answer": "7",
        "difficulty": "Medium",
        "explanation": "Division has higher precedence than addition, so 15 / 3 = 5, then 5 + 2 = 7."
    },
    {
        "question": "What does the % operator return in this code?\n```javascript\nconsole.log(17 % 5);\n```",
        "options": ["2", "3", "0", "5"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "The % operator returns the remainder of 17 divided by 5, which is 2 (17 = 5 * 3 + 2)."
    },
    {
        "question": "What is the result of this expression with parentheses?\n```javascript\nconsole.log(4 + 3 * (2 + 1));\n```",
        "options": ["13", "9", "10", "21"],
        "answer": "13",
        "difficulty": "Medium",
        "explanation": "Parentheses evaluate 2 + 1 = 3 first, then 3 * 3 = 9, and finally 4 + 9 = 13."
    },
    {
        "question": "What does this concatenation produce?\n```javascript\nlet num = 5;\nlet str = 'Items: ' + num;\nconsole.log(str);\n```",
        "options": ["Items: 5", "Items:5", "5Items", "Error"],
        "answer": "Items: 5",
        "difficulty": "Medium",
        "explanation": "The number 5 is coerced to a string and concatenated with 'Items: ', producing 'Items: 5'."
    },
    {
        "question": "What does this prompt return if the user enters nothing and clicks 'OK'?\n```javascript\nlet input = prompt('Enter text', 'Default');\nconsole.log(input);\n```",
        "options": ["'Default'", "''", "null", "undefined"],
        "answer": "''",
        "difficulty": "Medium",
        "explanation": "If the user enters nothing and clicks 'OK', prompt() returns an empty string ('')."
    },
    {
        "question": "What is the output of this if statement?\n```javascript\nlet marks = 65;\nif (marks >= 70) {\n  console.log('Pass');\n} else {\n  console.log('Fail');\n}\n```",
        "options": ["Pass", "Fail", "undefined", "Error"],
        "answer": "Fail",
        "difficulty": "Medium",
        "explanation": "Since 65 is less than 70, the else block executes, logging 'Fail'."
    },
    {
        "question": "What does this comparison evaluate to?\n```javascript\nconsole.log('10' == 10);\n```",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The == operator performs type coercion, converting '10' to the number 10, so '10' == 10 is true."
    },
    {
        "question": "What is the output of this else if code?\n```javascript\nlet speed = 80;\nif (speed > 100) {\n  console.log('Fast');\n} else if (speed > 60) {\n  console.log('Moderate');\n} else {\n  console.log('Slow');\n}\n```",
        "options": ["Fast", "Moderate", "Slow", "Error"],
        "answer": "Moderate",
        "difficulty": "Medium",
        "explanation": "Since 80 is not > 100 but is > 60, the else if block executes, logging 'Moderate'."
    },
    {
        "question": "What does this condition check return?\n```javascript\nlet a = 8, b = 12;\nif (a < 10 || b > 15) {\n  console.log('Valid');\n}\n```",
        "options": ["Valid", "Nothing", "false", "Error"],
        "answer": "Valid",
        "difficulty": "Medium",
        "explanation": "The || operator checks if either condition is true. Since a < 10 (8 < 10), the condition is true, logging 'Valid'."
    },
    {
        "question": "What does this nested if output?\n```javascript\nlet num = 20;\nif (num > 15) {\n  if (num % 4 === 0) {\n    console.log('Divisible by 4');\n  } else {\n    console.log('Not divisible');\n  }\n}\n```",
        "options": ["Divisible by 4", "Not divisible", "Nothing", "Error"],
        "answer": "Divisible by 4",
        "difficulty": "Medium",
        "explanation": "Since 20 > 15, the outer if block executes. Since 20 % 4 === 0, the inner if block executes, logging 'Divisible by 4'."
    },
    {
        "question": "What does this array access return?\n```javascript\nlet fruits = ['apple', 'banana', 'orange'];\nconsole.log(fruits[2]);\n```",
        "options": ["apple", "banana", "orange", "undefined"],
        "answer": "orange",
        "difficulty": "Medium",
        "explanation": "Array indices start at 0, so fruits[2] accesses the third element, 'orange'."
    },
    {
        "question": "What is the result after removing an element?\n```javascript\nlet arr = [10, 20, 30];\narr.pop();\nconsole.log(arr);\n```",
        "options": ["[10, 20]", "[20, 30]", "[10, 30]", "Error"],
        "answer": "[10, 20]",
        "difficulty": "Medium",
        "explanation": "The pop() method removes the last element (30), leaving [10, 20]."
    },
    {
        "question": "What does this splice operation produce?\n```javascript\nlet arr = ['x', 'y', 'z'];\narr.splice(1, 1, 'a');\nconsole.log(arr);\n```",
        "options": ["['x', 'a', 'z']", "['x', 'y', 'a']", "['a', 'z']", "Error"],
        "answer": "['x', 'a', 'z']",
        "difficulty": "Medium",
        "explanation": "splice(1, 1, 'a') removes 1 element at index 1 ('y') and inserts 'a', resulting in ['x', 'a', 'z']."
    },
    {
        "question": "What does this for loop output?\n```javascript\nfor (let i = 2; i <= 6; i += 2) {\n  console.log(i);\n}\n```",
        "options": ["2 4 6", "2 3 4 5 6", "4 6", "Error"],
        "answer": "2 4 6",
        "difficulty": "Medium",
        "explanation": "The loop starts at i=2, increments by 2, and stops at i<=6, logging 2, 4, 6."
    },
    {
        "question": "What does this loop with a break output?\n```javascript\nlet sum = 0;\nfor (let i = 1; i <= 5; i++) {\n  if (i === 4) break;\n  sum += i;\n}\nconsole.log(sum);\n```",
        "options": ["6", "10", "15", "4"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "The loop adds i=1,2,3 to sum (1+2+3=6) before breaking at i=4."
    },
    {
        "question": "What does this nested loop output?\n```javascript\nlet result = '';\nfor (let i = 1; i <= 2; i++) {\n  for (let j = 1; j <= 2; j++) {\n    result += (i * j) + ' ';\n  }\n}\nconsole.log(result);\n```",
        "options": ["1 2 2 4", "1 2 3 4", "2 4 4 8", "Error"],
        "answer": "1 2 2 4",
        "difficulty": "Medium",
        "explanation": "The loop calculates: (1*1)=1, (1*2)=2, (2*1)=2, (2*2)=4, producing '1 2 2 4'."
    },
    {
        "question": "What does this case conversion return?\n```javascript\nlet str = 'Test CASE';\nconsole.log(str.toUpperCase());\n```",
        "options": ["TEST CASE", "test case", "Test CASE", "Error"],
        "answer": "TEST CASE",
        "difficulty": "Medium",
        "explanation": "The toUpperCase() method converts all characters to uppercase, resulting in 'TEST CASE'."
    },
    {
        "question": "What is the length of this string?\n```javascript\nlet text = 'JavaScript!';\nconsole.log(text.length);\n```",
        "options": ["9", "10", "11", "Error"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "The string 'JavaScript!' has 10 characters, including the exclamation mark."
    },
    {
        "question": "What does this string search return?\n```javascript\nlet str = 'Learn JavaScript';\nconsole.log(str.indexOf('Java'));\n```",
        "options": ["6", "0", "-1", "5"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "indexOf('Java') returns the starting index of 'Java' in 'Learn JavaScript', which is 6."
    },
    {
        "question": "What character is returned by this code?\n```javascript\nlet str = 'Coding';\nconsole.log(str.charAt(4));\n```",
        "options": ["i", "n", "g", "d"],
        "answer": "n",
        "difficulty": "Medium",
        "explanation": "charAt(4) returns the character at index 4 in 'Coding', which is 'n'."
    },
    {
        "question": "What does this string replacement produce?\n```javascript\nlet str = 'I like to code';\nconsole.log(str.replace('code', 'program'));\n```",
        "options": ["I like to program", "I like to code", "program", "Error"],
        "answer": "I like to program",
        "difficulty": "Medium",
        "explanation": "The replace() method replaces 'code' with 'program', resulting in 'I like to program'."
    },
    {
        "question": "What is the result of this rounding?\n```javascript\nconsole.log(Math.round(7.8));\n```",
        "options": ["7", "8", "7.8", "Error"],
        "answer": "8",
        "difficulty": "Medium",
        "explanation": "Math.round(7.8) rounds to the nearest integer, which is 8."
    },
    {
        "question": "What range does this random number code produce?\n```javascript\nconsole.log(Math.floor(Math.random() * 6) + 1);\n```",
        "options": ["0 to 5", "1 to 6", "0 to 6", "1 to 5"],
        "answer": "1 to 6",
        "difficulty": "Medium",
        "explanation": "Math.random() generates 0 to <1, multiplied by 6 gives 0 to <6, Math.floor() rounds down to 0-5, and +1 shifts to 1-6."
    },
    {
        "question": "What does this parsing return?\n```javascript\nconsole.log(parseInt('42.78'));\n```",
        "options": ["42", "42.78", "43", "NaN"],
        "answer": "42",
        "difficulty": "Medium",
        "explanation": "parseInt('42.78') parses the string to an integer, stopping at the decimal, returning 42."
    },
    {
        "question": "What does this conversion output?\n```javascript\nlet num = 100;\nconsole.log(String(num));\n```",
        "options": ["'100'", "100", "NaN", "Error"],
        "answer": "'100'",
        "difficulty": "Medium",
        "explanation": "String(100) converts the number 100 to the string '100'."
    },
    {
        "question": "What does this decimal control return?\n```javascript\nlet num = 9.87654;\nconsole.log(num.toFixed(2));\n```",
        "options": ["9.88", "9.87", "9.876", "9.9"],
        "answer": "9.88",
        "difficulty": "Medium",
        "explanation": "toFixed(2) rounds the number to 2 decimal places, so 9.87654 becomes 9.88."
    },
    {
        "question": "What does this date operation return?\n```javascript\nlet date = new Date('2024-01-01');\nconsole.log(date.getMonth());\n```",
        "options": ["0", "1", "12", "Error"],
        "answer": "0",
        "difficulty": "Medium",
        "explanation": "getMonth() returns the month (0-11), so January 1, 2024, returns 0."
    },
    {
        "question": "What does this function output?\n```javascript\nfunction multiply(x, y) {\n  return x * y;\n}\nconsole.log(multiply(6, 7));\n```",
        "options": ["42", "13", "1", "Error"],
        "answer": "42",
        "difficulty": "Medium",
        "explanation": "The function returns 6 * 7 = 42."
    },
    {
        "question": "What does this function with default parameters return?\n```javascript\nfunction greet(name = 'Guest') {\n  return 'Hi, ' + name;\n}\nconsole.log(greet());\n```",
        "options": ["Hi, Guest", "Hi, undefined", "Hi, null", "Error"],
        "answer": "Hi, Guest",
        "difficulty": "Medium",
        "explanation": "If no argument is provided, the default parameter 'Guest' is used, returning 'Hi, Guest'."
    },
    {
        "question": "What does this date operation return?\n```javascript\nlet date = new Date('2025-06-06');\nconsole.log(date.getDay());\n```",
        "options": ["5", "6", "0", "1"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "June 6, 2025, was a Friday, and getDay() returns 5 for Friday (0=Sunday, 1=Monday, etc.)."
    },
    {
        "question": "What does this string slicing return?\n```javascript\nlet str = 'JavaScript';\nconsole.log(str.slice(4, 7));\n```",
        "options": ["Scri", "Scr", "ipt", "Java"],
        "answer": "Scr",
        "difficulty": "Medium",
        "explanation": "slice(4, 7) extracts characters from index 4 to 6 (end index is exclusive), returning 'Scr'."
    },
    {
        "question": "What does this array method return?\n```javascript\nlet arr = [1, 2, 3, 4];\nconsole.log(arr.shift());\n```",
        "options": ["1", "4", "[2, 3, 4]", "Error"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "shift() removes and returns the first element (1), modifying the array to [2, 3, 4]."
    },
    {
        "question": "What is the output of this loop?\n```javascript\nlet arr = [1, 2, 3];\nfor (let i = arr.length - 1; i >= 0; i--) {\n  console.log(arr[i]);\n}\n```",
        "options": ["3 2 1", "1 2 3", "2 3 1", "Error"],
        "answer": "3 2 1",
        "difficulty": "Medium",
        "explanation": "The loop iterates backward from index 2 to 0, logging 3, 2, 1."
    },
    {
        "question": "What does this code return?\n```javascript\nlet str = 'hello';\nconsole.log(str.substring(1, 4));\n```",
        "options": ["ell", "hel", "llo", "Error"],
        "answer": "ell",
        "difficulty": "Medium",
        "explanation": "substring(1, 4) extracts characters from index 1 to 3, returning 'ell'."
    },
    {
        "question": "What does this code output?\n```javascript\nlet num = 3.14159;\nconsole.log(Math.floor(num));\n```",
        "options": ["3", "4", "3.14", "Error"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "Math.floor(3.14159) rounds down to the nearest integer, returning 3."
    },
    {
        "question": "What does this code return?\n```javascript\nlet str = '123abc';\nconsole.log(parseFloat(str));\n```",
        "options": ["123", "123.0", "NaN", "Error"],
        "answer": "123.0",
        "difficulty": "Medium",
        "explanation": "parseFloat('123abc') parses the string to a floating-point number, stopping at the non-numeric 'abc', returning 123.0."
    },
    {
        "question": "What does this code output?\n```javascript\nlet arr = ['a', 'b'];\narr.unshift('c');\nconsole.log(arr);\n```",
        "options": ["['c', 'a', 'b']", "['a', 'b', 'c']", "['c', 'b']", "Error"],
        "answer": "['c', 'a', 'b']",
        "difficulty": "Medium",
        "explanation": "unshift('c') adds 'c' to the start of the array, resulting in ['c', 'a', 'b']."
    },
    {
        "question": "What does this code return?\n```javascript\nlet str = 'abcde';\nconsole.log(str.includes('cd'));\n```",
        "options": ["true", "false", "2", "Error"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "includes('cd') checks if 'cd' is a substring, returning true since 'cd' exists in 'abcde'."
    },
    {
        "question": "What does this code output?\n```javascript\nlet num = 0.1 + 0.2;\nconsole.log(num.toFixed(1));\n```",
        "options": ["0.3", "0.4", "0.2", "Error"],
        "answer": "0.3",
        "difficulty": "Medium",
        "explanation": "Due to floating-point precision, 0.3 is approximated, and toFixed(1) rounds it to 0.3."
    },
    {
        "question": "What does this code return?\n```javascript\nlet date = new Date('2025-06-06T10:29:00');\nconsole.log(date.getHours());\n```",
        "options": ["10", "11", "0", "Error"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "getHours() returns the hour (10) from the time 10:29:00."
    },
    {
        "question": "What does this function output?\n```javascript\nfunction isEven(num) {\n  return num % 2 === 0;\n}\nconsole.log(isEven(10));\n```",
        "options": ["true", "false", "10", "Error"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The function checks if 10 is divisible by 2 (10 % 2 === 0), returning true."
    },
    {
        "question": "What does this code output?\n```javascript\nlet arr = [1, 2, 3];\nconsole.log(arr.slice(1, 3));\n```",
        "options": ["[2, 3]", "[1, 2]", "[3]", "Error"],
        "answer": "[2, 3]",
        "difficulty": "Medium",
        "explanation": "slice(1, 3) extracts elements from index 1 to 2, returning [2, 3]."
    },
    {
        "question": "What does this code return?\n```javascript\nlet str = 'Hello World';\nconsole.log(str.split(' ')[0]);\n```",
        "options": ["Hello", "World", "Hello World", "Error"],
        "answer": "Hello",
        "difficulty": "Medium",
        "explanation": "split(' ') splits the string into ['Hello', 'World'], and [0] accesses 'Hello'."
    },
    {
        "question": "What does this code output?\n```javascript\nlet num = Math.ceil(4.2);\nconsole.log(num);\n```",
        "options": ["4", "5", "4.2", "Error"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "Math.ceil(4.2) rounds up to the next integer, returning 5."
    },
    {
        "question": "What does this code return?\n```javascript\nlet str = '100px';\nconsole.log(parseInt(str));\n```",
        "options": ["100", "100px", "NaN", "Error"],
        "answer": "100",
        "difficulty": "Medium",
        "explanation": "parseInt('100px') parses the string to an integer, stopping at 'px', returning 100."
    },
    {
        "question": "What does this code output?\n```javascript\nlet arr = [10, 20];\narr.splice(1, 0, 15);\nconsole.log(arr);\n```",
        "options": ["[10, 15, 20]", "[10, 20, 15]", "[15, 20]", "Error"],
        "answer": "[10, 15, 20]",
        "difficulty": "Medium",
        "explanation": "splice(1, 0, 15) inserts 15 at index 1 without removing elements, resulting in [10, 15, 20]."
    },
    {
        "question": "What does this code return?\n```javascript\nlet str = 'Test';\nconsole.log(str.charAt(10));\n```",
        "options": ["'T'", "''", "undefined", "Error"],
        "answer": "''",
        "difficulty": "Medium",
        "explanation": "charAt(10) returns an empty string for an index beyond the string's length."
    },
    {
        "question": "What does this code output?\n```javascript\nlet date = new Date('2025-06-06');\ndate.setDate(10);\nconsole.log(date.getDate());\n```",
        "options": ["6", "10", "0", "Error"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "setDate(10) sets the day to 10, and getDate() returns 10."
    },
    {
        "question": "What does this function output?\n```javascript\nfunction sumArray(arr) {\n  let sum = 0;\n  for (let num of arr) sum += num;\n  return sum;\n}\nconsole.log(sumArray([1, 2, 3]));\n```",
        "options": ["6", "123", "3", "Error"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "The function sums the array elements (1 + 2 + 3 = 6)."
    }
]

# Shuffle quiz and label options
def shuffle_quiz():
    shuffled = random.sample(quiz, len(quiz))
    for q in shuffled:
        labeled_options = list(zip(q['options'], ['A', 'B', 'C', 'D']))
        random.shuffle(labeled_options)
        q['display_options'] = [f"{label}: {option}" for option, label in labeled_options]
        for option, label in labeled_options:
            if option == q['answer']:
                q['labeled_answer'] = f"{label}: {option}"
                break
    return shuffled

# CSS for enhanced UI
st.markdown("""
    <style>
    body {
        background: linear-gradient(180deg, #1a1a3b, #2c2c54);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    .main-container {
        background: #2c2c54;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        max-width: 900px;
        margin: 20px auto;
    }
    .stButton>button {
        background: linear-gradient(45deg, #6b21a8, #a855f7);
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 12px;
        width: 100%;
        font-size: 15px;
        font-weight: 600;
        margin: 6px 0;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #8b5cf6, #c084fc);
        transform: translateY(-2px);
    }
    .question-container {
        background: #373760;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        margin-bottom: 15px;
    }
    .feedback-correct {
        color: #34c759;
        font-weight: 600;
        font-size: 18px;
        margin: 15px 0;
    }
    .feedback-wrong {
        color: #ff3b30;
        font-weight: 600;
        font-size: 18px;
        margin: 15px 0;
    }
    .progress-bar {
        background: #4b4b6b;
        border-radius: 10px;
        height: 10px;
        margin: 10px 0;
    }
    .progress-fill {
        background: linear-gradient(45deg, #6b21a8, #a855f7);
        height: 100%;
        border-radius: 10px;
        transition: width 0.3s ease;
    }
    .title {
        font-size: 36px;
        text-align: center;
        margin-bottom: 8px;
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
        background-color: #1e1e1e !important;
        border-radius: 8px;
        padding: 15px;
        font-family: 'Consolas', 'Monaco', monospace;
        font-size: 14px;
        line-height: 1.5;
        border: 1px solid #4b4b6b;
    }
    .stCodeBlock pre, .stCodeBlock code {
        color: #d4d4d4;
    }
    .stCodeBlock .hljs-keyword { color: #569cd6; }
    .stCodeBlock .hljs-string { color: #ce9178; }
    .stCodeBlock .hljs-number { color: #b5cea8; }
    .stCodeBlock .hljs-comment { color: #6a9955; }
    .stCodeBlock .hljs-operator, .stCodeBlock .hljs-punctuation { color: #d4d4d4; }
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
            padding: 10px;
        }
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Initialize session state
if 'quiz_data' not in st.session_state:
    st.session_state.update({
        'quiz_data': shuffle_quiz() if quiz else [],
        'score': 0,
        'current_q': 0,
        'start_time': datetime.now(),
        'answers': [None] * len(quiz) if quiz else [],
        'show_results': False,
        'selected_option': None,
        'feedback': None,
        'time_left': 1800  # 30 minutes in seconds
    })

# Timer logic
def update_timer():
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.session_state.time_left = max(1800 - elapsed, 0)
    if st.session_state.time_left <= 0:
        st.session_state.show_results = True
        st.rerun()

# Update timer
if not st.session_state.show_results:
    update_timer()
    minutes = int(st.session_state.time_left // 60)
    seconds = int(st.session_state.time_left % 60)
    st.markdown(f'<div class="timer">⏰ Time Left: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

# Main UI
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 JavaScript Quiz Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript Skills</p>', unsafe_allow_html=True)

if not st.session_state.quiz_data:
    st.error("No quiz questions available. Please add questions to start the quiz.")
else:
    progress = st.session_state.current_q / len(st.session_state.quiz_data)
    progress_percentage = int(progress * 100)
    st.markdown(f"""
    <div class="progress-bar">
        <div class="progress-fill" style="width: {progress_percentage}%"></div>
    </div>
    <div style="color: #b0b0d0; font-size: 13px; text-align: center;">
        Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.show_results:
        with st.container():
            st.markdown('<div class="question-container">', unsafe_allow_html=True)
            q = st.session_state.quiz_data[st.session_state.current_q]
            
            # Display difficulty
            st.markdown(f'<div class="difficulty">Difficulty: {q["difficulty"]}</div>', unsafe_allow_html=True)

            # Split question into text and code
            if "```javascript" in q['question']:
                question_parts = q['question'].split("```javascript\n")
                question_text = question_parts[0].strip()
                code_snippet = question_parts[1].split("```")[0].strip()
                st.markdown(f"### Question {st.session_state.current_q + 1}")
                st.markdown(f"**{question_text}**")
                st.code(code_snippet, language="javascript")
            else:
                st.markdown(f"### Question {st.session_state.current_q + 1}")
                st.markdown(f"**{q['question']}**")

            # Option buttons
            for i, option in enumerate(q['display_options']):
                if st.button(option, key=f"q{i}", disabled=st.session_state.selected_option is not None):
                    original_option = option[3:]
                    is_correct = option == q['labeled_answer']
                    st.session_state.selected_option = option
                    st.session_state.feedback = {'is_correct': is_correct, 'correct_answer': q['labeled_answer'], 'explanation': q['explanation']}
                    st.session_state.answers[st.session_state.current_q] = {
                        'question': q['question'], 'user_answer': option, 'correct_answer': q['labeled_answer'], 
                        'is_correct': is_correct,
                        'difficulty': q['difficulty']
                    }
                    if is_correct:
                        points = {'Easy': 1, 'Medium': 2, 'Hard': 3}[q['difficulty']]
                        st.session_state.score += points
                    st.rerun()

            # Feedback
            if st.session_state.feedback:
                if st.session_state.feedback['is_correct']:
                    st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div style="color: #b0b0d0; font-size: 14px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)
