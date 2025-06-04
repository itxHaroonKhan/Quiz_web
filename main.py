import streamlit as st
import random
from datetime import datetime, timedelta

# Sample quiz with one coding question
quiz = [
    {
        "question": "What does this JavaScript code output?\n```javascript\nlet x = 0;\nfor (let i = 1; i <= 3; i++) {\n    x += i;\n}\nconsole.log(x);\n```",
        "options": ["3", "6", "9", "Error"],
        "answer": "6"
    },
    {
        "question": "What is the output of the following code?\n```javascript\nconsole.log(typeof null);\n```",
        "options": ["object", "null", "undefined", "boolean"],
        "answer": "object"
    },
    {
        "question": "Which of the following is NOT a primitive data type in JavaScript?",
        "options": ["String", "Number", "Object", "Boolean"],
        "answer": "Object"
    },
    {
        "question": "What will this code output?\n```javascript\nlet a;\nconsole.log(a);\n```",
        "options": ["null", "0", "undefined", "Error"],
        "answer": "undefined"
    },
    {
        "question": "Which method is used to parse a JSON string into a JavaScript object?",
        "options": ["JSON.parse()", "JSON.stringify()", "JSON.object()", "JSON.toObject()"],
        "answer": "JSON.parse()"
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
        'time_left': 1800,  # 30 minutes in seconds
        'last_update': datetime.now()
    })

# Update timer
current_time = datetime.now()
elapsed_time = (current_time - st.session_state.start_time).total_seconds()
st.session_state.time_left = max(0, 1800 - int(elapsed_time))

# Periodic rerun to update timer (every 1 second)
if (current_time - st.session_state.last_update).total_seconds() >= 1 and not st.session_state.show_results:
    st.session_state.last_update = current_time
    st.rerun()

# Check for time-up condition
if st.session_state.time_left <= 0:
    st.session_state.show_results = True

# Display timer
minutes = st.session_state.time_left // 60
seconds = st.session_state.time_left % 60
timer_display = f"⏰ Time Left: {minutes:02d}:{seconds:02d}" if st.session_state.time_left > 0 else "⏰ Time Up!"
st.markdown(f'<div class="timer">{timer_display}</div>', unsafe_allow_html=True)

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
    st.markdown('<hr style="border-color: #4b4b6b;">', unsafe_allow_html=True)
    st.markdown('<div style="color: #ffffff; font-size: 16px;">ℹ️ About</div>', unsafe_allow_html=True)
    st.markdown('<div style="color: #b0b0d0; font-size: 13px;">JS Quiz Pro tests JavaScript skills with code-based questions.</div>', unsafe_allow_html=True)
