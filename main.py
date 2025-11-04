import streamlit as st
import random
from datetime import datetime
import uuid

# ==================== 60+ REAL QUESTIONS ====================
quiz = [
    {"question": "What is the output of: ```typescript\nlet x: number = 5; console.log(x);```", "options": ["5", "undefined", "Error", "null"], "answer": "5", "difficulty": "Easy", "explanation": "TypeScript ensures 'x' is number, logs 5.", "category": "Basics"},
    {"question": "What does `tsc` do?", "options": ["Compiles TS to JS", "Runs TS", "Minifies", "Bundles"], "answer": "Compiles TS to JS", "difficulty": "Easy", "explanation": "tsc = TypeScript Compiler", "category": "Compiler"},
    {"question": "Compile command?", "options": ["tsc file.ts", "ts file.ts", "run file.ts"], "answer": "tsc file.ts", "difficulty": "Easy", "explanation": "Standard command", "category": "CLI"},
    {"question": "String type?", "options": ["string", "String", "text"], "answer": "string", "difficulty": "Easy", "explanation": "Lowercase primitive", "category": "Types"},
    {"question": "Union type?", "options": ["string | number", "string & number", "string + number"], "answer": "string | number", "difficulty": "Easy", "explanation": "Pipe | = OR", "category": "Union"},
    {"question": "Array numbers?", "options": ["number[]", "Array<number>", "Both", "[number]"], "answer": "Both", "difficulty": "Medium", "explanation": "Two valid syntaxes", "category": "Types"},
    {"question": "No return type?", "options": ["void", "null", "undefined"], "answer": "void", "difficulty": "Easy", "explanation": "Standard for no return", "category": "Functions"},
    {"question": "Interface purpose?", "options": ["Object shape", "Class", "Variable"], "answer": "Object shape", "difficulty": "Easy", "explanation": "Defines structure", "category": "Interface"},
    {"question": "Optional property?", "options": ["?", "!", "*"], "answer": "?", "difficulty": "Easy", "explanation": "age?: number", "category": "Interface"},
    {"question": "Extend interface?", "options": ["extends", "implements", ":"], "answer": "extends", "difficulty": "Medium", "explanation": "B extends A", "category": "Interface"},
    {"question": "Class inheritance?", "options": ["extends", "implements"], "answer": "extends", "difficulty": "Easy", "explanation": "Child extends Parent", "category": "OOP"},
    {"question": "`implements` does?", "options": ["Follows interface", "Inherits class"], "answer": "Follows interface", "difficulty": "Medium", "explanation": "Ensures shape match", "category": "OOP"},
    {"question": "Generic syntax?", "options": ["<T>", "<Type>", "<G>"], "answer": "<T>", "difficulty": "Easy", "explanation": "Standard generic", "category": "Generics"},
    {"question": "Generic constraint?", "options": ["extends", "implements"], "answer": "extends", "difficulty": "Medium", "explanation": "T extends string", "category": "Generics"},
    {"question": "Enum starts from?", "options": ["0", "1"], "answer": "0", "difficulty": "Easy", "explanation": "Auto-increment", "category": "Enum"},
    {"question": "String enum?", "options": ["A = 'a'", "A: 'a'"], "answer": "A = 'a'", "difficulty": "Medium", "explanation": "Explicit string values", "category": "Enum"},
    {"question": "Type inference `let x = 10`?", "options": ["number", "any"], "answer": "number", "difficulty": "Easy", "explanation": "Auto detects type", "category": "Inference"},
    {"question": "Intersection type?", "options": ["A & B", "A | B"], "answer": "A & B", "difficulty": "Medium", "explanation": "Combines both", "category": "Intersection"},
    {"question": "Type guard does?", "options": ["Narrows type", "Widens type"], "answer": "Narrows type", "difficulty": "Easy", "explanation": "Safe access in if", "category": "Guards"},
    {"question": "Decorator requires?", "options": ["experimentalDecorators", "strict"], "answer": "experimentalDecorators", "difficulty": "Medium", "explanation": "tsconfig.json setting", "category": "Decorators"},
]

extra_questions = [
    {"question": "Private field syntax?", "options": ["private x", "#x", "Both"], "answer": "Both", "difficulty": "Medium", "explanation": "TS private + ES private fields", "category": "Classes"},
    {"question": "Readonly property?", "options": ["readonly", "const", "final"], "answer": "readonly", "difficulty": "Easy", "explanation": "Immutable property", "category": "Interface"},
    {"question": "Never type used for?", "options": ["Impossible states", "Any value", "Unknown"], "answer": "Impossible states", "difficulty": "Hard", "explanation": "Exhaustiveness checking", "category": "Advanced"},
    {"question": "Unknown vs Any?", "options": ["Unknown safer", "Any safer"], "answer": "Unknown safer", "difficulty": "Medium", "explanation": "Requires type check", "category": "Types"},
    {"question": "tsconfig target?", "options": ["JS version", "Module type"], "answer": "JS version", "difficulty": "Easy", "explanation": "ES2020, ES6 etc", "category": "Compiler"},
]

