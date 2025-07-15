import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 30 DOM-related questions
quiz = [
    {
        "question": "What is the DOM in JavaScript?",
        "options": [
            "A tree-like representation of a webpage's structure",
            "A database for storing webpage data",
            "A method for styling webpages",
            "A function for creating elements"
        ],
        "answer": "A tree-like representation of a webpage's structure",
        "difficulty": "Easy",
        "explanation": "The Document Object Model (DOM) is a tree-like structure representing the elements, attributes, and content of a webpage, allowing JavaScript to interact with it."
    },
    {
        "question": "How do you access the parent node of a DOM element?",
        "options": [
            "element.parentNode",
            "element.getParent()",
            "element.parent()",
            "element.ancestor()"
        ],
        "answer": "element.parentNode",
        "difficulty": "Medium",
        "explanation": "`parentNode` returns the immediate parent node of an element in the DOM tree, which could be an element or another node type."
    },
    {
        "question": "How do you get all child elements of a DOM node?",
        "options": [
            "element.children",
            "element.childNodes",
            "element.getChildren()",
            "element.kids()"
        ],
        "answer": "element.children",
        "difficulty": "Medium",
        "explanation": "`children` returns an HTMLCollection of only the element nodes that are direct children of the specified node."
    },
    {
        "question": "What does the `nodeType` property indicate in the DOM?",
        "options": [
            "The type of the node",
            "The number of child nodes",
            "The node's position in the DOM",
            "The node's CSS class"
        ],
        "answer": "The type of the node",
        "difficulty": "Medium",
        "explanation": "`nodeType` returns a number indicating the type of node, such as 1 for elements, 3 for text nodes, or 8 for comments."
    },
    {
        "question": "Which DOM nodeType value corresponds to an element node?",
        "options": [
            "1",
            "3",
            "8",
            "9"
        ],
        "answer": "1",
        "difficulty": "Hard",
        "explanation": "In the DOM, a `nodeType` value of 1 represents an element node, such as a `<div>` or `<p>`."
    },
    {
        "question": "How do you select an element by its ID in the DOM?",
        "options": [
            "document.getElementById('id')",
            "document.querySelector('id')",
            "document.getId('id')",
            "document.selectId('id')"
        ],
        "answer": "document.getElementById('id')",
        "difficulty": "Easy",
        "explanation": "`getElementById('id')` is the most efficient way to select a single element by its unique ID."
    },
    {
        "question": "How do you select all elements with a specific class using the DOM?",
        "options": [
            "document.getElementsByClassName('class')",
            "document.querySelector('.class')",
            "document.getClass('class')",
            "document.selectClass('class')"
        ],
        "answer": "document.getElementsByClassName('class')",
        "difficulty": "Medium",
        "explanation": "`getElementsByClassName('class')` returns a live HTMLCollection of elements with the specified class name."
    },
    {
        "question": "How do you select the first element matching a CSS selector?",
        "options": [
            "document.querySelector('selector')",
            "document.getElementsByTagName('selector')[0]",
            "document.select('selector')",
            "document.find('selector')"
        ],
        "answer": "document.querySelector('selector')",
        "difficulty": "Medium",
        "explanation": "`querySelector('selector')` returns the first element that matches the specified CSS selector."
    },
    {
        "question": "How do you select all elements matching a CSS selector?",
        "options": [
            "document.querySelectorAll('selector')",
            "document.getElementsBySelector('selector')",
            "document.selectAll('selector')",
            "document.findAll('selector')"
        ],
        "answer": "document.querySelectorAll('selector')",
        "difficulty": "Medium",
        "explanation": "`querySelectorAll('selector')` returns a static NodeList of all elements matching the CSS selector."
    },
    {
        "question": "How do you get the tag name of a DOM element?",
        "options": [
            "element.tagName",
            "element.name",
            "element.getTag()",
            "element.tag()"
        ],
        "answer": "element.tagName",
        "difficulty": "Medium",
        "explanation": "`tagName` returns the tag name of an element (e.g., 'DIV') in uppercase."
    },
    {
        "question": "What will `element.tagName` return for a `<p>` element?",
        "options": [
            "P",
            "p",
            "<p>",
            "paragraph"
        ],
        "answer": "P",
        "difficulty": "Medium",
        "explanation": "`tagName` returns the tag name in uppercase, so for a `<p>` element, it returns 'P'."
    },
    {
        "question": "How do you count the number of child elements in a DOM node?",
        "options": [
            "element.children.length",
            "element.childNodes.length",
            "element.countChildren()",
            "element.getChildCount()"
        ],
        "answer": "element.children.length",
        "difficulty": "Medium",
        "explanation": "The `length` property of `element.children` returns the number of child element nodes."
    },
    {
        "question": "How do you get the value of an attribute from a DOM element?",
        "options": [
            "element.getAttribute('attr')",
            "element.attribute('attr')",
            "element.attr('attr')",
            "element.getAttr('attr')"
        ],
        "answer": "element.getAttribute('attr')",
        "difficulty": "Medium",
        "explanation": "`getAttribute('attr')` retrieves the value of the specified attribute from an element."
    },
    {
        "question": "How do you set an attribute on a DOM element?",
        "options": [
            "element.setAttribute('attr', 'value')",
            "element.attribute('attr', 'value')",
            "element.attr('attr', 'value')",
            "element.setAttr('attr', 'value')"
        ],
        "answer": "element.setAttribute('attr', 'value')",
        "difficulty": "Medium",
        "explanation": "`setAttribute('attr', 'value')` sets or updates the value of the specified attribute."
    },
    {
        "question": "How do you remove an attribute from a DOM element?",
        "options": [
            "element.removeAttribute('attr')",
            "element.deleteAttribute('attr')",
            "element.removeAttr('attr')",
            "element.unsetAttribute('attr')"
        ],
        "answer": "element.removeAttribute('attr')",
        "difficulty": "Medium",
        "explanation": "`removeAttribute('attr')` removes the specified attribute from an element."
    },
    {
        "question": "How do you get the name of the first attribute of a DOM element?",
        "options": [
            "element.attributes[0].name",
            "element.attributes[0].key",
            "element.getAttributeName(0)",
            "element.attributes[0].id"
        ],
        "answer": "element.attributes[0].name",
        "difficulty": "Hard",
        "explanation": "The `attributes` property is a NamedNodeMap, and `element.attributes[0].name` gets the name of the first attribute."
    },
    {
        "question": "How do you get the value of the first attribute of a DOM element?",
        "options": [
            "element.attributes[0].value",
            "element.attributes[0].data",
            "element.getAttributeValue(0)",
            "element.attributes[0].attr"
        ],
        "answer": "element.attributes[0].value",
        "difficulty": "Hard",
        "explanation": "`element.attributes[0].value` retrieves the value of the first attribute in the element's attributes collection."
    },
    {
        "question": "How do you check if an element has a specific attribute?",
        "options": [
            "element.hasAttribute('attr')",
            "element.containsAttribute('attr')",
            "element.checkAttribute('attr')",
            "element.getAttribute('attr') !== null"
        ],
        "answer": "element.hasAttribute('attr')",
        "difficulty": "Medium",
        "explanation": "`hasAttribute('attr')` returns true if the element has the specified attribute, false otherwise."
    },
    {
        "question": "How do you create a new element in the DOM?",
        "options": [
            "document.createElement('tag')",
            "document.newElement('tag')",
            "document.addElement('tag')",
            "document.makeElement('tag')"
        ],
        "answer": "document.createElement('tag')",
        "difficulty": "Medium",
        "explanation": "`createElement('tag')` creates a new element node with the specified tag name."
    },
    {
        "question": "How do you add a new element as the last child of a parent node?",
        "options": [
            "parent.appendChild(element)",
            "parent.addChild(element)",
            "parent.insert(element)",
            "parent.append(element)"
        ],
        "answer": "parent.appendChild(element)",
        "difficulty": "Medium",
        "explanation": "`appendChild(element)` adds the specified element as the last child of the parent node."
    },
    {
        "question": "How do you insert an element before another element in the DOM?",
        "options": [
            "parent.insertBefore(newElement, referenceElement)",
            "parent.insert(newElement, referenceElement)",
            "parent.addBefore(newElement, referenceElement)",
            "parent.prepend(newElement, referenceElement)"
        ],
        "answer": "parent.insertBefore(newElement, referenceElement)",
        "difficulty": "Hard",
        "explanation": "`insertBefore(newElement, referenceElement)` inserts `newElement` before `referenceElement` as a child of `parent`."
    },
    {
        "question": "What happens if you call `appendChild` with a node already in the DOM?",
        "options": [
            "The node is moved to the new location",
            "The node is duplicated",
            "An error is thrown",
            "Nothing happens"
        ],
        "answer": "The node is moved to the new location",
        "difficulty": "Hard",
        "explanation": "`appendChild` moves an existing node to the new location if it’s already in the DOM, rather than duplicating it."
    },
    {
        "question": "How do you create a text node in the DOM?",
        "options": [
            "document.createTextNode('text')",
            "document.newText('text')",
            "document.createText('text')",
            "document.addText('text')"
        ],
        "answer": "document.createTextNode('text')",
        "difficulty": "Medium",
        "explanation": "`createTextNode('text')` creates a text node with the specified content."
    },
    {
        "question": "How do you distinguish between element and non-element nodes in the DOM?",
        "options": [
            "Check the nodeType property",
            "Check the tagName property",
            "Check the attributes property",
            "Check the children property"
        ],
        "answer": "Check the nodeType property",
        "difficulty": "Medium",
        "explanation": "`nodeType` identifies whether a node is an element (1), text (3), comment (8), etc."
    },
    {
        "question": "How do you get all child nodes, including text and comments?",
        "options": [
            "element.childNodes",
            "element.children",
            "element.getAllChildren()",
            "element.nodes()"
        ],
        "answer": "element.childNodes",
        "difficulty": "Medium",
        "explanation": "`childNodes` returns a live NodeList of all child nodes, including elements, text, and comments."
    },
    {
        "question": "What is the difference between `children` and `childNodes`?",
        "options": [
            "`children` returns only elements, `childNodes` includes all nodes",
            "`children` includes text nodes, `childNodes` includes elements",
            "`children` is a NodeList, `childNodes` is an HTMLCollection",
            "`children` is static, `childNodes` is live"
        ],
        "answer": "`children` returns only elements, `childNodes` includes all nodes",
        "difficulty": "Hard",
        "explanation": "`children` returns only element nodes, while `childNodes` includes all node types (elements, text, comments, etc.)."
    },
    {
        "question": "How do you replace an existing node with a new node in the DOM?",
        "options": [
            "parent.replaceChild(newNode, oldNode)",
            "parent.swapNode(newNode, oldNode)",
            "parent.replace(newNode, oldNode)",
            "parent.updateChild(newNode, oldNode)"
        ],
        "answer": "parent.replaceChild(newNode, oldNode)",
        "difficulty": "Hard",
        "explanation": "`replaceChild(newNode, oldNode)` replaces `oldNode` with `newNode` in the parent’s child list."
    },
    {
        "question": "How do you remove a child node from the DOM?",
        "options": [
            "parent.removeChild(child)",
            "child.removeNode()",
            "parent.deleteChild(child)",
            "child.detach()"
        ],
        "answer": "parent.removeChild(child)",
        "difficulty": "Medium",
        "explanation": "`removeChild(child)` removes the specified child node from the parent."
    },
    {
        "question": "What does `document.documentElement` return?",
        "options": [
            "The root element of the document (usually `<html>`)",
            "The first child of the `<body>`",
            "The `<head>` element",
            "The entire DOM tree"
        ],
        "answer": "The root element of the document (usually `<html>`)",
        "difficulty": "Medium",
        "explanation": "`document.documentElement` returns the root element of the document, typically the `<html>` element."
    },
    {
        "question": "How do you select elements by tag name in the DOM?",
        "options": [
            "document.getElementsByTagName('tag')",
            "document.querySelectorAll('tag')",
            "document.selectTag('tag')",
            "document.findByTag('tag')"
        ],
        "answer": "document.getElementsByTagName('tag')",
        "difficulty": "Medium",
        "explanation": "`getElementsByTagName('tag')` returns a live HTMLCollection of elements with the specified tag name."
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

# CSS for enhanced UI
st.markdown("""
    <style>
    body {
        background: var(--bg-gradient);
        color: var(--text-color);
        font-family: 'Inter', 'Arial', sans-serif;
        transition: all 0.3s ease;
    }
    :root {
        --bg-gradient: linear-gradient(180deg, #1a1a3b, #2c2c54);
        --bg-container: #2c2c54;
        --text-color: #ffffff;
        --button-bg: linear-gradient(45deg, #6b21a8, #a855f7);
        --button-hover: linear-gradient(45deg, #8b5cf6, #c084fc);
        --code-bg: #1e1e1e;
        --shadow: rgba(0,0,0,0.3);
    }
    [data-theme="light"] {
        --bg-gradient: linear-gradient(180deg, #e0e7ff, #f3e8ff);
        --bg-container: #ffffff;
        --text-color: #1f2937;
        --button-bg: linear-gradient(45deg, #4f46e5, #7c3aed);
        --button-hover: linear-gradient(45deg, #6366f1, #a78bfa);
        --code-bg: #f1f5f9;
        --shadow: rgba(0,0,0,0.1);
    }
    .main-container {
        background: var(--bg-container);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 25px var(--shadow);
        max-width: 900px;
        margin: 20px auto;
    }
    .stButton>button {
        background: var(--button-bg);
        color: var(--text-color);
        border: none;
        border-radius: 10px;
        padding: 12px;
        width: 100%;
        font-size: 16px;
        font-weight: 600;
        margin: 6px 0;
        cursor: pointer;
        transition: all 0.3s ease;
        transform: scale(1);
    }
    .stButton>button:hover {
        background: var(--button-hover);
        transform: scale(1.05);
        box-shadow: 0 4px 12px var(--shadow);
    }
    .stButton>button:disabled {
        background: #6b7280;
        cursor: not-allowed;
        transform: scale(1);
    }
    .selected-correct {
        background: #34c759 !important;
        transform: scale(1.05);
    }
    .selected-wrong {
        background: #ff3b30 !important;
        transform: scale(1.05);
    }
    .question-container {
        background: var(--bg-container);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 12px var(--shadow);
        margin-bottom: 15px;
    }
    .feedback-correct {
        color: #34c759;
        font-weight: 600;
        font-size: 18px;
        margin: 15px 0;
        animation: fadeIn 0.5s ease;
    }
    .feedback-wrong {
        color: #ff3b30;
        font-weight: 600;
        font-size: 18px;
        margin: 15px 0;
        animation: fadeIn 0.5s ease;
    }
    .progress-bar {
        background: #4b4b6b;
        border-radius: 10px;
        height: 12px;
        margin: 10px 0;
        position: relative;
    }
    .progress-fill {
        background: var(--button-bg);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    .progress-text {
        position: absolute;
        top: -20px;
        right: 0;
        color: var(--text-color);
        font-size: 12px;
    }
    .title {
        font-size: 36px;
        text-align: center;
        margin-bottom: 8px;
        color: var(--text-color);
    }
    .caption {
        text-align: center;
        color: #b0b0d0;
        font-size: 16px;
        margin-bottom: 20px;
    }
    .timer {
        font-size: 16px;
        color: #ff6b6b;
        font-weight: 600;
        text-align: center;
        margin-top: 10px;
    }
    .difficulty {
        font-size: 14px;
        color: #b0b0d0;
        margin-bottom: 10px;
    }
    .stCodeBlock {
        background-color: var(--code-bg) !important;
        border-radius: 8px;
        padding: 15px;
        font-family: 'Consolas', 'Monaco', monospace;
        font-size: 14px;
        line-height: 1.5;
        border: 1px solid #4b4b6b;
    }
    .stCodeBlock pre, .stCodeBlock code {
        color: var(--text-color);
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @media (max-width: 600px) {
        .main-container {
            padding: 15px;
            margin: 10px;
        }
        .title {
            font-size: 28px;
        }
        .stButton>button {
            font-size: 14px;
            padding: 8px;
        }
    }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
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
        <p style="color: #b0b0d0;">60 minutes, 2 points per correct answer. Ready?</p>
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
                    question_parts = q["question"].split("```javascript\n") if "```javascript
                    question_text = question_parts[0].strip()
                    code_snippet = question_parts[1].split("```")[0].strip()
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{question_text}**")
                    st.code(code_snippet, language="javascript" if "```javascript
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
            st.markdown(f'<h2 style="color: #34c759; text-align: center;">🏆 Score: {st.session_state.score}/{total_possible_score}</h2>', unsafe_allow_html=True)
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

            # Confetti for high score
            if accuracy > 80:
                st.markdown("""
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
                    st.markdown(f'<div style="color: var(--text-color);">Question {i+1}: {ans["question"]}<br>Your Answer: {ans["user_answer"]}<br>{status}<br>Explanation: {quiz[i]["explanation"]}</div>', unsafe_allow_html=True)

            # Play Again button
            if st.button("🔄 Play Again", key="play_again"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
