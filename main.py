import streamlit as st
import random
from datetime import datetime
import uuid

# ==================== 60+ QUESTIONS (4 OPTIONS ONLY) ====================
quiz = [
    {"q": "What is TypeScript?", "o": ["JS with types", "New language", "CSS framework", "Database"], "a": "JS with types", "d": "Easy"},
    {"q": "`tsc` ka matlab?", "o": ["Compile TS", "Run JS", "Minify code", "Bundle"], "a": "Compile TS", "d": "Easy"},
    {"q": "String type likhte hain?", "o": ["string", "String", "str", "text"], "a": "string", "d": "Easy"},
    {"q": "Union type ka sign?", "o": ["|", "&", "+", "||"], "a": "|", "d": "Easy"},
    {"q": "Array of numbers?", "o": ["number[]", "Array<number>", "Both", "Num[]"], "a": "Both", "d": "Medium"},
    {"q": "Function no return → type?", "o": ["void", "null", "any", "undefined"], "a": "void", "d": "Easy"},
    {"q": "Interface banane ka keyword?", "o": ["interface", "type", "class", "struct"], "a": "interface", "d": "Easy"},
    {"q": "Optional property?", "o": ["?", "!", "*", "~"], "a": "?", "d": "Easy"},
    {"q": "Class extends karta hai?", "o": ["Parent class", "Interface", "Type", "Enum"], "a": "Parent class", "d": "Easy"},
    {"q": "Generic syntax?", "o": ["<T>", "<Type>", "[T]", "{T}"], "a": "<T>", "d": "Easy"},
    {"q": "Enum default start?", "o": ["0", "1", "A", "null"], "a": "0", "d": "Easy"},
    {"q": "Type inference: `let x = 5` → x is?", "o": ["number", "any", "unknown", "let"], "a": "number", "d": "Easy"},
    {"q": "Intersection type?", "o": ["A & B", "A | B", "A + B", "A, B"], "a": "A & B", "d": "Medium"},
    {"q": "Type guard ka kaam?", "o": ["Narrow type", "Widen type", "Delete type", "Copy"], "a": "Narrow type", "d": "Easy"},
    {"q": "Decorator enable karne ke liye?", "o": ["experimentalDecorators", "strict", "noEmit", "target"], "a": "experimentalDecorators", "d": "Medium"},
    {"q": "Private field (new)?", "o": ["#name", "private name", "Both", "_name"], "a": "Both", "d": "Medium"},
    {"q": "Readonly property?", "o": ["readonly", "const", "immutable", "fixed"], "a": "readonly", "d": "Easy"},
    {"q": "`never` type kab use?", "o": ["Impossible code", "Any value", "Unknown", "All"], "a": "Impossible code", "d": "Hard"},
    {"q": "`unknown` vs `any`?", "o": ["unknown safer", "any safer", "same", "both bad"], "a": "unknown safer", "d": "Medium"},
    {"q": "`target` in tsconfig?", "o": ["JS version", "Module", "Output folder", "Filename"], "a": "JS version", "d": "Easy"},
]

# Add more to make 60+
extra = [
    {"q": "Type alias keyword?", "o": ["type", "interface", "alias", "typedef"], "a": "type", "d": "Easy"},
    {"q": "Keyof operator?", "o": ["Keys of object", "Values", "Both", "None"], "a": "Keys of object", "d": "Medium"},
    {"q": "Conditional types?", "o": ["T extends U ? X : Y", "T | U", "T & U", "T = U"], "a": "T extends U ? X : Y", "d": "Hard"},
    {"q": "Mapped types?", "o": ["{ [K in keyof T]: U }", "T[K]", "T | K", "T & K"], "a": "{ [K in keyof T]: U }", "d": "Hard"},
]
quiz.extend(extra * 10)
random.shuffle(quiz)
quiz = quiz[:60]  # Exactly 60 questions

