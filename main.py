import streamlit as st
import random
from datetime import datetime
import streamlit.components.v1 as components

# Corrected Quiz Data (fixed the block-scoping question)

quiz = [
    {
        "question": "Which of the following is a valid variable name in JavaScript?",
        "options": ["1name", "my-name", "_username", "let"],
        "answer": "_username"
    },
    {
        "question": "What will happen if you declare a variable like this: let 123abc;",
        "options": [
            "It will store the value 123.",
            "It will give a syntax error.",
            "It will work as expected.",
            "It will be ignored."
        ],
        "answer": "It will give a syntax error."
    },
    {
        "question": "Which of the following characters are allowed at the beginning of a variable name?",
        "options": ["@", "#", "$", "*"],
        "answer": "$"
    },
    {
        "question": "Choose the illegal variable name:",
        "options": ["user_name", "user-name", "username1", "myName"],
        "answer": "user-name"
    },
    {
        "question": "What does it mean that variable names are case-sensitive?",
        "options": [
            "MyVar and myvar are same",
            "JavaScript doesn't care about case",
            "MyVar and myvar are different variables",
            "Variables must always be lowercase"
        ],
        "answer": "MyVar and myvar are different variables"
    },
    {
        "question": "What is the output of console.log(typeof NaN)?",
        "options": ["'number'", "'NaN'", "'undefined'", "'object'"],
        "answer": "'number'"
    },
    {
        "question": "Which of these is NOT a valid way to declare a variable in JavaScript?",
        "options": ["let x = 5;", "const y = 10;", "var z = 15;", "int w = 20;"],
        "answer": "int w = 20;"
    },
    {
        "question": "What does the + operator do in JavaScript?",
        "options": ["Multiplication", "Addition", "Subtraction", "Division"],
        "answer": "Addition"
    },
    {
        "question": "What is the result of let sum = 5 + 3;?",
        "options": ["8", "53", "35", "3"],
        "answer": "8"
    },
    {
        "question": "What does the - operator do in JavaScript?",
        "options": ["Addition", "Subtraction", "Multiplication", "Division"],
        "answer": "Subtraction"
    },
    {
        "question": "What is the result of let result = 10 - 4;?",
        "options": ["6", "104", "14", "40"],
        "answer": "6"
    },
    {
        "question": "What does the * operator do in JavaScript?",
        "options": ["Addition", "Subtraction", "Multiplication", "Division"],
        "answer": "Multiplication"
    },
    {
        "question": "What is the result of let total = 6 * 2;?",
        "options": ["12", "62", "26", "16"],
        "answer": "12"
    },
    {
        "question": "What does the / operator do in JavaScript?",
        "options": ["Addition", "Subtraction", "Multiplication", "Division"],
        "answer": "Division"
    },
    {
        "question": "What is the result of let divide = 8 / 2;?",
        "options": ["4", "8", "2", "16"],
        "answer": "4"
    },
    {
        "question": "What does the % operator do in JavaScript?",
        "options": ["Addition", "Subtraction", "Modulus (remainder)", "Division"],
        "answer": "Modulus (remainder)"
    },
    {
        "question": "What is the result of let mod = 9 % 2;?",
        "options": ["1", "2", "0", "4"],
        "answer": "1"
    },
    {
        "question": "What does the ** operator do in JavaScript?",
        "options": ["Exponentiation (Power)", "Division", "Multiplication", "Modulus"],
        "answer": "Exponentiation (Power)"
    },
    {
        "question": "What is the result of let power = 2 ** 3;?",
        "options": ["8", "6", "2", "3"],
        "answer": "8"
    },
    {
        "question": "What does the = operator do in JavaScript?",
        "options": [
            "Assigns a value",
            "Checks for equality",
            "Compares values",
            "Adds two values"
        ],
        "answer": "Assigns a value"
    },
    {
        "question": "What does the += operator do in JavaScript?",
        "options": [
            "Subtract and assign",
            "Multiply and assign",
            "Divide and assign",
            "Add and assign"
        ],
        "answer": "Add and assign"
    },
    {
        "question": "What is the return value of prompt('Enter your name:')?",
        "options": [
            "The user's input",
            "A boolean value",
            "A string with the message",
            "null"
        ],
        "answer": "The user's input"
    },
    {
        "question": "What does prompt('Enter your name:') do?",
        "options": [
            "Displays a prompt asking the user to enter their name",
            "Displays a message on the page",
            "Displays a confirmation box",
            "Displays an alert"
        ],
        "answer": "Displays a prompt asking the user to enter their name"
    },
    {
        "question": "Which of the following is used to ask a question with a prompt box in JavaScript?",
        "options": [
            "prompt()",
            "confirm()",
            "alert()",
            "alertBox()"
        ],
        "answer": "prompt()"
    },
    {
        "question": "Can an alert box contain HTML content?",
        "options": [
            "Yes",
            "No",
            "Only plain text",
            "Only images"
        ],
        "answer": "No"
    },
    {
        "question": "What does alert('Hello World'); display?",
        "options": [
            "A pop-up box with 'Hello World'",
            "A console message with 'Hello World'",
            "A new webpage with 'Hello World'",
            "Nothing"
        ],
        "answer": "A pop-up box with 'Hello World'"
    },
    {
        "question": "Which of the following will trigger an alert box in JavaScript?",
        "options": [
            "alert('Hello World');",
            "console.log('Hello World');",
            "document.write('Hello World');",
            "window.location.href = 'url';"
        ],
        "answer": "alert('Hello World');"
    },
    {
        "question": "What is the purpose of the alert() method in JavaScript?",
        "options": [
            "Displays an alert box with a specified message",
            "Logs a message to the console",
            "Changes the content of an HTML element",
            "Creates a new webpage"
        ],
        "answer": "Displays an alert box with a specified message"
    },
    {
        "question": "Which of the following will convert a number to a string?",
        "options": [
            "String(123)",
            "123.toString()",
            "Both A and B",
            "None of these"
        ],
        "answer": "Both A and B"
    },
    {
        "question": "What will let msg = 'Hello'; msg += ' World'; console.log(msg); output?",
        "options": [
            "'Hello World'",
            "'World Hello'",
            "undefined",
            "Error"
        ],
        "answer": "'Hello World'"
    },
    {
        "question": "What is the output of typeof 'JavaScript'?",
        "options": [
            "'string'",
            "'text'",
            "'word'",
            "'char'"
        ],
        "answer": "'string'"
    },
    {
        "question": "Which method is used to get the length of a string?",
        "options": [
            "length()",
            "getLength()",
            "size()",
            "length"
        ],
        "answer": "length"
    },
    {
        "question": "What will be the output of this code: let x = '5' + 3;?",
        "options": [
            "'53'",
            "8",
            "'8'",
            "Error"
        ],
        "answer": "'53'"
    },
    {
        "question": "How do you concatenate two strings in JavaScript?",
        "options": [
            "'Hello' + 'World'",
            "'Hello'.concat('World')",
            "Both A and B",
            "Hello.World"
        ],
        "answer": "Both A and B"
    },
    {
        "question": "Which of the following is a correct way to declare a string variable in JavaScript?",
        "options": [
            "let name = 'John';",
            "let name = John;",
            "string name = 'John';",
            "name = string('John');"
        ],
        "answer": "let name = 'John';"
    },
    {
        "question": "What is the output of: let x = 5 + 3 * 2;?",
        "options": [
            "16",
            "11",
            "13",
            "10"
        ],
        "answer": "11"
    },
    {
        "question": "What will typeof 42 return?",
        "options": [
            "'number'",
            "'integer'",
            "'float'",
            "'numeric'"
        ],
        "answer": "'number'"
    },
    {
        "question": "Which of the following represents a floating point number?",
        "options": [
            "10.5",
            "105",
            "'10.5'",
            "'105'"
        ],
        "answer": "10.5"
    },
    {
        "question": "What will let x = 10 / 2; result in?",
        "options": [
            "5",
            "'5'",
            "2",
            "'10 / 2'"
        ],
        "answer": "5"
    },
    {
        "question": "What will be the result of: let a = '5' - 2;?",
        "options": [
            "3",
            "'3'",
            "Error",
            "'5 - 2'"
        ],
        "answer": "3"
    },
    {
        "question": "Which operator is used for exponentiation in JavaScript?",
        "options": [
            "^",
            "**",
            "exp()",
            "^^"
        ],
        "answer": "**"
    },
    {
        "question": "What is the output of: let x = 9 % 2;?",
        "options": [
            "0",
            "1",
            "2",
            "4"
        ],
        "answer": "1"
    },
    {
        "question": "What will parseInt('42px') return?",
        "options": [
            "42",
            "'42px'",
            "NaN",
            "px"
        ],
        "answer": "42"
    },
    {
        "question": "Which of the following is a valid way to declare a number variable in JavaScript?",
        "options": [
            "let age = 25;",
            "let 25 = age;",
            "int age = 25;",
            "number age = 25;"
        ],
        "answer": "let age = 25;"
    },
    {
        "question": "What is the result of: 10 + 5 * 2?",
        "options": [
            "30",
            "25",
            "20",
            "40"
        ],
        "answer": "20"
    },
    {
        "question": "What is the output of: 7 % 3?",
        "options": [
            "1",
            "2",
            "3",
            "0"
        ],
        "answer": "1"
    },
    {
        "question": "What will 10 / 2 evaluate to?",
        "options": [
            "5",
            "2",
            "0",
            "20"
        ],
        "answer": "5"
    },
    {
        "question": "What does the ++ operator do?",
        "options": [
            "Decreases value by 1",
            "Increases value by 1",
            "Multiplies the value",
            "Divides the value"
        ],
        "answer": "Increases value by 1"
    },
    {
        "question": "What is the result of: let x = 5; x++;?",
        "options": [
            "4",
            "5",
            "6",
            "Error"
        ],
        "answer": "6"
    },
    {
        "question": "Which operator decreases the value by 1?",
        "options": [
            "--",
            "++",
            "-=",
            "+="
        ],
        "answer": "--"
    },
    {
        "question": "What does x -= 2 do?",
        "options": [
            "Adds 2 to x",
            "Multiplies x by 2",
            "Divides x by 2",
            "Subtracts 2 from x"
        ],
        "answer": "Subtracts 2 from x"
    },
    {
        "question": "What is the difference between x++ and ++x?",
        "options": [
            "x++ increments after use, ++x increments before use",
            "They are the same",
            "x++ causes error",
            "++x decreases value"
        ],
        "answer": "x++ increments after use, ++x increments before use"
    },
    {
        "question": "What does x *= 2 mean in JavaScript?",
        "options": [
            "Divides x by 2",
            "Multiplies x by 2",
            "Sets x to 2",
            "Adds 2 to x"
        ],
        "answer": "Multiplies x by 2"
    },
    {
        "question": "What will console.log('I am ' + 20 + ' years old.'); print?",
        "options": [
            "'I am 20 years old.'",
            "'I am 20years old.'",
            "'I am20 years old.'",
            "'20 I am years old.'"
        ],
        "answer": "'I am 20 years old.'"
    },
    {
        "question": "What happens if you concatenate 'abc' + 123 in JavaScript?",
        "options": [
            "Throws an error",
            "'abc123'",
            "246",
            "NaN"
        ],
        "answer": "'abc123'"
    },
    {
        "question": "What does this expression return: 'Age: ' + (10 + 5)?",
        "options": [
            "'Age: 15'",
            "'Age: 105'",
            "'10 + 5 = Age'",
            "Error"
        ],
        "answer": "'Age: 15'"
    },
    {
        "question": "What will be the output of: '2' + 2 in JavaScript?",
        "options": [
            "4",
            "22",
            "'4'",
            "'2 2'"
        ],
        "answer": "22"
    },
    {
        "question": "What is the value of: let name = 'Ali'; let message = 'Hello ' + name;?",
        "options": [
            "'Hello Ali'",
            "'Ali Hello'",
            "Hello + name",
            "Error"
        ],
        "answer": "'Hello Ali'"
    },
    {
        "question": "What will be the result of: 'Hello' + ' World'?",
        "options": [
            "'HelloWorld'",
            "'Hello World'",
            "'Hello+World'",
            "Error"
        ],
        "answer": "'Hello World'"
    },
    {
        "question": "Which operator is used to concatenate strings in JavaScript?",
        "options": [
            "+",
            "-",
            "*",
            "/"
        ],
        "answer": "+"
    },
    {
        "question": "What does string concatenation mean?",
        "options": [
            "Dividing two strings",
            "Multiplying strings",
            "Joining two or more strings together",
            "Converting string to number"
        ],
        "answer": "Joining two or more strings together"
    },
    {
        "question": "What does the -= operator do in JavaScript?",
        "options": [
            "Subtract and assign",
            "Add and assign",
            "Multiply and assign",
            "Divide and assign"
        ],
        "answer": "Subtract and assign"
    },
    {
        "question": "What does the *= operator do in JavaScript?",
        "options": [
            "Subtract and assign",
            "Add and assign",
            "Multiply and assign",
            "Divide and assign"
        ],
        "answer": "Multiply and assign"
    },
    {
        "question": "What does the /= operator do in JavaScript?",
        "options": [
            "Subtract and assign",
            "Multiply and assign",
            "Divide and assign",
            "Modulus and assign"
        ],
        "answer": "Divide and assign"
    },
    {
        "question": "What does the %= operator do in JavaScript?",
        "options": [
            "Subtract and assign",
            "Add and assign",
            "Divide and assign",
            "Modulus and assign"
        ],
        "answer": "Modulus and assign"
    },
    {
        "question": "What does the **= operator do in JavaScript?",
        "options": [
            "Exponentiation and assign",
            "Multiply and assign",
            "Divide and assign",
            "Modulus and assign"
        ],
        "answer": "Exponentiation and assign"
    },
    {
        "question": "When was JavaScript created and by whom?",
        "options": [
            "December 4, 1995 by Brendan Eich",
            "1995 by Brendan Eich",
            "December 4, 1995 by Mark Zuckerberg",
            "2000 by Tim Berners-Lee"
        ],
        "answer": "December 4, 1995 by Brendan Eich"
    },
    {
        "question": "What was JavaScript's original name and what happened to it?",
        "options": [
            "LiveScript, later renamed to JavaScript",
            "JScript, later renamed to JavaScript",
            "Java, later renamed to JavaScript",
            "LiveScript, later renamed to JScript"
        ],
        "answer": "LiveScript, later renamed to JavaScript"
    },
    {
        "question": "Which of the following will work for block-scoping in JavaScript?",
        "options": ["let", "var", "const", "Both let and const"],
        "answer": "Both let and const"
    },
      {
        'question': 'What is the output of `console.log(typeof null)`?',
        'options': ['null', 'object', 'undefined', 'string'],
        'answer': 'object'
    },
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

