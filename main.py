import streamlit as st
import random
from datetime import datetime

# Quiz data with hints removed
quiz = [
    {
        "question": "What is the output of this code?\n```javascript\nlet name = 'Sara';\nconsole.log(name + 'h');\n```",
        "options": ["Sarah", "Sara h", "Sarh", "Error"],
        "answer": "Sarah",
        "difficulty": "Easy"
    },
    {
        "question": "What is the result of this operation?\n```javascript\nlet num = 8;\nconsole.log(num * 3);\n```",
        "options": ["24", "11", "NaN", "Error"],
        "answer": "24",
        "difficulty": "Easy"
    },
    {
        "question": "Which variable name is illegal?\n```javascript\nlet 1stPlace = 'Gold';\n```",
        "options": ["firstPlace", "_1stPlace", "1stPlace", "$place"],
        "answer": "1stPlace",
        "difficulty": "Easy"
    },
    {
        "question": "What is the output of this expression?\n```javascript\nconsole.log(5 + 4 * 2);\n```",
        "options": ["18", "13", "9", "10"],
        "answer": "13",
        "difficulty": "Medium"
    },
    {
        "question": "What does the ** operator do?\n```javascript\nconsole.log(2 ** 3);\n```",
        "options": ["6", "8", "9", "Error"],
        "answer": "8",
        "difficulty": "Easy"
    },
    {
        "question": "What is the output of this expression?\n```javascript\nconsole.log((3 + 2) * (4 - 1));\n```",
        "options": ["15", "10", "12", "9"],
        "answer": "15",
        "difficulty": "Medium"
    },
    {
        "question": "What does this concatenation produce?\n```javascript\nlet str = 'Test' + 2 * 2 + 'Case';\nconsole.log(str);\n```",
        "options": ["Test4Case", "Test22Case", "Test2Case", "Error"],
        "answer": "Test4Case",
        "difficulty": "Medium"
    },
    {
        "question": "What does this comparison return?\n```javascript\nconsole.log(5 === '5');\n```",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "false",
        "difficulty": "Easy"
    },
    {
        "question": "What is the output of this code?\n```javascript\nlet marks = 75;\nif (marks >= 80) {\n  console.log('A');\n} else if (marks >= 70) {\n  console.log('B');\n} else {\n  console.log('C');\n}\n```",
        "options": ["A", "B", "C", "Error"],
        "answer": "B",
        "difficulty": "Easy"
    },
    {
        "question": "What does this condition return?\n```javascript\nlet a = 10, b = '10';\nif (a == b && a !== b) {\n  console.log('Equal');\n}\n```",
        "options": ["Equal", "Nothing", "Error", "undefined"],
        "answer": "Equal",
        "difficulty": "Hard"
    },
    {
        "question": "What does this nested if output?\n```javascript\nlet num = 12;\nif (num > 10) {\n  if (num % 2 === 0) {\n    console.log('Even');\n  }\n}\n```",
        "options": ["Even", "Nothing", "Error", "undefined"],
        "answer": "Even",
        "difficulty": "Medium"
    },
    {
        "question": "What is the output of this array code?\n```javascript\nlet arr = [1, 2, 3];\nconsole.log(arr[2]);\n```",
        "options": ["1", "2", "3", "undefined"],
        "answer": "3",
        "difficulty": "Easy"
    },
    {
        "question": "What does this array operation produce?\n```javascript\nlet nums = [4, 5];\nnums.push(6, 7);\nconsole.log(nums);\n```",
        "options": ["[4, 5, 6]", "[4, 5, 6, 7]", "[6, 7, 4, 5]", "Error"],
        "answer": "[4, 5, 6, 7]",
        "difficulty": "Medium"
    },
    {
        "question": "What is the result of this splice operation?\n```javascript\nlet arr = ['p', 'q', 'r', 's'];\narr.splice(1, 1, 'x');\nconsole.log(arr);\n```",
        "options": ["['p', 'x', 'r', 's']", "['p', 'q', 'r']", "['x', 'r', 's']", "Error"],
        "answer": "['p', 'x', 'r', 's']",
        "difficulty": "Medium"
    },
    {
        "question": "What does this loop output?\n```javascript\nfor (let i = 1; i <= 5; i++) {\n  if (i % 2 !== 0) console.log(i);\n}\n```",
        "options": ["1 3 5", "2 4", "1 2 3 4 5", "Nothing"],
        "answer": "1 3 5",
        "difficulty": "Easy"
    },
    {
        "question": "What does this loop with break output?\n```javascript\nlet sum = 0;\nfor (let i = 1; i <= 4; i++) {\n  if (i === 3) break;\n  sum += i;\n}\nconsole.log(sum);\n```",
        "options": ["3", "6", "10", "1"],
        "answer": "3",
        "difficulty": "Medium"
    },
    {
        "question": "What does this nested loop output?\n```javascript\nlet output = '';\nfor (let i = 1; i <= 2; i++) {\n  for (let j = 1; j <= 2; j++) {\n    output += (i * j) + ' ';\n  }\n}\nconsole.log(output);\n```",
        "options": ["1 2 2 4", "1 2 3 4", "2 4 4 8", "Error"],
        "answer": "1 2 2 4",
        "difficulty": "Hard"
    },
    {
        "question": "What does this case conversion output?\n```javascript\nlet str = 'hello';\nconsole.log(str.toUpperCase());\n```",
        "options": ["HELLO", "hello", "Hello", "Error"],
        "answer": "HELLO",
        "difficulty": "Easy"
    },
    {
        "question": "What is the length of this string?\n```javascript\nlet str = 'Coding!';\nconsole.log(str.length);\n```",
        "options": ["6", "7", "8", "Error"],
        "answer": "7",
        "difficulty": "Easy"
    },
    {
        "question": "What does this string method return?\n```javascript\nlet str = 'Find the key';\nconsole.log(str.indexOf('key'));\n```",
        "options": ["-1", "9", "0", "5"],
        "answer": "9",
        "difficulty": "Medium"
    },
    {
        "question": "What character is returned?\n```javascript\nlet str = 'Script';\nconsole.log(str.charAt(2));\n```",
        "options": ["S", "r", "i", "p"],
        "answer": "r",
        "difficulty": "Easy"
    },
    {
        "question": "What does this string replacement do?\n```javascript\nlet str = 'cat and dog';\nconsole.log(str.replace('cat', 'rat'));\n```",
        "options": ["rat and dog", "cat and rat", "rat and rat", "Error"],
        "answer": "rat and dog",
        "difficulty": "Medium"
    },
    {
        "question": "What is the result of this rounding?\n```javascript\nconsole.log(Math.round(4.6));\n```",
        "options": ["4", "5", "4.6", "Error"],
        "answer": "5",
        "difficulty": "Easy"
    },
    {
        "question": "What does this random number code return?\n```javascript\nconsole.log(Math.floor(Math.random() * 5) + 1);\n```",
        "options": ["0 to 5", "1 to 5", "0 to 4", "1 to 4"],
        "answer": "1 to 5",
        "difficulty": "Medium"
    },
    {
        "question": "What does this parsing return?\n```javascript\nconsole.log(parseInt('123.45'));\n```",
        "options": ["123", "123.45", "NaN", "Error"],
        "answer": "123",
        "difficulty": "Medium"
    },
    {
        "question": "What does this conversion output?\n```javascript\nlet num = 42;\nconsole.log(num.toString());\n```",
        "options": ["'42'", "42", "NaN", "Error"],
        "answer": "'42'",
        "difficulty": "Easy"
    },
    {
        "question": "What does this decimal control return?\n```javascript\nlet num = 7.12345;\nconsole.log(num.toFixed(3));\n```",
        "options": ["7.123", "7.12", "7.1234", "7.1"],
        "answer": "7.123",
        "difficulty": "Easy"
    },
    {
        "question": "What does this function return?\n```javascript\nfunction add(a, b) {\n  return a + b;\n}\nconsole.log(add(3, 4));\n```",
        "options": ["7", "34", "Error", "undefined"],
        "answer": "7",
        "difficulty": "Easy"
    },
    {
        "question": "What does this function with parameters output?\n```javascript\nfunction greet(name) {\n  return 'Hello ' + name;\n}\nconsole.log(greet('Ali'));\n```",
        "options": ["Hello Ali", "Hello", "Ali", "Error"],
        "answer": "Hello Ali",
        "difficulty": "Easy"
    },
    {
        "question": "What does this date operation return?\n```javascript\nlet date = new Date('2023-06-05');\nconsole.log(date.getFullYear());\n```",
        "options": ["2023", "6", "5", "Error"],
        "answer": "2023",
        "difficulty": "Medium"
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
            st.markdown(f'<div style="color: #b0b0d0;">{i}. <b>{entry["name"]}</b>: {entry["score"]}/{total_possible_score} (Time: {entry["time"]//60}m {entry["time"]%60}s)</div>', unsafe_allow_html=True)