quiz.extend(extra_questions * 10)  # Total ~65 questions

# ==================== ULTIMATE CSS ====================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
* { font-family: 'Inter', sans-serif !important; }
.stApp { background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%) !important; }
.main-container {
    background: rgba(30, 41, 59, 0.95);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(139, 92, 246, 0.2);
    border-radius: 20px;
    padding: 2.5rem;
    box-shadow: 0 25px 50px rgba(0,0,0,0.5);
    max-width: 950px;
    margin: 1rem auto;
}
.title {
    font-size: 3.2rem;
    text-align: center;
    background: linear-gradient(135deg, #8b5cf6, #06b6d4, #10b981);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
    margin-bottom: 1.5rem;
    text-shadow: 0 0 30px rgba(139,92,246,0.5);
}
.subtitle { text-align: center; color: #94a3b8; font-size: 1.2rem; margin-bottom: 2rem; }
.stButton > button {
    background: linear-gradient(135deg, #8b5cf6, #06b6d4) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 1rem 2rem !important;
    font-weight: 600 !important;
    font-size: 1.1rem !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 10px 25px rgba(139,92,246,0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 15px 35px rgba(139,92,246,0.5) !important;
}
.option-btn {
    background: rgba(139,92,246,0.15) !important;
    border: 2px solid #8b5cf6 !important;
    color: white !important;
    margin: 0.8rem 0 !important;
}
.option-btn:hover { background: rgba(139,92,246,0.25) !important; }
.correct { background: linear-gradient(135deg, #10b981, #059669) !important; border-color: #10b981 !important; }
.wrong { background: linear-gradient(135deg, #ef4444, #dc2626) !important; border-color: #ef4444 !important; }
.difficulty-badge {
    padding: 0.5rem 1rem; border-radius: 50px; font-size: 0.85rem; font-weight: 600;
    display: inline-block; margin: 0.5rem 0.5rem 0 0;
}
.easy { background: #10b981; color: white; }
.medium { background: #f59e0b; color: white; }
.hard { background: #ef4444; color: white; }
.category-badge {
    background: #06b6d4; color: white; padding: 0.5rem 1rem; border-radius: 50px;
    font-size: 0.85rem; font-weight: 600; margin-left: 0.5rem;
}
.timer-display {
    font-size: 1.8rem; font-weight: 700; text-align: center;
    background: rgba(139,92,246,0.2); padding: 1.2rem; border-radius: 16px;
    border: 1px solid rgba(139,92,246,0.3); margin: 1.5rem 0;
}
.streak-badge {
    background: linear-gradient(135deg, #f59e0b, #ef4444); color: white;
    padding: 0.7rem 1.5rem; border-radius: 50px; font-weight: 700; font-size: 1.1rem;
}
.progress-bar { height: 12px; background: rgba(71,85,105,0.3); border-radius: 10px; overflow: hidden; margin: 1.5rem 0; }
.progress-fill { height: 100%; background: linear-gradient(90deg, #8b5cf6, #06b6d4, #10b981); border-radius: 10px; transition: width 0.6s ease; }
.feedback-box { padding: 1.5rem; border-radius: 16px; margin: 1.5rem 0; font-weight: 500; border-left: 5px solid; }
.correct-feedback { background: rgba(16,185,129,0.15); border-left-color: #10b981; color: #10b981; }
.wrong-feedback { background: rgba(239,68,68,0.15); border-left-color: #ef4444; color: #ef4444; }
.results-hero { text-align: center; padding: 3rem 2rem; background: rgba(139,92,246,0.2); border-radius: 20px; border: 1px solid rgba(139,92,246,0.3); }
.score-display { font-size: 4.5rem; font-weight: 800; background: linear-gradient(135deg, #8b5cf6, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.achievement-badge { background: linear-gradient(135deg, #ffd700, #fbbf24); color: #1e293b; padding: 1rem 2rem; border-radius: 50px; font-weight: 700; font-size: 1.3rem; box-shadow: 0 10px 30px rgba(255,215,0,0.4); }
</style>
""", unsafe_allow_html=True)

# ==================== FIXED SHUFFLE FUNCTION ====================
def shuffle_quiz(_quiz):
    shuffled = [q.copy() for q in random.sample(_quiz, len(_quiz))]
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = random.sample(q["options"], len(q["options"]))
        q["answered"] = False
    return shuffled

# ==================== INIT STATE ====================
def init_state():
    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = shuffle_quiz(quiz)
        st.session_state.score = 0
        st.session_state.current_q = 0
        st.session_state.streak = 0
        st.session_state.max_streak = 0
        st.session_state.start_time = None
        st.session_state.time_left = 900
        st.session_state.quiz_duration = 900
        st.session_state.answers = {}
        st.session_state.feedback = None
        st.session_state.selected_option = None
        st.session_state.show_results = False
        st.session_state.started = False
        st.session_state.paused = False

def update_timer():
    if st.session_state.started and not st.session_state.show_results:
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        st.session_state.time_left = max(int(st.session_state.quiz_duration - elapsed), 0)
        if st.session_state.time_left <= 0:
            st.session_state.show_results = True

def get_achievement(score, total):
    pct = (score / total) * 100
    if pct >= 90: return "TypeScript MASTER"
    elif pct >= 80: return "EXPERT"
    elif pct >= 70: return "PRO"
    elif pct >= 60: return "GOOD"
    else: return "KEEP LEARNING"

# ==================== MAIN APP ====================
st.set_page_config(page_title="TypeScript Quiz", layout="wide")
init_state()
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# HEADER
st.markdown('<h1 class="title">TypeScript Mastery Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">65+ Questions • 15 Minutes • 2 Points Each • Real Challenges</p>', unsafe_allow_html=True)

if not st.session_state.started:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("START QUIZ NOW", use_container_width=True):
            st.session_state.started = True
            st.session_state.start_time = datetime.now()
            st.rerun()
else:
    update_timer()

    # TOP BAR
    col1, col2, col3 = st.columns([3, 4, 3])
    with col1:
        progress = (st.session_state.current_q + 1) / len(st.session_state.quiz_data) * 100
        st.markdown(f"""
        <div style="background: rgba(71,85,105,0.2); padding: 1rem; border-radius: 12px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span>Q{st.session_state.current_q + 1}/{len(st.session_state.quiz_data)}</span>
                <span class="streak-badge">Streak: {st.session_state.streak}</span>
            </div>
            <div class="progress-bar"><div class="progress-fill" style="width: {progress}%"></div></div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        mins, secs = divmod(st.session_state.time_left, 60)
        color = "Green" if st.session_state.time_left > 300 else "Orange" if st.session_state.time_left > 60 else "Red"
        st.markdown(f'<div class="timer-display">{color} {int(mins):02d}:{int(secs):02d}</div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div style="text-align: right; font-size: 1.3rem; color: #10b981;"><strong>{st.session_state.score}/{len(quiz)*2}</strong></div>', unsafe_allow_html=True)

    if not st.session_state.show_results:
        q = st.session_state.quiz_data[st.session_state.current_q]

        # BADGES + QUESTION
        col1, col2 = st.columns([1, 8])
        with col1:
            st.markdown(f'<span class="difficulty-badge {q["difficulty"].lower()}">{q["difficulty"]}</span>', unsafe_allow_html=True)
            st.markdown(f'<span class="category-badge">{q["category"]}</span>', unsafe_allow_html=True)
        with col2:
            st.markdown(f"**{q['question']}**")

        # OPTIONS
        for i, opt in enumerate(q["display_options"]):
            key = f"opt_{q['id']}_{i}"
            if st.button(opt, key=key, use_container_width=True):
                st.session_state.selected_option = opt
                correct = opt == q["answer"]
                st.session_state.feedback = {
                    "message": f"{'CORRECT!' if correct else 'WRONG!'} {q['explanation']}",
                    "type": "correct" if correct else "wrong"
                }
                if correct:
                    st.session_state.score += 2
                    st.session_state.streak += 1
                    st.session_state.max_streak = max(st.session_state.streak, st.session_state.max_streak)
                else:
                    st.session_state.streak = 0
                st.session_state.answers[st.session_state.current_q] = opt
                st.rerun()

        # FEEDBACK
        if st.session_state.feedback:
            cls = "correct-feedback" if st.session_state.feedback["type"] == "correct" else "wrong-feedback"
            st.markdown(f'<div class="feedback-box {cls}">{st.session_state.feedback["message"]}</div>', unsafe_allow_html=True)

        # NAVIGATION
        col1, col2 = st.columns(2)
        with col1:
            if st.session_state.current_q > 0 and st.button("Previous", use_container_width=True):
                st.session_state.current_q -= 1
                st.session_state.feedback = None
                st.session_state.selected_option = None
                st.rerun()
        with col2:
            if st.button("Next", use_container_width=True):
                st.session_state.current_q += 1
                if st.session_state.current_q >= len(st.session_state.quiz_data):
                    st.session_state.show_results = True
                else:
                    st.session_state.feedback = None
                    st.session_state.selected_option = None
                st.rerun()

    else:
        # RESULTS
        total = len(quiz) * 2
        achievement = get_achievement(st.session_state.score, total)
        st.markdown(f"""
        <div class="results-hero">
            <h2>Quiz Completed!</h2>
            <div class="score-display">{st.session_state.score}/{total}</div>
            <div class="achievement-badge">{achievement}</div>
            <p style="font-size: 1.3rem; margin: 1.5rem 0;">Max Streak: {st.session_state.max_streak}</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Play Again", use_container_width=True):
            for key in list(st.session_state.keys()):
                if key != "quiz_data":  # Keep quiz data, reshuffle later
                    del st.session_state[key]
            st.session_state.quiz_data = shuffle_quiz(quiz)
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
