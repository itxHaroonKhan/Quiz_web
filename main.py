import streamlit as st
import random
from datetime import datetime

# Updated quiz with 50 questions, including difficulty and hints
quiz = [
    {
        "question": "What happens when this alert is executed?\n```javascript\nalert('Hello\\nWorld');\n```",
        "options": ["Displays 'Hello World'", "Displays 'Hello' and 'World' on two lines", "Throws an error", "Displays 'Hello\\nWorld'"],
        "answer": "Displays 'Hello' and 'World' on two lines",
        "difficulty": "Easy",
        "hint": "The \\n character creates a new line in strings."
    },
    {
        "question": "What is the output of this code?\n```javascript\nlet name = 'Ali';\nconsole.log(name + undefined);\n```",
        "options": ["Aliundefined", "NaN", "Error", "undefined"],
        "answer": "Aliundefined",
        "difficulty": "Medium",
        "hint": "String concatenation with undefined results in a string."
    },
    {
        "question": "What will this code output?\n```javascript\nlet num = 10.5;\nconsole.log(num * '2');\n```",
        "options": ["21", "NaN", "1052", "Error"],
        "answer": "21",
        "difficulty": "Medium",
        "hint": "JavaScript converts the string '2' to a number during multiplication."
    },
    {
        "question": "Which variable name is illegal?\n```javascript\nlet 2ndVar = 10;\n```",
        "options": ["my_variable", "_2ndVar", "2ndVar", "$var"],
        "answer": "2ndVar",
        "difficulty": "Easy",
        "hint": "Variable names cannot start with a number."
    },
    {
        "question": "What is the result of this expression?\n```javascript\nconsole.log(10 / 2 + 3 * 2 - 1);\n```",
        "options": ["10", "8", "11", "12"],
        "answer": "10",
        "difficulty": "Medium",
        "hint": "Follow the order of operations (PEMDAS)."
    },
    {
        "question": "What does the ** operator do in this code?\n```javascript\nconsole.log(3 ** 2);\n```",
        "options": ["6", "9", "8", "Error"],
        "answer": "9",
        "difficulty": "Easy",
        "hint": "** is the exponentiation operator."
    },
    {
        "question": "What is the output of this code?\n```javascript\nconsole.log((5 + 3) * (2 + 2) / 4);\n```",
        "options": ["8", "16", "4", "10"],
        "answer": "8",
        "difficulty": "Medium",
        "hint": "Parentheses ensure addition is performed first."
    },
    {
        "question": "What does this concatenation produce?\n```javascript\nlet str = 'Code' + 2 * 3 + 'Run';\nconsole.log(str);\n```",
        "options": ["Code6Run", "Code23Run", "Error", "NaN"],
        "answer": "Code6Run",
        "difficulty": "Medium",
        "hint": "Multiplication has higher precedence than concatenation."
    },
    {
        "question": "What does this prompt return if the user cancels it?\n```javascript\nlet input = prompt('Enter something:');\nconsole.log(input);\n```",
        "options": ["null", "undefined", "'' (empty string)", "Error"],
        "answer": "null",
        "difficulty": "Easy",
        "hint": "Canceling a prompt returns null."
    },
    {
        "question": "What will this code output?\n```javascript\nlet x = null;\nif (x || x === null) {\n  console.log('Nullish');\n}\n```",
        "options": ["Nullish", "Nothing", "undefined", "Error"],
        "answer": "Nullish",
        "difficulty": "Medium",
        "hint": "Check how null behaves in logical OR operations."
    },
    {
        "question": "What does this comparison return?\n```javascript\nconsole.log('10' !== 10);\n```",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true",
        "difficulty": "Easy",
        "hint": "Strict inequality checks both value and type."
    },
    {
        "question": "What is the output of this code?\n```javascript\nlet score = 65;\nif (score >= 90) {\n  console.log('A');\n} else if (score >= 80) {\n  console.log('B');\n} else if (score >= 60) {\n  console.log('C');\n} else {\n  console.log('D');\n}\n```",
        "options": ["A", "B", "C", "D"],
        "answer": "C",
        "difficulty": "Easy",
        "hint": "Check the conditions in order."
    },
    {
        "question": "What is the result of this condition?\n```javascript\nlet x = 7, y = '7';\nif (x == y && x !== y) {\n  console.log('Tricky');\n}\n```",
        "options": ["Tricky", "Nothing", "Error", "undefined"],
        "answer": "Tricky",
        "difficulty": "Hard",
        "hint": "Loose equality (==) ignores type, but strict inequality (!==) checks it."
    },
    {
        "question": "What does this nested if output?\n```javascript\nlet num = 15;\nif (num > 10) {\n  if (num % 3 === 0) {\n    console.log('Divisible by 3');\n  }\n}\n```",
        "options": ["Divisible by 3", "Nothing", "Error", "undefined"],
        "answer": "Divisible by 3",
        "difficulty": "Medium",
        "hint": "Check if 15 satisfies both conditions."
    },
    {
        "question": "What is the output of this array code?\n```javascript\nlet arr = [0, 1, 2, 3];\nconsole.log(arr[arr.length - 1]);\n```",
        "options": ["0", "1", "2", "3"],
        "answer": "3",
        "difficulty": "Easy",
        "hint": "arr.length - 1 gives the last index."
    },
    {
        "question": "What does this array operation produce?\n```javascript\nlet nums = [1, 2];\nnums.push(...[3, 4]);\nconsole.log(nums);\n```",
        "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "[1, 2, [3, 4]]", "Error"],
        "answer": "[1, 2, 3, 4]",
        "difficulty": "Medium",
        "hint": "The spread operator (...) unpacks the array."
    },
    {
        "question": "What is the result of this splice operation?\n```javascript\nlet arr = ['a', 'b', 'c', 'd'];\narr.splice(1, 2, 'x', 'y');\nconsole.log(arr);\n```",
        "options": ["['a', 'x', 'y', 'd']", "['a', 'b', 'c']", "['x', 'y', 'd']", "Error"],
        "answer": "['a', 'x', 'y', 'd']",
        "difficulty": "Medium",
        "hint": "Splice removes and inserts elements at the specified index."
    },
    {
        "question": "What does this loop output?\n```javascript\nfor (let i = 1; i <= 4; i++) {\n  if (i % 2 === 0) console.log(i);\n}\n```",
        "options": ["1 3", "2 4", "1 2 3 4", "Nothing"],
        "answer": "2 4",
        "difficulty": "Easy",
        "hint": "Only even numbers are logged."
    },
    {
        "question": "What does this loop with break output?\n```javascript\nlet product = 1;\nfor (let i = 1; i <= 5; i++) {\n  if (i === 3) break;\n  product *= i;\n}\nconsole.log(product);\n```",
        "options": ["2", "6", "15", "120"],
        "answer": "2",
        "difficulty": "Medium",
        "hint": "The loop stops before i reaches 3."
    },
    {
        "question": "What does this nested loop output?\n```javascript\nlet result = '';\nfor (let i = 1; i <= 2; i++) {\n  for (let j = 1; j <= 2; j++) {\n    result += (i + j) + ' ';\n  }\n}\nconsole.log(result);\n```",
        "options": ["2 3 3 4", "1 2 3 4", "2 4 4 6", "Error"],
        "answer": "2 3 3 4",
        "difficulty": "Hard",
        "hint": "Calculate the sum of i and j for each iteration."
    },
    {
        "question": "What does this code output?\n```javascript\nlet text = 'javascript';\nconsole.log(text.toUpperCase().slice(-3));\n```",
        "options": ["IPT", "ipt", "JAV", "Error"],
        "answer": "IPT",
        "difficulty": "Medium",
        "hint": "Negative slice index counts from the end."
    },
    {
        "question": "What is the result of this string operation?\n```javascript\nlet str = 'Hello World!';\nconsole.log(str.length);\n```",
        "options": ["10", "11", "12", "13"],
        "answer": "12",
        "difficulty": "Easy",
        "hint": "Count all characters, including spaces and punctuation."
    },
    {
        "question": "What does this string method return?\n```javascript\nlet str = 'Find the needle';\nconsole.log(str.indexOf('not'));\n```",
        "options": ["-1", "0", "5", "8"],
        "answer": "-1",
        "difficulty": "Medium",
        "hint": "indexOf returns -1 if the substring is not found."
    },
    {
        "question": "What character is returned?\n```javascript\nlet str = 'Programming';\nconsole.log(str.charAt(str.length - 1));\n```",
        "options": ["g", "n", "i", "m"],
        "answer": "g",
        "difficulty": "Easy",
        "hint": "charAt with length - 1 gets the last character."
    },
    {
        "question": "What does this string replacement do?\n```javascript\nlet str = 'I code, you code';\nconsole.log(str.replace(/code/g, 'program'));\n```",
        "options": ["I program, you program", "I program, you code", "I code, you program", "Error"],
        "answer": "I program, you program",
        "difficulty": "Hard",
        "hint": "The /g flag replaces all occurrences."
    },
    {
        "question": "What is the result of this rounding?\n```javascript\nconsole.log(Math.round(-7.6));\n```",
        "options": ["-7", "-8", "-7.6", "Error"],
        "answer": "-8",
        "difficulty": "Medium",
        "hint": "Math.round rounds to the nearest integer."
    },
    {
        "question": "What does this random number code return?\n```javascript\nconsole.log(Math.floor(Math.random() * 6) + 1);\n```",
        "options": ["0 to 6", "1 to 6", "0 to 5", "1 to 5"],
        "answer": "1 to 6",
        "difficulty": "Easy",
        "hint": "Math.random() generates a number from 0 to <1."
    },
    {
        "question": "What does this parsing return?\n```javascript\nconsole.log(parseInt('-42.7'));\n```",
        "options": ["-42", "42", "NaN", "Error"],
        "answer": "-42",
        "difficulty": "Medium",
        "hint": "parseInt handles negative numbers."
    },
    {
        "question": "What is the output of this conversion?\n```javascript\nconsole.log(Number('12.34.56'));\n```",
        "options": ["12.34", "12.3456", "NaN", "Error"],
        "answer": "NaN",
        "difficulty": "Medium",
        "hint": "Number() expects a valid number string."
    },
    {
        "question": "What does this decimal control return?\n```javascript\nlet num = 9.87654;\nconsole.log(num.toFixed(2));\n```",
        "options": ["9.88", "9.87", "9.876", "9.9"],
        "answer": "9.88",
        "difficulty": "Easy",
        "hint": "toFixed rounds to the specified decimals."
    },
    {
        "question": "What does this strict comparison return?\n```javascript\nconsole.log(undefined === null);\n```",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "false",
        "difficulty": "Medium",
        "hint": "Strict comparison checks both value and type."
    },
    {
        "question": "What is the output of this code?\n```javascript\nlet x = '5';\nlet y = 5;\nconsole.log(x != y);\n```",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "false",
        "difficulty": "Easy",
        "hint": "Loose inequality ignores type."
    },
    {
        "question": "What does this array operation do?\n```javascript\nlet arr = [1, 2, 3];\narr.unshift(...[0, -1]);\nconsole.log(arr);\n```",
        "options": ["[0, -1, 1, 2, 3]", "[1, 2, 3, 0, -1]", "[0, -1]", "Error"],
        "answer": "[0, -1, 1, 2, 3]",
        "difficulty": "Medium",
        "hint": "unshift with spread adds elements to the start."
    },
    {
        "question": "What does this array method return?\n```javascript\nlet arr = ['x', 'y', 'z'];\nconsole.log(arr.pop());\n```",
        "options": ["x", "y", "z", "undefined"],
        "answer": "z",
        "difficulty": "Easy",
        "hint": "pop() removes and returns the last element."
    },
    {
        "question": "What is the array length after this operation?\n```javascript\nlet arr = [1, 2, 3, 4, 5];\narr.splice(1, 3);\nconsole.log(arr.length);\n```",
        "options": ["2", "3", "4", "5"],
        "answer": "2",
        "difficulty": "Medium",
        "hint": "splice removes elements and changes length."
    },
    {
        "question": "What does this boolean flag code output?\n```javascript\nlet found = false;\nlet arr = [1, 2, 3, 4];\nfor (let i = 0; i < arr.length; i++) {\n  if (arr[i] === 3) {\n    found = true;\n    break;\n  }\n}\nconsole.log(found);\n```",
        "options": ["true", "false", "3", "Error"],
        "answer": "true",
        "difficulty": "Medium",
        "hint": "The loop breaks when 3 is found."
    },
    {
        "question": "What does this string extraction return?\n```javascript\nlet str = 'JavaScript';\nconsole.log(str.slice(-4, -1));\n```",
        "options": ["rip", "ript", "Scri", "Java"],
        "answer": "rip",
        "difficulty": "Hard",
        "hint": "Negative indices count from the end."
    },
    {
        "question": "What does this case conversion output?\n```javascript\nlet str = 'javascript';\nconsole.log(str[0].toUpperCase() + str.slice(1, -1) + str.slice(-1).toUpperCase());\n```",
        "options": ["JavascriptT", "JAVASCRIPt", "JavascripT", "Error"],
        "answer": "JavascripT",
        "difficulty": "Hard",
        "hint": "Manipulate the first and last characters."
    },
    {
        "question": "What does this parse return?\n```javascript\nconsole.log(parseFloat('12.34abc45'));\n```",
        "options": ["12.34", "12.3445", "NaN", "Error"],
        "answer": "12.34",
        "difficulty": "Medium",
        "hint": "parseFloat stops at the first invalid character."
    },
    {
        "question": "What does this number-to-string conversion output?\n```javascript\nlet num = 255;\nconsole.log(num.toString(16));\n```",
        "options": ["'255'", "'ff'", "'100'", "Error"],
        "answer": "'ff'",
        "difficulty": "Hard",
        "hint": "toString(16) converts to hexadecimal."
    },
    {
        "question": "What does this floor operation return?\n```javascript\nconsole.log(Math.floor(5.999));\n```",
        "options": ["5", "6", "5.999", "Error"],
        "answer": "5",
        "difficulty": "Easy",
        "hint": "Math.floor rounds down to the nearest integer."
    },
    {
        "question": "What does this string method return?\n```javascript\nlet str = 'Hello World';\nconsole.log(str.substring(2, 5));\n```",
        "options": ["llo", "ll", "lo ", "Error"],
        "answer": "llo",
        "difficulty": "Easy",
        "hint": "substring extracts from start to end-1 index."
    },
    {
        "question": "What does this loop output?\n```javascript\nlet i = 0;\nwhile (i < 3) {\n  console.log(i++);\n}\n```",
        "options": ["0 1 2", "1 2 3", "0 1", "Error"],
        "answer": "0 1 2",
        "difficulty": "Easy",
        "hint": "i++ logs first, then increments."
    },
    {
        "question": "What does this type check return?\n```javascript\nconsole.log(typeof ('5' + 5));\n```",
        "options": ["number", "string", "object", "undefined"],
        "answer": "string",
        "difficulty": "Easy",
        "hint": "String + number results in a string."
    },
    {
        "question": "What does this loose comparison return?\n```javascript\nconsole.log(0 == '0');\n```",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true",
        "difficulty": "Medium",
        "hint": "Loose equality converts types."
    },
    {
        "question": "What does this string method return?\n```javascript\nlet str = 'JavaScript is fun';\nconsole.log(str.includes('Script'));\n```",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true",
        "difficulty": "Easy",
        "hint": "includes checks for a substring."
    },
    {
        "question": "What does this array slice return?\n```javascript\nlet arr = [1, 2, 3, 4, 5];\nconsole.log(arr.slice(-3));\n```",
        "options": ["[1, 2, 3]", "[3, 4, 5]", "[2, 3, 4]", "[4, 5]"],
        "answer": "[3, 4, 5]",
        "difficulty": "Medium",
        "hint": "Negative slice index starts from the end."
    },
    {
        "question": "What does this code output?\n```javascript\nlet str = 'JavaScript';\nconsole.log(str.replace(/a/g, '4').toUpperCase());\n```",
        "options": ["J4V4SCRIPT", "JAVA4SCRIPT", "J4VASCRIPT", "Error"],
        "answer": "J4V4SCRIPT",
        "difficulty": "Hard",
        "hint": "/g replaces all occurrences of 'a'."
    },
    {
        "question": "What does this random number code return?\n```javascript\nconsole.log(Math.ceil(Math.random() * 10));\n```",
        "options": ["0 to 10", "1 to 10", "0 to 9", "1 to 9"],
        "answer": "1 to 10",
        "difficulty": "Medium",
        "hint": "Math.ceil rounds up the random number."
    },
    {
        "question": "What is the output of this nested condition?\n```javascript\nlet x = 8;\nif (x > 5) {\n  if (x < 10) {\n    if (x % 2 === 0) {\n      console.log('Even and in range');\n    }\n  }\n}\n```",
        "options": ["Even and in range", "Nothing", "Error", "undefined"],
        "answer": "Even and in range",
        "difficulty": "Hard",
        "hint": "Check all nested conditions for x = 8."
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
    .hint {
        font-size: 13px;
        color: #b0b0d0;
        background: #2c2c54;
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
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

# Timer logic in Python
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
                    st.session_state.feedback = {'is_correct': is_correct, 'correct_answer': q['labeled_answer']}
                    st.session_state.answers[st.session_state.current_q] = {
                        'question': q['question'], 'user_answer': option, 'correct_answer': q['labeled_answer'], 
                        'is_correct': is_correct, 'difficulty': q['difficulty']
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

            # Hint
            with st.expander("💡 Show Hint"):
                st.markdown(f'<div class="hint">{q["hint"]}</div>', unsafe_allow_html=True)

            # Navigation
            col_prev, col_next = st.columns(2)
            with col_prev:
                if st.button("⬅ Previous", disabled=st.session_state.current_q == 0):
                    if st.session_state.answers[st.session_state.current_q] and st.session_state.answers[st.session_state.current_q]['is_correct']:
                        points = {'Easy': 1, 'Medium': 2, 'Hard': 3}[st.session_state.answers[st.session_state.current_q]['difficulty']]
                        st.session_state.score -= points
                    st.session_state.current_q -= 1
                    st.session_state.selected_option = None
                    st.session_state.feedback = None
                    st.rerun()
            with col_next:
                if st.session_state.current_q < len(quiz) - 1:
                    if st.button("➡️ Next", disabled=st.session_state.selected_option is None):
                        st.session_state.current_q += 1
                        st.session_state.selected_option = None
                        st.session_state.feedback = None
                        st.rerun()
                else:
                    if st.button("🏁 Finish", disabled=st.session_state.selected_option is None):
                        st.session_state.show_results = True
                        st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

    else:
        time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 1800)
        total_possible_score = sum({'Easy': 1, 'Medium': 2, 'Hard': 3}[q['difficulty']] for q in quiz)
        accuracy = (st.session_state.score / total_possible_score) * 100 if total_possible_score > 0 else 0
        st.markdown('<div class="question-container">', unsafe_allow_html=True)
        st.markdown(f'<h2 style="color: #34c759; text-align: center;">🏆 Score: {st.session_state.score}/{total_possible_score}</h2>', unsafe_allow_html=True)
        st.markdown(f"""
        <h3>📊 Results</h3>
        <div style="color: #b0b0d0; font-size: 15px;">
            - ⏱️ Time: {int(time_taken) // 60}m {int(time_taken) % 60}s<br>
            - 🎯 Accuracy: {accuracy:.1f}%<br>
            - ✅ Correct: {sum(1 for a in st.session_state.answers if a and a['is_correct'])}<br>
            - ❌ Wrong: {sum(1 for a in st.session_state.answers if a and not a['is_correct'])}
        </div>
        """, unsafe_allow_html=True)

        # Leaderboard
        leaderboard = [
            {"name": "Alex", "score": 45, "time": 600},
            {"name": "Sam", "score": 40, "time": 700},
            {"name": "You", "score": st.session_state.score, "time": int(time_taken)}
        ]
        leaderboard.sort(key=lambda x: (-x['score'], x['time']))
        st.markdown('<h3>🏅 Leaderboard</h3>', unsafe_allow_html=True)
        for i, entry in enumerate(leaderboard[:5], 1):
            st.markdown(f'<div style="color: #b0b0d0;">{i}. <b>{entry["name"]}</b>: {entry["score"]}/{total_possible_score} (Time: {entry["time"]//60}m {entry["time"]%60}s)</div>', unsafe_allow_html=True) ye qiuz work nhi kar raha 
