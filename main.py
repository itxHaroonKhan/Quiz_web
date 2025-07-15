import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 10 general JavaScript questions
quiz = [
    {
        "question": "How do you declare a variable in JavaScript?",
        "options": ["var myVar;", "variable myVar;", "let myVar;", "Both var and let"],
        "answer": "Both var and let",
        "difficulty": "Easy",
        "explanation": "In JavaScript, variables can be declared using `var`, `let`, or `const`. Both `var` and `let` are correct, though `let` is preferred in modern JavaScript for block scoping."
    },
    {
        "question": "What is the output of `typeof null` in JavaScript?",
        "options": ["null", "object", "undefined", "string"],
        "answer": "object",
        "difficulty": "Medium",
        "explanation": "In JavaScript, `typeof null` returns `'object'` due to a historical bug in the language, even though `null` is a primitive value."
    },
    {
        "question": "Which method adds an element to the end of an array?",
        "options": ["push()", "pop()", "shift()", "unshift()"],
        "answer": "push()",
        "difficulty": "Easy",
        "explanation": "The `push()` method adds one or more elements to the end of an array and returns the new length."
    },
    {
        "question": "What does the `===` operator check in JavaScript?",
        "options": ["Value only", "Type only", "Value and type", "Reference only"],
        "answer": "Value and type",
        "difficulty": "Medium",
        "explanation": "The `===` operator checks for both value and type equality, unlike `==` which performs type coercion."
    },
    {
        "question": "How do you create a function in JavaScript?",
        "options": [
            "function myFunc() {}",
            "def myFunc() {}",
            "func myFunc() {}",
            "function = myFunc() {}"
        ],
        "answer": "function myFunc() {}",
        "difficulty": "Easy",
        "explanation": "A function in JavaScript is declared using the `function` keyword, followed by a name, parentheses, and curly braces."
    },
    {
        "question": "What is the purpose of `setTimeout`?",
        "options": [
            "Executes a function immediately",
            "Delays execution of a function",
            "Repeats a function indefinitely",
            "Stops a function"
        ],
        "answer": "Delays execution of a function",
        "difficulty": "Medium",
        "explanation": "`setTimeout` schedules a function to run after a specified delay in milliseconds."
    },
    {
        "question": "What is a closure in JavaScript?",
        "options": [
            "A loop structure",
            "A function with access to its outer scope",
            "A type of variable",
            "A built-in object"
        ],
        "answer": "A function with access to its outer scope",
        "difficulty": "Hard",
        "explanation": "A closure is a function that retains access to its lexical scope, even when the function is executed outside that scope."
    },
    {
        "question": "What does `Array.prototype.map()` do?",
        "options": [
            "Removes elements",
            "Transforms elements",
            "Filters elements",
            "Sorts elements"
        ],
        "answer": "Transforms elements",
        "difficulty": "Medium",
        "explanation": "The `map()` method creates a new array with the results of calling a provided function on every element."
    },
    {
        "question": "What is the output of `console.log(0.1 + 0.2 === 0.3)`?",
        "options": ["true", "false", "undefined", "NaN"],
        "answer": "false",
        "difficulty": "Hard",
        "explanation": "Due to floating-point precision issues in JavaScript, `0.1 + 0.2` equals `0.30000000000000004`, so it is not strictly equal to `0.3`."
    },
    {
        "question": "How do you check if a variable is an array?",
        "options": [
            "typeof myVar === 'array'",
            "Array.isArray(myVar)",
            "myVar instanceof Array",
            "Both Array.isArray and instanceof"
        ],
        "answer": "Both Array.isArray and instanceof",
        "difficulty": "Medium",
        "explanation": "Both `Array.isArray(myVar)` and `myVar instanceof Array` can check if a variable is an array, though `Array.isArray` is more reliable."
    }
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

# Simplified CSS for UI
st.markdown("""
<style>
/* Global styles */
.main-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
}

/* Theme-specific styles */
.main-container[data-theme="dark"] {
    background-color: #1a1a1a;
    color: #ffffff;
    --primary-color: #34c759;
    --secondary-color: #2c2c2e;
    --button-bg: #2c2c2e;
    --button-hover: #3a3a3c;
    --feedback-correct-bg: #34c759;
    --feedback-wrong-bg: #ff3b30;
    --progress-fill: #34c759;
}

.main-container[data-theme="light"] {
    background-color: #ffffff;
    color: #333333;
    --primary-color: #28a745;
    --secondary-color: #f5f5f5;
    --button-bg: #f5f5f5;
    --button-hover: #e0e0e0;
    --feedback-correct-bg: #28a745;
    --feedback-wrong-bg: #dc3545;
    --progress-fill: #28a745;
}

/* Title and caption */
.title {
    font-size: 2.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 10px;
    color: var(--primary-color);
}

.caption {
    font-size: 1.1rem;
    text-align: center;
    color: var(--text-color);
    margin-bottom: 20px;
}

/* Timer */
.timer {
    font-size: 1rem;
    font-weight: 600;
    text-align: right;
    color: var(--primary-color);
    margin-bottom: 15px;
}

/* Progress bar */
.progress-bar {
    background-color: var(--secondary-color);
    border-radius: 10px;
    height: 20px;
    position: relative;
    margin: 20px 0;
}

.progress-fill {
    background-color: var(--progress-fill);
    height: 100%;
    border-radius: 10px;
}

.progress-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 0.9rem;
    font-weight: 600;
}

/* Question container */
.question-container {
    background-color: var(--secondary-color);
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
}

/* Difficulty and streak */
.difficulty {
    font-size: 0.9rem;
    opacity: 0.7;
    margin-bottom: 15px;
    text-align: right;
}

/* Buttons */
.stButton > button {
    width: 100%;
    background-color: var(--button-bg);
    color: var(--text-color);
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    padding: 12px;
    margin: 8px 0;
    font-size: 1rem;
    text-align: left;
}

.stButton > button:hover {
    background-color: var(--button-hover);
}

.stButton > button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

/* Selected button states */
.selected-correct {
    background-color: var(--feedback-correct-bg) !important;
    color: white !important;
}

.selected-wrong {
    background-color: var(--feedback-wrong-bg) !important;
    color: white !important;
}

/* Feedback */
.feedback-correct {
    background-color: var(--feedback-correct-bg);
    color: white;
    padding: 10px;
    border-radius: 8px;
    margin-top: 15px;
    text-align: center;
}

.feedback-wrong {
    background-color: var(--feedback-wrong-bg);
    color: white;
    padding: 10px;
    border-radius: 8px;
    margin-top: 15px;
    text-align: center;
}

/* Code block */
.stCodeBlock {
    background-color: #2f2f2f;
    border-radius: 8px;
    padding: 15px;
    margin: 10px 0;
}

.main-container[data-theme="light"] .stCodeBlock {
    background-color: #f5f5f5;
}

/* Theme toggle, start, and play again buttons */
.stButton > button[key="theme_toggle"],
.stButton > button[key="start_quiz"],
.stButton > button[key="play_again"] {
    background-color: var(--primary-color);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    margin: 10px auto;
    display: block;
}

.stButton > button[key="theme_toggle"]:hover,
.stButton > button[key="start_quiz"]:hover,
.stButton > button[key="play_again"]:hover {
    background-color: #2c974b;
}

.main-container[data-theme="light"] .stButton > button[key="theme_toggle"],
.main-container[data-theme="light"] .stButton > button[key="start_quiz"],
.main-container[data-theme="light"] .stButton > button[key="play_again"] {
    background-color: #218838;
}
</style>
""", unsafe_allow_html=True)

# Main UI
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 JavaScript Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript Skills!</p>', unsafe_allow_html=True)

# Theme toggle button
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen
if not st.session_state.started:
    st.markdown("""
    <div style="text-align: center;">
        <p style="font-size: 18px;">Test your JavaScript skills with 10 questions!</p>
        <p style="opacity: 0.8;">60 minutes, 2 points per correct answer. Ready?</p>
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
            <div style="font-size: 13px; text-align: center;">
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

                # Display question
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
                            st.session_state.score += 2
                            st.session_state.streak += 1
                            if st.session_state.streak > st.session_state.max_streak:
                                st.session_state.max_streak = st.session_state.streak
                        else:
                            st.session_state.streak = 0
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
                        st.markdown(f'<div style="font-size: 14px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

        else:
            # Results
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 3600)
            total_possible_score = len(quiz) * 2
            accuracy = (st.session_state.score / total_possible_score) * 100 if total_possible_score > 0 else 0
            st.markdown('<div class="results-container">', unsafe_allow_html=True)
            st.markdown(f'<div style="font-size: 2rem; text-align: center;">Score: {st.session_state.score}/{total_possible_score}</div>', unsafe_allow_html=True)
            st.markdown(f"""
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin: 1.5rem 0;">
                <div style="text-align: center;">
                    <div style="font-size: 1.2rem;">⏱️ {int(time_taken) // 60}m {int(time_taken) % 60}s</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">Time Taken</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1.2rem;">🎯 {accuracy:.1f}%</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">Accuracy</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1.2rem;">✅ {sum(1 for ans in st.session_state.answers if ans and ans["is_correct"])}</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">Correct</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1.2rem;">❌ {sum(1 for ans in st.session_state.answers if ans and not ans["is_correct"])}</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">Incorrect</div>
                </div>
            </div>
            <div style="text-align: center; margin: 1.5rem 0;">
                <div style="font-size: 1.2rem;">🔥 Max Streak: {st.session_state.max_streak}</div>
            </div>
            """, unsafe_allow_html=True)

            # Review Answers
            st.markdown('<h3 style="margin-bottom: 1rem;">📝 Review Your Answers</h3>', unsafe_allow_html=True)
            for i, ans in enumerate(st.session_state.answers):
                if ans:
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})"
                    st.markdown(f"""
                    <div style="background: var(--secondary-color); padding: 1rem; border-radius: 12px; margin-bottom: 1rem;">
                        <div style="font-weight: 600; margin-bottom: 0.5rem;">Question {i+1}: {ans["question"]}</div>
                        <div style="margin-bottom: 0.25rem;">Your Answer: {ans["user_answer"]}</div>
                        <div style="margin-bottom: 0.5rem; color: {'var(--feedback-correct-bg)' if ans["is_correct"] else 'var(--feedback-wrong-bg)'}">{status}</div>
                        <div style="font-size: 0.9rem; opacity: 0.8; padding: 0.75rem; background: rgba(0, 0, 0, 0.05); border-radius: 8px;">
                            Explanation: {quiz[i]["explanation"]}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

            # Play Again button
            if st.button("🔄 Play Again", key="play_again"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
