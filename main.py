import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 30 DOM-related questions
quiz = [
    {
        "question": "How do you convert a string to uppercase in JavaScript?",
        "options": [
            "str.toUpperCase()",
            "str.upperCase()",
            "str.toUpper()",
            "str.makeUpperCase()"
        ],
        "answer": "str.toUpperCase()",
        "difficulty": "Easy",
        "explanation": "The `toUpperCase()` method converts all characters in a string to uppercase."
    },
    {
        "question": "How do you measure the length of a string in JavaScript?",
        "options": [
            "str.length",
            "str.size()",
            "str.len()",
            "str.count()"
        ],
        "answer": "str.length",
        "difficulty": "Easy",
        "explanation": "The `length` property returns the number of characters in a string."
    },
    {
        "question": "How do you select an element by its ID in the DOM?",
        "options": [
            "document.getElementById()",
            "document.querySelector()",
            "document.getElementsByClassName()",
            "document.getElement()"
        ],
        "answer": "document.getElementById()",
        "difficulty": "Easy",
        "explanation": "`getElementById()` selects an element by its unique ID."
    },
    {
        "question": "What method adds a new element to the end of a parent element?",
        "options": [
            "parent.appendChild()",
            "parent.insertBefore()",
            "parent.addChild()",
            "parent.append()"
        ],
        "answer": "parent.appendChild()",
        "difficulty": "Easy",
        "explanation": "`appendChild()` adds a node as the last child of a parent."
    },
    {
        "question": "How do you remove an element from the DOM?",
        "options": [
            "element.remove()",
            "element.delete()",
            "element.removeChild()",
            "element.detach()"
        ],
        "answer": "element.remove()",
        "difficulty": "Medium",
        "explanation": "`remove()` deletes an element from the DOM directly."
    },
    {
        "question": "What does `querySelectorAll()` return?",
        "options": [
            "NodeList",
            "Array",
            "HTMLElement",
            "Single Element"
        ],
        "answer": "NodeList",
        "difficulty": "Medium",
        "explanation": "`querySelectorAll()` returns a NodeList of all matching elements."
    },
    {
        "question": "How do you add an event listener to an element?",
        "options": [
            "element.addEventListener()",
            "element.on()",
            "element.attachEvent()",
            "element.bind()"
        ],
        "answer": "element.addEventListener()",
        "difficulty": "Easy",
        "explanation": "`addEventListener()` attaches an event handler to an element."
    },
    {
        "question": "What property gets the text content of an element?",
        "options": [
            "element.textContent",
            "element.innerText",
            "element.innerHTML",
            "element.content"
        ],
        "answer": "element.textContent",
        "difficulty": "Medium",
        "explanation": "`textContent` retrieves or sets the text content of an element."
    },
    {
        "question": "How do you change an element's class in the DOM?",
        "options": [
            "element.classList.add()",
            "element.className()",
            "element.setClass()",
            "element.addClass()"
        ],
        "answer": "element.classList.add()",
        "difficulty": "Medium",
        "explanation": "`classList.add()` adds a class to an element's class list."
    },
    {
        "question": "What does `event.preventDefault()` do?",
        "options": [
            "Prevents the default action",
            "Stops event propagation",
            "Removes the event listener",
            "Cancels the event"
        ],
        "answer": "Prevents the default action",
        "difficulty": "Medium",
        "explanation": "`preventDefault()` stops the default behavior of an event."
    },
    {
        "question": "How do you access the parent element of a node?",
        "options": [
            "node.parentElement",
            "node.parentNode",
            "node.parent()",
            "node.getParent()"
        ],
        "answer": "node.parentElement",
        "difficulty": "Medium",
        "explanation": "`parentElement` returns the parent element of a node."
    },
    {
        "question": "What is the purpose of `element.innerHTML`?",
        "options": [
            "Gets or sets HTML content",
            "Gets text content",
            "Sets CSS styles",
            "Removes an element"
        ],
        "answer": "Gets or sets HTML content",
        "difficulty": "Easy",
        "explanation": "`innerHTML` gets or sets the HTML content of an element."
    },
    {
        "question": "How do you create a new element in the DOM?",
        "options": [
            "document.createElement()",
            "document.newElement()",
            "document.makeElement()",
            "document.buildElement()"
        ],
        "answer": "document.createElement()",
        "difficulty": "Easy",
        "explanation": "`createElement()` creates a new DOM element."
    },
    {
        "question": "What does `element.classList.toggle()` do?",
        "options": [
            "Toggles a class on/off",
            "Adds a class",
            "Removes a class",
            "Replaces a class"
        ],
        "answer": "Toggles a class on/off",
        "difficulty": "Medium",
        "explanation": "`classList.toggle()` adds a class if absent, removes it if present."
    },
    {
        "question": "How do you get an element's attribute?",
        "options": [
            "element.getAttribute()",
            "element.attribute()",
            "element.getAttr()",
            "element.fetchAttribute()"
        ],
        "answer": "element.getAttribute()",
        "difficulty": "Easy",
        "explanation": "`getAttribute()` retrieves the value of an element's attribute."
    },
    {
        "question": "What is the purpose of `event.target`?",
        "options": [
            "Identifies the element that triggered the event",
            "Gets the parent element",
            "Stops event propagation",
            "Sets the event type"
        ],
        "answer": "Identifies the element that triggered the event",
        "difficulty": "Medium",
        "explanation": "`event.target` refers to the element that triggered the event."
    },
    {
        "question": "How do you set an element's style property?",
        "options": [
            "element.style.property = value",
            "element.setStyle()",
            "element.css()",
            "element.style = value"
        ],
        "answer": "element.style.property = value",
        "difficulty": "Easy",
        "explanation": "`style.property` sets inline CSS styles for an element."
    },
    {
        "question": "What does `document.querySelector()` return?",
        "options": [
            "First matching element",
            "NodeList",
            "Array",
            "All matching elements"
        ],
        "answer": "First matching element",
        "difficulty": "Medium",
        "explanation": "`querySelector()` returns the first element matching the selector."
    },
    {
        "question": "How do you remove an event listener?",
        "options": [
            "element.removeEventListener()",
            "element.detachEvent()",
            "element.off()",
            "element.removeEvent()"
        ],
        "answer": "element.removeEventListener()",
        "difficulty": "Medium",
        "explanation": "`removeEventListener()` detaches an event handler."
    },
    {
        "question": "What is the purpose of `element.dataset`?",
        "options": [
            "Accesses data-* attributes",
            "Sets element classes",
            "Gets text content",
            "Modifies inline styles"
        ],
        "answer": "Accesses data-* attributes",
        "difficulty": "Medium",
        "explanation": "`dataset` provides access to custom data attributes."
    },
    {
        "question": "How do you clone a DOM element?",
        "options": [
            "element.cloneNode()",
            "element.copyNode()",
            "element.duplicate()",
            "element.clone()"
        ],
        "answer": "element.cloneNode()",
        "difficulty": "Medium",
        "explanation": "`cloneNode()` creates a copy of a node."
    },
    {
        "question": "What does `element.closest()` do?",
        "options": [
            "Finds the closest ancestor matching a selector",
            "Gets the nearest sibling",
            "Finds the closest child",
            "Returns the element itself"
        ],
        "answer": "Finds the closest ancestor matching a selector",
        "difficulty": "Hard",
        "explanation": "`closest()` returns the nearest ancestor matching the selector."
    },
    {
        "question": "How do you check if an element has a specific class?",
        "options": [
            "element.classList.contains()",
            "element.hasClass()",
            "element.className()",
            "element.isClass()"
        ],
        "answer": "element.classList.contains()",
        "difficulty": "Medium",
        "explanation": "`classList.contains()` checks if an element has a class."
    },
    {
        "question": "What is the purpose of `element.scrollIntoView()`?",
        "options": [
            "Scrolls the element into view",
            "Sets element visibility",
            "Scrolls the page to the top",
            "Hides the element"
        ],
        "answer": "Scrolls the element into view",
        "difficulty": "Medium",
        "explanation": "`scrollIntoView()` scrolls the element into the viewport."
    },
    {
        "question": "How do you get all child elements of a node?",
        "options": [
            "node.children",
            "node.childNodes",
            "node.getChildren()",
            "node.childElements()"
        ],
        "answer": "node.children",
        "difficulty": "Medium",
        "explanation": "`children` returns an HTMLCollection of child elements."
    },
    {
        "question": "What does `event.stopPropagation()` do?",
        "options": [
            "Stops event bubbling",
            "Prevents default action",
            "Removes the event",
            "Triggers the event"
        ],
        "answer": "Stops event bubbling",
        "difficulty": "Medium",
        "explanation": "`stopPropagation()` prevents further event propagation."
    },
    {
        "question": "How do you set an attribute on an element?",
        "options": [
            "element.setAttribute()",
            "element.attribute()",
            "element.addAttribute()",
            "element.setAttr()"
        ],
        "answer": "element.setAttribute()",
        "difficulty": "Easy",
        "explanation": "`setAttribute()` sets the value of an element's attribute."
    },
    {
        "question": "What is the purpose of `document.createTextNode()`?",
        "options": [
            "Creates a text node",
            "Creates an element",
            "Sets text content",
            "Removes text"
        ],
        "answer": "Creates a text node",
        "difficulty": "Medium",
        "explanation": "`createTextNode()` creates a new text node."
    },
    {
        "question": "How do you get the current URL in the browser?",
        "options": [
            "window.location.href",
            "document.url",
            "window.href",
            "document.location"
        ],
        "answer": "window.location.href",
        "difficulty": "Easy",
        "explanation": "`window.location.href` returns the current URL."
    },
    {
        "question": "What does `element.matches()` do?",
        "options": [
            "Checks if an element matches a CSS selector",
            "Matches elements by ID",
            "Compares two elements",
            "Checks element visibility"
        ],
        "answer": "Checks if an element matches a CSS selector",
        "difficulty": "Hard",
        "explanation": "`matches()` checks if an element matches a CSS selector."
    }
]

