import streamlit as st
import random
from datetime import datetime
import streamlit.components.v1 as components

quiz = [
    {"question": "Which function shows a message popup?", "options": ["alert()", "prompt()", "confirm()", "message()"], "answer": "alert()"},
    {"question": "What does alert('Hello') display?", "options": ["'Hello'", "undefined", "null", "Error"], "answer": "'Hello'"},
    {"question": "What is alert()'s return value?", "options": ["string", "undefined", "null", "boolean"], "answer": "undefined"},
    {"question": "What does alert(5 + 3) show?", "options": ["'5 + 3'", "8", "'8'", "Error"], "answer": "'8'"},
    {"question": "How do you add a line break in alert?", "options": ["<br>", "\\n", "/n", ";"], "answer": "\\n"},
    {"question": "What does alert('Hi\\nThere') show?", "options": ["HiThere", "Hi There", "Hi\\nThere", "Error"], "answer": "Hi There"},
    {"question": "Can alert() take multiple arguments?", "options": ["Yes", "No", "Only strings", "Only numbers"], "answer": "No"},
    {"question": "What happens if alert() has no argument?", "options": ["Empty popup", "Throws error", "Shows 'undefined'", "Does nothing"], "answer": "Shows 'undefined'"},
    {"question": "How do you declare a string variable?", "options": ["let str = 'text';", "let str = text;", "string str = 'text';", "var str = (text);"], "answer": "let str = 'text';"},
    {"question": "What is typeof 'code'?", "options": ["'string'", "'text'", "'object'", "'char'"], "answer": "'string'"},
    {"question": "What is 'hello'.length?", "options": ["4", "5", "6", "undefined"], "answer": "5"},
    {"question": "What does 'test'.toUpperCase() return?", "options": ["'TEST'", "'test'", "'Test'", "undefined"], "answer": "'TEST'"},
    {"question": "What is 'code'[1]?", "options": ["'c'", "'o'", "'d'", "undefined"], "answer": "'o'"},
    {"question": "What does 'hi'.charAt(0) return?", "options": ["'h'", "'i'", "0", "undefined"], "answer": "'h'"},
    {"question": "What is let str = 'abc'; str = 'def';?", "options": ["'abc'", "'def'", "undefined", "Error"], "answer": "'def'"},
    {"question": "What does 'javascript'.toLowerCase() return?", "options": ["'JAVASCRIPT'", "'javascript'", "'Javascript'", "undefined"], "answer": "'javascript'"},
    {"question": "Which is a valid number declaration?", "options": ["let num = '10';", "let num = 10;", "let num = ten;", "let num = [10];"], "answer": "let num = 10;"},
    {"question": "What is typeof 100?", "options": ["'number'", "'int'", "'float'", "'integer'"], "answer": "'number'"},
    {"question": "What does parseInt('25') return?", "options": ["25", "'25'", "NaN", "undefined"], "answer": "25"},
    {"question": "What is parseFloat('4.5')?", "options": ["4", "4.5", "'4.5'", "NaN"], "answer": "4.5"},
    {"question": "What does Number('50') return?", "options": ["50", "'50'", "NaN", "undefined"], "answer": "50"},
    {"question": "What is let num = 3; num = 7;?", "options": ["3", "7", "undefined", "Error"], "answer": "7"},
    {"question": "What does isNaN('abc') return?", "options": ["true", "false", "NaN", "undefined"], "answer": "true"},
    {"question": "What is typeof 7.5?", "options": ["'number'", "'float'", "'double'", "'decimal'"], "answer": "'number'"},
    {"question": "Which is a legal variable name?", "options": ["myVar", "1var", "my-var", "let"], "answer": "myVar"},
    {"question": "Which can start a variable name?", "options": ["number", "letter", "_", "Both B and C"], "answer": "Both B and C"},
    {"question": "Which is NOT a reserved keyword?", "options": ["if", "else", "value", "while"], "answer": "value"},
    {"question": "Is 'my_name' a legal variable name?", "options": ["Yes", "No", "Only in strict mode", "Only with let"], "answer": "Yes"},
    {"question": "What happens if you use 'return' as a variable name?", "options": ["Works fine", "SyntaxError", "ReferenceError", "undefined"], "answer": "SyntaxError"},
    {"question": "Which is a valid variable name?", "options": ["$count", "count!", "count#", "count space"], "answer": "$count"},
    {"question": "Is '2start' a legal variable name?", "options": ["Yes", "No", "Only in strict mode", "Only with var"], "answer": "No"},
    {"question": "What is the convention for constants?", "options": ["camelCase", "UPPER_CASE", "PascalCase", "kebab-case"], "answer": "UPPER_CASE"},
    {"question": "What is 4 + 2 * 3?", "options": ["18", "10", "12", "9"], "answer": "10"},
    {"question": "What is 15 / 3 - 1?", "options": ["4", "5", "6", "2"], "answer": "4"},
    {"question": "What is 10 % 3?", "options": ["1", "3", "0", "2"], "answer": "1"},
    {"question": "What is 7 * 2 + 1?", "options": ["14", "15", "13", "16"], "answer": "15"},
    {"question": "What is 20 - 8 / 4?", "options": ["18", "12", "10", "6"], "answer": "18"},
    {"question": "What is 3 + 5 - 2?", "options": ["6", "8", "10", "4"], "answer": "6"},
    {"question": "What does 3 ** 2 return?", "options": ["6", "9", "8", "Error"], "answer": "9"},
    {"question": "What does x++ do if x is 4?", "options": ["3", "4", "5", "Error"], "answer": "5"},
    {"question": "What is x -= 2 if x is 7?", "options": ["5", "9", "7", "Error"], "answer": "5"},
    {"question": "What does ++x do if x is 3?", "options": ["2", "3", "4", "Error"], "answer": "4"},
    {"question": "What is 2 ** 4?", "options": ["8", "16", "6", "Error"], "answer": "16"},
    {"question": "What does x += 3 do if x is 5?", "options": ["8", "5", "3", "Error"], "answer": "8"},
    {"question": "What is (3 + 2) * 4?", "options": ["20", "14", "12", "10"], "answer": "20"},
    {"question": "What does (10 / 2) + 3 return?", "options": ["8", "15", "6", "Error"], "answer": "8"},
    {"question": "What is 6 * (2 + 1)?", "options": ["18", "12", "9", "15"], "answer": "18"},
    {"question": "How do you make 2 + 3 * 4 equal 20?", "options": ["Use spaces", "Use parentheses", "Use comments", "Use variables"], "answer": "Use parentheses"},
    {"question": "What is 8 / (2 + 2)?", "options": ["2", "4", "1", "Error"], "answer": "2"},
    {"question": "What does (5 - 1) * 2 return?", "options": ["8", "6", "10", "4"], "answer": "8"},
    {"question": "What is 'Hi' + ' ' + 'There'?", "options": ["'HiThere'", "'Hi There'", "'Hi + There'", "Error"], "answer": "'Hi There'"},
    {"question": "What is '10' + 5?", "options": ["15", "'15'", "'105'", "Error"], "answer": "'105'"},
    {"question": "What is `Hello ${'World'}`?", "options": ["'HelloWorld'", "'Hello World'", "'Hello ${World}'", "Error"], "answer": "'Hello World'"},
    {"question": "What is 2 + '3'?", "options": ["5", "'5'", "'23'", "Error"], "answer": "'23'"},
    {"question": "How do you convert a number to string for concatenation?", "options": ["num.toString()", "String(num)", "num + ''", "All of the above"], "answer": "All of the above"},
    {"question": "What is 'abc' + null?", "options": ["'abcnull'", "'abc'", "null", "Error"], "answer": "'abcnull'"},
    {"question": "What is `Sum: ${3 + 2}`?", "options": ["'Sum: 5'", "'Sum: 3+2'", "'Sum: 32'", "Error"], "answer": "'Sum: 5'"},
    {"question": "What is 'x' + 'y' + 'z'?", "options": ["'xyz'", "'x y z'", "'x+y+z'", "Error"], "answer": "'xyz'"},
    {"question": "What does prompt('Name') return on Cancel?", "options": ["null", "empty string", "undefined", "Error"], "answer": "null"},
    {"question": "What does confirm('OK?') return on OK?", "options": ["true", "false", "'OK'", "null"], "answer": "true"},
    {"question": "What does prompt('Age', '20') return if user enters '25'?", "options": ["20", "25", "'25'", "null"], "answer": "'25'"},
    {"question": "How do you convert prompt input to a number?", "options": ["parseInt(prompt())", "prompt().toNumber()", "prompt().parse()", "Not possible"], "answer": "parseInt(prompt())"},
    {"question": "What does prompt('Enter') return if user clicks OK with no input?", "options": ["null", "empty string", "undefined", "Error"], "answer": "empty string"},
    {"question": "What does confirm('Delete?') return on Cancel?", "options": ["true", "false", "'Cancel'", "null"], "answer": "false"},
    {"question": "What is Number(prompt('Num', '10')) if user enters '5'?", "options": ["5", "'5'", "10", "null"], "answer": "5"},
    {"question": "Can prompt() have multiple default values?", "options": ["Yes", "No", "Only strings", "Only numbers"], "answer": "No"},
    {"question": "What is the correct if statement syntax?", "options": ["if (x == 5) {}", "if x = 5 {}", "if (x = 5) {}", "if x == 5 then"], "answer": "if (x == 5) {}"},
    {"question": "When does an if statement run its block?", "options": ["Always", "When true", "When false", "At runtime"], "answer": "When true"},
    {"question": "What does if (x) {} evaluate?", "options": ["A number", "A boolean", "A string", "Any value"], "answer": "Any value"},
    {"question": "What happens if if (x == 5) {} is false?", "options": ["Runs block", "Skips block", "Throws error", "Returns null"], "answer": "Skips block"},
    {"question": "What does x === 5 check?", "options": ["Value only", "Type only", "Value and type", "Reference"], "answer": "Value and type"},
    {"question": "What is 5 == '5'?", "options": ["true", "false", "undefined", "Error"], "answer": "true"},
    {"question": "What does 10 !== '10' return?", "options": ["true", "false", "undefined", "Error"], "answer": "true"},
    {"question": "What is 7 > 4?", "options": ["true", "false", "undefined", "Error"], "answer": "true"},
    {"question": "What does 3 <= 3 return?", "options": ["true", "false", "undefined", "Error"], "answer": "true"},
    {"question": "What is '5' != 5?", "options": ["true", "false", "undefined", "Error"], "answer": "false"},
    {"question": "What does else do in an if...else statement?", "options": ["Runs if true", "Runs if false", "Always runs", "Skips condition"], "answer": "Runs if false"},
    {"question": "What is the output of: let x = 3; if (x > 5) { console.log('big'); } else { console.log('small'); }?", "options": ["'big'", "'small'", "undefined", "Error"], "answer": "'small'"},
    {"question": "What does else if do?", "options": ["Multiple conditions", "Error handling", "Looping", "Variable declaration"], "answer": "Multiple conditions"},
    {"question": "What is the output of: let x = 0; if (x > 0) { console.log('positive'); } else if (x < 0) { console.log('negative'); } else { console.log('zero'); }?", "options": ["'positive'", "'negative'", "'zero'", "Error"], "answer": "'zero'"},
    {"question": "How many else if statements can you have?", "options": ["1", "2", "As many as needed", "None"], "answer": "As many as needed"},
    {"question": "What does x > 3 && x < 7 test?", "options": ["x is between 3 and 7", "x is less than 3 or greater than 7", "x equals 3 or 7", "x is not a number"], "answer": "x is between 3 and 7"},
    {"question": "What is true || false?", "options": ["true", "false", "undefined", "Error"], "answer": "true"},
    {"question": "What does x === 4 || x === 8 return if x is 8?", "options": ["true", "false", "undefined", "Error"], "answer": "true"},
    {"question": "What is !true?", "options": ["true", "false", "undefined", "Error"], "answer": "false"},
    {"question": "What does 3 > 5 || 5 < 10 return?", "options": ["true", "false", "undefined", "Error"], "answer": "true"},
    {"question": "What is a nested if statement?", "options": ["An if inside another if", "An if after else", "Multiple else ifs", "An if with many conditions"], "answer": "An if inside another if"},
    {"question": "What is the output of: let x = 7; if (x > 5) { if (x < 10) { console.log('valid'); } }?", "options": ["'valid'", "undefined", "Error", "Nothing"], "answer": "'valid'"},
    {"question": "What does: let x = 12; if (x > 10) { if (x < 15) { console.log('range'); } } output?", "options": ["'range'", "undefined", "Error", "Nothing"], "answer": "'range'"},
    {"question": "What is the output of: let x = 3; if (x > 0) { if (x > 5) { console.log('big'); } else { console.log('small'); } }?", "options": ["'big'", "'small'", "undefined", "Error"], "answer": "'small'"},
    {"question": "Can a nested if have an else?", "options": ["Yes", "No", "Only in strict mode", "Only with let"], "answer": "Yes"},
    {"question": "How do you create an array?", "options": ["let arr = [1, 2, 3];", "let arr = (1, 2, 3);", "let arr = {1, 2, 3};", "let arr = 1, 2, 3;"], "answer": "let arr = [1, 2, 3];"},
    {"question": "What is [4, 5, 6].length?", "options": ["2", "3", "4", "undefined"], "answer": "3"},
    {"question": "What does [1, 2, 3][2] return?", "options": ["1", "2", "3", "undefined"], "answer": "3"},
    {"question": "What does [1, 2, 3].includes(1) return?", "options": ["true", "false", "undefined", "Error"], "answer": "true"},
    {"question": "What does [1, 2, 3].join(',') return?", "options": ["'1,2,3'", "'123'", "'1, 2, 3'", "Error"], "answer": "'1,2,3'"},
    {"question": "What does [1, 2, 3].push(4) do?", "options": ["Adds 4 to start", "Adds 4 to end", "Removes 4", "Replaces 3"], "answer": "Adds 4 to end"},
    {"question": "What does [1, 2, 3].pop() return?", "options": ["1", "2", "3", "undefined"], "answer": "3"},
    {"question": "What does [1, 2, 3].slice(0, 2) return?", "options": ["[1, 2]", "[2, 3]", "[1]", "Error"], "answer": "[1, 2]"},
    {"question": "What is the output of: if (5 < 10) { console.log('yes'); }?", "options": ["'yes'", "undefined", "true", "Error"], "answer": "'yes'"},
    {"question": "What does true && false return?", "options": ["true", "false", "undefined", "Error"], "answer": "false"}
]

