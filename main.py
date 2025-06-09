import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data (unchanged)
quiz = [
    {
        "question": "What is logged to the console when the user clicks 'Cancel'?\n```javascript\nlet result = prompt('Enter name');\nconsole.log(result);\n```",
        "options": ["null", "undefined", "'Cancel'", "''"],
        "answer": "null",
        "difficulty": "Medium",
        "explanation": "The `prompt()` function returns `null` when the user clicks 'Cancel'. This value is assigned to `result` and logged to the console.",
        "hint": "Consider what `prompt()` returns when no input is provided."
    },
    # ... (other questions unchanged, omitted for brevity)
]

# Cache shuffled quiz (unchanged)
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

# Initialize session state (unchanged)
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

# Theme toggle (unchanged)
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# Timer logic (unchanged)
def update_timer():
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.session_state.time_left = max(1800 - elapsed, 0)
    if st.session_state.time_left <= 0:
        st.session_state.show_results = True
        st.rerun()

# Reset quiz (unchanged)
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

# NEW: Progress snapshot function
def show_progress_snapshot():
    answered = sum(1 for ans in st.session_state.answers if ans is not None)
    st.markdown("""
        <div style='background: var(--bg-container); padding: 15px; border-radius: 10px; box-shadow: 0 4px 12px var(--shadow); margin: 10px 0;'>
            <h4 style='color: var(--text-color);'>📊 Progress Snapshot</h4>
            <div style='color: var(--text-color); font-size: 14px;'>
                - 🏆 Current Score: {score}<br>
                - 🔥 Streak: {streak}<br>
                - ✅ Questions Answered: {answered}/{total}
            </div>
        </div>
    """.format(
        score=st.session_state.score,
        streak=st.session_state.streak,
        answered=answered,
        total=len(st.session_state.quiz_data)
    ), unsafe_allow_html=True)

# CSS (unchanged)
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

# Main UI (unchanged)
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 JavaScript Quiz Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript Skills!</p>', unsafe_allow_html=True)

# Theme toggle button (unchanged)
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen (unchanged)
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
    # Timer (unchanged)
    if not st.session_state.show_results:
        update_timer()
        minutes = int(st.session_state.time_left // 60)
        seconds = int(st.session_state.time_left % 60)
        st.markdown(f'<div class="timer">⏰ Time Left: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

    if not st.session_state.quiz_data:
        st.error("No quiz questions available.")
    else:
        # Progress bar (unchanged)
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

                # Display difficulty and streak (unchanged)
                st.markdown(f'<div class="difficulty">Difficulty: {q["difficulty"]} | Streak: 🔥 {st.session_state.streak}</div>', unsafe_allow_html=True)

                # Split question into text and code (unchanged)
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

                # Option buttons (unchanged)
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

                # Feedback (unchanged)
                if st.session_state.feedback:
                    if st.session_state.feedback["is_correct"]:
                        st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="color: var(--text-color); font-size: 14px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                # Hint button (unchanged)
                if st.button("💡 Show Hint", key="hint", disabled=st.session_state.show_hint or st.session_state.selected_option is not None):
                    st.session_state.show_hint = True
                    st.session_state.score = max(0, st.session_state.score - 0.5)
                    st.rerun()
                if st.session_state.show_hint:
                    st.markdown(f'<div style="color: #facc15; font-size: 14px;">Hint: {q["hint"]}</div>', unsafe_allow_html=True)

                # CHANGED: Updated navigation (removed Previous and Skip, added Progress Snapshot)
                col1, col2 = st.columns(2)  # Now only two columns
                with col1:
                    if st.button("📊 Progress Snapshot", key="progress"):
                        show_progress_snapshot()
                with col2:
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

                # Reset quiz button (unchanged)
                if st.button("🔄 Reset Quiz", key="reset"):
                    reset_quiz()

                st.markdown("</div>", unsafe_allow_html=True)