# Cache shuffled quiz
@st.cache_data
def shuffle_quiz(_quiz):
    shuffled = random.sample(_quiz, len(_quiz))
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = q["options"].copy()
        random.shuffle(q["display_options"])
        q["labeled_answer"] = q["answer"]
    return shuffled

# Initialize session state
if "quiz_data" not in st.session_state:
    st.session_state.update({
        "quiz_data": shuffle_quiz(quiz) if quiz else [],
        "score": 0,
        "current_q": 0,
        "start_time": datetime.now(),
        "answers": [None] * len(quiz) if quiz else [],
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 3600,  # 60 minutes
        "theme": "dark",
        "streak": 0,
        "started": False
    })

# Theme toggle
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# Timer logic
def update_timer():
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.session_state.time_left = max(3600 - elapsed, 0)
    if st.session_state.time_left <= 0:
        st.session_state.show_results = True
        st.rerun()

# Reset quiz
def reset_quiz():
    st.session_state.update({
        "quiz_data": shuffle_quiz(quiz),
        "score": 0,
        "current_q": 0,
        "start_time": datetime.now(),
        "answers": [None] * len(quiz),
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 3600,
        "streak": 0,
        "started": False
    })
    st.rerun()

# Enhanced CSS for UI
st.markdown("""
<style>
/* Global styles */
.main-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    transition: all 0.3s ease;
}

/* Theme-specific styles */
.main-container[data-theme="dark"] {
    background-color: #1a1a1a;
    color: #ffffff;
    --text-color: #ffffff;
    --primary-color: #34c759;
    --secondary-color: #2c2c2e;
    --button-bg: #2c2c2e;
    --button-hover: #3a3a3c;
    --feedback-correct-bg: #34c759;
    --feedback-wrong-bg: #ff3b30;
    --progress-fill: #34c759;
}

.main-container[data-theme="light"] {
    background-color: #ffffff;
    color: #333333;
    --text-color: #333333;
    --primary-color: #28a745;
    --secondary-color: #f5f5f5;
    --button-bg: #f5f5f5;
    --button-hover: #e0e0e0;
    --feedback-correct-bg: #28a745;
    --feedback-wrong-bg: #dc3545;
    --progress-fill: #28a745;
}

/* Title and caption */
.title {
    font-size: 2.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 10px;
    color: var(--primary-color);
    animation: fadeIn 0.5s ease-in;
}

.caption {
    font-size: 1.1rem;
    text-align: center;
    color: var(--text-color);
    opacity: 0.8;
    margin-bottom: 20px;
}

/* Timer */
.timer {
    font-size: 1rem;
    font-weight: 600;
    text-align: right;
    color: var(--primary-color);
    margin-bottom: 15px;
}

/* Progress bar */
.progress-bar {
    background-color: var(--secondary-color);
    border-radius: 10px;
    height: 20px;
    position: relative;
    margin: 20px 0;
    overflow: hidden;
}

.progress-fill {
    background-color: var(--progress-fill);
    height: 100%;
    border-radius: 10px;
    transition: width 0.3s ease;
}

.progress-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--text-color);
}

/* Question container */
.question-container {
    background-color: var(--secondary-color);
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    animation: slideUp 0.3s ease;
}

/* Difficulty and streak */
.difficulty {
    font-size: 0.9rem;
    color: var(--text-color);
    opacity: 0.7;
    margin-bottom: 15px;
    text-align: right;
}

/* Buttons */
.stButton > button {
    width: 100%;
    background-color: var(--button-bg);
    color: var(--text-color);
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    padding: 12px;
    margin: 8px 0;
    font-size: 1rem;
    font-weight: 500;
    transition: all 0.2s ease;
    text-align: left;
}

.stButton > button:hover {
    background-color: var(--button-hover);
    transform: translateY(-2px);
}

.stButton > button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

/* Selected button states */
.selected-correct {
    background-color: var(--feedback-correct-bg) !important;
    color: white !important;
    border-color: var(--feedback-correct-bg) !important;
}

.selected-wrong {
    background-color: var(--feedback-wrong-bg) !important;
    color: white !important;
    border-color: var(--feedback-wrong-bg) !important;
}

/* Feedback */
.feedback-correct {
    background-color: var(--feedback-correct-bg);
    color: white;
    padding: 10px;
    border-radius: 8px;
    margin-top: 15px;
    font-weight: 500;
    text-align: center;
    animation: fadeIn 0.3s ease;
}

.feedback-wrong {
    background-color: var(--feedback-wrong-bg);
    color: white;
    padding: 10px;
    border-radius: 8px;
    margin-top: 15px;
    font-weight: 500;
    text-align: center;
    animation: fadeIn 0.3s ease;
}

/* Code block */
.stCodeBlock {
    background-color: #2f2f2f;
    border-radius: 8px;
    padding: 15px;
    margin: 10px 0;
    font-size: 0.95rem;
}

.main-container[data-theme="light"] .stCodeBlock {
    background-color: #f5f5f5;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideUp {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

/* Responsive design */
@media (max-width: 600px) {
    .title {
        font-size: 2rem;
    }
    
    .question-container {
        padding: 15px;
    }
    
    .stButton > button {
        font-size: 0.9rem;
        padding: 10px;
    }
    
    .timer {
        font-size: 0.9rem;
        text-align: center;
    }
}

/* Theme toggle, start, and play again buttons */
.stButton > button[key="theme_toggle"],
.stButton > button[key="start_quiz"],
.stButton > button[key="play_again"] {
    background-color: var(--primary-color);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 600;
    transition: all 0.2s ease;
    width: auto;
    margin: 10px auto;
    display: block;
}

.stButton > button[key="theme_toggle"]:hover,
.stButton > button[key="start_quiz"]:hover,
.stButton > button[key="play_again"]:hover {
    background-color: #2c974b;
    transform: translateY(-2px);
}

.main-container[data-theme="light"] .stButton > button[key="theme_toggle"],
.main-container[data-theme="light"] .stButton > button[key="start_quiz"],
.main-container[data-theme="light"] .stButton > button[key="play_again"] {
    background-color: #218838;
}

.main-container[data-theme="light"] .stButton > button[key="theme_toggle"]:hover,
.main-container[data-theme="light"] .stButton > button[key="start_quiz"]:hover,
.main-container[data-theme="light"] .stButton > button[key="play_again"]:hover {
    background-color: #1c7430;
}
</style>
""", unsafe_allow_html=True)

