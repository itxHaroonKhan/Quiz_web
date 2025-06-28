import streamlit as st
import random
from datetime import datetime
import uuid

# Custom CSS for improved UI
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stRadio > label {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    .stRadio > label:hover {
        background-color: #e6f3ff;
        border-color: #007bff;
    }
    .stButton > button {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    .question-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .score-history {
        font-size: 14px;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Quiz data with explanations
quiz_data = [
    {
        "question": "JavaScript mein variable declare karne ke liye kaunsa keyword use hota hai?",
        "options": ["var", "int", "string", "float"],
        "correct_answer": "var",
        "explanation": "JavaScript mein `var`, `let`, aur `const` variables declare karne ke liye use hote hain. `var` sabse purana aur commonly used keyword hai."
    },
    {
        "question": "JavaScript ka file extension kya hai?",
        "options": [".js", ".java", ".py", ".html"],
        "correct_answer": ".js",
        "explanation": "JavaScript files ka extension `.js` hota hai, jo unhe identify karta hai."
    },
    {
        "question": "JavaScript mein array ki length kaise pata karte hain?",
        "options": ["length()", "size()", "count()", "length"],
        "correct_answer": "length",
        "explanation": "JavaScript mein array ki length `length` property se pata ki jati hai, jo ek number return karti hai."
    },
    {
        "question": "JavaScript mein function define karne ka syntax kya hai?",
        "options": ["function myFunc()", "def myFunc()", "func myFunc()", "myFunc()"],
        "correct_answer": "function myFunc()",
        "explanation": "`function` keyword ke saath function ka naam aur parentheses use hote hain JavaScript mein."
    },
    {
        "question": "JavaScript mein `===` operator ka kya matlab hai?",
        "options": ["Assignment", "Equality", "Strict Equality", "Comparison"],
        "correct_answer": "Strict Equality",
        "explanation": "`===` operator type aur value dono ko check karta hai, jabki `==` sirf value check karta hai."
    },
    {
        "question": "JavaScript mein `null` ka matlab kya hai?",
        "options": ["Undefined", "Empty", "No Value", "Zero"],
        "correct_answer": "No Value",
        "explanation": "`null` ek intentional absence of value ko represent karta hai, jabki `undefined` uninitialized variables ke liye hota hai."
    },
    {
        "question": "JavaScript mein `forEach` ka use kya hai?",
        "options": ["Loop through array", "Define function", "Create object", "Sort array"],
        "correct_answer": "Loop through array",
        "explanation": "`forEach` method array ke har element par ek function execute karta hai."
    },
    {
        "question": "JavaScript mein `NaN` ka matlab kya hai?",
        "options": ["Not a Number", "Null and Negative", "No Action Needed", "New Array Number"],
        "correct_answer": "Not a Number",
        "explanation": "`NaN` ek special value hai jo invalid number operations ko represent karta hai, jaise `0/0`."
    },
    {
        "question": "JavaScript mein `this` keyword kya refer karta hai?",
        "options": ["Global object", "Current object", "Previous object", "Function"],
        "correct_answer": "Current object",
        "explanation": "`this` keyword current execution context ke object ko refer karta hai, jaise function ke andar ya object ke method mein."
    },
    {
        "question": "JavaScript mein arrow function ka syntax kya hai?",
        "options": ["=> myFunc()", "function => ()", "() => {}", "func => {}"],
        "correct_answer": "() => {}",
        "explanation": "Arrow functions ES6 mein introduce hue, aur unka syntax `() => {}` hota hai, jo concise functions banane ke liye use hota hai."
    }
]

# Streamlit app
st.set_page_config(page_title="JavaScript Quiz App", page_icon=":rocket:", layout="centered")
st.title("🎓 JavaScript Quiz App")
st.markdown("**Test your JavaScript knowledge with this interactive quiz!**")

# Initialize session state
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None
if 'shuffled_questions' not in st.session_state:
    st.session_state.shuffled_questions = random.sample(quiz_data, len(quiz_data))
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.now()
if 'score_history' not in st.session_state:
    st.session_state.score_history = []

# Sidebar for session info and score history
st.sidebar.header("Quiz Info")
st.sidebar.markdown(f"**Session ID**: {st.session_state.session_id}")
st.sidebar.markdown("### Score History")
for i, score in enumerate(st.session_state.score_history, 1):
    st.sidebar.markdown(f"<div class='score-history'>Attempt {i}: {score}/{len(quiz_data)}</div>", unsafe_allow_html=True)

# Progress bar
progress = (st.session_state.question_index / len(quiz_data)) * 100
st.progress(progress)

# Function to display the current question
def display_question():
    question = st.session_state.shuffled_questions[st.session_state.question_index]
    with st.container():
        st.markdown(f"<div class='question-card'><h3>Question {st.session_state.question_index + 1} of {len(quiz_data)}</h3><p>{question['question']}</p></div>", unsafe_allow_html=True)
        
        # Display radio buttons for options
        selected_option = st.radio("Choose an option:", question["options"], key=f"q{st.session_state.question_index}")
        
        if st.button("Submit Answer", key="submit"):
            st.session_state.answered = True
            st.session_state.selected_option = selected_option

# Function to check answer and show explanation
def check_answer():
    question = st.session_state.shuffled_questions[st.session_state.question_index]
    with st.container():
        st.markdown(f"<div class='question-card'><h3>Question {st.session_state.question_index + 1} of {len(quiz_data)}</h3><p>{question['question']}</p></div>", unsafe_allow_html=True)
        if st.session_state.selected_option == question["correct_answer"]:
            st.session_state.score += 1
            st.success("Correct Answer! 🎉")
        else:
            st.error(f"Wrong Answer! Correct answer is: **{question['correct_answer']}**")
        
        st.markdown(f"**Explanation**: {question['explanation']}")
        
        if st.button("Next Question", key="next"):
            st.session_state.question_index += 1
            st.session_state.answered = False
            st.session_state.selected_option = None

# Main logic
if st.session_state.question_index < len(quiz_data):
    if not st.session_state.answered:
        display_question()
    else:
        check_answer()
else:
    st.balloons()
    st.markdown("<div class='question-card'><h2>Quiz Completed! 🏆</h2>", unsafe_allow_html=True)
    st.markdown(f"**Your Score**: {st.session_state.score}/{len(quiz_data)}")
    percentage = (st.session_state.score / len(quiz_data)) * 100
    st.markdown(f"**Percentage**: {percentage:.2f}%")
    
    # Calculate and display time taken
    end_time = datetime.now()
    time_taken = end_time - st.session_state.start_time
    st.markdown(f"**Time Taken**: {time_taken.seconds // 60} minutes {time_taken.seconds % 60} seconds")
    
    # Save score to history
    st.session_state.score_history.append(st.session_state.score)
    
    if st.button("Restart Quiz", key="restart"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.answered = False
        st.session_state.selected_option = None
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.shuffled_questions = random.sample(quiz_data, len(quiz_data))
        st.session_state.start_time = datetime.now()
