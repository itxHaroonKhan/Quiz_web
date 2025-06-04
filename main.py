import streamlit as st
import random
from datetime import datetime

# Sample quiz with one coding question
quiz = [
  {
    "question": "What happens when this alert is executed?\n```javascript\nalert('Hello\\nWorld');\n```",
    "options": ["Displays 'Hello World'", "Displays 'Hello' and 'World' on two lines", "Throws an error", "Displays 'Hello\\nWorld'"],
    "answer": "Displays 'Hello' and 'World' on two lines"
  },
  {
    "question": "What is the output of this code?\n```javascript\nlet name = 'Ali';\nalert(name + 42);\n```",
    "options": ["Ali42", "NaN", "Error", "42Ali"],
    "answer": "Ali42"
  },
  {
    "question": "What will this code output?\n```javascript\nlet num = 10.5;\nconsole.log(num * 2);\n```",
    "options": ["21", "20", "10.5", "NaN"],
    "answer": "21"
  },
  {
    "question": "Which variable name is illegal?\n```javascript\nlet my-variable = 10;\n```",
    "options": ["my_variable", "myVariable", "my-variable", "_variable"],
    "answer": "my-variable"
  },
  {
    "question": "What is the result of this expression?\n```javascript\nconsole.log(10 - 3 * 2 + 4);\n```",
    "options": ["8", "16", "20", "5"],
    "answer": "8"
  },
  {
    "question": "What does the ** operator do in this code?\n```javascript\nconsole.log(2 ** 3);\n```",
    "options": ["6", "8", "9", "Error"],
    "answer": "8"
  },
  {
    "question": "What is the output of this code?\n```javascript\nconsole.log(2 * (3 + 4) / 2);\n```",
    "options": ["7", "14", "5", "10"],
    "answer": "7"
  },
  {
    "question": "What does this concatenation produce?\n```javascript\nlet str = 'Code' + 2 + 'Run';\nconsole.log(str);\n```",
    "options": ["Code2Run", "CodeRun", "Error", "NaN"],
    "answer": "Code2Run"
  },
  {
    "question": "What does this prompt return if the user enters nothing and clicks OK?\n```javascript\nlet input = prompt('Enter something:');\nconsole.log(input);\n```",
    "options": ["null", "undefined", "'' (empty string)", "Error"],
    "answer": "'' (empty string)"
  },
  {
    "question": "What will this code output?\n```javascript\nlet x = 0;\nif (x || x === 0) {\n  console.log('Zero');\n}\n```",
    "options": ["Zero", "Nothing", "undefined", "Error"],
    "answer": "Zero"
  },
  {
    "question": "What does this comparison return?\n```javascript\nconsole.log('10' === 10);\n```",
    "options": ["true", "false", "undefined", "Error"],
    "answer": "false"
  },
  {
    "question": "What is the output of this code?\n```javascript\nlet score = 75;\nif (score >= 90) {\n  console.log('A');\n} else if (score >= 70) {\n  console.log('B');\n} else {\n  console.log('C');\n}\n```",
    "options": ["A", "B", "C", "Nothing"],
    "answer": "B"
  },
  {
    "question": "What is the result of this condition?\n```javascript\nlet a = 5, b = 10;\nif (a > 3 && b < 15) {\n  console.log('Both true');\n}\n```",
    "options": ["Both true", "Nothing", "Error", "undefined"],
    "answer": "Both true"
  },
  {
    "question": "What does this nested if output?\n```javascript\nlet num = 12;\nif (num > 10) {\n  if (num % 2 === 0) {\n    console.log('Even and greater than 10');\n  }\n}\n```",
    "options": ["Even and greater than 10", "Nothing", "Error", "undefined"],
    "answer": "Even and greater than 10"
  },
  {
    "question": "What is the output of this array code?\n```javascript\nlet arr = [1, 2, 3];\nconsole.log(arr[2]);\n```",
    "options": ["1", "2", "3", "undefined"],
    "answer": "3"
  },
  {
    "question": "What does this array operation produce?\n```javascript\nlet nums = [1, 2];\nnums.push(3, 4);\nconsole.log(nums);\n```",
    "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "[3, 4]", "Error"],
    "answer": "[1, 2, 3, 4]"
  },
  {
    "question": "What is the result of this splice operation?\n```javascript\nlet arr = ['a', 'b', 'c', 'd'];\narr.splice(1, 2, 'x');\nconsole.log(arr);\n```",
    "options": ["['a', 'x', 'd']", "['a', 'b', 'c']", "['x', 'd']", "Error"],
    "answer": "['a', 'x', 'd']"
  },
  {
    "question": "What does this loop output?\n```javascript\nfor (let i = 1; i <= 3; i++) {\n  console.log(i * i);\n}\n```",
    "options": ["1 4 9", "1 2 3", "3 6 9", "Error"],
    "answer": "1 4 9"
  },
  {
    "question": "What does this loop with break output?\n```javascript\nlet sum = 0;\nfor (let i = 1; i <= 5; i++) {\n  if (i === 4) break;\n  sum += i;\n}\nconsole.log(sum);\n```",
    "options": ["6", "10", "15", "3"],
    "answer": "6"
  },
  {
    "question": "What does this nested loop output?\n```javascript\nlet str = '';\nfor (let i = 1; i <= 2; i++) {\n  for (let j = 1; j <= 2; j++) {\n    str += i * j + ' ';\n  }\n}\nconsole.log(str);\n```",
    "options": ["1 2 2 4", "1 2 3 4", "2 4 6 8", "Error"],
    "answer": "1 2 2 4"
  },
  {
    "question": "What does this code output?\n```javascript\nlet text = 'javascript';\nconsole.log(text.toUpperCase().slice(0, 4));\n```",
    "options": ["JAVA", "java", "JAVAS", "Error"],
    "answer": "JAVA"
  },
  {
    "question": "What is the result of this string operation?\n```javascript\nlet str = 'Hello World';\nconsole.log(str.length);\n```",
    "options": ["10", "11", "12", "9"],
    "answer": "11"
  },
  {
    "question": "What does this string method return?\n```javascript\nlet str = 'Find the needle';\nconsole.log(str.indexOf('needle'));\n```",
    "options": ["9", "10", "11", "-1"],
    "answer": "10"
  },
  {
    "question": "What character is returned?\n```javascript\nlet str = 'Programming';\nconsole.log(str.charAt(3));\n```",
    "options": ["g", "r", "o", "p"],
    "answer": "g"
  },
  {
    "question": "What does this string replacement do?\n```javascript\nlet str = 'I like to code';\nconsole.log(str.replace('code', 'program'));\n```",
    "options": ["I like to program", "I like to code", "Error", "undefined"],
    "answer": "I like to program"
  },
  {
    "question": "What is the result of this rounding?\n```javascript\nconsole.log(Math.round(7.49));\n```",
    "options": ["7", "8", "7.5", "Error"],
    "answer": "7"
  },
  {
    "question": "What does this random number code return?\n```javascript\nconsole.log(Math.floor(Math.random() * 5));\n```",
    "options": ["0 to 4", "1 to 5", "0 to 5", "1 to 4"],
    "answer": "0 to 4"
  },
  {
    "question": "What does this parsing return?\n```javascript\nconsole.log(parseInt('42px'));\n```",
    "options": ["42", "NaN", "Error", "42px"],
    "answer": "42"
  },
  {
    "question": "What is the output of this conversion?\n```javascript\nconsole.log(Number('123.45'));\n```",
    "options": ["123", "123.45", "NaN", "Error"],
    "answer": "123.45"
  },
  {
    "question": "What does this decimal control return?\n```javascript\nlet num = 9.87654;\nconsole.log(num.toFixed(3));\n```",
    "options": ["9.876", "9.877", "9.88", "9.87"],
    "answer": "9.877"
  },
  {
    "question": "What does this strict comparison return?\n```javascript\nconsole.log(0 === false);\n```",
    "options": ["true", "false", "undefined", "Error"],
    "answer": "false"
  },
  {
    "question": "What is the output of this code?\n```javascript\nlet x = '10';\nlet y = 10;\nconsole.log(x !== y);\n```",
    "options": ["true", "false", "undefined", "Error"],
    "answer": "true"
  },
  {
    "question": "What does this array operation do?\n```javascript\nlet arr = [1, 2, 3];\narr.unshift(0);\nconsole.log(arr);\n```",
    "options": ["[0, 1, 2, 3]", "[1, 2, 3, 0]", "[0, 2, 3]", "Error"],
    "answer": "[0, 1, 2, 3]"
  },
  {
    "question": "What does this array method return?\n```javascript\nlet arr = ['a', 'b', 'c'];\nconsole.log(arr.shift());\n```",
    "options": ["a", "b", "c", "undefined"],
    "answer": "a"
  },
  {
    "question": "What is the array length after this operation?\n```javascript\nlet arr = [1, 2, 3, 4];\narr.pop();\nconsole.log(arr.length);\n```",
    "options": ["3", "4", "2", "1"],
    "answer": "3"
  },
  {
    "question": "What does this boolean flag code output?\n```javascript\nlet flag = true;\nfor (let i = 0; i < 3; i++) {\n  if (!flag) break;\n  console.log(i);\n  flag = false;\n}\n```",
    "options": ["0", "0 1 2", "0 1", "Error"],
    "answer": "0"
  },
  {
    "question": "What does this string extraction return?\n```javascript\nlet str = 'JavaScript';\nconsole.log(str.slice(4, 7));\n```",
    "options": ["Scr", "Scri", "ipt", "Java"],
    "answer": "Scr"
  },
  {
    "question": "What does this case conversion output?\n```javascript\nlet str = 'HELLO';\nconsole.log(str[0].toLowerCase() + str.slice(1));\n```",
    "options": ["hELLO", "HELLO", "hello", "error"],
    "answer": "hELLO"
  },
  {
    "question": "What does this parse return?\n```javascript\nconsole.log(parseFloat('12.34.56'));\n```",
    "options": ["12.34", "12.3456", "NaN", "Error"],
    "answer": "12.34"
  },
  {
    "question "question": "What does this number-to-string conversion output?\n```javascript\nlet num = 100;\nconsole.log(num.toString(2));\n```",
    "options": ["'100'", "'64'", "'1100100'", "Error"],
    "answer": "'1100100'"
  },
  {
    "question": "What does this floor operation return?\n```javascript\nconsole.log(Math.floor(-3.7));\n```",
    "options": ["-3", "-4", "-3.7", "Error"],
    "answer": "-4"
  },
  {
    "question": "What does this string method return?\n```javascript\nlet str = 'Hello World';\nconsole.log(str.substring(6));\n```",
    "options": ["World", "Hello", "rld", "Error"],
    "answer": "World"
  },
  {
    "question": "What does this loop output?\n```javascript\ndo {\n  console.log('Run');\n} while (false);\n```",
    "options": ["Run", "Nothing", "Error", "undefined"],
    "answer": "Run"
  },
  {
    "question": "What does this type check return?\n```javascript\nconsole.log(typeof (10 + '5'));\n```",
    "options": ["number", "string", "object", "undefined"],
    "answer": "string"
  },
  {
    "question": "What does this loose comparison return?\n```javascript\nconsole.log(null == undefined);\n```",
    "options": ["true", "false", "undefined", "Error"],
    "answer": "true"
  },
  {
    "question": "What does this string method return?\n```javascript\nlet str = 'Hello World';\nconsole.log(str.includes('lo W'));\n```",
    "options": ["true", "false", "undefined", "Error"],
    "answer": "true"
  },
  {
    "question": "What does this array slice return?\n```javascript\nlet arr = [1, 2, 3, 4];\nconsole.log(arr.slice(1, 3));\n```",
    "options": ["[1, 2]", "[2, 3]", "[1, 2, 3]", "[2, 3, 4]"],
    "answer": "[2, 3]"
  },
  {
    "question": "What does this code output?\n```javascript\nlet str = 'JavaScript';\nconsole.log(str.replace('a', '4').replace('S', '5'));\n```",
    "options": ["J4v4Script", "J4va5cript", "JavaScript", "Error"],
    "answer": "J4va5cript"
  },
  {
    "question": "What does this random number code return?\n```javascript\nconsole.log(Math.floor(Math.random() * 10) + 1);\n```",
    "options": ["0 to 10", "1 to 10", "0 to 9", "1 to 9"],
    "answer": "1 to 10"
  },
  {
    "question": "What is the output of this nested condition?\n```javascript\nlet x = 5;\nif (x > 0) {\n  if (x < 10) {\n    if (x % 2 === 1) {\n      console.log('Odd and small');\n    }\n  }\n}\n```",
    "options": ["Odd and small", "Nothing", "Error", "undefined"],
    "answer": "Odd and small"
  }
];

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