# Main UI
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 DOM Mastery Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript DOM Skills!</p>', unsafe_allow_html=True)

# Theme toggle button
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen
if not st.session_state.started:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: var(--text-color); font-size: 18px;">Test your DOM skills with 30 comprehensive questions!</p>
        <p style="color: var(--text-color); opacity: 0.8;">60 minutes, 2 points per correct answer, +0.5 bonus for streaks ≥3. Ready?</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Quiz", key="start_quiz"):
        st.session_state.started = True
        st.session_state.start_time = datetime.now()
        st.rerun()
else:
    # Timer
    if not st.session_state.show_results:
        update_timer()
        minutes = int(st.session_state.time_left // 60)
        seconds = int(st.session_state.time_left % 60)
        st.markdown(f'<div class="timer">⏰ Time Left: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

    if not st.session_state.quiz_data:
        st.error("No quiz questions available.")
    else:
        # Progress bar
        progress = st.session_state.current_q / len(st.session_state.quiz_data)
        progress_percentage = int(progress * 100)
        st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress_percentage}%"></div>
            <div class="progress-text">{progress_percentage}%</div>
        </div>
        <div style="color: var(--text-color); font-size: 13px; text-align: center;">
            Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
        </div>
        """, unsafe_allow_html=True)

        if not st.session_state.show_results:
            with st.container():
                st.markdown('<div class="question-container">', unsafe_allow_html=True)
                q = st.session_state.quiz_data[st.session_state.current_q]

                # Display difficulty and streak
                st.markdown(f'<div class="difficulty">Difficulty: {q["difficulty"]} | Streak: 🔥 {st.session_state.streak}</div>', unsafe_allow_html=True)

                # Split question into text and code
                if "```javascript" in q["question"] or "```html
                    if "```javascript" in q["question"]:
                        language = "javascript"
                        question_parts = q["question"].split("```javascript
                    else:
                        language = "html"
                        question_parts = q["question"].split("```html\n")
                    
                    question_text = question_parts[0].strip()
                    code_snippet = question_parts[1].split("```")[0].strip()
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{question_text}**")
                    st.code(code_snippet, language=language)
                else:
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{q['question']}**")

                # Option buttons
                for i, option in enumerate(q["display_options"]):
                    button_class = ""
                    if st.session_state.selected_option == option:
                        button_class = "selected-correct" if option == q["labeled_answer"] else "selected-wrong"
                    if st.button(
                        option,
                        key=f"q{i}",
                        disabled=st.session_state.selected_option is not None
                    ):
                        is_correct = option == q["labeled_answer"]
                        st.session_state.selected_option = option
                        st.session_state.feedback = {
                            "is_correct": is_correct,
                            "correct_answer": q["labeled_answer"],
                            "explanation": q["explanation"]
                        }
                        st.session_state.answers[st.session_state.current_q] = {
                            "question": q["question"],
                            "user_answer": option,
                            "correct_answer": q["labeled_answer"],
                            "is_correct": is_correct,
                            "difficulty": q["difficulty"]
                        }
                        if is_correct:
                            st.session_state.score += 2  # 2 points for correct answer
                            st.session_state.streak += 1
                            if st.session_state.streak >= 3:
                                st.session_state.score += 0.5
                        else:
                            st.session_state.streak = 0
                        # Automatically move to next question or show results
                        if st.session_state.current_q < len(quiz) - 1:
                            st.session_state.current_q += 1
                            st.session_state.selected_option = None
                            st.session_state.feedback = None
                        else:
                            st.session_state.show_results = True
                        st.rerun()

                # Feedback
                if st.session_state.feedback:
                    if st.session_state.feedback["is_correct"]:
                        st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="color: var(--text-color); font-size: 14px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

        else:
            # Results
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 3600)
            total_possible_score = len(quiz) * 2  # 2 points per question
            accuracy = (st.session_state.score / total_possible_score) * 100 if total_possible_score > 0 else 0
            st.markdown('<div class="question-container">', unsafe_allow_html=True)
            st.markdown(f'<h2 style="color: var(--primary-color); text-align: center;">🏆 Score: {st.session_state.score}/{total_possible_score}</h2>', unsafe_allow_html=True)
            st.markdown(f"""
            <h3>📊 Results</h3>
            <div style="color: var(--text-color); font-size: 15px;">
                - ⏱️ Time: {int(time_taken) // 60}m {int(time_taken) % 60}s<br>
                - 🎯 Accuracy: {accuracy:.1f}%<br>
                - ✅ Correct: {sum(1 for ans in st.session_state.answers if ans and ans["is_correct"])}<br>
                - ❌ Incorrect: {sum(1 for ans in st.session_state.answers if ans and not ans["is_correct"])}<br>
                - 🔥 Max Streak: {st.session_state.streak}
            </div>
            """, unsafe_allow_html=True)

            # Confetti for high score (requires external confetti.js library)
            if accuracy > 80:
                st.markdown("""
                <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
                <script>
                    confetti({
                        particleCount: 100,
                        spread: 70,
                        origin: { y: 0.6 }
                    });
                </script>
                """, unsafe_allow_html=True)

            # Leaderboard
            leaderboard = [
                {"name": "Alice", "score": 48, "time": 2000},
                {"name": "Bob", "score": 45, "time": 2100},
                {"name": "Charlie", "score": 42, "time": 2050},
                {"name": "You", "score": st.session_state.score, "time": int(time_taken)}
            ]
            leaderboard.sort(key=lambda x: (-x["score"], x["time"]))
            st.markdown('<h3>🏅 Leaderboard</h3>', unsafe_allow_html=True)
            for i, entry in enumerate(leaderboard[:4], 1):
                st.markdown(f'<div style="color: var(--text-color);">{i}. <b>{entry["name"]}</b>: {entry["score"]}/{total_possible_score} (Time: {entry["time"]//60}m {entry["time"]%60}s)</div>', unsafe_allow_html=True)

            # Review Answers
            st.markdown('<h3>📝 Review Your Answers</h3>', unsafe_allow_html=True)
            for i, ans in enumerate(st.session_state.answers):
                if ans:
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})"
                    st.markdown(f'<div style="color: var(--text-color); margin-bottom: 15px;">Question {i+1}: {ans["question"]}<br>Your Answer: {ans["user_answer"]}<br>{status}<br>Explanation: {quiz[i]["explanation"]}</div>', unsafe_allow_html=True)

            # Play Again button
            if st.button("🔄 Play Again", key="play_again"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
