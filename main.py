import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data
quiz_data = [
    {
        "question": "JavaScript mein variable declare karne ke liye kaunsa keyword use hota hai?",
        "options": ["var", "int", "string", "float"],
        "correct_answer": "var"
    },
    {
        "question": "JavaScript ka extension kya hai?",
        "options": [".js", ".java", ".py", ".html"],
        "correct_answer": ".js"
    },
    {
        "question": "JavaScript mein array ki length kaise pata karte hain?",
        "options": ["length()", "size()", "count()", "length"],
        "correct_answer": "length"
    },
    {
        "question": "JavaScript mein function define karne ka syntax kya hai?",
        "options": ["function myFunc()", "def myFunc()", "func myFunc()", "myFunc()"],
        "correct_answer": "function myFunc()"
    }
]

# Streamlit app
st.title("JavaScript Quiz App")
st.write("Test your JavaScript knowledge!")

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

# Function to display the current question
def display_question():
    question = st.session_state.shuffled_questions[st.session_state.question_index]
    st.subheader(f"Question {st.session_state.question_index + 1}")
    st.write(question["question"])
    
    # Display radio buttons for options
    selected_option = st.radio("Choose an option:", question["options"], key=f"q{st.session_state.question_index}")
    
    if st.button("Submit Answer"):
        st.session_state.answered = True
        st.session_state.selected_option = selected_option

# Function to check answer and move to next question
def check_answer():
    question = st.session_state.shuffled_questions[st.session_state.question_index]
    if st.session_state.selected_option == question["correct_answer"]:
        st.session_state.score += 1
        st.success("Correct Answer!")
    else:
        st.error(f"Wrong Answer! Correct answer is: {question['correct_answer']}")
    
    if st.button("Next Question"):
        st.session_state.question_index += 1
        st.session_state.answered = False
        st.session_state.selected_option = None

# Display session ID
st.sidebar.write(f"Session ID: {st.session_state.session_id}")

# Main logic
if st.session_state.question_index < len(st.session_state.shuffled_questions):
    if not st.session_state.answered:
        display_question()
    else:
        check_answer()
else:
    st.subheader("Quiz Completed!")
    st.write(f"Your Score: {st.session_state.score}/{len(quiz_data)}")
    percentage = (st.session_state.score / len(quiz_data)) * 100
    st.write(f"Percentage: {percentage}%")
    
    # Calculate and display time taken
    end_time = datetime.now()
    time_taken = end_time - st.session_state.start_time
    st.write(f"Time Taken: {time_taken.seconds // 60} minutes {time_taken.seconds % 60} seconds")
    
    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.answered = False
        st.session_state.selected_option = None
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.shuffled_questions = random.sample(quiz_data, len(quiz_data))
        st.session_state.start_time = datetime.now()
