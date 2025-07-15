import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 30 DOM-related questions
quiz = [
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
        "question": "How do you measure the length of a string in JavaScript?",
        "options": [
            "str.length",
            "str.size()",
            "str.len()",
            "str.count()"
        ],
        "answer": "str.length",
        "difficulty": "Easy",
        "explanation": "The `length` property returns the number of characters in a string."
    },
    # ... (include all your remaining quiz questions here)
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

# Enhanced CSS
st.markdown("""
    <style>
    :root {
        --primary: #6b21a8;
        --primary-light: #a855f7;
        --secondary: #f3e8ff;
        --text: #1f2937;
        --text-light: #6b7280;
        --bg: #ffffff;
        --card-bg: #f9fafb;
        --correct: #34c759;
        --wrong: #ff3b30;
        --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    [data-theme="dark"] {
        --primary: #8b5cf6;
        --primary-light: #c084fc;
        --secondary: #2c2c54;
        --text: #f3f4f6;
        --text-light: #d1d5db;
        --bg: #1a1a3b;
        --card-bg: #2c2c54;
        --correct: #4ade80;
        --wrong: #f87171;
        --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }

    .main-container {
        background: var(--bg);
        color: var(--text);
        min-height: 100vh;
        padding: 2rem 1rem;
        transition: all 0.3s ease;
    }

    .title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(45deg, var(--primary), var(--primary-light));
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .caption {
        font-size: 1.1rem;
        color: var(--text-light);
        text-align: center;
        margin-bottom: 2rem;
    }

    .stButton>button {
        background: linear-gradient(45deg, var(--primary), var(--primary-light));
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: var(--shadow);
        width: 100%;
        margin: 0.5rem 0;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }

    .stButton>button:disabled {
        background: #9ca3af;
        transform: none;
        cursor: not-allowed;
    }

    .question-container {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: var(--shadow);
        transition: all 0.3s ease;
    }

    .difficulty {
        font-size: 0.9rem;
        color: var(--text-light);
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .feedback-correct {
        color: var(--correct);
        font-weight: 600;
        font-size: 1.1rem;
        margin: 1rem 0;
        animation: fadeIn 0.5s ease;
    }

    .feedback-wrong {
        color: var(--wrong);
        font-weight: 600;
        font-size: 1.1rem;
        margin: 1rem 0;
        animation: fadeIn 0.5s ease;
    }

    .progress-container {
        margin: 1.5rem 0;
    }

    .progress-bar {
        background: #e5e7eb;
        border-radius: 12px;
        height: 8px;
        overflow: hidden;
        position: relative;
    }

    .progress-fill {
        background: linear-gradient(45deg, var(--primary), var(--primary-light));
        height: 100%;
        border-radius: 12px;
        transition: width 0.5s ease;
    }

    .progress-text {
        position: absolute;
        top: -22px;
        right: 0;
        color: var(--text);
        font-size: 0.8rem;
    }

    .timer {
        font-size: 1rem;
        color: var(--primary-light);
        font-weight: 600;
        text-align: center;
        margin: 1rem 0;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }

    .results-container {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: var(--shadow);
    }

    .score-display {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 1.5rem;
        background: linear-gradient(45deg, var(--primary), var(--primary-light));
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        margin-bottom: 2rem;
    }

    .stat-item {
        background: rgba(168, 85, 247, 0.1);
        padding: 1rem;
        border-radius: 12px;
        text-align: center;
    }

    .selected-correct {
        background: var(--correct) !important;
        color: white !important;
        animation: pulse 0.5s ease;
    }

    .selected-wrong {
        background: var(--wrong) !important;
        color: white !important;
        animation: pulse 0.5s ease;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    @media (max-width: 768px) {
        .title {
            font-size: 2rem;
        }
        .stats-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Main UI
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 DOM Mastery Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript DOM Skills!</p>', unsafe_allow_html=True)

# Theme toggle button
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen
if not st.session_state.started:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: var(--text); font-size: 18px;">Test your DOM skills with 30 comprehensive questions!</p>
        <p style="color: var(--text-light);">60 minutes, 2 points per correct answer. Ready?</p>
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
            <div style="color: var(--text); font-size: 13px; text-align: center;">
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
                if "```javascript" in q["question"] or "```html" in q["question"]:
                    if "```javascript" in q["question"]:
                        language = "javascript"
                        question_parts = q["question"].split("```javascript\n")
                    else:
                        language = "html"
                        question_parts = q["question"].split("```html\n")
                    
                    question_text = question_parts[0].strip()
                    code_snippet = question_parts[1].split("```")[0].strip()
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{question_text}**")
                    st.code(code_snippet, language=language)
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
                        # Automatically move to next question or show results
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
                        st.markdown(f'<div style="color: var(--text); font-size: 14px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

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
                <div style="font-size: 1.2rem; color: var(--text);">🔥 Max Streak: {st.session_state.max_streak}</div>
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
            st.markdown('<h3 style="color: var(--text); margin-bottom: 1rem;">📝 Review Your Answers</h3>', unsafe_allow_html=True)
            for i, ans in enumerate(st.session_state.answers):
                if ans:
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})"
                    st.markdown(f"""
                    <div style="background: var(--card-bg); padding: 1rem; border-radius: 12px; margin-bottom: 1rem; box-shadow: var(--shadow);">
                        <div style="font-weight: 600; color: var(--text); margin-bottom: 0.5rem;">Question {i+1}: {ans["question"]}</div>
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
