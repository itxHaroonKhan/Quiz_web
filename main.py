import streamlit as st
import random
from datetime import datetime
import uuid

# --- QUIZ DATA ---
quiz = [
    {
        "question": "How do you write a nested for loop to iterate over a 2D array in JavaScript?",
        "options": [
            "for (let i = 0; i < array.length; i++) { for (let j = 0; j < array[i].length; j++) { } }",
            "for (let i = 0; i < array; i++) { for (let j = 0; j < array[i]; j++) { } }",
            "for (let i in array) { for (let j in array[i]) { } }",
            "for (let i of array) { for (let j of array) { } }"
        ],
        "answer": "for (let i = 0; i < array.length; i++) { for (let j = 0; j < array[i].length; j++) { } }",
        "difficulty": "Medium",
        "explanation": "A nested for loop uses two indices: `i` for rows and `j` for columns, accessing each element as `array[i][j]`."
    },
    # Add more questions here
]

# --- FUNCTIONS ---
@st.cache_data
def shuffle_quiz(_quiz):
    shuffled = random.sample(_quiz, len(_quiz))
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = q["options"].copy()
        random.shuffle(q["display_options"])
        q["labeled_answer"] = q["answer"]
    return shuffled

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

def update_timer():
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.session_state.time_left = max(3600 - elapsed, 0)
    if st.session_state.time_left <= 0:
        st.session_state.show_results = True
        st.rerun()

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

# --- INITIAL STATE ---
if "quiz_data" not in st.session_state:
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
        "theme": "dark",
        "streak": 0,
        "started": False,
        "max_streak": 0
    })

# --- UI ---
st.set_page_config(page_title="DOM Quiz", layout="centered")
st.markdown("""
    <style>
    .main-container { max-width: 700px; margin: auto; padding: 20px; }
    .question-box { background: #f0f0f5; padding: 15px; border-radius: 10px; margin-bottom: 15px; }
    .option-btn { margin: 5px 0; width: 100%; }
    .correct { color: green; }
    .wrong { color: red; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("🚀 DOM Mastery Quiz")

if st.button("🌗 Toggle Theme"):
    toggle_theme()
    st.rerun()

if not st.session_state.started:
    st.info("Click below to start the quiz.")
    if st.button("Start Quiz"):
        st.session_state.started = True
        st.session_state.start_time = datetime.now()
        st.rerun()
else:
    update_timer()
    minutes = int(st.session_state.time_left // 60)
    seconds = int(st.session_state.time_left % 60)
    st.markdown(f"**Time Left:** {minutes:02d}:{seconds:02d}")

    if not st.session_state.show_results:
        if st.session_state.current_q < len(quiz):
            q = st.session_state.quiz_data[st.session_state.current_q]
            st.markdown(f"### Q{st.session_state.current_q + 1}: {q['question']}")
            for opt in q["display_options"]:
                if st.button(opt, key=opt, disabled=st.session_state.selected_option is not None):
                    is_correct = opt == q["labeled_answer"]
                    st.session_state.selected_option = opt
                    st.session_state.feedback = {
                        "is_correct": is_correct,
                        "correct_answer": q["labeled_answer"],
                        "explanation": q["explanation"]
                    }
                    st.session_state.answers[st.session_state.current_q] = {
                        "question": q["question"],
                        "user_answer": opt,
                        "correct_answer": q["labeled_answer"],
                        "is_correct": is_correct
                    }
                    if is_correct:
                        st.session_state.score += 2
                        st.session_state.streak += 1
                        if st.session_state.streak > st.session_state.max_streak:
                            st.session_state.max_streak = st.session_state.streak
                    else:
                        st.session_state.streak = 0

        if st.session_state.feedback:
            fb = st.session_state.feedback
            if fb["is_correct"]:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Wrong! Correct: {fb['correct_answer']}")
            st.info(f"💡 {fb['explanation']}")

            if st.button("Next Question"):
                st.session_state.current_q += 1
                st.session_state.selected_option = None
                st.session_state.feedback = None
                st.rerun()

    else:
        total_possible = len(quiz) * 2
        score = st.session_state.score
        st.success(f"🎉 Your Score: {score}/{total_possible}")
        correct = sum(1 for ans in st.session_state.answers if ans and ans["is_correct"])
        wrong = len(quiz) - correct
        st.write(f"Correct: {correct}")
        st.write(f"Incorrect: {wrong}")
        st.write(f"Max Streak: {st.session_state.max_streak}")
        if st.button("Play Again"):
            reset_quiz()

st.markdown('</div>', unsafe_allow_html=True)
