
import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 67 questions covering specified JavaScript topics
quiz = [
    {
        "question": "What does the 'click' event do when attached to a button element?",
        "options": [
            "Triggers when the button is hovered over",
            "Triggers when the button is clicked",
            "Triggers when the button loses focus",
            "Triggers when the button is double-clicked"
        ],
        "answer": "Triggers when the button is clicked",
        "difficulty": "Medium",
        "explanation": "The 'click' event fires when a user presses and releases the mouse button on an element, such as a button."
    },
    {
        "question": "How can you add an event listener to a button with the ID 'myButton' in JavaScript?",
        "options": [
            "document.getElementById('myButton').addEventListener('click', myFunction);",
            "document.getElementById('myButton').onclick = myFunction();",
            "document.getElementById('myButton').on('click', myFunction);",
            "document.getElementById('myButton').addListener('click', myFunction);"
        ],
        "answer": "document.getElementById('myButton').addEventListener('click', myFunction);",
        "difficulty": "Medium",
        "explanation": "The `addEventListener` method is the standard way to attach an event handler to an element without overwriting existing handlers."
    },
    {
        "question": "Which event is triggered when a user moves the mouse pointer over an element?",
        "options": [
            "onclick",
            "onmouseover",
            "onmousemove",
            "onmouseout"
        ],
        "answer": "onmouseover",
        "difficulty": "Medium",
        "explanation": "The 'onmouseover' event fires when the mouse pointer enters an element's boundaries."
    },
    {
        "question": "What does the 'input' event do when attached to a text field?",
        "options": [
            "Fires when the field is clicked",
            "Fires when the field value changes",
            "Fires when the field loses focus",
            "Fires when the form is submitted"
        ],
        "answer": "Fires when the field value changes",
        "difficulty": "Medium",
        "explanation": "The 'input' event triggers whenever the value of an input element changes, such as when typing in a text field."
    },
    {
        "question": "How do you read the value of a text input with ID 'username'?",
        "options": [
            "document.getElementById('username').value",
            "document.getElementById('username').text",
            "document.getElementById('username').innerText",
            "document.getElementById('username').innerHTML"
        ],
        "answer": "document.getElementById('username').value",
        "difficulty": "Medium",
        "explanation": "The `value` property retrieves the current value of an input element, such as a text field."
    },
    {
        "question": "How can you set the value of an input field with ID 'email' to 'test@example.com'?",
        "options": [
            "document.getElementById('email').value = 'test@example.com';",
            "document.getElementById('email').innerHTML = 'test@example.com';",
            "document.getElementById('email').text = 'test@example.com';",
            "document.getElementById('email').setValue('test@example.com');"
        ],
        "answer": "document.getElementById('email').value = 'test@example.com';",
        "difficulty": "Medium",
        "explanation": "The `value` property is used to set the value of an input element programmatically."
    },
    {
        "question": "How do you change the text content of a paragraph with ID 'info'?",
        "options": [
            "document.getElementById('info').innerHTML = 'New text';",
            "document.getElementById('info').value = 'New text';",
            "document.getElementById('info').text = 'New text';",
            "document.getElementById('info').setText('New text');"
        ],
        "answer": "document.getElementById('info').innerHTML = 'New text';",
        "difficulty": "Medium",
        "explanation": "The `innerHTML` property is used to set the content of non-input elements like paragraphs."
    },
    {
        "question": "How can you change the source of an image with ID 'myImage' to 'new.jpg'?",
        "options": [
            "document.getElementById('myImage').src = 'new.jpg';",
            "document.getElementById('myImage').image = 'new.jpg';",
            "document.getElementById('myImage').url = 'new.jpg';",
            "document.getElementById('myImage').innerHTML = 'new.jpg';"
        ],
        "answer": "document.getElementById('myImage').src = 'new.jpg';",
        "difficulty": "Medium",
        "explanation": "The `src` property is used to set or change the source URL of an image element."
    },
    {
        "question": "How do you swap the source of an image with ID 'img1' between 'pic1.jpg' and 'pic2.jpg' on click?",
        "options": [
            "document.getElementById('img1').addEventListener('click', () => { document.getElementById('img1').src = document.getElementById('img1').src === 'pic1.jpg' ? 'pic2.jpg' : 'pic1.jpg'; });",
            "document.getElementById('img1').onclick = () => { document.getElementById('img1').src = 'pic2.jpg'; };",
            "document.getElementById('img1').src = 'pic1.jpg' ? 'pic2.jpg' : 'pic1.jpg';",
            "document.getElementById('img1').toggle('pic1.jpg', 'pic2.jpg');"
        ],
        "answer": "document.getElementById('img1').addEventListener('click', () => { document.getElementById('img1').src = document.getElementById('img1').src === 'pic1.jpg' ? 'pic2.jpg' : 'pic1.jpg'; });",
        "difficulty": "Medium",
        "explanation": "The event listener checks the current `src` and toggles it between 'pic1.jpg' and 'pic2.jpg' using a ternary operator."
    },
    {
        "question": "How do you add a class 'active' to an element with ID 'myDiv'?",
        "options": [
            "document.getElementById('myDiv').classList.add('active');",
            "document.getElementById('myDiv').className = 'active';",
            "document.getElementById('myDiv').addClass('active');",
            "document.getElementById('myDiv').class = 'active';"
        ],
        "answer": "document.getElementById('myDiv').classList.add('active');",
        "difficulty": "Medium",
        "explanation": "The `classList.add` method safely adds a class to an element without overwriting existing classes."
    },
    {
        "question": "How can you set the background color of an element with ID 'box' to blue?",
        "options": [
            "document.getElementById('box').style.backgroundColor = 'blue';",
            "document.getElementById('box').background = 'blue';",
            "document.getElementById('box').style.color = 'blue';",
            "document.getElementById('box').setStyle('backgroundColor', 'blue');"
        ],
        "answer": "document.getElementById('box').style.backgroundColor = 'blue';",
        "difficulty": "Medium",
        "explanation": "The `style` property allows direct manipulation of CSS properties, with `backgroundColor` being the correct property name."
    },
    {
        "question": "How do you select all paragraph elements in a document?",
        "options": [
            "document.getElementsByTagName('p');",
            "document.querySelectorAll('paragraph');",
            "document.getElementsByClassName('p');",
            "document.getElementById('p');"
        ],
        "answer": "document.getElementsByTagName('p');",
        "difficulty": "Medium",
        "explanation": "The `getElementsByTagName` method returns a live HTMLCollection of all elements with the specified tag name."
    },
    {
        "question": "How can you select all elements with the class 'item' using querySelectorAll?",
        "options": [
            "document.querySelectorAll('.item');",
            "document.getElementsByClassName('item');",
            "document.querySelectorAll('#item');",
            "document.querySelectorAll('item');"
        ],
        "answer": "document.querySelectorAll('.item');",
        "difficulty": "Medium",
        "explanation": "The `querySelectorAll` method with a '.class' selector returns all elements with the specified class."
    },
    {
        "question": "What does the DOM stand for in JavaScript?",
        "options": [
            "Document Object Model",
            "Data Object Model",
            "Document Order Model",
            "Dynamic Object Manipulation"
        ],
        "answer": "Document Object Model",
        "difficulty": "Medium",
        "explanation": "The DOM is a programming interface that represents the structure of a webpage as a tree of objects."
    },
    {
        "question": "How can you access the parent element of an element with ID 'child'?",
        "options": [
            "document.getElementById('child').parentNode;",
            "document.getElementById('child').parent;",
            "document.getElementById('child').getParent();",
            "document.getElementById('child').parentElementNode;"
        ],
        "answer": "document.getElementById('child').parentNode;",
        "difficulty": "Medium",
        "explanation": "The `parentNode` property returns the parent node of an element in the DOM tree."
    },
    {
        "question": "How do you access the first child element of an element with ID 'parent'?",
        "options": [
            "document.getElementById('parent').firstChild;",
            "document.getElementById('parent').child[0];",
            "document.getElementById('parent').firstElement;",
            "document.getElementById('parent').children.first;"
        ],
        "answer": "document.getElementById('parent').firstChild;",
        "difficulty": "Medium",
        "explanation": "The `firstChild` property returns the first child node, which may include text or comment nodes."
    },
    {
        "question": "What is the purpose of the `nodeType` property in the DOM?",
        "options": [
            "To identify the type of a node (e.g., element, text, comment)",
            "To count the number of child nodes",
            "To get the tag name of an element",
            "To check if a node is visible"
        ],
        "answer": "To identify the type of a node (e.g., element, text, comment)",
        "difficulty": "Medium",
        "explanation": "The `nodeType` property returns a number indicating the type of node, such as 1 for elements or 3 for text."
    },
    {
        "question": "How can you select an element with the class 'highlight' using querySelector?",
        "options": [
            "document.querySelector('.highlight');",
            "document.getElementByClass('highlight');",
            "document.querySelector('#highlight');",
            "document.querySelector('highlight');"
        ],
        "answer": "document.querySelector('.highlight');",
        "difficulty": "Medium",
        "explanation": "The `querySelector` method with a '.class' selector returns the first element with the specified class."
    },
    {
        "question": "How do you get the tag name of an element with ID 'myElement'?",
        "options": [
            "document.getElementById('myElement').tagName;",
            "document.getElementById('myElement').name;",
            "document.getElementById('myElement').elementName;",
            "document.getElementById('myElement').getTag();"
        ],
        "answer": "document.getElementById('myElement').tagName;",
        "difficulty": "Medium",
        "explanation": "The `tagName` property returns the tag name of an element in uppercase (e.g., 'DIV')."
    },
    {
        "question": "How can you count the number of list items in an unordered list with ID 'myList'?",
        "options": [
            "document.getElementById('myList').getElementsByTagName('li').length;",
            "document.getElementById('myList').children.count;",
            "document.getElementById('myList').items.length;",
            "document.getElementById('myList').childNodes.length;"
        ],
        "answer": "document.getElementById('myList').getElementsByTagName('li').length;",
        "difficulty": "Medium",
        "explanation": "The `getElementsByTagName` method returns a collection of 'li' elements, and `length` gives the count."
    },
    {
        "question": "How do you get the value of an attribute named 'data-id' from an element with ID 'myElement'?",
        "options": [
            "document.getElementById('myElement').getAttribute('data-id');",
            "document.getElementById('myElement').dataId;",
            "document.getElementById('myElement').attribute('data-id');",
            "document.getElementById('myElement').getData('id');"
        ],
        "answer": "document.getElementById('myElement').getAttribute('data-id');",
        "difficulty": "Medium",
        "explanation": "The `getAttribute` method retrieves the value of the specified attribute from an element."
    },
    {
        "question": "How can you set the 'title' attribute of an element with ID 'myDiv' to 'Tooltip'?",
        "options": [
            "document.getElementById('myDiv').setAttribute('title', 'Tooltip');",
            "document.getElementById('myDiv').title = 'Tooltip';",
            "document.getElementById('myDiv').attribute('title', 'Tooltip');",
            "document.getElementById('myDiv').setTitle('Tooltip');"
        ],
        "answer": "document.getElementById('myDiv').setAttribute('title', 'Tooltip');",
        "difficulty": "Medium",
        "explanation": "The `setAttribute` method sets or updates the value of an attribute on an element."
    },
    {
        "question": "How do you create a new paragraph element in JavaScript?",
        "options": [
            "document.createElement('p');",
            "document.newElement('p');",
            "document.createNode('p');",
            "document.makeElement('p');"
        ],
        "answer": "document.createElement('p');",
        "difficulty": "Medium",
        "explanation": "The `createElement` method creates a new element node with the specified tag name."
    },
    {
        "question": "How can you append a new paragraph element to a div with ID 'container'?",
        "options": [
            "document.getElementById('container').appendChild(document.createElement('p'));",
            "document.getElementById('container').add(document.createElement('p'));",
            "document.getElementById('container').insert(document.createElement('p'));",
            "document.getElementById('container').append(document.createElement('p'));"
        ],
        "answer": "document.getElementById('container').appendChild(document.createElement('p'));",
        "difficulty": "Medium",
        "explanation": "The `appendChild` method adds a node as the last child of the specified parent element."
    },
    {
        "question": "What happens when you use `insertBefore(newNode, referenceNode)`?",
        "options": [
            "Inserts newNode before referenceNode in the parent",
            "Inserts newNode after referenceNode in the parent",
            "Replaces referenceNode with newNode",
            "Appends newNode as the last child"
        ],
        "answer": "Inserts newNode before referenceNode in the parent",
        "difficulty": "Medium",
        "explanation": "The `insertBefore` method inserts a new node before the specified reference node in the parent's child list."
    },
    {
        "question": "Which event is triggered when a user clicks a link?",
        "options": [
            "onclick",
            "onlink",
            "onhref",
            "onnavigate"
        ],
        "answer": "onclick",
        "difficulty": "Medium",
        "explanation": "The 'onclick' event is used to detect clicks on any element, including links (<a> tags)."
    },
    {
        "question": "How do you prevent the default behavior of a link when clicked?",
        "options": [
            "event.preventDefault();",
            "event.stopPropagation();",
            "event.cancel();",
            "event.stopDefault();"
        ],
        "answer": "event.preventDefault();",
        "difficulty": "Medium",
        "explanation": "The `preventDefault` method stops the default action of an event, such as navigating to a link's URL."
    },
    {
        "question": "What does `event.target` refer to in an event handler?",
        "options": [
            "The element that triggered the event",
            "The parent of the element",
            "The document object",
            "The event type"
        ],
        "answer": "The element that triggered the event",
        "difficulty": "Medium",
        "explanation": "The `event.target` property refers to the element that dispatched the event."
    },
    {
        "question": "How can you get the value of a select dropdown with ID 'options'?",
        "options": [
            "document.getElementById('options').value;",
            "document.getElementById('options').selected;",
            "document.getElementById('options').innerHTML;",
            "document.getElementById('options').text;"
        ],
        "answer": "document.getElementById('options').value;",
        "difficulty": "Medium",
        "explanation": "The `value` property of a `<select>` element returns the value of the selected option."
    },
    {
        "question": "How do you toggle a class 'hidden' on an element with ID 'myElement'?",
        "options": [
            "document.getElementById('myElement').classList.toggle('hidden');",
            "document.getElementById('myElement').className = 'hidden';",
            "document.getElementById('myElement').toggleClass('hidden');",
            "document.getElementById('myElement').classList.add('hidden');"
        ],
        "answer": "document.getElementById('myElement').classList.toggle('hidden');",
        "difficulty": "Medium",
        "explanation": "The `classList.toggle` method adds the class if it’s not present and removes it if it is."
    },
    {
        "question": "How do you set the font size of an element with ID 'text' to 20px?",
        "options": [
            "document.getElementById('text').style.fontSize = '20px';",
            "document.getElementById('text').fontSize = '20px';",
            "document.getElementById('text').style.font = '20px';",
            "document.getElementById('text').setStyle('fontSize', '20px');"
        ],
        "answer": "document.getElementById('text').style.fontSize = '20px';",
        "difficulty": "Medium",
        "explanation": "The `style.fontSize` property sets the font size of an element in CSS units like 'px'."
    },
    {
        "question": "How can you select all div elements with the class 'box'?",
        "options": [
            "document.querySelectorAll('div.box');",
            "document.getElementsByClassName('box');",
            "document.querySelectorAll('.box.div');",
            "document.getElementsByTagName('div.box');"
        ],
        "answer": "document.querySelectorAll('div.box');",
        "difficulty": "Medium",
        "explanation": "The `querySelectorAll` method with 'tag.class' syntax selects all elements of the specified tag with the given class."
    },
    {
        "question": "What is the difference between `childNodes` and `children` in the DOM?",
        "options": [
            "`childNodes` includes all nodes, `children` includes only element nodes",
            "`childNodes` includes only elements, `children` includes all nodes",
            "`childNodes` includes parents, `children` includes siblings",
            "`childNodes` is read-only, `children` is modifiable"
        ],
        "answer": "`childNodes` includes all nodes, `children` includes only element nodes",
        "difficulty": "Medium",
        "explanation": "`childNodes` returns all child nodes (including text and comments), while `children` returns only element nodes."
    },
    {
        "question": "How do you check if an element has a specific class 'active'?",
        "options": [
            "document.getElementById('myElement').classList.contains('active');",
            "document.getElementById('myElement').hasClass('active');",
            "document.getElementById('myElement').className.includes('active');",
            "document.getElementById('myElement').class.contains('active');"
        ],
        "answer": "document.getElementById('myElement').classList.contains('active');",
        "difficulty": "Medium",
        "explanation": "The `classList.contains` method checks if an element has the specified class."
    },
    {
        "question": "How do you remove a class 'highlight' from an element with ID 'myDiv'?",
        "options": [
            "document.getElementById('myDiv').classList.remove('highlight');",
            "document.getElementById('myDiv').className = '';",
            "document.getElementById('myDiv').removeClass('highlight');",
            "document.getElementById('myDiv').classList.delete('highlight');"
        ],
        "answer": "document.getElementById('myDiv').classList.remove('highlight');",
        "difficulty": "Medium",
        "explanation": "The `classList.remove` method removes the specified class from an element."
    },
    {
        "question": "What does `document.createTextNode('Hello')` do?",
        "options": [
            "Creates a text node with the content 'Hello'",
            "Creates a paragraph element with 'Hello'",
            "Appends 'Hello' to the document",
            "Creates an attribute named 'Hello'"
        ],
        "answer": "Creates a text node with the content 'Hello'",
        "difficulty": "Medium",
        "explanation": "The `createTextNode` method creates a text node that can be appended to an element."
    },
    {
        "question": "How can you insert a new div before the first child of an element with ID 'container'?",
        "options": [
            "document.getElementById('container').insertBefore(document.createElement('div'), document.getElementById('container').firstChild);",
            "document.getElementById('container').prepend(document.createElement('div'));",
            "document.getElementById('container').insert(document.createElement('div'));",
            "document.getElementById('container').addFirst(document.createElement('div'));"
        ],
        "answer": "document.getElementById('container').insertBefore(document.createElement('div'), document.getElementById('container').firstChild);",
        "difficulty": "Medium",
        "explanation": "The `insertBefore` method inserts a new node before the specified child node."
    },
    {
        "question": "How do you get the number of attributes on an element with ID 'myElement'?",
        "options": [
            "document.getElementById('myElement').attributes.length;",
            "document.getElementById('myElement').getAttributes().length;",
            "document.getElementById('myElement').attributeCount;",
            "document.getElementById('myElement').attributes.count;"
        ],
        "answer": "document.getElementById('myElement').attributes.length;",
        "difficulty": "Medium",
        "explanation": "The `attributes` property returns a collection of an element's attributes, and `length` gives the count."
    },
    {
        "question": "What is the purpose of the `onfocus` event?",
        "options": [
            "Triggers when an element gains focus",
            "Triggers when an element loses focus",
            "Triggers when an element is clicked",
            "Triggers when an element is hovered"
        ],
        "answer": "Triggers when an element gains focus",
        "difficulty": "Medium",
        "explanation": "The `onfocus` event fires when an element, such as an input, becomes active or gains focus."
    },
    {
        "question": "How do you get the text content of an element without its HTML tags?",
        "options": [
            "document.getElementById('myElement').textContent;",
            "document.getElementById('myElement').innerHTML;",
            "document.getElementById('myElement').value;",
            "document.getElementById('myElement').innerText;"
        ],
        "answer": "document.getElementById('myElement').textContent;",
        "difficulty": "Medium",
        "explanation": "The `textContent` property returns the text content of an element, excluding HTML tags."
    },
    {
        "question": "How can you remove an element with ID 'myElement' from the DOM?",
        "options": [
            "document.getElementById('myElement').remove();",
            "document.getElementById('myElement').delete();",
            "document.getElementById('myElement').removeChild();",
            "document.getElementById('myElement').parentNode.remove();"
        ],
        "answer": "document.getElementById('myElement').remove();",
        "difficulty": "Medium",
        "explanation": "The `remove` method removes an element from the DOM tree."
    },
    {
        "question": "What does the `onblur` event do?",
        "options": [
            "Triggers when an element loses focus",
            "Triggers when an element is clicked",
            "Triggers when an element is hovered",
            "Triggers when an element is submitted"
        ],
        "answer": "Triggers when an element loses focus",
        "difficulty": "Medium",
        "explanation": "The `onblur` event fires when an element, such as an input, loses focus."
    },
    {
        "question": "How do you get all child elements of a div with ID 'container'?",
        "options": [
            "document.getElementById('container').children;",
            "document.getElementById('container').childNodes;",
            "document.getElementById('container').getChildren();",
            "document.getElementById('container').allChildren;"
        ],
        "answer": "document.getElementById('container').children;",
        "difficulty": "Medium",
        "explanation": "The `children` property returns a live HTMLCollection of an element's child elements."
    },
    {
        "question": "How can you check if an element has a specific attribute 'data-type'?",
        "options": [
            "document.getElementById('myElement').hasAttribute('data-type');",
            "document.getElementById('myElement').containsAttribute('data-type');",
            "document.getElementById('myElement').getAttribute('data-type') !== null;",
            "document.getElementById('myElement').has('data-type');"
        ],
        "answer": "document.getElementById('myElement').hasAttribute('data-type');",
        "difficulty": "Medium",
        "explanation": "The `hasAttribute` method checks if an element has the specified attribute."
    },
    {
        "question": "How do you create a new text node and append it to a paragraph with ID 'myPara'?",
        "options": [
            "document.getElementById('myPara').appendChild(document.createTextNode('Hello'));",
            "document.getElementById('myPara').addText('Hello');",
            "document.getElementById('myPara').text = 'Hello';",
            "document.getElementById('myPara').innerHTML = 'Hello';"
        ],
        "answer": "document.getElementById('myPara').appendChild(document.createTextNode('Hello'));",
        "difficulty": "Medium",
        "explanation": "The `createTextNode` method creates a text node, which can be appended using `appendChild`."
    },
    {
        "question": "How do you get the name of an input element's attribute, such as 'name'?",
        "options": [
            "document.getElementById('myInput').getAttribute('name');",
            "document.getElementById('myInput').name;",
            "document.getElementById('myInput').attributeName;",
            "document.getElementById('myInput').getName();"
        ],
        "answer": "document.getElementById('myInput').getAttribute('name');",
        "difficulty": "Medium",
        "explanation": "The `getAttribute` method retrieves the value of the 'name' attribute, or you can use the `name` property directly."
    },
    {
        "question": "How can you replace an existing node with a new div element in a parent with ID 'container'?",
        "options": [
            "document.getElementById('container').replaceChild(document.createElement('div'), document.getElementById('container').firstChild);",
            "document.getElementById('container').replace(document.createElement('div'));",
            "document.getElementById('container').swap(document.createElement('div'));",
            "document.getElementById('container').replaceNode(document.createElement('div'));"
        ],
        "answer": "document.getElementById('container').replaceChild(document.createElement('div'), document.getElementById('container').firstChild);",
        "difficulty": "Medium",
        "explanation": "The `replaceChild` method replaces an existing child node with a new node in the parent."
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