# CSS for VS Code-like code block and UI
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
        max-width: 800px;
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
    .progress-container {
        text-align: center;
        margin-bottom: 15px;
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
        font-size: 14px;
        color: #ff6b6b;
        font-weight: 600;
        text-align: center;
        margin-top: 10px;
    }
    .stCodeBlock {
        background-color: #1e1e1e !important;
        border-radius: 8px;
        padding: 10px;
        font-family: 'Consolas', 'Monaco', monospace;
        font-size: 14px;
        line-height: 1.5;
    }
    .stCodeBlock pre, .stCodeBlock code {
        color: #d4d4d4;
    }
    .stCodeBlock .hljs-keyword { color: #569cd6; }
    .stCodeBlock .hljs-string { color: #ce9178; }
    .stCodeBlock .hljs-number { color: #b5cea8; }
    .stCodeBlock .hljs-comment { color: #6a9955; }
    .stCodeBlock .hljs-operator, .stCodeBlock .hljs-punctuation { color: #d4d4d4; }
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

# Live timer using JavaScript in st.markdown
timer_html = f"""
<div id="timer" class="timer">⏰ Time Left: 30:00</div>
<script>
    let timeLeft = {st.session_state.time_left};
    const timerElement = document.getElementById('timer');
    function updateTimer() {{
        if (timeLeft <= 0) {{
            timerElement.innerHTML = '⏰ Time Up!';
            // Signal time-up to Python via form submission
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '';
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'time_up';
            input.value = 'true';
            form.appendChild(input);
            document.body.appendChild(form);
            form.submit();
            return;
        }}
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        timerElement.innerHTML = `⏰ Time Left: ${{minutes.toString().padStart(2, '0')}}:${{seconds.toString().padStart(2, '0')}}`;
        timeLeft--;
        setTimeout(updateTimer, 1000);
    }}
    updateTimer();
</script>
"""
st.markdown(timer_html, unsafe_allow_html=True)

# Check for time-up via query params
if st.query_params.get('time_up', 'false') == 'true':
    st.session_state.show_results = True
    st.query_params.clear()

# Fallback: Check elapsed time since start
elapsed_time = (datetime.now() - st.session_state.start_time).total_seconds()
if elapsed_time >= 1800:
    st.session_state.show_results = True

# Main UI
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 JavaScript Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Test Your JavaScript Knowledge</p>', unsafe_allow_html=True)

if not st.session_state.quiz_data:
    st.error("No quiz questions available. Please add questions to start the quiz.")
else:
    progress = st.session_state.current_q / len(st.session_state.quiz_data)
    progress_percentage = int(progress * 100)
    progress_svg = f"""
    <div class="progress-container">
        <svg width="80" height="80" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="40" stroke="#4b4b6b" stroke-width="8" fill="none"/>
            <circle cx="50" cy="50" r="40" stroke="#6b21a8" stroke-width="8" fill="none"
                stroke-dasharray="251" stroke-dashoffset="{251 * (1 - progress)}"/>
            <text x="50" y="55" fill="#ffffff" font-size="18" text-anchor="middle">{progress_percentage}%</text>
        </svg>
        <div style="color: #b0b0d0; font-size: 13px; margin-top: 8px;">
            Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
        </div>
    </div>
    """
    st.markdown(progress_svg, unsafe_allow_html=True)

    if not st.session_state.show_results:
        with st.container():
            st.markdown('<div class="question-container">', unsafe_allow_html=True)
            q = st.session_state.quiz_data[st.session_state.current_q]
            
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

            for i, option in enumerate(q['display_options']):
                if st.button(option, key=f"q{i}", disabled=st.session_state.selected_option is not None):
                    original_option = option[3:]
                    is_correct = option == q['labeled_answer']
                    st.session_state.selected_option = option
                    st.session_state.feedback = {'is_correct': is_correct, 'correct_answer': q['labeled_answer']}
                    st.session_state.answers[st.session_state.current_q] = {
                        'question': q['question'], 'user_answer': option, 'correct_answer': q['labeled_answer'], 'is_correct': is_correct
                    }
                    if is_correct:
                        st.session_state.score += 1
                    st.rerun()

            if st.session_state.feedback:
                if st.session_state.feedback['is_correct']:
                    st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)

            col_prev, col_next = st.columns(2)
            with col_prev:
                if st.button("⬅ Previous", disabled=st.session_state.current_q == 0):
                    if st.session_state.answers[st.session_state.current_q] and st.session_state.answers[st.session_state.current_q]['is_correct']:
                        st.session_state.score -= 1
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
        accuracy = (st.session_state.score / len(quiz)) * 100 if quiz else 0
        st.markdown('<div class="question-container">', unsafe_allow_html=True)
        st.markdown(f'<h2 style="color: #34c759; text-align: center;">🏆 Score: {st.session_state.score}/{len(quiz)}</h2>', unsafe_allow_html=True)
        st.markdown(f"""
        <h3>📊 Results</h3>
        <div style="color: #b0b0d0; font-size: 15px;">
            - ⏱️ Time: {int(time_taken) // 60}m {int(time_taken) % 60}s<br>
            - 🎯 Accuracy: {accuracy:.1f}%<br>
            - ✅ Correct: {st.session_state.score}<br>
            - ❌ Wrong: {len(quiz) - st.session_state.score}
        </div>
        """, unsafe_allow_html=True)

        leaderboard = [
            {"name": "Alex", "score": 8, "time": 180},
            {"name": "Sam", "score": 7, "time": 200},
            {"name": "You", "score": st.session_state.score, "time": int(time_taken)}
        ]
        leaderboard.sort(key=lambda x: (-x['score'], x['time']))
        st.markdown('<h3>🏅 Leaderboard</h3>', unsafe_allow_html=True)
        for i, entry in enumerate(leaderboard[:5], 1):
            st.markdown(f'<div style="color: #b0b0d0;">{i}. <b>{entry["name"]}</b>: {entry["score"]}/{len(quiz)} (Time: {entry["time"]//60}m {entry["time"]%60}s)</div>', unsafe_allow_html=True)

        with st.expander("📝 Review", expanded=True):
            for i, answer in enumerate(st.session_state.answers):
                if answer:
                    if "```javascript" in answer["question"]:
                        question_parts = answer["question"].split("```javascript\n")
                        question_text = question_parts[0].strip()
                        code_snippet = question_parts[1].split("```")[0].strip()
                        st.markdown(f'<b style="color: #ffffff;">Q{i+1}:</b> {question_text}', unsafe_allow_html=True)
                        st.code(code_snippet, language="javascript")
                    else:
                        st.markdown(f'<b style="color: #ffffff;">Q{i+1}:</b> {answer["question"]}', unsafe_allow_html=True)
                    col1, col2 = st.columns(2)
                    with col1:
                        status = "✅" if answer['is_correct'] else "❌"
                        st.markdown(f'<span style="color: #b0b0d0;">{status} Your: {answer["user_answer"]}</span>', unsafe_allow_html=True)
                    with col2:
                        if not answer['is_correct']:
                            st.markdown(f'<span style="color: #b0b0d0;">Correct: {answer["correct_answer"]}</span>', unsafe_allow_html=True)
                    st.markdown('<hr style="border-color: #4b4b6b;">', unsafe_allow_html=True)

        col_restart, col_share = st.columns(2)
        with col_restart:
            if st.button("🔄 Try Again", type="primary"):
                st.session_state.clear()
                st.rerun()
        with col_share:
            if st.button("📤 Share Score"):
                share_text = f"Scored {st.session_state.score}/{len(quiz)} ({accuracy:.1f}%) on JS Quiz Pro!"
                st.code(share_text, language="text")

        st.markdown('</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div style="color: #ffffff; font-size: 22px;">📚 Quiz Info</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color: #b0b0d0;">Questions: {len(quiz)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color: #b0b0d0;">Score: {st.session_state.score}/{len(quiz)}</div>', unsafe_allow_html=True)
    if not st.session_state.show_results:
        st.markdown(f'<div style="color: #b0b0d0;">Timer above ⬆️</div>', unsafe_allow_html=True)
    else:
        time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 1800)
        st.markdown(f'<div style="color: #b0b0d0;">Time: {int(time_taken) // 60}m {int(time_taken) % 60}s</div>', unsafe_allow_html=True)