st.set_page_config(page_title="JS Quiz Pro", page_icon="🚀", layout="wide")

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

st.markdown("""
    <style>
    body {
        background: linear-gradient(180deg, #1a1a3b, #2c2c54);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    .main-container {
        background: #2c2c54;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        max-width: 900px;
        margin: 30px auto;
    }
    .stButton>button {
        background: linear-gradient(45deg, #6b21a8, #a855f7);
        color: #ffffff;
        border: none;
        border-radius: 12px;
        padding: 15px;
        width: 100%;
        font-size: 16px;
        font-weight: 600;
        margin: 8px 0;
        cursor: pointer;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #8b5cf6, #c084fc);
        transform: translateY(-3px);
    }
    .question-container {
        background: #373760;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    .feedback-correct {
        color: #34c759;
        font-weight: 700;
        font-size: 20px;
        margin: 20px 0;
    }
    .feedback-wrong {
        color: #ff3b30;
        font-weight: 700;
        font-size: 20px;
        margin: 20px 0;
    }
    .progress-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .title {
        font-size: 42px;
        text-align: center;
        margin-bottom: 10px;
    }
    .caption {
        text-align: center;
        color: #b0b0d0;
        font-size: 18px;
        margin-bottom: 30px;
    }
    .timer {
        font-size: 15px;
        color: #ff6b6b;
        font-weight: 700;
        text-align: center;
        margin-top: 15px;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
""", unsafe html=True)

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
        'time_left': 300
    })