# ==================== CSS + PAGE ====================
st.set_page_config(page_title="TS Quiz", layout="centered")
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&display=swap');
    * { font-family: 'Poppins', sans-serif !important; }
    .stApp { background: linear-gradient(135deg, #1e1b4b, #0f172a); color: white; }
    .quiz-box { background: rgba(30, 41, 59, 0.9); backdrop-filter: blur(12px); border-radius: 20px; padding: 2rem; max-width: 700px; margin: auto; border: 1px solid #4c1d95; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    .title { font-size: 2.8rem; text-align: center; background: linear-gradient(90deg, #a855f7, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 700; }
    .timer { font-size: 2rem; font-weight: 700; text-align: center; padding: 1rem; background: #1e293b; border-radius: 12px; border: 2px solid #a855f7; }
    .option { background: #1e293b; border: 2px solid #4c1d95; margin: 0.8rem 0; padding: 1rem; border-radius: 12px; transition: all 0.3s; }
    .option:hover { background: #4c1d95; transform: translateY(-3px); }
    .correct { background: #166534 !important; border-color: #22c55e !important; }
    .wrong { background: #7f1d1d !important; border-color: #ef4444 !important; }
    .badge { padding: 0.4rem 0.8rem; border-radius: 50px; font-size: 0.8rem; font-weight: 600; }
    .easy { background: #166534; }
    .medium { background: #ca8a04; }
    .hard { background: #7f1d1d; }
</style>
""", unsafe_allow_html=True)

# ==================== STATE INIT ====================
if "q_idx" not in st.session_state:
    st.session_state.update({
        "q_idx": 0,
        "score": 0,
        "streak": 0,
        "answers": [],
        "start_time": None,
        "shuffled": [q.copy() | {"id": str(uuid.uuid4()), "options": random.sample(q["o"], 4)} for q in quiz],
        "show_result": False
    })

q = st.session_state.shuffled[st.session_state.q_idx]
total_q = len(st.session_state.shuffled)

# Start timer on first question
if st.session_state.start_time is None:
    st.session_state.start_time = datetime.now()

# Timer (60 sec per question)
elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
time_left = max(60 - int(elapsed), 0)

# Auto next when time up
if time_left == 0 and not st.session_state.show_result:
    st.session_state.q_idx += 1
    st.session_state.start_time = datetime.now()
    st.rerun()

# ==================== UI ====================
st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
st.markdown('<h1 class="title">TypeScript Blitz</h1>', unsafe_allow_html=True)

# Top Bar
col1, col2, col3 = st.columns([2, 3, 2])
with col1: st.markdown(f"<div class='badge easy'>Q{st.session_state.q_idx + 1}/{total_q}</div>", unsafe_allow_html=True)
with col2: 
    color = "lime" if time_left > 20 else "orange" if time_left > 10 else "red"
    st.markdown(f'<div class="timer" style="color:{color};">⏰ {time_left}s</div>', unsafe_allow_html=True)
with col3: st.markdown(f"<div style='text-align:right; font-size:1.3rem;'>Score: <b>{st.session_state.score}</b></div>", unsafe_allow_html=True)

# Question
st.markdown(f"### {q['q']}")
st.markdown(f"<small>Difficulty: <span class='badge {q['d'].lower()}'>{q['d']}</span></small>", unsafe_allow_html=True)

# Options
selected = st.session_state.answers[-1] if st.session_state.answers and len(st.session_state.answers) > st.session_state.q_idx else None

for opt in q["options"]:
    key = f"opt_{q['id']}_{opt}"
    btn = st.button(opt, key=key, use_container_width=True)
    
    if btn:
        correct = opt == q["a"]
        st.session_state.answers.append(opt)
        
        if correct:
            st.session_state.score += 2
            st.session_state.streak += 1
            st.success(f"CORRECT! {q.get('exp', 'Great job!')}")
        else:
            st.session_state.streak = 0
            st.error(f"WRONG! Answer: {q['a']}")
        
        # Next question
        if st.session_state.q_idx < total_q - 1:
            st.session_state.q_idx += 1
            st.session_state.start_time = datetime.now()
        else:
            st.session_state.show_result = True
        st.rerun()

# Show feedback if answered
if len(st.session_state.answers) > st.session_state.q_idx:
    ans = st.session_state.answers[st.session_state.q_idx]
    is_correct = ans == q["a"]
    cls = "correct" if is_correct else "wrong"
    icon = "Correct" if is_correct else "Wrong"
    st.markdown(f'<div class="option {cls}">→ Your answer: <b>{ans}</b></div>', unsafe_allow_html=True)

# Progress
progress = (st.session_state.q_idx + (1 if len(st.session_state.answers) > st.session_state.q_idx else 0)) / total_q
st.progress(progress)

# Results
if st.session_state.show_result:
    st.balloons()
    pct = st.session_state.score / (total_q * 2) * 100
    rank = "MASTER" if pct >= 90 else "EXPERT" if pct >= 75 else "GOOD" if pct >= 60 else "KEEP GOING"
    st.markdown(f"""
    <div style='text-align:center; padding:2rem; background:#1e293b; border-radius:16px;'>
        <h2>Quiz Complete!</h2>
        <h1 style='font-size:4rem; color:#a855f7;'>{st.session_state.score}/{total_q*2}</h1>
        <h3>{rank}</h3>
        <p>Streak: {st.session_state.streak} | Accuracy: {pct:.1f}%</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Play Again", use_container_width=True):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
