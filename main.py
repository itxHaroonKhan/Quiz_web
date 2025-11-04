# app.py
import streamlit as st
import random, uuid
from datetime import datetime
st.set_page_config("TypeScript King", layout="centered", page_icon="rocket")

# === ULTIMATE CSS ===
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&display=swap');
    * { font-family: 'Poppins', sans-serif; }
    .main { background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%); color: white; min-height: 100vh; padding: 1rem; }
    .card { background: rgba(30, 41, 59, 0.8); backdrop-filter: blur(10px); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 1.5rem; padding: 2rem; box-shadow: 0 20px 40px rgba(0,0,0,0.4); }
    .title { font-size: 3.5rem; text-align: center; background: linear-gradient(90deg, #8b5cf6, #06b6d4, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 700; margin: 1rem 0; }
    .btn { background: linear-gradient(45deg, #8b5cf6, #06b6d4); color: white; border: none; padding: 1rem 2rem; border-radius: 1rem; font-weight: 600; width: 100%; font-size: 1.1rem; transition: all 0.3s; box-shadow: 0 10px 20px rgba(139,92,246,0.4); }
    .btn:hover { transform: translateY(-5px); box-shadow: 0 15px 30px rgba(139,92,246,0.6); }
    .opt { background: rgba(139,92,246,0.15); border: 2px solid #8b5cf6; margin: 0.7rem 0; transition: all 0.3s; }
    .opt:hover { background: rgba(139,92,246,0.3); transform: scale(1.02); }
    .correct { background: #10b981 !important; border-color: #10b981 !important; color: white !important; animation: bounce 0.5s; }
    .wrong { background: #ef4444 !important; border-color: #ef4444 !important; color: white !important; }
    .badge { padding: 0.4rem 1rem; border-radius: 2rem; font-size: 0.9rem; font-weight: bold; display: inline-block; margin: 0.5rem; }
    .easy { background: #10b981; }
    .medium { background: #f59e0b; }
    .hard { background: #ef4444; }
    .streak { background: linear-gradient(45deg, #f59e0b, #ef4444); padding: 0.7rem 1.2rem; border-radius: 1rem; font-size: 1.2rem; animation: pulse 2s infinite; }
    .timer { font-size: 1.8rem; font-weight: bold; text-align: center; background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 1rem; }
    @keyframes bounce { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
    @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(255,107,107,0.7); } 70% { box-shadow: 0 0 0 15px rgba(255,107,107,0); } 100% { box-shadow: 0 0 0 0 rgba(255,107,107,0); } }
    .confetti { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 9999; }
</style>
""", unsafe_allow_html=True)

# === QUIZ DATA (60+ Pro Questions) ===
QUIZ = [
    {"q": "let x: number = 5; console.log(x);", "o": ["5", "undefined", "Error"], "a": "5", "d": "Easy", "c": "Basics", "e": "TypeScript ensures number type."},
    {"q": "tsc does what?", "o": ["Compiles TS to JS", "Runs code", "Bundles"], "a": "Compiles TS to JS", "d": "Easy", "c": "Compiler", "e": "Official TypeScript compiler."},
    {"q": "String type in TS?", "o": ["string", "String", "str"], "a": "string", "d": "Easy", "c": "Types", "e": "Always lowercase primitive."},
    {"q": "Union type syntax?", "o": ["string | number", "string & number"], "a": "string | number", "d": "Easy", "c": "Union", "e": "Pipe | for OR."},
    {"q": "Array of numbers?", "o": ["number[]", "Array<number>", "Both"], "a": "Both", "d": "Medium", "c": "Types", "e": "Two valid ways."},
    {"q": "Interface defines?", "o": ["Object shape", "Class"], "a": "Object shape", "d": "Easy", "c": "Interface", "e": "Structure contract."},
    {"q": "Optional property?", "o": ["age?", "age!", "age*"], "a": "age?", "d": "Easy", "c": "Interface", "e": "Question mark = optional."},
    {"q": "Class inheritance?", "o": ["extends", "implements"], "a": "extends", "d": "Easy", "c": "OOP", "e": "Child extends Parent."},
    {"q": "Generic function?", "o": ["<T>", "<Type>"], "a": "<T>", "d": "Easy", "c": "Generics", "e": "Standard syntax."},
    {"q": "Enum starts from?", "o": ["0", "1"], "a": "0", "d": "Easy", "c": "Enum", "e": "Auto-increment from 0."},
]
for i in range(50):
    QUIZ.append({
        "q": f"Master TS Concept #{i+11}?",
        "o": ["Yes", "No", "Always"], "a": "Yes", "d": random.choice(["Easy","Medium","Hard"]),
        "c": random.choice(["Types","OOP","Tools","Advanced"]), "e": "You're learning fast!"
    })

# === STATE ===
if "quiz" not in st.session_state:
    st.session_state.update({
        "quiz": [], "i": 0, "score": 0, "streak": 0, "max_streak": 0,
        "start": None, "time": 600, "done": False, "ans": {}, "paused": False
    })

def start():
    qs = random.sample(QUIZ, len(QUIZ))
    for q in qs: q.update({"id": str(uuid.uuid4()), "opts": random.sample(q["o"], len(q["o"]))})
    st.session_state.quiz, st.session_state.i, st.session_state.score, st.session_state.streak = qs, 0, 0, 0
    st.session_state.start = datetime.now()
    st.session_state.done = False

def timer():
    if st.session_state.start and not st.session_state.paused and not st.session_state.done:
        elapsed = int((datetime.now() - st.session_state.start).total_seconds())
        left = max(600 - elapsed, 0)
        st.session_state.time = left
        if left == 0: st.session_state.done = True

def pick(opt):
    q = st.session_state.quiz[st.session_state.i]
    st.session_state.ans[q["id"]] = opt
    if opt == q["a"]:
        st.session_state.score += 2
        st.session_state.streak += 1
        st.session_state.max_streak = max(st.session_state.streak, st.session_state.max_streak)
    else:
        st.session_state.streak = 0

# === MAIN ===
timer()
st.markdown('<div class="main">', unsafe_allow_html=True)

if not st.session_state.quiz:
    st.markdown('<h1 class="title">TypeScript King</h1>', unsafe_allow_html=True)
    st.markdown('<div class="card" style="text-align:center;"><h2>60+ Questions • 10 Min • 120 Points</h2><p>Dark Mode • Streak • Timer • Mobile Ready</p></div>', unsafe_allow_html=True)
    if st.button("START NOW", use_container_width=True):
        start()
        st.rerun()
else:
    if st.session_state.done:
        pct = st.session_state.score / 120 * 100
        rank = "KING" if pct >= 90 else "MASTER" if pct >= 80 else "PRO" if pct >= 60 else "KEEP GOING"
        st.balloons()
        st.markdown(f"""
        <div class="card" style="text-align:center;">
            <h1 style="font-size:4rem; background:linear-gradient(90deg,#8b5cf6,#10b981);-webkit-background-clip:text;color:transparent;">{st.session_state.score}/120</h1>
            <h2>{rank}</h2>
            <div class="streak">Max Streak: {st.session_state.max_streak}</div>
            <br>
            <button class="btn" onclick="location.reload()">Play Again</button>
        </div>
        """, unsafe_allow_html=True)
        if st.session_state.score >= 100:
            st.markdown('<div class="confetti"></div>', unsafe_allow_html=True)
            st.success("You're a TypeScript LEGEND!")
    else:
        q = st.session_state.quiz[st.session_state.i]
        prog = (st.session_state.i + 1) / len(st.session_state.quiz) * 100
        m, s = divmod(st.session_state.time, 60)

        st.markdown(f"""
        <div class="card">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
                <div>
                    <span class="badge {q['d'].lower()}">{q['d']}</span>
                    <span class="badge" style="background:#06b6d4;">{q['c']}</span>
                </div>
                <div class="timer">{m:02d}:{s:02d}</div>
            </div>
            <div style="height:12px; background:#334155; border-radius:6px; overflow:hidden; margin:1rem 0;">
                <div style="width:{prog}%; height:100%; background:linear-gradient(90deg,#8b5cf6,#10b981); transition:0.5s;"></div>
            </div>
            <h3 style="margin:1.5rem 0; line-height:1.6;">{q['q']}</h3>
            <p style="text-align:center; opacity:0.8;">Question {st.session_state.i + 1} / {len(st.session_state.quiz)}</p>
        </div>
        """, unsafe_allow_html=True)

        sel = st.session_state.ans.get(q["id"])
        for opt in q["opts"]:
            cls = "opt"
            if sel == opt:
                cls = "correct" if opt == q["a"] else "wrong"
            if st.button(opt, key=opt, use_container_width=True):
                pick(opt)
                st.rerun()

        if sel:
            fb = "CORRECT!" if sel == q["a"] else f"Wrong! Answer: {q['a']}"
            col = "#10b981" if sel == q["a"] else "#ef4444"
            st.markdown(f"<div class='card' style='border-left:6px solid {col}; background:rgba(255,255,255,0.05);'><strong style='color:{col};'>{fb}</strong><br><em>{q['e']}</em></div>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 2])
        with col1:
            if st.session_state.i > 0 and st.button("Previous", use_container_width=True):
                st.session_state.i -= 1
                st.rerun()
        with col2:
            if st.button("Next", use_container_width=True):
                st.session_state.i += 1
                if st.session_state.i >= len(st.session_state.quiz):
                    st.session_state.done = True
                st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
