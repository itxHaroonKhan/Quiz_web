import streamlit as st
import random
from datetime import datetime
import streamlit.components.v1 as components

# Corrected Quiz Data (fixed the block-scoping question)
quiz = [
    # Alerts
    {
        "question": "Which method displays an alert dialog box with a message?",
        "options": [
            "alertBox()",
            "message()",
            "alert()",
            "showDialog()"
        ],
        "answer": "alert()"
    },
    {
        "question": "What happens when you call alert('Hello')?",
        "options": [
            "Prints 'Hello' to console",
            "Displays 'Hello' in a popup with OK button",
            "Creates a variable named Hello",
            "Nothing happens"
        ],
        "answer": "Displays 'Hello' in a popup with OK button"
    },

    # Variables for Strings
    {
        "question": "How do you declare a string variable?",
        "options": [
            "let str = 'text';",
            "let str = text;",
            "string str = 'text';",
            "var str = text;"
        ],
        "answer": "let str = 'text';"
    },
    {
        "question": "What is the result of typeof 'hello'?",
        "options": [
            "'string'",
            "'text'",
            "'object'",
            "'char'"
        ],
        "answer": "'string'"
    },

    # Variables for Numbers
    {
        "question": "Which is NOT a valid number declaration?",
        "options": [
            "let num = 10;",
            "let num = 10.5;",
            "let num = '10';",
            "let num = 1_000"
        ],
        "answer": "let num = '10';"
    },
    {
        "question": "What is the result of typeof 42?",
        "options": [
            "'number'",
            "'int'",
            "'float'",
            "'integer'"
        ],
        "answer": "'number'"
    },

    # Variable Names Legal and Illegal
    {
        "question": "Which is a legal variable name?",
        "options": [
            "1stPlace",
            "first-name",
            "firstName",
            "let"
        ],
        "answer": "firstName"
    },
    {
        "question": "Which character CANNOT start a variable name?",
        "options": [
            "letter",
            "$",
            "_",
            "number"
        ],
        "answer": "number"
    },

    # Math Expressions: Familiar Operators
    {
        "question": "What is 10 % 3?",
        "options": [
            "3",
            "1",
            "0",
            "3.333"
        ],
        "answer": "1"
    },
    {
        "question": "What is the result of 2 + 3 * 4?",
        "options": [
            "20",
            "14",
            "24",
            "10"
        ],
        "answer": "14"
    },

    # Math Expressions: Unfamiliar Operators
    {
        "question": "What does the ** operator do?",
        "options": [
            "Multiplication",
            "Exponentiation",
            "Concatenation",
            "Division"
        ],
        "answer": "Exponentiation"
    },
    {
        "question": "What is 2 ** 3?",
        "options": [
            "6",
            "8",
            "23",
            "5"
        ],
        "answer": "8"
    },

    # Math Expressions: Eliminating Ambiguity
    {
        "question": "How can you make (2 + 3) * 4 clearer?",
        "options": [
            "Use more spaces",
            "Add comments",
            "Use parentheses",
            "All of the above"
        ],
        "answer": "All of the above"
    },
    {
        "question": "What does operator precedence determine?",
        "options": [
            "The order of operations",
            "Variable names",
            "Data types",
            "Function outputs"
        ],
        "answer": "The order of operations"
    },

    # Concatenating Text Strings
    {
        "question": "What is 'Hello' + ' ' + 'World'?",
        "options": [
            "'HelloWorld'",
            "'Hello World'",
            "'Hello + World'",
            "Error"
        ],
        "answer": "'Hello World'"
    },
    {
        "question": "What is '5' + 2?",
        "options": [
            "7",
            "'52'",
            "Error",
            "5"
        ],
        "answer": "'52'"
    },

    # Prompts
    {
        "question": "What does prompt() return if user clicks Cancel?",
        "options": [
            "empty string",
            "null",
            "undefined",
            "false"
        ],
        "answer": "null"
    },
    {
        "question": "How do you add a default value to prompt()?",
        "options": [
            "prompt('Message', 'default')",
            "prompt('Message').default('value')",
            "prompt().setDefault('value')",
            "You can't"
        ],
        "answer": "prompt('Message', 'default')"
    },

    # if statements
    {
        "question": "What is the correct if statement syntax?",
        "options": [
            "if x == 5 {}",
            "if (x = 5) {}",
            "if (x === 5) {}",
            "if x = 5 then"
        ],
        "answer": "if (x === 5) {}"
    },
    {
        "question": "When does an if statement execute its code block?",
        "options": [
            "Always",
            "When condition is truthy",
            "When condition is false",
            "Only at runtime"
        ],
        "answer": "When condition is truthy"
    },

    # Comparison Operators
    {
        "question": "Which operator checks value AND type?",
        "options": [
            "==",
            "===",
            "=",
            "!=="
        ],
        "answer": "==="
    },
    {
        "question": "What is 5 == '5'?",
        "options": [
            "true",
            "false",
            "Error",
            "null"
        ],
        "answer": "true"
    },

    # if...else and else if statements
    {
        "question": "What is the purpose of else if?",
        "options": [
            "To create multiple conditions",
            "To handle errors",
            "To loop through code",
            "To declare variables"
        ],
        "answer": "To create multiple conditions"
    },
    {
        "question": "How many else if blocks can you have?",
        "options": [
            "Only 1",
            "Up to 3",
            "As many as needed",
            "Exactly 2"
        ],
        "answer": "As many as needed"
    },

    # Testing Sets of Conditions
    {
        "question": "What is (x > 5 && x < 10) testing?",
        "options": [
            "If x is between 5 and 10",
            "If x is less than 5 or greater than 10",
            "If x equals 5 or 10",
            "If x is not a number"
        ],
        "answer": "If x is between 5 and 10"
    },
    {
        "question": "Which operator would test if x is 5 OR 10?",
        "options": [
            "x == 5 && x == 10",
            "x === 5 || x === 10",
            "x == 5 ! x == 10",
            "x === 5 & x === 10"
        ],
        "answer": "x === 5 || x === 10"
    },

    # Nested if statements
    {
        "question": "What is a nested if statement?",
        "options": [
            "An if inside another if",
            "An if after an else",
            "Multiple else ifs",
            "An if with many conditions"
        ],
        "answer": "An if inside another if"
    },
    {
        "question": "When would you use nested ifs?",
        "options": [
            "To check multiple related conditions",
            "To make code run faster",
            "To reduce code length",
            "To declare variables"
        ],
        "answer": "To check multiple related conditions"
    },

    # Arrays
    {
        "question": "How do you create an array with 3 elements?",
        "options": [
            "let arr = [1, 2, 3];",
            "let arr = (1, 2, 3);",
            "let arr = {1, 2, 3};",
            "let arr = new Array(1 2 3);"
        ],
        "answer": "let arr = [1, 2, 3];"
    },
    {
        "question": "What is arr.length for [10, 20, 30]?",
        "options": [
            "2",
            "3",
            "30",
            "undefined"
        ],
        "answer": "3"
    },

    # Arrays: Adding and Removing Elements
    {
        "question": "Which method adds to the end of an array?",
        "options": [
            "push()",
            "pop()",
            "shift()",
            "unshift()"
        ],
        "answer": "push()"
    },
    {
        "question": "What does pop() return?",
        "options": [
            "The removed element",
            "The new array length",
            "The array without last element",
            "undefined"
        ],
        "answer": "The removed element"
    },

    # Arrays: Removing, Inserting, Extracting
    {
        "question": "What does splice(1, 2) do?",
        "options": [
            "Removes 2 elements starting at index 1",
            "Adds 2 elements at index 1",
            "Extracts elements without modifying array",
            "Reverses the array"
        ],
        "answer": "Removes 2 elements starting at index 1"
    },
    {
        "question": "How do you extract a portion of an array without modifying it?",
        "options": [
            "slice()",
            "splice()",
            "cut()",
            "extract()"
        ],
        "answer": "slice()"
    }
]



