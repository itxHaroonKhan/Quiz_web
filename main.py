import streamlit as st
import random
from datetime import datetime

# Quiz data (same as provided, 50 questions)
quiz = [
    {"question": "What happens when this alert is executed?\n```javascript\nalert('Hello\\nWorld');\n```", "options": ["Displays 'Hello World'", "Displays 'Hello' and 'World' on two lines", "Throws an error", "Displays 'Hello\\nWorld'"], "answer": "Displays 'Hello' and 'World' on two lines", "difficulty": "Easy", "hint": "The \\n character creates a new line in strings."},
    # ... (Include all 50 questions as in your original code; truncated for brevity)
    # Add the remaining 49 questions here to avoid repetition
]

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

# Simplified CSS for reliability
st.markdown("""
    <style>
    .main-container { background: #2c2c54; padding: 20px; border-radius: 10px; max-width: 800px; margin: 10px auto; color: #ffffff; font-family: Arial, sans-serif; }
    .stButton>button { background: #6b21a8; color: #ffffff; border: none; border-radius: 8px; padding: 10px; width: 100%; font-size: 14px; margin: 5px 0; }
    .stButton>button:hover { background: #a855f7; }
    .question-container { background: #373760; padding: 15px; border-radius: 8px; margin-bottom: 10px; }
    .feedback-correct { color: #34c759; font-weight: bold; }
    .feedback-wrong { color: #ff3b30; font-weight: bold; }
    .progress-bar { background: #4b4b6b; border-radius: 5px; height: 8px; }
    .progress-fill { background: #6b21a8; height: 100%; border-radius: 5px; }
    .timer { color: #ff6b6b; font-weight: bold; text-align: center; }
    .hint { color: #b0b0d0; background: #2c2c54; padding: 8px; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'quiz_data' not in st.session_state:
    st.session_state.update({
        'quiz_data': shuffle_quiz(),
        'score': 0,
        'current_q': 0,
        'start_time': datetime.now(),
        'answers': [None] * len(quiz),
        'show_results': False,
        'selected_option': None,
        'feedback': None,
        'time_left': 1800
    })

# Timer logic
def update_timer():
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.session_state.time_left = max(1800 - elapsed, 0)
    if st.session_state.time_left <= 0 and not st.session_state.show_results:
        st.session_state.show_results = True
        st.rerun()

# Main UI
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1>🚀 JavaScript Quiz</h1>', unsafe_allow_html=True)

if not st.session_state.quiz_data:
    st.error("No quiz questions available.")
else:
    update_timer()
    minutes = int(st.session_state.time_left // 60)
    seconds = int(st.session_state.time_left % 60)
    st.markdown(f'<div class="timer">Time Left: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

    progress = st.session_state.current_q / len(st.session_state.quiz_data)
    st.markdown(f'<div class="progress-bar"><div class="progress-fill" style="width: {progress*100}%"></div></div>', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align: center;">Question {st.session_state.current_q + 1}/{len(st.session_state.quiz_data)}</div>', unsafe_allow_html=True)

    if not st.session_state.show_results:
        with st.container():
            st.markdown('<div class="question-container">', unsafe_allow_html=True)
            q = st.session_state.quiz_data[st.session_state.current_q]
            st.markdown(f'<div>Difficulty: {q["difficulty"]}</div>', unsafe_allow_html=True)

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
                        'question': q['question'], 'user_answer': option, 'correct_answer': q['labeled_answer'], 
                        'is_correct': is_correct, 'difficulty': q['difficulty']
                    }
                    if is_correct:
                        points = {'Easy': 1, 'Medium': 2, 'Hard': 3}[q['difficulty']]
                        st.session_state.score += points
                    st.rerun()

            if st.session_state.feedback:
                if st.session_state.feedback['is_correct']:
                    st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)

            with st.expander("Show Hint"):
                st.markdown(f'<div class="hint">{q["hint"]}</div>', unsafe_allow_html=True)

            col_prev, col_next = st.columns(2)
            with col_prev:
                if st.button("Previous", disabled=st.session_state.current_q == 0):
                    if st.session_state.answers[st.session_state.current_q] and st.session_state.answers[st.session_state.current_q]['is_correct']:
                        points = {'Easy': 1, 'Medium': 2, 'Hard': 3}[st.session_state.answers[st.session_state.current_q]['difficulty']]
                        st.session_state.score -= points
                    st.session_state.current_q -= 1
                    st.session_state.selected_option = None
                    st.session_state.feedback = None
                    st.rerun()
            with col_next:
                if st.session_state.current_q < len(st.session_state.quiz_data) - 1:
                    if st.button("Next", disabled=st.session_state.selected_option is None):
                        st.session_state.current_q += 1
                        st.session_state.selected_option = None
                        st.session_state.feedback = None
                        st.rerun()
                else:
                    if st.button("Finish", disabled=st.session_state.selected_option is None):
                        st.session_state.show_results = True
                        st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    else:
        time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 1800)
        total_possible_score = sum({'Easy': 1, 'Medium': 2, 'Hard': 3}[q['difficulty']] for q in quiz)
        accuracy = (st.session_state.score / total_possible_score) * 100 if total_possible_score > 0 else 0
        st.markdown('<div class="question-container">', unsafe_allow_html=True)
        st.markdown(f'<h2 style="color: #34c759; text-align: center;">Score: {st.session_state.score}/{total_possible_score}</h2>', unsafe_allow_html=True)
        st.markdown(f"""
            <h3>Results</h3>
            <div>
                - Time: {int(time_taken) // 60}m {int(time_taken) % 60}s<br>
                - Accuracy: {accuracy:.1f}%<br>
                - Correct: {sum(1 for a in st.session_state.answers if a and a['is_correct'])}<br>
                - Wrong: {sum(1 for a in st.session_state.answers if a and not a['is_correct'])}
            </div>
        """, unsafe_allow_html=True)

        leaderboard = [
            {"name": "Alex", "score": 45, "time": 600},
            {"name": "Sam", "score": 40, "time": 700},
            {"name": "You", "score": st.session_state.score, "time": int(time_taken)}
        ]
        leaderboard.sort(key=lambda x: (-x['score'], x['time']))
        st.markdown('<h3>Leaderboard</h3>', unsafe_allow_html=True)
        for i, entry in enumerate(leaderboard[:5], 1):
            st.markdown(f'<div>{i}. <b>{entry["name"]}</b>: {entry["score"]}/{total_possible_score} (Time: {entry["time"]//60}m {entry["time"]%60}s)</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
