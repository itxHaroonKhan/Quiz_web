
import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 67 questions covering specified JavaScript topics
quiz = [
    {
        "question": "Which event is triggered when a user clicks on an HTML element?",
        "options": ["onmouseover", "onclick", "onchange", "onkeydown"],
        "answer": "onclick",
        "difficulty": "Easy",
        "explanation": "The 'onclick' event is triggered when a user clicks on an element."
    },
    {
        "question": "What does the 'onmouseover' event do?",
        "options": [
            "Triggers when the mouse pointer moves over an element",
            "Triggers when an element is clicked",
            "Triggers when a key is pressed",
            "Triggers when a form is submitted"
        ],
        "answer": "Triggers when the mouse pointer moves over an element",
        "difficulty": "Easy",
        "explanation": "The 'onmouseover' event fires when the mouse pointer enters an element."
    },
    {
        "question": "How do you add an event listener to a button in JavaScript?",
        "options": [
            "button.addEventListener('click', myFunction);",
            "button.onClick = myFunction;",
            "button.attachEvent('click', myFunction);",
            "button.event('click', myFunction);"
        ],
        "answer": "button.addEventListener('click', myFunction);",
        "difficulty": "Medium",
        "explanation": "'addEventListener' is the standard way to attach an event handler to an element."
    },
    {
        "question": "Which event is fired when a user presses a key on the keyboard?",
        "options": ["onkeypress", "onchange", "onclick", "onfocus"],
        "answer": "onkeypress",
        "difficulty": "Easy",
        "explanation": "The 'onkeypress' event is triggered when a key is pressed and released."
    },
    {
        "question": "How can you get the value of an input field with id='myInput'?",
        "options": [
            "document.getElementById('myInput').value",
            "document.querySelector('myInput').value",
            "document.getElementById('myInput').text",
            "document.getElementById('myInput').innerHTML"
        ],
        "answer": "document.getElementById('myInput').value",
        "difficulty": "Medium",
        "explanation": "The 'value' property retrieves the current value of an input element."
    },
    {
        "question": "How do you set the value of an input field with id='myInput' to 'Hello'?",
        "options": [
            "document.getElementById('myInput').value = 'Hello';",
            "document.getElementById('myInput').text = 'Hello';",
            "document.getElementById('myInput').innerHTML = 'Hello';",
            "document.querySelector('myInput').value = 'Hello';"
        ],
        "answer": "document.getElementById('myInput').value = 'Hello';",
        "difficulty": "Medium",
        "explanation": "The 'value' property is used to set the value of an input element."
    },
    {
        "question": "How can you change the text of a paragraph with id='myPara' to 'New Text'?",
        "options": [
            "document.getElementById('myPara').innerText = 'New Text';",
            "document.getElementById('myPara').value = 'New Text';",
            "document.getElementById('myPara').style = 'New Text';",
            "document.getElementById('myPara').textContent = 'New Text';"
        ],
        "answer": "document.getElementById('myPara').innerText = 'New Text';",
        "difficulty": "Medium",
        "explanation": "Both 'innerText' and 'textContent' can be used, but 'innerText' is more commonly used for visible text."
    },
    {
        "question": "What is the difference between 'innerText' and 'textContent'?",
        "options": [
            "'innerText' considers CSS styling, 'textContent' includes all text including hidden elements",
            "'innerText' is for inputs, 'textContent' is for divs",
            "'innerText' is faster, 'textContent' is slower",
            "There is no difference"
        ],
        "answer": "'innerText' considers CSS styling, 'textContent' includes all text including hidden elements",
        "difficulty": "Hard",
        "explanation": "'innerText' reflects visible text, while 'textContent' includes all text, even in hidden elements."
    },
    {
        "question": "How do you change the source of an image with id='myImage' to 'new.jpg'?",
        "options": [
            "document.getElementById('myImage').src = 'new.jpg';",
            "document.getElementById('myImage').image = 'new.jpg';",
            "document.getElementById('myImage').url = 'new.jpg';",
            "document.getElementById('myImage').href = 'new.jpg';"
        ],
        "answer": "document.getElementById('myImage').src = 'new.jpg';",
        "difficulty": "Medium",
        "explanation": "The 'src' property is used to set the source of an image element."
    },
    {
        "question": "How can you swap the sources of two images with ids 'img1' and 'img2'?",
        "options": [
            "let temp = img1.src; img1.src = img2.src; img2.src = temp;",
            "img1.src = img2.src; img2.src = img1.src;",
            "img1.swap(img2);",
            "img1.src.swap(img2.src);"
        ],
        "answer": "let temp = img1.src; img1.src = img2.src; img2.src = temp;",
        "difficulty": "Medium",
        "explanation": "A temporary variable is needed to swap the 'src' properties to avoid overwriting."
    },
    {
        "question": "How do you add a class 'active' to an element with id='myDiv'?",
        "options": [
            "document.getElementById('myDiv').classList.add('active');",
            "document.getElementById('myDiv').class = 'active';",
            "document.getElementById('myDiv').style = 'active';",
            "document.getElementById('myDiv').addClass('active');"
        ],
        "answer": "document.getElementById('myDiv').classList.add('active');",
        "difficulty": "Medium",
        "explanation": "'classList.add' is the proper way to add a class without overwriting existing classes."
    },
    {
        "question": "How do you set the background color of an element with id='myDiv' to blue?",
        "options": [
            "document.getElementById('myDiv').style.backgroundColor = 'blue';",
            "document.getElementById('myDiv').background = 'blue';",
            "document.getElementById('myDiv').style.color = 'blue';",
            "document.getElementById('myDiv').style = 'blue';"
        ],
        "answer": "document.getElementById('myDiv').style.backgroundColor = 'blue';",
        "difficulty": "Medium",
        "explanation": "The 'style.backgroundColor' property sets the background color of an element."
    },
    {
        "question": "How do you select all 'div' elements on a page?",
        "options": [
            "document.getElementsByTagName('div');",
            "document.querySelector('div');",
            "document.getElementsByClassName('div');",
            "document.getElementById('div');"
        ],
        "answer": "document.getElementsByTagName('div');",
        "difficulty": "Medium",
        "explanation": "'getElementsByTagName' returns a live HTMLCollection of all elements with the specified tag."
    },
    {
        "question": "How do you select all elements with class 'item'?",
        "options": [
            "document.querySelectorAll('.item');",
            "document.getElementsByTagName('.item');",
            "document.getElementById('item');",
            "document.querySelector('item');"
        ],
        "answer": "document.querySelectorAll('.item');",
        "difficulty": "Medium",
        "explanation": "'querySelectorAll' returns a NodeList of elements matching the CSS selector."
    },
    {
        "question": "What is the DOM in JavaScript?",
        "options": [
            "A programming interface for HTML and XML documents",
            "A database for storing web data",
            "A styling framework for web pages",
            "A JavaScript library"
        ],
        "answer": "A programming interface for HTML and XML documents",
        "difficulty": "Easy",
        "explanation": "The DOM (Document Object Model) represents the structure of a document as a tree of objects."
    },
    {
        "question": "How do you access the parent node of an element?",
        "options": [
            "element.parentNode",
            "element.childNode",
            "element.nextSibling",
            "element.previousSibling"
        ],
        "answer": "element.parentNode",
        "difficulty": "Medium",
        "explanation": "'parentNode' returns the parent node of the specified element in the DOM tree."
    },
    {
        "question": "How do you get all child nodes of an element with id='myDiv'?",
        "options": [
            "document.getElementById('myDiv').childNodes",
            "document.getElementById('myDiv').childrenNodes",
            "document.getElementById('myDiv').nodes",
            "document.getElementById('myDiv').child"
        ],
        "answer": "document.getElementById('myDiv').childNodes",
        "difficulty": "Medium",
        "explanation": "'childNodes' returns a NodeList of all child nodes, including text and comment nodes."
    },
    {
        "question": "What is the difference between 'childNodes' and 'children'?",
        "options": [
            "'childNodes' includes all nodes, 'children' includes only element nodes",
            "'childNodes' is for text, 'children' is for images",
            "'childNodes' is faster, 'children' is slower",
            "There is no difference"
        ],
        "answer": "'childNodes' includes all nodes, 'children' includes only element nodes",
        "difficulty": "Hard",
        "explanation": "'childNodes' includes text, comments, and elements, while 'children' includes only HTML elements."
    },
    {
        "question": "What is the 'nodeType' property used for in the DOM?",
        "options": [
            "To identify the type of a node",
            "To count the number of nodes",
            "To set the style of a node",
            "To find the parent node"
        ],
        "answer": "To identify the type of a node",
        "difficulty": "Medium",
        "explanation": "'nodeType' returns a number indicating the type of node (e.g., 1 for element, 3 for text)."
    },
    {
        "question": "Which 'nodeType' value represents an element node?",
        "options": ["1", "3", "8", "10"],
        "answer": "1",
        "difficulty": "Hard",
        "explanation": "A 'nodeType' of 1 indicates an element node in the DOM."
    },
    {
        "question": "How do you select an element with a specific attribute, like [data-id='123']?",
        "options": [
            "document.querySelector('[data-id=\"123\"]');",
            "document.getElementById('data-id=123');",
            "document.getElementsByTagName('data-id');",
            "document.querySelectorAll('data-id=123');"
        ],
        "answer": "document.querySelector('[data-id=\"123\"]');",
        "difficulty": "Medium",
        "explanation": "'querySelector' uses CSS selector syntax to find the first matching element."
    },
    {
        "question": "How do you get the tag name of an element?",
        "options": [
            "element.tagName",
            "element.name",
            "element.id",
            "element.className"
        ],
        "answer": "element.tagName",
        "difficulty": "Medium",
        "explanation": "'tagName' returns the tag name of an element (e.g., 'DIV', 'P') in uppercase."
    },
    {
        "question": "How do you count the number of 'p' elements on a page?",
        "options": [
            "document.getElementsByTagName('p').length",
            "document.querySelector('p').length",
            "document.getElementsByClassName('p').length",
            "document.getElementById('p').length"
        ],
        "answer": "document.getElementsByTagName('p').length",
        "difficulty": "Medium",
        "explanation": "'getElementsByTagName' returns a collection, and 'length' gives the count."
    },
    {
        "question": "How do you check if an element has a specific attribute?",
        "options": [
            "element.hasAttribute('name');",
            "element.getAttribute('name');",
            "element.attribute('name');",
            "element.checkAttribute('name');"
        ],
        "answer": "element.hasAttribute('name');",
        "difficulty": "Medium",
        "explanation": "'hasAttribute' returns true if the element has the specified attribute."
    },
    {
        "question": "How do you get the value of an attribute 'data-id' from an element?",
        "options": [
            "element.getAttribute('data-id');",
            "element.dataId;",
            "element.attribute('data-id');",
            "element.getProperty('data-id');"
        ],
        "answer": "element.getAttribute('data-id');",
        "difficulty": "Medium",
        "explanation": "'getAttribute' retrieves the value of the specified attribute."
    },
    {
        "question": "How do you set an attribute 'data-id' to '123' on an element?",
        "options": [
            "element.setAttribute('data-id', '123');",
            "element.dataId = '123';",
            "element.attribute('data-id', '123');",
            "element.setProperty('data-id', '123');"
        ],
        "answer": "element.setAttribute('data-id', '123');",
        "difficulty": "Medium",
        "explanation": "'setAttribute' sets the value of an attribute on an element."
    },
    {
        "question": "How do you create a new 'div' element in JavaScript?",
        "options": [
            "document.createElement('div');",
            "document.newElement('div');",
            "document.createNode('div');",
            "document.addElement('div');"
        ],
        "answer": "document.createElement('div');",
        "difficulty": "Medium",
        "explanation": "'createElement' creates a new element node with the specified tag name."
    },
    {
        "question": "How do you append a new element as a child of an element with id='myDiv'?",
        "options": [
            "document.getElementById('myDiv').appendChild(newElement);",
            "document.getElementById('myDiv').addChild(newElement);",
            "document.getElementById('myDiv').insert(newElement);",
            "document.getElementById('myDiv').append(newElement);"
        ],
        "answer": "document.getElementById('myDiv').appendChild(newElement);",
        "difficulty": "Medium",
        "explanation": "'appendChild' adds a node as the last child of the specified parent."
    },
    {
        "question": "How do you insert an element before another element in the DOM?",
        "options": [
            "parentElement.insertBefore(newElement, referenceElement);",
            "parentElement.addBefore(newElement, referenceElement);",
            "parentElement.insert(newElement, referenceElement);",
            "parentElement.prepend(newElement, referenceElement);"
        ],
        "answer": "parentElement.insertBefore(newElement, referenceElement);",
        "difficulty": "Hard",
        "explanation": "'insertBefore' inserts a new node before the specified reference node."
    },
    {
        "question": "What happens when you use 'element.remove()'?",
        "options": [
            "Removes the element from the DOM",
            "Hides the element",
            "Clears the element's content",
            "Removes the element's attributes"
        ],
        "answer": "Removes the element from the DOM",
        "difficulty": "Medium",
        "explanation": "'remove' removes the element and its children from the DOM tree."
    },
    {
        "question": "How do you toggle a class 'active' on an element?",
        "options": [
            "element.classList.toggle('active');",
            "element.classList.switch('active');",
            "element.toggleClass('active');",
            "element.className = 'active';"
        ],
        "answer": "element.classList.toggle('active');",
        "difficulty": "Medium",
        "explanation": "'classList.toggle' adds the class if absent, removes it if present."
    },
    {
        "question": "What does 'querySelectorAll' return?",
        "options": [
            "A static NodeList of matching elements",
            "A single element",
            "A live HTMLCollection",
            "An array of elements"
        ],
        "answer": "A static NodeList of matching elements",
        "difficulty": "Medium",
        "explanation": "'querySelectorAll' returns a static NodeList of elements matching the CSS selector."
    },
    {
        "question": "How do you get the first child element of a parent element?",
        "options": [
            "parentElement.firstElementChild",
            "parentElement.firstChild",
            "parentElement.children[0]",
            "Both A and C"
        ],
        "answer": "Both A and C",
        "difficulty": "Hard",
        "explanation": "'firstElementChild' and 'children[0]' both return the first child element, excluding non-element nodes."
    },
    {
        "question": "What is the purpose of 'element.innerHTML'?",
        "options": [
            "Gets or sets the HTML content of an element",
            "Gets or sets the text content of an element",
            "Gets or sets the style of an element",
            "Gets or sets the attributes of an element"
        ],
        "answer": "Gets or sets the HTML content of an element",
        "difficulty": "Medium",
        "explanation": "'innerHTML' allows you to read or write HTML content within an element."
    },
    {
        "question": "What is a potential risk of using 'innerHTML'?",
        "options": [
            "It can lead to cross-site scripting (XSS) attacks",
            "It slows down the browser",
            "It removes all event listeners",
            "It only works in older browsers"
        ],
        "answer": "It can lead to cross-site scripting (XSS) attacks",
        "difficulty": "Hard",
        "explanation": "Using 'innerHTML' with untrusted input can allow malicious scripts to execute."
    },
    {
        "question": "How do you remove an attribute 'data-id' from an element?",
        "options": [
            "element.removeAttribute('data-id');",
            "element.deleteAttribute('data-id');",
            "element.remove('data-id');",
            "element.setAttribute('data-id', null);"
        ],
        "answer": "element.removeAttribute('data-id');",
        "difficulty": "Medium",
        "explanation": "'removeAttribute' removes the specified attribute from an element."
    },
    {
        "question": "What does 'element.nextSibling' return?",
        "options": [
            "The next node in the DOM, including text or comment nodes",
            "The next element node only",
            "The parent node",
            "The previous node"
        ],
        "answer": "The next node in the DOM, including text or comment nodes",
        "difficulty": "Hard",
        "explanation": "'nextSibling' returns the next node, which could be an element, text, or comment."
    },
    {
        "question": "How do you get the last child element of a parent element?",
        "options": [
            "parentElement.lastElementChild",
            "parentElement.lastChild",
            "parentElement.children[-1]",
            "parentElement.childNodes.last"
        ],
        "answer": "parentElement.lastElementChild",
        "difficulty": "Medium",
        "explanation": "'lastElementChild' returns the last child element, excluding non-element nodes."
    },
    {
        "question": "What does 'document.createTextNode' do?",
        "options": [
            "Creates a new text node",
            "Creates a new element node",
            "Creates a new attribute",
            "Creates a new comment node"
        ],
        "answer": "Creates a new text node",
        "difficulty": "Medium",
        "explanation": "'createTextNode' creates a text node that can be added to the DOM."
    },
    {
        "question": "How do you replace an existing node with a new node?",
        "options": [
            "parentElement.replaceChild(newNode, oldNode);",
            "parentElement.swapChild(newNode, oldNode);",
            "parentElement.replace(newNode, oldNode);",
            "parentElement.insertChild(newNode, oldNode);"
        ],
        "answer": "parentElement.replaceChild(newNode, oldNode);",
        "difficulty": "Hard",
        "explanation": "'replaceChild' replaces an existing child node with a new node."
    },
    {
        "question": "What is the purpose of 'element.className'?",
        "options": [
            "Gets or sets the class attribute of an element",
            "Adds a new class to an element",
            "Removes a class from an element",
            "Toggles a class on an element"
        ],
        "answer": "Gets or sets the class attribute of an element",
        "difficulty": "Medium",
        "explanation": "'className' gets or sets the entire class string, but 'classList' is preferred for manipulation."
    },
    {
        "question": "How do you check if an element has a specific class?",
        "options": [
            "element.classList.contains('className');",
            "element.className.includes('className');",
            "element.hasClass('className');",
            "element.class('className');"
        ],
        "answer": "element.classList.contains('className');",
        "difficulty": "Medium",
        "explanation": "'classList.contains' checks if the specified class is present on the element."
    },
    {
        "question": "What does 'element.getBoundingClientRect()' return?",
        "options": [
            "An object with the element's size and position",
            "The element's text content",
            "The element's attributes",
            "The element's parent node"
        ],
        "answer": "An object with the element's size and position",
        "difficulty": "Hard",
        "explanation": "'getBoundingClientRect' returns an object with properties like width, height, top, and left."
    },
    {
        "question": "How do you get all attributes of an element?",
        "options": [
            "element.attributes",
            "element.getAttributes()",
            "element.allAttributes",
            "element.attributeList"
        ],
        "answer": "element.attributes",
        "difficulty": "Hard",
        "explanation": "'attributes' returns a NamedNodeMap of all attributes on the element."
    },
    {
        "question": "What is the difference between 'appendChild' and 'append'?",
        "options": [
            "'appendChild' adds one node, 'append' can add multiple nodes or strings",
            "'appendChild' is faster, 'append' is slower",
            "'appendChild' adds text, 'append' adds elements",
            "There is no difference"
        ],
        "answer": "'appendChild' adds one node, 'append' can add multiple nodes or strings",
        "difficulty": "Hard",
        "explanation": "'append' is more flexible, allowing multiple nodes or strings, while 'appendChild' takes a single node."
    },
    {
        "question": "How do you get the computed style of an element?",
        "options": [
            "window.getComputedStyle(element);",
            "element.style;",
            "element.getStyle();",
            "document.getStyle(element);"
        ],
        "answer": "window.getComputedStyle(element);",
        "difficulty": "Hard",
        "explanation": "'getComputedStyle' returns the computed CSS styles applied to an element."
    },
    {
        "question": "What does 'element.closest(selector)' do?",
        "options": [
            "Finds the nearest ancestor matching the selector",
            "Finds the nearest sibling matching the selector",
            "Finds all descendants matching the selector",
            "Finds the parent element only"
        ],
        "answer": "Finds the nearest ancestor matching the selector",
        "difficulty": "Hard",
        "explanation": "'closest' traverses up the DOM to find the nearest ancestor that matches the selector."
    },
    {
        "question": "How do you prevent the default action of an event?",
        "options": [
            "event.preventDefault();",
            "event.stopPropagation();",
            "event.cancel();",
            "event.defaultPrevent();"
        ],
        "answer": "event.preventDefault();",
        "difficulty": "Medium",
        "explanation": "'preventDefault' stops the default action of an event, like form submission or link navigation."
    },
    {
        "question": "What does 'event.stopPropagation()' do?",
        "options": [
            "Prevents the event from bubbling up the DOM tree",
            "Prevents the default action of the event",
            "Stops all events on the page",
            "Removes the event listener"
        ],
        "answer": "Prevents the event from bubbling up the DOM tree",
        "difficulty": "Hard",
        "explanation": "'stopPropagation' prevents the event from reaching parent elements in the bubbling phase."
    },
    {
        "question": "How do you clone an element in the DOM?",
        "options": [
            "element.cloneNode(true);",
            "element.copyNode();",
            "element.clone();",
            "element.duplicate();"
        ],
        "answer": "element.cloneNode(true);",
        "difficulty": "Hard",
        "explanation": "'cloneNode(true)' creates a deep copy of the element, including its children."
    }
]
# Cache shuffled quiz (removed for testing, re-add if needed)
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
    if not quiz:
        st.error("Quiz list is empty!")
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
        "started": False,
        "max_streak": 0
    })
    st.write(f"Initialized quiz with {len(st.session_state.quiz_data)} questions")