timer_html = f"""
<div id="timer" class="timer">⏰ Time Left: {st.session_state.time_left//60:02d}:{st.session_state.time_left%60:02d}</div>
<script>
    let timeLeft = {st.session_state.time_left};
    const timerElement = document.getElementById('timer');
    function updateTimer() {{
        if (timeLeft <= 0) {{
            timerElement.innerHTML = '⏰ Time Up!';
            window.Streamlit.setComponentValue({{time_up: true}});
            return;
        }}
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        timerElement.innerHTML = `⏰ Time Left: ${{'${{minutes}}'.padStart(2, '0')}}:${{'${{seconds}}'.padStart(2, '0')}}`;
        timeLeft--;
        setTimeout(updateTimer, 1000);
    }}
    updateTimer();
</script>
"""
components.html(timer_html, height=50)

if st.session_state.get('timer_value', {}).get('time_up', False):
    st.session_state.show_results = True

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1 class="title">😈 JavaScript Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Test Your JavaScript Knowledge</p>', unsafe_allow_html=True)

if not st.session_state.quiz_data:
    st.error("Quiz data is empty")
else:
    progress = st.session_state.current_q / len(st.session_state.quiz_data)
    progress_percentage = int(progress * 100)
    progress_svg = f"""
    <div class="progress-container">
        <svg width="100" height="100" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="45" stroke="#4b4b6b" stroke-width="10" fill="none"/>
            <circle cx="50" cy="50" r="45" stroke="#6b21a8" stroke-width="10" fill="none"
                stroke-dasharray="283" stroke-dashoffset="{283 * (1 - progress)}"/>
            <text x="50" y="55" fill="#ffffff" font-size="20" text-anchor="middle">{progress_percentage}%</text>
        </svg>
        <div style="color: #b0b0d0; font-size: 14px; margin-top: 10px;">
            Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
        </div>
    </div>
    """
    st.markdown(progress_svg, unsafe_allow_html=True)

    if not st.session_state.show_results:
        with st.container():
            st.markdown('<div class="question-container">', unsafe_html=True)
            q = st.session_state.quiz_data[st.session_state.current_q]
            st.markdown(f"### Question {st.session_state.current_q + 1}")
            st.markdown(f"**{q['question']}")

            for i, option in enumerate(q['display_options']):
                if st.button(option, key=f"q{i}", use_container_width=True, disabled=st.session_state.selected_option is not None):
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

            col_prev, col_next = st.columns([1, 1])
            with col_prev:
                if st.button("⬅ Previous", disabled=st.session_state.current_q == 0):
                    if st.session_state.answers[st.session_state.current_q]['is_correct']:
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
        time_taken = datetime.now() - st.session_state.start_time
        accuracy = (st.session_state.score / len(quiz)) * 100
        st.markdown('<div class="question-container">', unsafe_allow_html=True)
        st.markdown(f'<h2 style="color: #34c759; text-align: center;">🏆 Score: {st.session_state.score}/{len(quiz)}</h2>', unsafe_allow_html=True)
        st.markdown(f"""
        <h3>📊 Results</h3>
        <div style="color: #b0b0d0; font-size: 16px;">
            - ⏱️ Time: {time_taken.seconds // 60}m {time_taken.seconds % 60}s<br>
            - 🎯 Accuracy: {accuracy:.1f}%<br>
            - ✅ Correct: {st.session_state.score}<br>
            - ❌ Wrong: {len(quiz) - st.session_state.score}
        </div>
        """, unsafe_allow_html=True)

        leaderboard = [
            {"name": "Alex", "score": 8, "time": 180},
            {"name": "Sam", "score": 7, "time": 200},
            {"name": "You", "score": st.session_state.score, "time": time_taken.seconds}
        ]
        leaderboard.sort(key=lambda x: (-x['score'], x['time']))
        st.markdown('<h3>🏅 Leaderboard</h3>', unsafe_allow_html=True)
        for i, entry in enumerate(leaderboard[:5], 1):
            st.markdown(f'<div style="color: #b0b0d0;">{i}. <b>{entry["name"]}</b>: {entry["score"]}/{len(quiz)} (Time: {entry["time"]//60}m {entry["time"]%60}s)</div>', unsafe_allow_html=True)

        with st.expander("📝 Review", expanded=True):
            for i, answer in enumerate(st.session_state.answers):
                if answer:
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

with st.sidebar:
    st.markdown('<div style="color: #ffffff; font-size: 24px;">📚 Quiz Info</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color: #b0b0d0;">Questions: {len(quiz)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color: #b0b0d0;">Score: {st.session_state.score}/{len(quiz)}</div>', unsafe_allow_html=True)
    if not st.session_state.show_results:
        st.markdown(f'<div style="color: #b0b0d0;">Timer above ⬆️</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="color: #b0b0d0;">Time: {time_taken.seconds // 60}m {time_taken.seconds % 60}s</div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-color: #4b4b6b;">', unsafe_allow_html=True)
    st.markdown('<div style="color: #ffffff; font-size: 18px;">ℹ️ About</div>', unsafe_allow_html=True)
    st.markdown('<div style="color: #b0b0d0; font-size: 14px;">JS Quiz Pro tests JavaScript skills.</div>', unsafe_allow_html=True)
