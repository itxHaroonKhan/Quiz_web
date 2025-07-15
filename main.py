import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 50 questions covering all specified topics, options without a, b, c, d labels
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
        "question": "How do you extract a substring from index 2 to 5 in a string?",
        "options": [
            "str.substring(2, 5)",
            "str.slice(2, 6)",
            "str.substr(2, 5)",
            "str.extract(2, 5)"
        ],
        "answer": "str.substring(2, 5)",
        "difficulty": "Medium",
        "explanation": "`substring(2, 5)` extracts characters from index 2 up to, but not including, index 5."
    },
    {
        "question": "How do you find the index of the first occurrence of 'cat' in a string?",
        "options": [
            "str.indexOf('cat')",
            "str.search('cat')",
            "str.find('cat')",
            "str.locate('cat')"
        ],
        "answer": "str.indexOf('cat')",
        "difficulty": "Medium",
        "explanation": "`indexOf('cat')` returns the index of the first occurrence of 'cat' or -1 if not found."
    },
    {
        "question": "How do you find the character at index 3 in a string?",
        "options": [
            "str.charAt(3)",
            "str[3]",
            "str.getChar(3)",
            "str.at(3)"
        ],
        "answer": "str.charAt(3)",
        "difficulty": "Easy",
        "explanation": "`charAt(3)` returns the character at index 3 in the string."
    },
    {
        "question": "How do you replace all occurrences of 'a' with 'b' in a string?",
        "options": [
            "str.replace(/a/g, 'b')",
            "str.replace('a', 'b')",
            "str.swap('a', 'b')",
            "str.replaceAll('a', 'b')"
        ],
        "answer": "str.replace(/a/g, 'b')",
        "difficulty": "Medium",
        "explanation": "`replace(/a/g, 'b')` uses a regular expression with the global flag to replace all 'a's with 'b's."
    },
    {
        "question": "How do you round a number to the nearest integer in JavaScript?",
        "options": [
            "Math.round(num)",
            "Math.floor(num)",
            "Math.ceil(num)",
            "Math.trunc(num)"
        ],
        "answer": "Math.round(num)",
        "difficulty": "Easy",
        "explanation": "`Math.round(num)` rounds the number to the nearest integer."
    },
    {
        "question": "How do you generate a random number between 0 and 1 in JavaScript?",
        "options": [
            "Math.random()",
            "Math.rand()",
            "Random.next()",
            "Math.randomNumber()"
        ],
        "answer": "Math.random()",
        "difficulty": "Easy",
        "explanation": "`Math.random()` generates a random number between 0 (inclusive) and 1 (exclusive)."
    },
    {
        "question": "How do you convert the string '123' to an integer?",
        "options": [
            "parseInt('123')",
            "Number('123')",
            "parseFloat('123')",
            "int('123')"
        ],
        "answer": "parseInt('123')",
        "difficulty": "Medium",
        "explanation": "`parseInt('123')` converts a string to an integer."
    },
    {
        "question": "How do you convert a number to a string in JavaScript?",
        "options": [
            "num.toString()",
            "String(num)",
            "num.toStr()",
            "convertToString(num)"
        ],
        "answer": "num.toString()",
        "difficulty": "Easy",
        "explanation": "`toString()` converts a number to its string representation."
    },
    {
        "question": "How do you limit a number to two decimal places?",
        "options": [
            "num.toFixed(2)",
            "num.round(2)",
            "num.toPrecision(2)",
            "num.fixed(2)"
        ],
        "answer": "num.toFixed(2)",
        "difficulty": "Medium",
        "explanation": "`toFixed(2)` formats a number to two decimal places."
    },
    {
        "question": "How do you get the current date and time in JavaScript?",
        "options": [
            "new Date()",
            "Date.now()",
            "Date.current()",
            "new DateTime()"
        ],
        "answer": "new Date()",
        "difficulty": "Easy",
        "explanation": "`new Date()` creates a new Date object with the current date and time."
    },
    {
        "question": "How do you extract the year from a Date object?",
        "options": [
            "date.getFullYear()",
            "date.getYear()",
            "date.year()",
            "date.getDate()"
        ],
        "answer": "date.getFullYear()",
        "difficulty": "Medium",
        "explanation": "`getFullYear()` returns the four-digit year from a Date object."
    },
    {
        "question": "How do you create a Date object for January 1, 2023?",
        "options": [
            "new Date(2023, 0, 1)",
            "new Date('2023-01-01')",
            "new Date(2023, 1, 1)",
            "Date.create(2023, 1, 1)"
        ],
        "answer": "new Date(2023, 0, 1)",
        "difficulty": "Medium",
        "explanation": "Months are zero-based in JavaScript, so January is 0."
    },
    {
        "question": "How do you set the year of a Date object to 2024?",
        "options": [
            "date.setFullYear(2024)",
            "date.setYear(2024)",
            "date.year = 2024",
            "date.updateYear(2024)"
        ],
        "answer": "date.setFullYear(2024)",
        "difficulty": "Medium",
        "explanation": "`setFullYear(2024)` sets the year of a Date object."
    },
    {
        "question": "How do you define a function in JavaScript?",
        "options": [
            "function myFunc() {}",
            "def myFunc() {}",
            "func myFunc() {}",
            "myFunc() => {}"
        ],
        "answer": "function myFunc() {}",
        "difficulty": "Easy",
        "explanation": "A function is defined using the `function` keyword followed by the name and parentheses."
    },
    {
        "question": "How do you pass a parameter to a function?",
        "options": [
            "function myFunc(param) {}",
            "function myFunc: param {}",
            "function myFunc[param] {}",
            "function myFunc { param }"
        ],
        "answer": "function myFunc(param) {}",
        "difficulty": "Easy",
        "explanation": "Parameters are passed inside the parentheses of the function definition."
    },
    {
        "question": "How do you return a value from a function?",
        "options": [
            "return value;",
            "send value;",
            "output value;",
            "yield value;"
        ],
        "answer": "return value;",
        "difficulty": "Easy",
        "explanation": "The `return` statement sends a value back from a function."
    },
    {
        "question": "What is the difference between local and global variables?",
        "options": [
            "Local variables are declared inside a function, global outside",
            "Local variables are declared with `var`, global with `let`",
            "Local variables are global, global are local",
            "Local variables are constant, global are mutable"
        ],
        "answer": "Local variables are declared inside a function, global outside",
        "difficulty": "Medium",
        "explanation": "Local variables are scoped to the function they are declared in, while global variables are declared outside and accessible everywhere."
    },
    {
        "question": "How do you start a switch statement in JavaScript?",
        "options": [
            "switch (expression) {",
            "case (expression) {",
            "switch { expression }",
            "if (expression) {"
        ],
        "answer": "switch (expression) {",
        "difficulty": "Easy",
        "explanation": "A switch statement begins with `switch` followed by the expression in parentheses and an opening brace."
    },
    {
        "question": "How do you complete a switch statement?",
        "options": [
            "Add a `default` case and close with `}`",
            "Add a `break` and close with `}`",
            "Add a `return` and close with `}`",
            "Close with `end switch`"
        ],
        "answer": "Add a `default` case and close with `}`",
        "difficulty": "Medium",
        "explanation": "A switch statement typically includes a `default` case and ends with a closing brace `}`."
    },
    {
        "question": "How do you write a while loop in JavaScript?",
        "options": [
            "while (condition) {}",
            "loop (condition) {}",
            "while condition {}",
            "do while (condition) {}"
        ],
        "answer": "while (condition) {}",
        "difficulty": "Easy",
        "explanation": "A while loop uses the `while` keyword followed by a condition in parentheses and a block."
    },
    {
        "question": "How do you write a do...while loop?",
        "options": [
            "do {} while (condition);",
            "while (condition) do {}",
            "do {condition} while {};",
            "loop {} until (condition);"
        ],
        "answer": "do {} while (condition);",
        "difficulty": "Medium",
        "explanation": "A do...while loop executes the block first, then checks the condition, ending with a semicolon."
    },
    {
        "question": "Where should JavaScript scripts be placed in an HTML file?",
        "options": [
            "Inside `<script>` tags in `<head>` or `<body>`",
            "Inside `<js>` tags in `<head>`",
            "Directly in `<body>` without tags",
            "Only in external `.js` files"
        ],
        "answer": "Inside `<script>` tags in `<head>` or `<body>`",
        "difficulty": "Easy",
        "explanation": "JavaScript is placed in `<script>` tags, typically in `<head>` with `defer` or at the end of `<body>`."
    },
    {
        "question": "How do you write a single-line comment in JavaScript?",
        "options": [
            "// Comment",
            "# Comment",
            "/* Comment */",
            "<!-- Comment -->"
        ],
        "answer": "// Comment",
        "difficulty": "Easy",
        "explanation": "Single-line comments in JavaScript start with `//`."
    },
    {
        "question": "How do you handle a click event on a link?",
        "options": [
            "link.addEventListener('click', handler)",
            "link.onClick(handler)",
            "link.click(handler)",
            "link.event('click', handler)"
        ],
        "answer": "link.addEventListener('click', handler)",
        "difficulty": "Medium",
        "explanation": "`addEventListener('click', handler)` attaches a click event handler to a link."
    },
    {
        "question": "How do you handle a click event on a button?",
        "options": [
            "button.addEventListener('click', handler)",
            "button.onClick(handler)",
            "button.click(handler)",
            "button.event('click', handler)"
        ],
        "answer": "button.addEventListener('click', handler)",
        "difficulty": "Medium",
        "explanation": "`addEventListener('click', handler)` is used to handle button clicks."
    },
    {
        "question": "How do you detect a mouseover event?",
        "options": [
            "element.addEventListener('mouseover', handler)",
            "element.onMouseOver(handler)",
            "element.mouseOver(handler)",
            "element.event('mouseover', handler)"
        ],
        "answer": "element.addEventListener('mouseover', handler)",
        "difficulty": "Medium",
        "explanation": "`mouseover` event is detected using `addEventListener`."
    },
    {
        "question": "How do you handle input field events?",
        "options": [
            "field.addEventListener('input', handler)",
            "field.onInput(handler)",
            "field.input(handler)",
            "field.event('input', handler)"
        ],
        "answer": "field.addEventListener('input', handler)",
        "difficulty": "Medium",
        "explanation": "The `input` event is handled using `addEventListener` on input fields."
    },
    {
        "question": "How do you read the value of an input field?",
        "options": [
            "field.value",
            "field.getValue()",
            "field.text",
            "field.innerText"
        ],
        "answer": "field.value",
        "difficulty": "Easy",
        "explanation": "The `value` property retrieves the current value of an input field."
    },
    {
        "question": "How do you set the value of an input field?",
        "options": [
            "field.value = 'new value'",
            "field.setValue('new value')",
            "field.text = 'new value'",
            "field.innerText = 'new value'"
        ],
        "answer": "field.value = 'new value'",
        "difficulty": "Easy",
        "explanation": "Assigning to the `value` property sets the input field's value."
    },
    {
        "question": "How do you set the text content of a paragraph?",
        "options": [
            "para.textContent = 'text'",
            "para.innerText = 'text'",
            "para.innerHTML = 'text'",
            "para.content = 'text'"
        ],
        "answer": "para.textContent = 'text'",
        "difficulty": "Medium",
        "explanation": "`textContent` safely sets the text content of a paragraph."
    },
    {
        "question": "How do you change the source of an image element?",
        "options": [
            "img.src = 'new.jpg'",
            "img.setSrc('new.jpg')",
            "img.image = 'new.jpg'",
            "img.source = 'new.jpg'"
        ],
        "answer": "img.src = 'new.jpg'",
        "difficulty": "Easy",
        "explanation": "The `src` property sets the source of an image element."
    },
    {
        "question": "How do you swap an image using JavaScript?",
        "options": [
            "img.src = 'new.jpg'",
            "img.swap('new.jpg')",
            "img.setImage('new.jpg')",
            "img.change('new.jpg')"
        ],
        "answer": "img.src = 'new.jpg'",
        "difficulty": "Easy",
        "explanation": "Assigning a new URL to `img.src` swaps the image."
    },
    {
        "question": "How do you add a class to an element?",
        "options": [
            "element.classList.add('class')",
            "element.className = 'class'",
            "element.addClass('class')",
            "element.setClass('class')"
        ],
        "answer": "element.classList.add('class')",
        "difficulty": "Medium",
        "explanation": "`classList.add('class')` adds a class to an element without overwriting existing classes."
    },
    {
        "question": "How do you set the style of an element?",
        "options": [
            "element.style.property = 'value'",
            "element.setStyle('property', 'value')",
            "element.css('property', 'value')",
            "element.style = 'property: value'"
        ],
        "answer": "element.style.property = 'value'",
        "difficulty": "Medium",
        "explanation": "The `style` property is used to set CSS properties directly, e.g., `element.style.color = 'red'`."
    },
    {
        "question": "How do you select all elements by tag name?",
        "options": [
            "document.getElementsByTagName('tag')",
            "document.querySelectorAll('tag')",
            "document.getTag('tag')",
            "document.selectTag('tag')"
        ],
        "answer": "document.getElementsByTagName('tag')",
        "difficulty": "Medium",
        "explanation": "`getElementsByTagName('tag')` returns a live HTMLCollection of elements with the specified tag."
    },
    {
        "question": "How do you select some elements by tag name with a specific class?",
        "options": [
            "document.querySelectorAll('tag.class')",
            "document.getElementsByClassName('class')",
            "document.getElementsByTag('tag.class')",
            "document.select('tag.class')"
        ],
        "answer": "document.querySelectorAll('tag.class')",
        "difficulty": "Medium",
        "explanation": "`querySelectorAll('tag.class')` selects elements with the specified tag and class."
    },
    {
        "question": "What is the DOM in JavaScript?",
        "options": [
            "Document Object Model",
            "Data Object Model",
            "Dynamic Object Model",
            "Document Order Model"
        ],
        "answer": "Document Object Model",
        "difficulty": "Easy",
        "explanation": "The DOM is a tree-like representation of the webpage's structure."
    },
    {
        "question": "How do you access the parent of a DOM element?",
        "options": [
            "element.parentNode",
            "element.parent()",
            "element.getParent()",
            "element.parentElementNode"
        ],
        "answer": "element.parentNode",
        "difficulty": "Medium",
        "explanation": "`parentNode` returns the parent node of an element in the DOM."
    },
    {
        "question": "How do you find the children of a DOM element?",
        "options": [
            "element.children",
            "element.childNodes",
            "element.getChildren()",
            "element.kids()"
        ],
        "answer": "element.children",
        "difficulty": "Medium",
        "explanation": "`children` returns an HTMLCollection of an element's child elements."
    },
    {
        "question": "What is the `nodeType` property used for in the DOM?",
        "options": [
            "To identify the type of a node",
            "To count nodes",
            "To get node attributes",
            "To set node styles"
        ],
        "answer": "To identify the type of a node",
        "difficulty": "Medium",
        "explanation": "`nodeType` returns a number indicating the type of node (e.g., 1 for elements, 3 for text)."
    },
    {
        "question": "How do you select an element by its ID in the DOM?",
        "options": [
            "document.getElementById('id')",
            "document.querySelector('#id')",
            "document.getId('id')",
            "document.selectId('id')"
        ],
        "answer": "document.getElementById('id')",
        "difficulty": "Easy",
        "explanation": "`getElementById('id')` selects a single element by its ID."
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
        "explanation": "`tagName` returns the tag name of an element in uppercase."
    },
    {
        "question": "How do you count the number of child elements in a DOM node?",
        "options": [
            "element.children.length",
            "element.childCount()",
            "element.children.size",
            "element.getChildLength()"
        ],
        "answer": "element.children.length",
        "difficulty": "Medium",
        "explanation": "The `length` property of `element.children` gives the number of child elements."
    },
    {
        "question": "How do you get an attribute of a DOM element?",
        "options": [
            "element.getAttribute('attr')",
            "element.attribute('attr')",
            "element.attr('attr')",
            "element.getAttr('attr')"
        ],
        "answer": "element.getAttribute('attr')",
        "difficulty": "Medium",
        "explanation": "`getAttribute('attr')` retrieves the value of the specified attribute."
    },
    {
        "question": "How do you get the name of an attribute at index 0?",
        "options": [
            "element.attributes[0].name",
            "element.attributes[0].key",
            "element.getAttributeName(0)",
            "element.attributes[0].id"
        ],
        "answer": "element.attributes[0].name",
        "difficulty": "Hard",
        "explanation": "`element.attributes[0].name` returns the name of the attribute at index 0."
    },
    {
        "question": "How do you add a new element to the DOM?",
        "options": [
            "document.createElement('tag')",
            "document.newElement('tag')",
            "document.addElement('tag')",
            "document.makeElement('tag')"
        ],
        "answer": "document.createElement('tag')",
        "difficulty": "Medium",
        "explanation": "`createElement('tag')` creates a new element node with the specified tag."
    },
    {
        "question": "How do you insert a node as a child of another node?",
        "options": [
            "parent.appendChild(node)",
            "parent.addChild(node)",
            "parent.insert(node)",
            "parent.append(node)"
        ],
        "answer": "parent.appendChild(node)",
        "difficulty": "Medium",
        "explanation": "`appendChild(node)` adds a node as the last child of the parent."
    },
    {
        "question": "How do you create an object in JavaScript?",
        "options": [
            "let obj = {}",
            "let obj = new Object{}",
            "let obj = Object.create()",
            "let obj = []"
        ],
        "answer": "let obj = {}",
        "difficulty": "Easy",
        "explanation": "An object literal is created using curly braces `{}`."
    },
    {
        "question": "How do you add a property to an object?",
        "options": [
            "obj.property = value",
            "obj.addProperty('property', value)",
            "obj.set('property', value)",
            "obj['property'] = value"
        ],
        "answer": "obj.property = value",
        "difficulty": "Easy",
        "explanation": "Properties are added using dot notation or bracket notation."
    },
    {
        "question": "How do you add a method to an object?",
        "options": [
            "obj.method = function() {}",
            "obj.addMethod(function() {})",
            "obj.setMethod(function() {})",
            "obj.function = method()"
        ],
        "answer": "obj.method = function() {}",
        "difficulty": "Medium",
        "explanation": "A method is added by assigning a function to an object property."
    },
    {
        "question": "How do you create an object constructor?",
        "options": [
            "function MyObj() {}",
            "class MyObj {}",
            "constructor MyObj() {}",
            "object MyObj() {}"
        ],
        "answer": "function MyObj() {}",
        "difficulty": "Medium",
        "explanation": "A constructor is a function used with `new` to create objects."
    },
    {
        "question": "How do you add a method to a constructor?",
        "options": [
            "MyObj.prototype.method = function() {}",
            "MyObj.method = function() {}",
            "MyObj.addMethod(function() {})",
            "MyObj.function = method()"
        ],
        "answer": "MyObj.prototype.method = function() {}",
        "difficulty": "Hard",
        "explanation": "Methods are added to a constructor's prototype to be shared by all instances."
    },
    {
        "question": "What is a prototype in JavaScript?",
        "options": [
            "An object from which other objects inherit properties",
            "A function that creates objects",
            "A property of an object",
            "A type of variable"
        ],
        "answer": "An object from which other objects inherit properties",
        "difficulty": "Hard",
        "explanation": "Prototypes are used for inheritance, allowing objects to share properties and methods."
    },
    {
        "question": "How do you check if an object has a specific property?",
        "options": [
            "'property' in obj",
            "obj.hasProperty('property')",
            "obj.propertyExists('property')",
            "obj.checkProperty('property')"
        ],
        "answer": "'property' in obj",
        "difficulty": "Medium",
        "explanation": "The `in` operator checks if a property exists in an object or its prototype chain."
    },
    {
        "question": "How do you convert a string to lowercase and then capitalize only its first letter?\n```javascript\nlet str = 'JAVASCRIPT';\n```",
        "options": [
            "str.toLowerCase()[0].toUpperCase() + str.slice(1)",
            "str.toLowerCase().charAt(0).toUpperCase() + str.slice(1)",
            "str[0].toUpperCase() + str.toLowerCase().slice(1)",
            "str.toLowerCase().replace(str[0], str[0].toUpperCase())"
        ],
        "answer": "str.toLowerCase().charAt(0).toUpperCase() + str.slice(1)",
        "difficulty": "Medium",
        "explanation": "Convert the string to lowercase with `toLowerCase()`, use `charAt(0)` to get the first character, capitalize it with `toUpperCase()`, and append the rest with `slice(1)`."
    },

    {
        "question": "How does a do...while loop ensure at least one execution?\n```javascript\nlet i = 0;\ndo {} while (i < 0);\n```",
        "options": ["Condition is checked after the block", "Condition is checked before", "It uses a counter", "It requires a break"],
        "answer": "Condition is checked after the block",
        "difficulty": "Medium",
        "explanation": "A `do...while` loop runs the block first, then checks the condition, ensuring at least one execution."
    },
    {
        "question": "Why might you place a `<script>` tag in the `<head>` with a defer attribute?",
        "options": ["To load the script asynchronously", "To execute after DOM is parsed", "To improve performance", "Both To execute after DOM is parsed and To improve performance"],
        "answer": "Both To execute after DOM is parsed and To improve performance",
        "difficulty": "Medium",
        "explanation": "The `defer` attribute ensures the script runs after the DOM is fully parsed, improving performance."
    },
    {
        "question": "How do you write a multi-line comment that explains a function’s purpose?",
        "options": ["/* Comment */", "// Comment", "# Comment", "<!-- Comment -->"],
        "answer": "/* Comment */",
        "difficulty": "Medium",
        "explanation": "Multi-line comments use `/* */` to document code, such as a function’s purpose."
    },
    {
        "question": "How do you handle a double-click event on a link?\n```javascript\nlet link = document.querySelector('a');\n```",
        "options": ["link.addEventListener('dblclick', func)", "link.onclick = func", "link.doubleClick = func", "link.on('dblclick', func)"],
        "answer": "link.addEventListener('dblclick', func)",
        "difficulty": "Medium",
        "explanation": "The `dblclick` event is handled using `addEventListener` for double-clicks."
    },
    {
        "question": "How do you detect when a button is right-clicked?\n```javascript\nlet button = document.querySelector('button');\n```",
        "options": ["button.addEventListener('contextmenu', func)", "button.onrightclick = func", "button.onclick = func", "button.addEventListener('rightclick', func)"],
        "answer": "button.addEventListener('contextmenu', func)",
        "difficulty": "Medium",
        "explanation": "The `contextmenu` event fires on right-clicks, typically used for context menus."
    },
    {
        "question": "How do you handle a mouse leaving an element?\n```javascript\nlet el = document.querySelector('div');\n```",
        "options": ["el.addEventListener('mouseout', func)", "el.addEventListener('mouseleave', func)", "el.addEventListener('mouseexit', func)", "Both el.addEventListener('mouseout', func) and el.addEventListener('mouseleave', func)"],
        "answer": "Both el.addEventListener('mouseout', func) and el.addEventListener('mouseleave', func)",
        "difficulty": "Medium",
        "explanation": "`mouseout` and `mouseleave` both detect when the mouse leaves an element, with `mouseleave` not bubbling."
    },
    {
        "question": "How do you detect when an input field loses focus?\n```javascript\nlet input = document.querySelector('input');\n```",
        "options": ["input.addEventListener('blur', func)", "input.addEventListener('focusout', func)", "input.addEventListener('change', func)", "Both input.addEventListener('blur', func) and input.addEventListener('focusout', func)"],
        "answer": "Both input.addEventListener('blur', func) and input.addEventListener('focusout', func)",
        "difficulty": "Medium",
        "explanation": "`blur` and `focusout` both trigger when an input loses focus, with `focusout` bubbling."
    },
    {
        "question": "How do you validate an input field’s value before reading it?\n```javascript\nlet input = document.querySelector('input');\n```",
        "options": ["if (input.value) {}", "if (input.value !== '') {}", "if (input.checkValidity()) {}", "Both if (input.value !== '') {} and if (input.checkValidity()) {}"],
        "answer": "Both if (input.value !== '') {} and if (input.checkValidity()) {}",
        "difficulty": "Medium",
        "explanation": "Check if `value` is not empty or use `checkValidity()` for HTML5 validation constraints."
    },
    {
        "question": "How do you programmatically set a number input to 42?\n```javascript\nlet input = document.querySelector('input[type=\"number\"]');\n```",
        "options": ["input.value = 42", "input.value = '42'", "input.setAttribute('value', 42)", "All of the above"],
        "answer": "All of the above",
        "difficulty": "Medium",
        "explanation": "Setting `value` directly or via `setAttribute` updates the input; numbers are coerced to strings."
    },
    {
        "question": "How do you update a paragraph’s HTML content safely?\n```javascript\nlet p = document.querySelector('p');\n```",
        "options": ["p.innerHTML = '<b>Text</b>'", "p.textContent = '<b>Text</b>'", "p.innerText = '<b>Text</b>'", "p.setHTML('<b>Text</b>')"],
        "answer": "p.innerHTML = '<b>Text</b>'",
        "difficulty": "Medium",
        "explanation": "`innerHTML` sets HTML content, but use with caution to avoid XSS; `textContent` escapes HTML."
    },
    {
        "question": "How do you toggle an image’s visibility using styles?\n```javascript\nlet img = document.querySelector('img');\n```",
        "options": ["img.style.display = img.style.display === 'none' ? 'block' : 'none'", "img.toggle('visible')", "img.style.visible = 'toggle'", "img.style.opacity = 0"],
        "answer": "img.style.display = img.style.display === 'none' ? 'block' : 'none'",
        "difficulty": "Medium",
        "explanation": "Toggling `display` between 'none' and 'block' shows or hides the image."
    },
    {
        "question": "How do you swap an image and add a class on click?\n```javascript\nlet img = document.querySelector('img');\n```",
        "options": ["img.src = 'new.jpg'; img.classList.add('active')", "img.setAttribute('src', 'new.jpg'); img.className = 'active'", "img.swapImage('new.jpg'); img.classList.add('active')", "Both img.src = 'new.jpg'; img.classList.add('active') and img.setAttribute('src', 'new.jpg'); img.className = 'active'"],
        "answer": "Both img.src = 'new.jpg'; img.classList.add('active') and img.setAttribute('src', 'new.jpg'); img.className = 'active'",
        "difficulty": "Medium",
        "explanation": "Both setting `src` and `classList.add` or `setAttribute` and `className` work to swap the image and add a class."
    },
    {
        "question": "How do you set multiple styles on an element?\n```javascript\nlet el = document.querySelector('div');\n```",
        "options": ["el.style.cssText = 'color: blue; font-size: 16px'", "el.style = {color: 'blue', fontSize: '16px'}", "el.setStyles({color: 'blue', fontSize: '16px'})", "el.style.set('color: blue; font-size: 16px')"],
        "answer": "el.style.cssText = 'color: blue; font-size: 16px'",
        "difficulty": "Medium",
        "explanation": "`cssText` sets multiple inline styles as a single CSS string."
    },
    {
        "question": "How do you select all `<div>` elements and modify the first one?\n```javascript\nlet divs = document.getElementsByTagName('div');\n```",
        "options": ["divs[0].style.color = 'blue'", "divs.first().style.color = 'blue'", "divs.item(0).style.color = 'blue'", "Both divs[0].style.color = 'blue' and divs.item(0).style.color = 'blue'"],
        "answer": "Both divs[0].style.color = 'blue' and divs.item(0).style.color = 'blue'",
        "difficulty": "Medium",
        "explanation": "`getElementsByTagName` returns an HTMLCollection; access the first element with `[0]` or `item(0)`."
    },
    {
        "question": "How do you select `<p>` elements with a specific class?\n```javascript\ndocument.querySelectorAll('p.className');\n```",
        "options": ["document.querySelectorAll('p.className')", "document.getElementsByClassName('className')", "document.querySelectorAll('p[class=\"className\"]')", "Both document.querySelectorAll('p.className') and document.querySelectorAll('p[class=\"className\"]')"],
        "answer": "Both document.querySelectorAll('p.className') and document.querySelectorAll('p[class=\"className\"]')",
        "difficulty": "Medium",
        "explanation": "CSS selectors `p.className` and `p[class=\"className\"]` both select `<p>` elements with the class 'className'."
    },
    {
        "question": "What is the DOM in JavaScript?",
        "options": ["A programming interface for HTML documents", "A database of elements", "A styling framework", "A JavaScript library"],
        "answer": "A programming interface for HTML documents",
        "difficulty": "Medium",
        "explanation": "The DOM (Document Object Model) is a tree-like structure representing HTML, allowing JavaScript to manipulate it."
    },
    {
        "question": "How do you access the parent of an element?\n```javascript\nlet el = document.querySelector('span');\n```",
        "options": ["el.parentNode", "el.parentElement", "el.getParent()", "Both el.parentNode and el.parentElement"],
        "answer": "Both el.parentNode and el.parentElement",
        "difficulty": "Medium",
        "explanation": "`parentNode` and `parentElement` both return the parent; `parentElement` returns null for non-element nodes."
    },
    {
        "question": "How do you get all child elements of a node?\n```javascript\nlet parent = document.querySelector('div');\n```",
        "options": ["parent.children", "parent.childNodes", "parent.getChildren()", "Both parent.children and parent.childNodes"],
        "answer": "Both parent.children and parent.childNodes",
        "difficulty": "Medium",
        "explanation": "`children` returns only element children; `childNodes` includes all nodes (e.g., text nodes)."
    },
    {
        "question": "How do you filter out non-element nodes from a node’s children?\n```javascript\nlet parent = document.querySelector('div');\n```",
        "options": ["[...parent.childNodes].filter(node => node.nodeType === 1)", "[...parent.children].filter(node => node.nodeType === 1)", "parent.childNodes.filter(node => node.nodeType === 3)", "parent.getElements()"],
        "answer": "[...parent.childNodes].filter(node => node.nodeType === 1)",
        "difficulty": "Medium",
        "explanation": "`childNodes` includes all nodes; filter with `nodeType === 1` to get only elements."
    },
    {
        "question": "How do you select an element by its ID using the DOM?\n```javascript\ndocument.getElementById('myId');\n```",
        "options": ["document.getElementById('myId')", "document.querySelector('#myId')", "document.find('#myId')", "Both document.getElementById('myId') and document.querySelector('#myId')"],
        "answer": "Both document.getElementById('myId') and document.querySelector('#myId')",
        "difficulty": "Medium",
        "explanation": "`getElementById` and `querySelector('#myId')` both select an element by its ID."
    },
    {
        "question": "How do you get the tag name of an element?\n```javascript\nlet el = document.querySelector('div');\n```",
        "options": ["el.tagName", "el.nodeName", "el.name", "Both el.tagName and el.nodeName"],
        "answer": "Both el.tagName and el.nodeName",
        "difficulty": "Medium",
        "explanation": "`tagName` and `nodeName` both return the tag name (e.g., 'DIV') of an element."
    },
    {
        "question": "How do you count the number of `<p>` elements in a document?",
        "options": ["document.querySelectorAll('p').length", "document.getElementsByTagName('p').count", "document.count('p')", "document.querySelector('p').length"],
        "answer": "document.querySelectorAll('p').length",
        "difficulty": "Medium",
        "explanation": "`querySelectorAll('p')` returns a NodeList, and `length` gives the count of `<p>` elements."
    },
    {
        "question": "How do you check if an element has a specific attribute?\n```javascript\nlet el = document.querySelector('input');\n```",
        "options": ["el.hasAttribute('type')", "el.getAttribute('type')", "el.attributes['type']", "Both el.hasAttribute('type') and el.attributes['type']"],
        "answer": "el.hasAttribute('type')",
        "difficulty": "Medium",
        "explanation": "`hasAttribute()` checks if an attribute exists, returning true or false."
    },
    {
        "question": "How do you get the value of an element’s attribute?\n```javascript\nlet el = document.querySelector('input');\n```",
        "options": ["el.getAttribute('value')", "el.attributes.value", "el.value", "Both el.getAttribute('value') and el.value"],
        "answer": "Both el.getAttribute('value') and el.value",
        "difficulty": "Medium",
        "explanation": "`getAttribute('value')` gets the attribute value; `value` directly accesses the input’s current value."
    },
    {
        "question": "How do you create and append a new `<div>` to the DOM?\n```javascript\nlet parent = document.querySelector('body');\n```",
        "options": ["let div = document.createElement('div'); parent.appendChild(div)", "let div = new Element('div'); parent.append(div)", "parent.addElement('div')", "parent.createChild('div')"],
        "answer": "let div = document.createElement('div'); parent.appendChild(div)",
        "difficulty": "Medium",
        "explanation": "`createElement` creates a new element, and `appendChild` adds it to the parent."
    },
    {
        "question": "How do you insert a new element before an existing one?\n```javascript\nlet parent = document.querySelector('div');\nlet child = parent.firstChild;\n```",
        "options": ["parent.insertBefore(newEl, child)", "parent.prepend(newEl)", "parent.insert(newEl, child)", "parent.addBefore(child, newEl)"],
        "answer": "parent.insertBefore(newEl, child)",
        "difficulty": "Medium",
        "explanation": "`insertBefore(newEl, child)` inserts `newEl` before the specified `child` in the parent."
    },
    {
        "question": "How do you create an object with a property in JavaScript?\n```javascript\nlet obj = {};\n```",
        "options": ["obj.name = 'John'", "obj['name'] = 'John'", "obj.set('name', 'John')", "Both obj.name = 'John' and obj['name'] = 'John'"],
        "answer": "Both obj.name = 'John' and obj['name'] = 'John'",
        "difficulty": "Medium",
        "explanation": "Properties can be set using dot notation (`obj.name`) or bracket notation (`obj['name']`)."
    },
    {
        "question": "How do you define a method in an object literal?\n```javascript\nlet obj = {};\n```",
        "options": ["obj.method = function() {}", "obj: method() {}", "obj.method() {}", "Both obj.method = function() {} and obj.method() {}"],
        "answer": "obj.method = function() {}",
        "difficulty": "Medium",
        "explanation": "Methods are defined by assigning a function to a property, e.g., `obj.method = function() {}`."
    },
    {
        "question": "How do you create an object method using concise syntax?\n```javascript\nlet obj = {\n  method() {}\n};\n```",
        "options": ["method() {}", "function method() {}", "method: function() {}", "method = function() {}"],
        "answer": "method() {}",
        "difficulty": "Medium",
        "explanation": "ES6 allows concise method syntax in object literals: `method() {}`."
    },
    {
        "question": "How do you define a constructor function for objects?\n```javascript\nfunction Person(name) {}\n```",
        "options": ["function Person(name) { this.name = name; }", "Person(name) { this.name = name; }", "class Person { name = name; }", "function Person(name) { name: name; }"],
        "answer": "function Person(name) { this.name = name; }",
        "difficulty": "Medium",
        "explanation": "A constructor uses `function` and sets properties on `this`."
    },
    {
        "question": "How do you add a method to a constructor’s prototype?\n```javascript\nfunction Person() {}\n```",
        "options": ["Person.prototype.greet = function() {}", "Person.greet = function() {}", "Person.addMethod('greet', function() {})", "Person.method.greet = function() {}"],
        "answer": "Person.prototype.greet = function() {}",
        "difficulty": "Medium",
        "explanation": "Methods added to `prototype` are shared by all instances of the constructor."
    },
    {
        "question": "How do you add a property to all instances of a constructor?\n```javascript\nfunction Person() {}\n```",
        "options": ["Person.prototype.prop = 'value'", "Person.prop = 'value'", "Person.setProp('value')", "Person.add('prop', 'value')"],
        "answer": "Person.prototype.prop = 'value'",
        "difficulty": "Medium",
        "explanation": "Properties on `prototype` are inherited by all instances of the constructor."
    },
    {
        "question": "How do you check if an object has a specific property?\n```javascript\nlet obj = {name: 'John'};\n```",
        "options": ["'name' in obj", "obj.hasOwnProperty('name')", "obj.isProperty('name')", "Both 'name' in obj and obj.hasOwnProperty('name')"],
        "answer": "Both 'name' in obj and obj.hasOwnProperty('name')",
        "difficulty": "Medium",
        "explanation": "`in` checks for properties in the object and its prototype chain; `hasOwnProperty` checks only the object itself."
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
        "time_left": 1800,  # 30 minutes
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
    st.session_state.time_left = max(1800 - elapsed, 0)
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
        "time_left": 1800,
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
        <p style="color: var(--text-color); font-size: 18px;">Test your JavaScript skills with 50 comprehensive questions!</p>
        <p style="color: #b0b0d0;">30 minutes, 2 points per correct answer. Ready?</p>
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
                if "```javascript" in q["question"] or "```html" in q["question"]:
                    question_parts = q["question"].split("```javascript\n") if "```javascript" in q["question"] else q["question"].split("```html\n")
                    question_text = question_parts[0].strip()
                    code_snippet = question_parts[1].split("```")[0].strip()
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{question_text}**")
                    st.code(code_snippet, language="javascript" if "```javascript" in q["question"] else "html")
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
                            st.session_state.score += 2  # 2 points for Medium difficulty
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
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 1800)
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
                {"name": "Alice", "score": 80, "time": 1200},
                {"name": "Bob", "score": 75, "time": 1300},
                {"name": "Charlie", "score": 70, "time": 1250},
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