# Set page configuration
st.set_page_config(page_title="JS Quiz Pro", page_icon="🚀", layout="wide")

def shuffle_quiz():
    """Shuffle questions and options randomly, mapping options to A, B, C, D"""
    if not quiz:
        st.error("No quiz data available. Please add questions.")
        return []
    shuffled = random.sample(quiz, len(quiz))
    for q in shuffled:
        labeled_options = list(zip(q['options'], ['A', 'B', 'C', 'D'][:len(q['options'])]))
        random.shuffle(labeled_options)
        q['display_options'] = [f"{label}: {option}" for option, label in labeled_options]
        for option, label in labeled_options:
            if option == q['answer']:
                q['labeled_answer'] = f"{label}: {option}"
                break
    return shuffled

# Custom CSS for premium UI
st.markdown("""
    <style>
    body {
        background: linear-gradient(180deg, #1a1a3b, #2c2c54);
        color: #ffffff;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    .main-container {
        background: #2c2c54;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4), inset 0 2px 5px rgba(255,255,255,0.1);
        max-width: 900px;
        margin: 30px auto;
        animation: fadeIn 0.8s ease;
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
        transition: all 0.3s ease;
        margin: 8px 0;
        cursor: pointer;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #8b5cf6, #c084fc);
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.4);
    }
    .stButton>button:active {
        transform: translateY(0);
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .stButton>button:disabled {
        background: #4b4b6b;
        cursor: not-allowed;
        opacity: 0.7;
    }
    .question-container {
        background: #373760;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3), inset 0 2px 3px rgba(255,255,255,0.05);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .question-container:hover {
        transform: translateY(-5px);
    }
    .feedback-correct {
        color: #34c759;
        font-weight: 700;
        font-size: 20px;
        margin: 20px 0;
        animation: bounce 0.5s;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .feedback-wrong {
        color: #ff3b30;
        font-weight: 700;
        font-size: 20px;
        margin: 20px 0;
        animation: shake 0.5s;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .progress-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .title {
        font-size: 42px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 0 2px 5px rgba(0,0,0,0.3);
    }
    .caption {
        text-align: center;
        color: #b0b0d0;
        font-size: 18px;
        margin-bottom: 30px;
    }
    .sidebar .sidebar-content {
        background: #2c2c54;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .timer {
        font-size: 20px;
        color: #ff6b6b;
        font-weight: 700;
        text-align: center;
        margin-top: 15px;
        text-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-12px); }
        60% { transform: translateY(-6px); }
    }
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-6px); }
        20%, 40%, 60%, 80% { transform: translateX(6px); }
    }
    @media (max-width: 600px) {
        .main-container {
            padding: 20px;
            margin: 15px;
        }
        .stButton>button {
            font-size: 14px;
            padding: 12px;
        }
        .question-container {
            padding: 20px;
        }
        .title {
            font-size: 32px;
        }
        .caption {
            font-size: 16px;
        }
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
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
        'time_left': 1800  # 30 minutes in seconds
    })

# JavaScript timer
timer_html = """
<div id="timer" class="timer">⏰ Time Left: 30:00</div>
<script>
    let timeLeft = """ + str(st.session_state.time_left) + """;
    const timerElement = document.getElementById('timer');
    function updateTimer() {
        if (timeLeft <= 0) {
            timerElement.innerHTML = '⏰ Time Up!';
            window.Streamlit.setComponentValue({time_up: true});
            return;
        }
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        timerElement.innerHTML = `⏰ Time Left: ${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        timeLeft--;
        setTimeout(updateTimer, 1000);
    }
    updateTimer();
</script>
"""
timer_component = components.html(timer_html, height=50)

# Check if time is up
timer_value = st.session_state.get('timer_value', {})
if timer_value.get('time_up', False):
    st.session_state.show_results = True

# Main UI
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1 class="title">😈 JavaScript Mastery Quiz 👿</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption"> by Haroon Rasheed 😎 Master JavaScript with Style</p>', unsafe_allow_html=True)

# Check if quiz data is valid
if not st.session_state.quiz_data:
    st.error("Quiz data is empty or invalid. Please check the quiz list.")
else:
    # Progress circle
    progress = st.session_state.current_q / len(st.session_state.quiz_data)
    progress_percentage = int(progress * 100)
    progress_svg = f"""
    <div class="progress-container">
        <svg width="100" height="100" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="45" stroke="#4b4b6b" stroke-width="10" fill="none"/>
            <circle cx="50" cy="50" r="45" stroke="#6b21a8" stroke-width="10" fill="none"
                stroke-dasharray="283" stroke-dashoffset="{283 * (1 - progress)}"
                style="transition: stroke-dashoffset 0.5s ease;"/>
            <text x="50" y="55" fill="#ffffff" font-size="20" text-anchor="middle">{progress_percentage}%</text>
        </svg>
        <div style="color: #b0b0d0; font-size: 14px; margin-top: 10px;">
            Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
        </div>
    </div>
    """
    st.markdown(progress_svg, unsafe_allow_html=True)

    # Quiz interface
    if not st.session_state.show_results:
        with st.container():
            st.markdown('<div class="question-container">', unsafe_allow_html=True)
            q = st.session_state.quiz_data[st.session_state.current_q]

            st.markdown(f"### Question {st.session_state.current_q + 1}")
            st.markdown(f"**{q['question']}**")

            # Display options as buttons
            for i, display_option in enumerate(q['display_options']):
                if st.button(display_option, key=f"q{st.session_state.current_q}opt{i}",
                            use_container_width=True, disabled=st.session_state.selected_option is not None):
                    original_option = display_option[3:]
                    is_correct = (display_option == q['labeled_answer'])
                    st.session_state.selected_option = display_option
                    st.session_state.feedback = {
                        'is_correct': is_correct,
                        'correct_answer': q['labeled_answer']
                    }
                    st.session_state.answers[st.session_state.current_q] = {
                        'question': q['question'],
                        'user_answer': display_option,
                        'correct_answer': q['labeled_answer'],
                        'is_correct': is_correct
                    }
                    if is_correct:
                        st.session_state.score += 1
                        try:
                            confetti_script = """
                            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                            <script>
                            confetti({
                                particleCount: 150,
                                spread: 80,
                                origin: { y: 0.6 },
                                colors: ['#6b21a8', '#a855f7', '#ffffff']
                            });
                            </script>
                            """
                            st.markdown(confetti_script, unsafe_allow_html=True)
                        except:
                            pass
                    st.rerun()

            # Display feedback
            if st.session_state.feedback:
                if st.session_state.feedback['is_correct']:
                    st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="feedback-wrong">❌ Wrong! Correct answer: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)

            # Navigation buttons
            col_prev, col_next = st.columns([1, 1])
            with col_prev:
                if st.button("⬅️ Previous", disabled=st.session_state.current_q == 0):
                    if st.session_state.answers[st.session_state.current_q] and st.session_state.answers[st.session_state.current_q]['is_correct']:
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

    # Results page
    else:
        time_taken = datetime.now() - st.session_state.start_time
        accuracy = (st.session_state.score / len(quiz)) * 100

        st.markdown('<div class="question-container">', unsafe_allow_html=True)
        st.markdown(f'<h2 style="color: #34c759; text-align: center;">🏆 Final Score: {st.session_state.score}/{len(quiz)}</h2>', unsafe_allow_html=True)
        st.markdown(f"""
        <h3 style="color: #ffffff;">📊 Performance Analysis</h3>
        <div style="color: #b0b0d0; font-size: 16px;">
            - ⏱️ Time Taken: {time_taken.seconds // 60}m {time_taken.seconds % 60}s<br>
            - 🎯 Accuracy: {accuracy:.1f}%<br>
            - ✅ Correct Answers: {st.session_state.score}<br>
            - ❌ Wrong Answers: {len(quiz) - st.session_state.score}
        </div>
        """, unsafe_allow_html=True)

        # Leaderboard
        leaderboard = [
            {"name": "Alex", "score": 8, "time": 180},
            {"name": "Sam", "score": 7, "time": 200},
            {"name": "You", "score": st.session_state.score, "time": time_taken.seconds}
        ]
        leaderboard = sorted(leaderboard, key=lambda x: (-x['score'], x['time']))

        st.markdown('<h3 style="color: #ffffff;">🏅 Leaderboard</h3>', unsafe_allow_html=True)
        for i, entry in enumerate(leaderboard[:5], 1):
            st.markdown(f'<div style="color: #b0b0d0; font-size: 16px;">{i}. <b>{entry["name"]}</b>: {entry["score"]}/{len(quiz)} (Time: {entry["time"]//60}m {entry["time"]%60}s)</div>', unsafe_allow_html=True)

        # Detailed review
        with st.expander("📝 Detailed Review", expanded=True):
            for i, answer in enumerate(st.session_state.answers):
                if answer:
                    st.markdown(f'<b style="color: #ffffff;">Q{i+1}:</b> {answer["question"]}', unsafe_allow_html=True)
                    col1, col2 = st.columns(2)
                    with col1:
                        status = "✅" if answer['is_correct'] else "❌"
                        st.markdown(f'<span style="color: #b0b0d0;">{status} Your answer: {answer["user_answer"]}</span>', unsafe_allow_html=True)
                    with col2:
                        if not answer['is_correct']:
                            st.markdown(f'<span style="color: #b0b0d0;">💡 Correct answer: {answer["correct_answer"]}</span>', unsafe_allow_html=True)
                    st.markdown('<hr style="border-color: #4b4b6b;">', unsafe_allow_html=True)

        # Restart or share results
        col_restart, col_share = st.columns(2)
        with col_restart:
            if st.button("🔄 Try Again", type="primary"):
                st.session_state.clear()
                st.rerun()
        with col_share:
            if st.button("📤 Share Score"):
                share_text = f"I scored {st.session_state.score}/{len(quiz)} ({accuracy:.1f}%) on the JS Quiz Pro! 🚀 Test your JavaScript skills at [your-app-link]!"
                st.code(share_text, language="text")
                st.markdown('<div style="color: #b0b0d0; font-size: 14px;">Copy and share your achievement!</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div style="color: #ffffff; font-size: 24px; font-weight: 700;">📚 Quiz Info</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color: #b0b0d0;">Total Questions: {len(quiz)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color: #b0b0d0;">Current Score: {st.session_state.score}/{len(quiz)}</div>', unsafe_allow_html=True)
    if not st.session_state.show_results:
        st.markdown(f'<div style="color: #b0b0d0;">Timer updates above ⬆️</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="color: #b0b0d0;">Time Taken: {time_taken.seconds // 60}m {time_taken.seconds % 60}s</div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-color: #4b4b6b;">', unsafe_allow_html=True)
    st.markdown('<div style="color: #ffffff; font-size: 18px; font-weight: 600;">💡 Tips</div>', unsafe_allow_html=True)
    st.markdown('<div style="color: #b0b0d0; font-size: 14px;">- Click an option for instant feedback.<br>- Use Previous/Next to navigate.<br>- Finish to see results!</div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-color: #4b4b6b;">', unsafe_allow_html=True)
    st.markdown('<div style="color: #ffffff; font-size: 18px; font-weight: 600;">ℹ️ About</div>', unsafe_allow_html=True)
    st.markdown('<div style="color: #b0b0d0; font-size: 14px;">JS Quiz Pro is built with Streamlit to master JavaScript. Feedback: [your-contact-link]</div>', unsafe_allow_html=True)

