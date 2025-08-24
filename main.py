
import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 67 questions covering specified JavaScript topics
quiz =[
  {
    "question": "What is the primary purpose of a while loop in JavaScript?",
    "options": [
      "To execute a block of code a fixed number of times",
      "To execute a block of code as long as a condition is true",
      "To define a function",
      "To create an array"
    ],
    "answer": "To execute a block of code as long as a condition is true",
    "difficulty": "Easy",
    "explanation": "A while loop continues to execute its block of code as long as the specified condition evaluates to true."
  },
  {
    "question": "What happens if the condition in a while loop is never false?",
    "options": [
      "The loop runs once",
      "The loop causes an infinite loop",
      "The loop skips the code block",
      "The loop throws an error"
    ],
    "answer": "The loop causes an infinite loop",
    "difficulty": "Easy",
    "explanation": "If the condition in a while loop never becomes false, it will run indefinitely, causing an infinite loop."
  },
  {
    "question": "Which keyword can be used to exit a while loop prematurely?",
    "options": [
      "continue",
      "break",
      "return",
      "exit"
    ],
    "answer": "break",
    "difficulty": "Easy",
    "explanation": "The 'break' keyword immediately exits a while loop, stopping further iterations."
  },
  {
    "question": "What is the main difference between a while loop and a do...while loop?",
    "options": [
      "A do...while loop runs at least once",
      "A while loop always runs at least once",
      "A do...while loop cannot use break",
      "A while loop is faster"
    ],
    "answer": "A do...while loop runs at least once",
    "difficulty": "Easy",
    "explanation": "A do...while loop executes its code block at least once before checking the condition."
  },
  {
    "question": "What is guaranteed in a do...while loop?",
    "options": [
      "The loop runs indefinitely",
      "The loop executes at least once",
      "The loop never runs",
      "The loop requires a counter"
    ],
    "answer": "The loop executes at least once",
    "difficulty": "Easy",
    "explanation": "A do...while loop always executes its code block at least once before evaluating the condition."
  },
  {
    "question": "Where is the condition checked in a do...while loop?",
    "options": [
      "Before the loop starts",
      "After the loop executes once",
      "During the loop execution",
      "At the end of each iteration"
    ],
    "answer": "After the loop executes once",
    "difficulty": "Medium",
    "explanation": "The condition in a do...while loop is checked after the code block executes, ensuring at least one run."
  },
  {
    "question": "Where should JavaScript scripts typically be placed in an HTML file for optimal performance?",
    "options": [
      "In the <head> section",
      "At the top of the <body> section",
      "At the bottom of the <body> section",
      "In a separate CSS file"
    ],
    "answer": "At the bottom of the <body> section",
    "difficulty": "Easy",
    "explanation": "Placing scripts at the bottom of the <body> allows the HTML content to load before the script runs."
  },
  {
    "question": "What does the 'defer' attribute do when added to a <script> tag?",
    "options": [
      "Executes the script immediately",
      "Delays script execution until the DOM is fully loaded",
      "Prevents the script from running",
      "Loads the script asynchronously without waiting"
    ],
    "answer": "Delays script execution until the DOM is fully loaded",
    "difficulty": "Medium",
    "explanation": "The 'defer' attribute ensures the script runs after the HTML is fully parsed."
  },
  {
    "question": "Which symbol is used for single-line comments in JavaScript?",
    "options": [
      "//",
      "/* */",
      "#",
      "<!-- -->"
    ],
    "answer": "//",
    "difficulty": "Easy",
    "explanation": "Single-line comments in JavaScript start with '//' and continue until the end of the line."
  },
  {
    "question": "How do you write a multi-line comment in JavaScript?",
    "options": [
      "// Comment",
      "/* Comment */",
      "# Comment",
      "<!-- Comment -->"
    ],
    "answer": "/* Comment */",
    "difficulty": "Easy",
    "explanation": "Multi-line comments are enclosed within '/*' and '*/' in JavaScript."
  },
  {
    "question": "Which event is triggered when a user clicks a link?",
    "options": [
      "onmouseover",
      "onclick",
      "onchange",
      "onload"
    ],
    "answer": "onclick",
    "difficulty": "Easy",
    "explanation": "The 'onclick' event fires when a user clicks a link or any element."
  },
  {
    "question": "How can you prevent the default behavior of a link click event?",
    "options": [
      "event.stopPropagation()",
      "event.preventDefault()",
      "event.cancel()",
      "event.halt()"
    ],
    "answer": "event.preventDefault()",
    "difficulty": "Medium",
    "explanation": "Calling 'event.preventDefault()' stops the default action, such as navigating to a link's href."
  },
  {
    "question": "Which event is triggered when a button is clicked?",
    "options": [
      "onfocus",
      "onclick",
      "onhover",
      "onsubmit"
    ],
    "answer": "onclick",
    "difficulty": "Easy",
    "explanation": "The 'onclick' event is triggered when a user clicks a button."
  },
  {
    "question": "What does the 'ondblclick' event do?",
    "options": [
      "Triggers on a single click",
      "Triggers on a double click",
      "Triggers on mouse hover",
      "Triggers on form submission"
    ],
    "answer": "Triggers on a double click",
    "difficulty": "Medium",
    "explanation": "The 'ondblclick' event fires when an element is double-clicked."
  },
  {
    "question": "Which mouse event is triggered when the mouse pointer enters an element?",
    "options": [
      "onmouseout",
      "onmouseover",
      "onmousedown",
      "onmouseup"
    ],
    "answer": "onmouseover",
    "difficulty": "Easy",
    "explanation": "The 'onmouseover' event occurs when the mouse pointer enters an element."
  },
  {
    "question": "What does the 'onmouseout' event do?",
    "options": [
      "Triggers when the mouse clicks an element",
      "Triggers when the mouse leaves an element",
      "Triggers when the mouse moves over an element",
      "Triggers when the mouse button is pressed"
    ],
    "answer": "Triggers when the mouse leaves an element",
    "difficulty": "Easy",
    "explanation": "The 'onmouseout' event fires when the mouse pointer leaves an element."
  },
  {
    "question": "Which event is triggered when an input field gains focus?",
    "options": [
      "onchange",
      "onblur",
      "onfocus",
      "onselect"
    ],
    "answer": "onfocus",
    "difficulty": "Easy",
    "explanation": "The 'onfocus' event occurs when an input field or element gains focus."
  },
  {
    "question": "What does the 'onchange' event do for form fields?",
    "options": [
      "Triggers when the field is clicked",
      "Triggers when the field's value changes and loses focus",
      "Triggers when the field gains focus",
      "Triggers when the form is submitted"
    ],
    "answer": "Triggers when the field's value changes and loses focus",
    "difficulty": "Medium",
    "explanation": "The 'onchange' event fires when a field's value changes and it loses focus."
  },
  {
    "question": "How do you read the value of an input field with id='myInput'?",
    "options": [
      "document.getElementById('myInput').value",
      "document.querySelector('myInput').value",
      "document.getElementById('myInput').text",
      "document.getElementById('myInput').innerHTML"
    ],
    "answer": "document.getElementById('myInput').value",
    "difficulty": "Easy",
    "explanation": "The 'value' property retrieves the current value of an input field."
  },
  {
    "question": "How can you set the value of an input field with id='myInput' to 'Hello'?",
    "options": [
      "document.getElementById('myInput').value = 'Hello';",
      "document.getElementById('myInput').text = 'Hello';",
      "document.getElementById('myInput').innerHTML = 'Hello';",
      "document.querySelector('myInput').value = 'Hello';"
    ],
    "answer": "document.getElementById('myInput').value = 'Hello';",
    "difficulty": "Easy",
    "explanation": "The 'value' property is used to set the value of an input field."
  },
  {
    "question": "How do you read the text content of a paragraph with id='myPara'?",
    "options": [
      "document.getElementById('myPara').value",
      "document.getElementById('myPara').innerHTML",
      "document.getElementById('myPara').textContent",
      "document.querySelector('myPara').text"
    ],
    "answer": "document.getElementById('myPara').textContent",
    "difficulty": "Easy",
    "explanation": "'textContent' retrieves the text content of an element, excluding HTML tags."
  },
  {
    "question": "How do you set the text content of a paragraph with id='myPara' to 'New Text'?",
    "options": [
      "document.getElementById('myPara').value = 'New Text';",
      "document.getElementById('myPara').innerHTML = 'New Text';",
      "document.getElementById('myPara').textContent = 'New Text';",
      "document.getElementById('myPara').setText('New Text');"
    ],
    "answer": "document.getElementById('myPara').textContent = 'New Text';",
    "difficulty": "Easy",
    "explanation": "'textContent' sets the text content of an element without interpreting HTML."
  },
  {
    "question": "How can you change the src attribute of an image with id='myImage'?",
    "options": [
      "document.getElementById('myImage').src = 'new.jpg';",
      "document.getElementById('myImage').image = 'new.jpg';",
      "document.getElementById('myImage').setSrc('new.jpg');",
      "document.querySelector('myImage').src = 'new.jpg';"
    ],
    "answer": "document.getElementById('myImage').src = 'new.jpg';",
    "difficulty": "Easy",
    "explanation": "The 'src' property is used to change the source of an image element."
  },
  {
    "question": "What is a common way to swap images on a mouseover event?",
    "options": [
      "Change the image's class",
      "Change the image's src attribute",
      "Change the image's textContent",
      "Change the image's innerHTML"
    ],
    "answer": "Change the image's src attribute",
    "difficulty": "Medium",
    "explanation": "Swapping images typically involves changing the 'src' attribute to a new image URL."
  },
  {
    "question": "How do you swap an image and add a class to it?",
    "options": [
      "element.src = 'new.jpg'; element.classList.add('newClass');",
      "element.src = 'new.jpg'; element.className = 'newClass';",
      "element.image = 'new.jpg'; element.classList.add('newClass');",
      "element.src = 'new.jpg'; element.addClass('newClass');"
    ],
    "answer": "element.src = 'new.jpg'; element.classList.add('newClass');",
    "difficulty": "Medium",
    "explanation": "Use 'src' to swap the image and 'classList.add' to apply a class."
  },
  {
    "question": "How do you set the CSS style of an element with id='myElement' to have a red background?",
    "options": [
      "document.getElementById('myElement').style.backgroundColor = 'red';",
      "document.getElementById('myElement').css.background = 'red';",
      "document.getElementById('myElement').style = 'red';",
      "document.getElementById('myElement').background = 'red';"
    ],
    "answer": "document.getElementById('myElement').style.backgroundColor = 'red';",
    "difficulty": "Easy",
    "explanation": "The 'style' property is used to set CSS properties, such as 'backgroundColor'."
  },
  {
    "question": "How do you select all <p> elements in a document?",
    "options": [
      "document.querySelector('p')",
      "document.getElementsByTagName('p')",
      "document.getElementById('p')",
      "document.querySelectorAll('p')"
    ],
    "answer": "document.querySelectorAll('p')",
    "difficulty": "Easy",
    "explanation": "'querySelectorAll' returns a NodeList of all elements matching the tag name."
  },
  {
    "question": "How do you select some <div> elements with a specific class 'myClass'?",
    "options": [
      "document.getElementsByClassName('myClass')",
      "document.querySelector('div.myClass')",
      "document.getElementsByTagName('div.myClass')",
      "document.querySelectorAll('div.myClass')"
    ],
    "answer": "document.querySelectorAll('div.myClass')",
    "difficulty": "Medium",
    "explanation": "'querySelectorAll' selects all <div> elements with the class 'myClass'."
  },
  {
    "question": "What does the DOM represent in JavaScript?",
    "options": [
      "Document Object Model",
      "Data Object Model",
      "Dynamic Object Method",
      "Document Order Model"
    ],
    "answer": "Document Object Model",
    "difficulty": "Easy",
    "explanation": "The DOM is a programming interface for HTML and XML documents, representing their structure."
  },
  {
    "question": "In the DOM, what is a parent element?",
    "options": [
      "An element inside another element",
      "An element containing other elements",
      "The first element in the document",
      "An element with no attributes"
    ],
    "answer": "An element containing other elements",
    "difficulty": "Easy",
    "explanation": "A parent element contains child elements in the DOM hierarchy."
  },
  {
    "question": "How do you access the first child of an element in the DOM?",
    "options": [
      "element.firstChild",
      "element.childNodes[0]",
      "element.children[0]",
      "All of the above"
    ],
    "answer": "All of the above",
    "difficulty": "Medium",
    "explanation": "'firstChild', 'childNodes[0]', and 'children[0]' can all access the first child, though 'children' excludes non-element nodes."
  },
  {
    "question": "What is the purpose of the nodeType property in the DOM?",
    "options": [
      "To identify the type of a node",
      "To count the number of nodes",
      "To set the node’s value",
      "To change the node’s style"
    ],
    "answer": "To identify the type of a node",
    "difficulty": "Medium",
    "explanation": "The 'nodeType' property returns a number indicating the type of node, such as 1 for elements or 3 for text."
  },
  {
    "question": "Which nodeType value represents an element node?",
    "options": [
      "1",
      "3",
      "8",
      "9"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "A 'nodeType' of 1 indicates an element node in the DOM."
  },
  {
    "question": "How can you target an element by its class name in the DOM?",
    "options": [
      "document.getElementById('class')",
      "document.querySelector('.className')",
      "document.getElementsByTagName('class')",
      "document.querySelector('#className')"
    ],
    "answer": "document.querySelector('.className')",
    "difficulty": "Easy",
    "explanation": "'querySelector' with a '.' prefix targets elements by class name."
  },
  {
    "question": "How do you get the tag name of a DOM element?",
    "options": [
      "element.tagName",
      "element.nodeName",
      "element.name",
      "Both element.tagName and element.nodeName"
    ],
    "answer": "Both element.tagName and element.nodeName",
    "difficulty": "Medium",
    "explanation": "Both 'tagName' and 'nodeName' return the tag name of an element, in uppercase for HTML."
  },
  {
    "question": "How can you count the number of <div> elements in a document?",
    "options": [
      "document.getElementsByTagName('div').length",
      "document.querySelector('div').count",
      "document.getElementsByClassName('div').length",
      "document.querySelectorAll('div').count"
    ],
    "answer": "document.getElementsByTagName('div').length",
    "difficulty": "Easy",
    "explanation": "'getElementsByTagName' returns a collection, and 'length' gives the count."
  },
  {
    "question": "How do you check if an element has a specific attribute?",
    "options": [
      "element.hasAttribute('attr')",
      "element.getAttribute('attr')",
      "element.attribute('attr')",
      "element.checkAttribute('attr')"
    ],
    "answer": "element.hasAttribute('attr')",
    "difficulty": "Medium",
    "explanation": "'hasAttribute' returns true if the element has the specified attribute."
  },
  {
    "question": "How do you get the value of an attribute from an element?",
    "options": [
      "element.getAttribute('attr')",
      "element.attribute('attr')",
      "element.getProperty('attr')",
      "element.value('attr')"
    ],
    "answer": "element.getAttribute('attr')",
    "difficulty": "Easy",
    "explanation": "'getAttribute' retrieves the value of a specified attribute."
  },
  {
    "question": "How do you add a new div element to the DOM?",
    "options": [
      "document.createElement('div')",
      "document.newElement('div')",
      "document.addElement('div')",
      "document.createNode('div')"
    ],
    "answer": "document.createElement('div')",
    "difficulty": "Easy",
    "explanation": "'createElement' creates a new element node with the specified tag name."
  },
  {
    "question": "How do you insert a new node as a child of an existing element?",
    "options": [
      "parent.appendChild(newNode)",
      "parent.insertChild(newNode)",
      "parent.addNode(newNode)",
      "parent.append(newNode)"
    ],
    "answer": "parent.appendChild(newNode)",
    "difficulty": "Medium",
    "explanation": "'appendChild' adds a new node as the last child of the parent element."
  },
  {
    "question": "What does the 'insertBefore' method do in the DOM?",
    "options": [
      "Inserts a node after a reference node",
      "Inserts a node before a reference node",
      "Replaces a node",
      "Removes a node"
    ],
    "answer": "Inserts a node before a reference node",
    "difficulty": "Medium",
    "explanation": "'insertBefore' inserts a new node before a specified child node in the parent."
  },
  {
    "question": "What is a common use of comments in JavaScript code?",
    "options": [
      "To execute code faster",
      "To explain or document the code",
      "To style the webpage",
      "To create loops"
    ],
    "answer": "To explain or document the code",
    "difficulty": "Easy",
    "explanation": "Comments are used to add explanations or notes to make code more readable."
  },
  {
    "question": "Which event is triggered when a user presses a key in an input field?",
    "options": [
      "onkeypress",
      "onclick",
      "onchange",
      "onfocus"
    ],
    "answer": "onkeypress",
    "difficulty": "Medium",
    "explanation": "The 'onkeypress' event fires when a key is pressed in an input field."
  },
  {
    "question": "How do you set the innerHTML of an element with id='myDiv' to '<p>Hello</p>'?",
    "options": [
      "document.getElementById('myDiv').textContent = '<p>Hello</p>';",
      "document.getElementById('myDiv').innerHTML = '<p>Hello</p>';",
      "document.getElementById('myDiv').value = '<p>Hello</p>';",
      "document.getElementById('myDiv').html = '<p>Hello</p>';"
    ],
    "answer": "document.getElementById('myDiv').innerHTML = '<p>Hello</p>';",
    "difficulty": "Easy",
    "explanation": "'innerHTML' sets the HTML content of an element, parsing the string as HTML."
  },
  {
    "question": "What happens when you use 'querySelector' with a non-existent selector?",
    "options": [
      "Returns null",
      "Throws an error",
      "Returns an empty array",
      "Returns undefined"
    ],
    "answer": "Returns null",
    "difficulty": "Medium",
    "explanation": "'querySelector' returns null if no element matches the selector."
  },
  {
    "question": "How do you access the parent element of a node in the DOM?",
    "options": [
      "node.parentNode",
      "node.parentElement",
      "node.getParent()",
      "Both node.parentNode and node.parentElement"
    ],
    "answer": "Both node.parentNode and node.parentElement",
    "difficulty": "Medium",
    "explanation": "Both 'parentNode' and 'parentElement' return the parent, but 'parentElement' returns null for non-element parents."
  },
  {
    "question": "Which method removes a child node from the DOM?",
    "options": [
      "parent.removeChild(child)",
      "child.removeNode()",
      "parent.deleteChild(child)",
      "child.remove()"
    ],
    "answer": "parent.removeChild(child)",
    "difficulty": "Medium",
    "explanation": "'removeChild' removes a specified child node from its parent."
  },
  {
    "question": "What does the 'children' property of an element return?",
    "options": [
      "All child nodes including text and comments",
      "Only element child nodes",
      "All parent nodes",
      "Only text nodes"
    ],
    "answer": "Only element child nodes",
    "difficulty": "Medium",
    "explanation": "The 'children' property returns a collection of only element child nodes."
  },
  {
    "question": "How do you set multiple classes to an element?",
    "options": [
      "element.className = 'class1 class2';",
      "element.classList.add('class1', 'class2');",
      "Both of the above",
      "element.setClass('class1 class2');"
    ],
    "answer": "Both of the above",
    "difficulty": "Medium",
    "explanation": "'className' sets all classes as a string, while 'classList.add' adds individual classes."
  },
  {
    "question": "What is the nodeType value for a text node?",
    "options": [
      "1",
      "3",
      "8",
      "9"
    ],
    "answer": "3",
    "difficulty": "Medium",
    "explanation": "A 'nodeType' of 3 indicates a text node in the DOM."
  },
  {
    "question": "How do you check if an element has a specific class?",
    "options": [
      "element.classList.contains('className')",
      "element.className.includes('className')",
      "element.hasClass('className')",
      "element.getClass('className')"
    ],
    "answer": "element.classList.contains('className')",
    "difficulty": "Medium",
    "explanation": "'classList.contains' checks if an element has a specific class."
  },
  {
    "question": "How do you create a text node in the DOM?",
    "options": [
      "document.createTextNode('text')",
      "document.createText('text')",
      "document.newTextNode('text')",
      "document.addText('text')"
    ],
    "answer": "document.createTextNode('text')",
    "difficulty": "Medium",
    "explanation": "'createTextNode' creates a new text node with the specified text."
  },
  {
    "question": "What does the 'getElementsByClassName' method return?",
    "options": [
      "A single element",
      "A NodeList of elements",
      "An array of elements",
      "A single class name"
    ],
    "answer": "A NodeList of elements",
    "difficulty": "Easy",
    "explanation": "'getElementsByClassName' returns a live NodeList of elements with the specified class."
  },
  {
    "question": "How do you toggle a class on an element?",
    "options": [
      "element.classList.toggle('className')",
      "element.className.toggle('className')",
      "element.toggleClass('className')",
      "element.switchClass('className')"
    ],
    "answer": "element.classList.toggle('className')",
    "difficulty": "Medium",
    "explanation": "'classList.toggle' adds a class if absent or removes it if present."
  },
  {
    "question": "What is the purpose of the 'setAttribute' method?",
    "options": [
      "To remove an attribute",
      "To add or update an attribute",
      "To get an attribute value",
      "To check if an attribute exists"
    ],
    "answer": "To add or update an attribute",
    "difficulty": "Easy",
    "explanation": "'setAttribute' sets the value of a specified attribute on an element."
  },
  {
    "question": "How do you replace an existing node with a new node in the DOM?",
    "options": [
      "parent.replaceChild(newNode, oldNode)",
      "parent.swapNode(newNode, oldNode)",
      "parent.replaceNode(newNode, oldNode)",
      "parent.changeChild(newNode, oldNode)"
    ],
    "answer": "parent.replaceChild(newNode, oldNode)",
    "difficulty": "Medium",
    "explanation": "'replaceChild' replaces an existing child node with a new node."
  },
  {
    "question": "What does the 'querySelectorAll' method return?",
    "options": [
      "A single element",
      "A NodeList of elements",
      "An array of elements",
      "A single node"
    ],
    "answer": "A NodeList of elements",
    "difficulty": "Easy",
    "explanation": "'querySelectorAll' returns a static NodeList of all elements matching the selector."
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