# Theme toggle
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# Timer logic
def update_timer():
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.session_state.time_left = max(3600 - elapsed, 0)  # 60 minutes
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
        "time_left": 3600,  # 60 minutes
        "streak": 0,
        "max_streak": 0,
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
st.markdown('<h1 class="title">🚀 JavaScript Mastery Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript Expertise!</p>', unsafe_allow_html=True)

# Theme toggle button
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen
if not st.session_state.started:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: var(--text-color); font-size: 18px;">Test your JavaScript skills with 67 comprehensive questions!</p>
        <p style="color: #b0b0d0;">60 minutes, 2 points per correct answer. Ready?</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Quiz", key="start_quiz"):
        st.session_state.started = True
        st.session_state.start_time = datetime.now()
        st.write(f"Quiz started with {len(st.session_state.quiz_data)} questions")
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
                if "```javascript" in q["question"]:
                    question_parts = q["question"].split("```javascript\n")
                    question_text = question_parts[0].strip()
                    code_snippet = question_parts[1].split("```")[0].strip()
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{question_text}**")
                    st.code(code_snippet, language="javascript")
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
                        key=f"q{i}_{st.session_state.current_q}",
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
                            st.session_state.score += 2
                            st.session_state.streak += 1
                            if st.session_state.streak > st.session_state.max_streak:
                                st.session_state.max_streak = st.session_state.streak
                            if st.session_state.streak >= 3:
                                st.session_state.score += 0.5
                        else:
                            st.session_state.streak = 0
                        # Move to next question or show results
                        if st.session_state.current_q < len(st.session_state.quiz_data) - 1:
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
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 3600)  # 60 minutes
            total_possible_score = len(quiz) * 2
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
                - 🔥 Max Streak: {st.session_state.max_streak}
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

            # Review Answers
            st.markdown('<h3>📝 Review Your Answers</h3>', unsafe_allow_html=True)
            for i, ans in enumerate(st.session_state.answers):
                if ans:
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})"
                    st.markdown(f"""
                    <div style="color: var(--text-color); margin-bottom: 10px;">
                        Question {i+1}: {ans["question"]}<br>
                        Your Answer: {ans["user_answer"]}<br>
                        {status}<br>
                        Explanation: {quiz[i]["explanation"]}
                    </div>
                    """, unsafe_allow_html=True)

            # Play Again button
            if st.button("🔄 Play Again", key="play_again"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
