import streamlit as st
import random
from datetime import datetime
import uuid

# === 100 TypeScript Questions (Same as before) ===
quiz = [ ... ]  # Paste the full quiz list here (from your code)

# === Super Clean CSS ===
st.markdown("""
<style>
    * { box-sizing: border-box; }
    body { background: #1a0033; color: #e6ccff; font-family: 'Segoe UI', sans-serif; }
    .main { max-width: 800px; margin: 2rem auto; padding: 2rem; background: #2d1b4d; border-radius: 20px; box-shadow: 0 0 30px rgba(139, 92, 246, 0.3); }
    h1 { text-align: center; background: linear-gradient(90deg, #9d4edd, #c77dff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.8rem; }
    .qbox { background: #3d2b66; padding: 1.5rem; border-radius: 15px; margin: 1.5rem 0; border: 2px solid #9d4edd; }
    .opt { background: #5d3a99; margin: 0.8rem 0; padding: 1rem; border-radius: 12px; text-align: left; font-size: 1.1rem; border: 2px solid transparent; transition: all 0.3s; }
    .opt:hover { background: #7a4bc7; border-color: #c77dff; }
    .correct { background: #2d8a2d !important; border-color: #34c759 !important; color: white !important; }
    .wrong { background: #8a2d2d !important; border-color: #ff3b30 !important; color: white !important; }
    .btn { 
        background: linear-gradient(45deg, #9d4edd, #c77dff); 
        color: white; border: none; padding: 1rem 2rem; 
        font-size: 1.2rem; font-weight: bold; border-radius: 50px; 
        width: 48%; margin: 1rem 1%; cursor: pointer; 
        box-shadow: 0 5px 15px rgba(157, 78, 221, 0.4);
        transition: all 0.3s;
    }
    .btn:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(157, 78, 221, 0.6); }
    .timer { text-align: center; font-size: 1.8rem; font-weight: bold; background: #3d2b66; padding: 0.8rem; border-radius: 15px; }
    .progress { height: 12px; background: #3d2b66; border-radius: 6px; overflow: hidden; margin: 1rem 0; }
    .fill { height: 100%; background: linear-gradient(90deg, #9d4edd, #c77dff); transition: width 0.5s; }
    .badge { padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.9rem; font-weight: bold; display: inline-block; margin: 0.3rem; }
    .easy { background: #34c759; color: white; }
    .medium { background: #ff9500; color: white; }
    .hard { background: #ff3b30; color: white; }
</style>
""", unsafe_allow_html=True)

# === Session Setup ===
if "q" not in st.session_state:
    random.shuffle(quiz)
    for q in quiz:
        q["id"] = str(uuid.uuid4())
        q["shuffled"] = q["options"][:]
        random.shuffle(q["shuffled"])
    st.session_state.update({
        "quiz": quiz,
        "i": 0,
        "score": 0,
        "start": None,
        "selected": None,
        "done": False,
        "answers": {}
    })

# === Timer ===
def timer():
    if st.session_state.start:
        elapsed = int((datetime.now() - st.session_state.start).total_seconds())
        left = max(600 - elapsed, 0)
        if left == 0:
            st.session_state.done = True
        m, s = divmod(left, 60)
        return f"{m:02d}:{s:02d}"
    return "10:00"

# === Main ===
st.markdown('<div class="main">', unsafe_allow_html=True)

if not st.session_state.start:
    st.markdown("<h1>🚀 TypeScript Quiz</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:1.3rem;'>100 Questions • 10 Minutes • 2 Points Each</p>", unsafe_allow_html=True)
    if st.button("🎯 START QUIZ", key="start", help="Let's go!"):
        st.session_state.start = datetime.now()
        st.rerun()

else:
    if st.session_state.done or st.session_state.i >= len(quiz):
        st.markdown(f"<h1>🎉 Done!</h1>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align:center;'>Score: {st.session_state.score}/200</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center; font-size:1.5rem;'>You are a TypeScript {['Noob', 'Learner', 'Pro', 'Ninja', 'God'][min(st.session_state.score//40, 4)]}!</p>", unsafe_allow_html=True)
        if st.button("🔄 Play Again"):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()
    else:
        q = st.session_state.quiz[st.session_state.i]
        st.markdown(f"<div class='timer'>⏰ {timer()}</div>", unsafe_allow_html=True)
        progress = (st.session_state.i + 1) / len(quiz)
        st.markdown(f"<div class='progress'><div class='fill' style='width:{progress*100}%'></div></div>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center;'><strong>{st.session_state.i+1}/100</strong> • Score: {st.session_state.score}</p>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class='qbox'>
            <span class='badge {q['difficulty'].lower()}'>{q['difficulty']}</span>
            <span class='badge' style='background:#7b2cbf;'>#{q['category']}</span>
            <p style='margin:1rem 0; font-size:1.2rem;'><strong>{q['question']}</strong></p>
        </div>
        """, unsafe_allow_html=True)

        for opt in q["shuffled"]:
            key = f"opt_{q['id']}_{opt}"
            cls = "opt"
            if st.session_state.selected == opt:
                cls += " correct" if opt == q["answer"] else " wrong"
            if st.button(opt, key=key, disabled=bool(st.session_state.selected)):
                if not st.session_state.selected:
                    st.session_state.selected = opt
                    st.session_state.answers[st.session_state.i] = opt
                    if opt == q["answer"]:
                        st.session_state.score += 2
                    st.rerun()

        if st.session_state.selected:
            ans = q["answer"]
            exp = q["explanation"]
            color = "#34c759" if st.session_state.selected == ans else "#ff3b30"
            icon = "Correct!" if st.session_state.selected == ans else "Wrong!"
            st.markdown(f"<p style='text-align:center; color:{color}; font-weight:bold; font-size:1.3rem;'>{icon} {exp}</p>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("◀ Back", disabled=st.session_state.i==0):
                st.session_state.i -= 1
                st.session_state.selected = st.session_state.answers.get(st.session_state.i)
                st.rerun()
        with col2:
            if st.button("Next ▶"):
                st.session_state.i += 1
                st.session_state.selected = st.session_state.answers.get(st.session_state.i)
                st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
