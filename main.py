
import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 67 questions covering specified JavaScript topics
quiz =[
  {
    "question": "What is the purpose of a while loop in JavaScript?",
    "options": [
      "To execute code once",
      "To repeat code while a condition is true",
      "To define a function",
      "To create an array"
    ],
    "answer": "To repeat code while a condition is true",
    "difficulty": "Easy",
    "explanation": "A while loop repeatedly executes a block of code as long as its condition evaluates to true."
  },
  {
    "question": "What happens if the condition in a while loop is never false?",
    "options": [
      "The loop executes once",
      "The loop becomes infinite",
      "The loop skips execution",
      "The code throws an error"
    ],
    "answer": "The loop becomes infinite",
    "difficulty": "Medium",
    "explanation": "If the condition never becomes false, the while loop runs indefinitely, potentially causing the program to hang."
  },
  {
    "question": "Which keyword is used to exit a while loop prematurely?",
    "options": [
      "return",
      "break",
      "continue",
      "exit"
    ],
    "answer": "break",
    "difficulty": "Easy",
    "explanation": "The 'break' statement immediately exits the loop, stopping further iterations."
  },
  {
    "question": "What does the 'continue' statement do in a while loop?",
    "options": [
      "Stops the loop entirely",
      "Skips the current iteration and continues with the next",
      "Restarts the loop",
      "Throws an error"
    ],
    "answer": "Skips the current iteration and continues with the next",
    "difficulty": "Medium",
    "explanation": "The 'continue' statement skips the rest of the current iteration and evaluates the loop's condition again."
  },
  {
    "question": "What is the output of: let i = 0; while (i < 3) { console.log(i); i++; }?",
    "options": [
      "0 1 2",
      "1 2 3",
      "0 1 2 3",
      "Nothing is output"
    ],
    "answer": "0 1 2",
    "difficulty": "Easy",
    "explanation": "The loop runs while i < 3, logging 0, 1, and 2, and increments i each iteration."
  },
  {
    "question": "What is the correct syntax for an if statement in JavaScript?",
    "options": [
      "if (condition) { code }",
      "if condition { code }",
      "if { condition } code",
      "if: condition { code }"
    ],
    "answer": "if (condition) { code }",
    "difficulty": "Easy",
    "explanation": "An if statement uses the syntax 'if (condition) { code }' to execute code if the condition is true."
  },
  {
    "question": "Which comparison operator checks for equality without type conversion?",
    "options": [
      "==",
      "===",
      "!=",
      "!=="
    ],
    "answer": "===",
    "difficulty": "Easy",
    "explanation": "The '===' operator checks for strict equality, comparing both value and type."
  },
  {
    "question": "What does the 'else if' statement do?",
    "options": [
      "Executes code if the previous condition is true",
      "Tests a new condition if the previous if condition is false",
      "Repeats the loop",
      "Stops the program"
    ],
    "answer": "Tests a new condition if the previous if condition is false",
    "difficulty": "Medium",
    "explanation": "An 'else if' statement allows testing additional conditions if the previous if or else if conditions are false."
  },
  {
    "question": "How do you combine multiple conditions in an if statement?",
    "options": [
      "Using + or -",
      "Using && or ||",
      "Using * or /",
      "Using = or !="
    ],
    "answer": "Using && or ||",
    "difficulty": "Easy",
    "explanation": "The logical operators '&&' (AND) and '||' (OR) combine multiple conditions in an if statement."
  },
  {
    "question": "What is the purpose of nested if statements?",
    "options": [
      "To repeat code multiple times",
      "To check conditions within conditions",
      "To define a function",
      "To create an array"
    ],
    "answer": "To check conditions within conditions",
    "difficulty": "Medium",
    "explanation": "Nested if statements allow you to evaluate additional conditions inside an if block."
  },
  {
    "question": "How do you create an array in JavaScript?",
    "options": [
      "let arr = [];",
      "let arr = {};",
      "let arr = ();",
      "let arr = <>;"
    ],
    "answer": "let arr = [];",
    "difficulty": "Easy",
    "explanation": "Arrays in JavaScript are created using square brackets '[]' to define a list of elements."
  },
  {
    "question": "Which method adds an element to the end of an array?",
    "options": [
      "push()",
      "pop()",
      "shift()",
      "unshift()"
    ],
    "answer": "push()",
    "difficulty": "Easy",
    "explanation": "The 'push()' method adds one or more elements to the end of an array."
  },
  {
    "question": "How do you remove the first element from an array?",
    "options": [
      "pop()",
      "shift()",
      "splice()",
      "slice()"
    ],
    "answer": "shift()",
    "difficulty": "Easy",
    "explanation": "The 'shift()' method removes and returns the first element of an array."
  },
  {
    "question": "What does the splice() method do?",
    "options": [
      "Extracts a portion of an array",
      "Adds/removes elements at a specific index",
      "Reverses the array",
      "Joins array elements into a string"
    ],
    "answer": "Adds/removes elements at a specific index",
    "difficulty": "Medium",
    "explanation": "The 'splice()' method can add or remove elements at a specified index in an array."
  },
  {
    "question": "What is the syntax for a for loop in JavaScript?",
    "options": [
      "for (init; condition; update) { code }",
      "for { init; condition; update } code",
      "for (condition) { code }",
      "for: init; condition; update { code }"
    ],
    "answer": "for (init; condition; update) { code }",
    "difficulty": "Easy",
    "explanation": "A for loop uses the syntax 'for (initialization; condition; update) { code }' to repeat code."
  },
  {
    "question": "What does the 'break' statement do in a for loop?",
    "options": [
      "Skips the current iteration",
      "Exits the loop entirely",
      "Restarts the loop",
      "Pauses the loop"
    ],
    "answer": "Exits the loop entirely",
    "difficulty": "Easy",
    "explanation": "The 'break' statement terminates the for loop immediately."
  },
  {
    "question": "What is the purpose of a nested for loop?",
    "options": [
      "To iterate over multiple arrays or dimensions",
      "To define a function",
      "To create an object",
      "To stop the program"
    ],
    "answer": "To iterate over multiple arrays or dimensions",
    "difficulty": "Medium",
    "explanation": "Nested for loops are used to iterate over multi-dimensional data, like arrays within arrays."
  },
  {
    "question": "How do you convert a string to uppercase in JavaScript?",
    "options": [
      "toUpperCase()",
      "toLowerCase()",
      "upperCase()",
      "toUpper()"
    ],
    "answer": "toUpperCase()",
    "difficulty": "Easy",
    "explanation": "The 'toUpperCase()' method converts all characters in a string to uppercase."
  },
  {
    "question": "How do you find the length of a string in JavaScript?",
    "options": [
      "string.size",
      "string.length",
      "string.count",
      "string.len"
    ],
    "answer": "string.length",
    "difficulty": "Easy",
    "explanation": "The 'length' property returns the number of characters in a string."
  },
  {
    "question": "Which method finds the first occurrence of a substring in a string?",
    "options": [
      "indexOf()",
      "search()",
      "find()",
      "includes()"
    ],
    "answer": "indexOf()",
    "difficulty": "Easy",
    "explanation": "The 'indexOf()' method returns the index of the first occurrence of a substring or -1 if not found."
  },
  {
    "question": "How do you get the character at a specific index in a string?",
    "options": [
      "charAt()",
      "getChar()",
      "characterAt()",
      "char()"
    ],
    "answer": "charAt()",
    "difficulty": "Easy",
    "explanation": "The 'charAt()' method returns the character at a specified index in a string."
  },
  {
    "question": "Which method replaces the first occurrence of a substring in a string?",
    "options": [
      "replace()",
      "swap()",
      "change()",
      "substitute()"
    ],
    "answer": "replace()",
    "difficulty": "Easy",
    "explanation": "The 'replace()' method replaces the first occurrence of a substring with a new value."
  },
  {
    "question": "How do you round a number to the nearest integer in JavaScript?",
    "options": [
      "Math.round()",
      "Math.floor()",
      "Math.ceil()",
      "Math.trunc()"
    ],
    "answer": "Math.round()",
    "difficulty": "Easy",
    "explanation": "The 'Math.round()' method rounds a number to the nearest integer."
  },
  {
    "question": "How do you generate a random number between 0 and 1 in JavaScript?",
    "options": [
      "Math.random()",
      "Math.rand()",
      "Random()",
      "Math.generate()"
    ],
    "answer": "Math.random()",
    "difficulty": "Easy",
    "explanation": "The 'Math.random()' method returns a random number between 0 (inclusive) and 1 (exclusive)."
  },
  {
    "question": "How do you convert a string to an integer in JavaScript?",
    "options": [
      "parseInt()",
      "parseFloat()",
      "toString()",
      "Number()"
    ],
    "answer": "parseInt()",
    "difficulty": "Easy",
    "explanation": "The 'parseInt()' function converts a string to an integer, parsing until a non-numeric character is encountered."
  },
  {
    "question": "How do you convert a number to a string in JavaScript?",
    "options": [
      "toString()",
      "parseString()",
      "convertString()",
      "stringify()"
    ],
    "answer": "toString()",
    "difficulty": "Easy",
    "explanation": "The 'toString()' method converts a number to a string."
  },
  {
    "question": "How do you limit the number of decimal places in a number?",
    "options": [
      "toFixed()",
      "toPrecision()",
      "round()",
      "limit()"
    ],
    "answer": "toFixed()",
    "difficulty": "Easy",
    "explanation": "The 'toFixed()' method formats a number to a specified number of decimal places and returns it as a string."
  },
  {
    "question": "How do you get the current date and time in JavaScript?",
    "options": [
      "new Date()",
      "Date.now()",
      "getDate()",
      "new Time()"
    ],
    "answer": "new Date()",
    "difficulty": "Easy",
    "explanation": "The 'new Date()' constructor creates a Date object representing the current date and time."
  },
  {
    "question": "How do you extract the year from a Date object?",
    "options": [
      "getFullYear()",
      "getYear()",
      "getDate()",
      "getMonth()"
    ],
    "answer": "getFullYear()",
    "difficulty": "Easy",
    "explanation": "The 'getFullYear()' method returns the four-digit year of a Date object."
  },
  {
    "question": "How do you create a Date object for a specific date?",
    "options": [
      "new Date('YYYY-MM-DD')",
      "new Date('MM-DD-YYYY')",
      "Date.create('YYYY-MM-DD')",
      "new Date(YYYY, MM, DD)"
    ],
    "answer": "new Date('YYYY-MM-DD')",
    "difficulty": "Medium",
    "explanation": "A Date object can be created using a string like 'YYYY-MM-DD' or by passing year, month, and day as arguments."
  },
  {
    "question": "How do you set the year of a Date object?",
    "options": [
      "setFullYear()",
      "setYear()",
      "changeYear()",
      "updateYear()"
    ],
    "answer": "setFullYear()",
    "difficulty": "Medium",
    "explanation": "The 'setFullYear()' method sets the year of a Date object."
  },
  {
    "question": "What is the purpose of a function in JavaScript?",
    "options": [
      "To store data",
      "To repeat code",
      "To perform a specific task",
      "To create arrays"
    ],
    "answer": "To perform a specific task",
    "difficulty": "Easy",
    "explanation": "Functions are reusable blocks of code designed to perform a specific task."
  },
  {
    "question": "How do you pass data to a function?",
    "options": [
      "Using parameters",
      "Using global variables",
      "Using arrays",
      "Using objects"
    ],
    "answer": "Using parameters",
    "difficulty": "Easy",
    "explanation": "Data is passed to functions through parameters defined in the function declaration."
  },
  {
    "question": "How do you return a value from a function?",
    "options": [
      "Using return",
      "Using break",
      "Using continue",
      "Using yield"
    ],
    "answer": "Using return",
    "difficulty": "Easy",
    "explanation": "The 'return' statement sends a value back from a function and ends its execution."
  },
  {
    "question": "What is a local variable in a function?",
    "options": [
      "A variable accessible globally",
      "A variable defined inside a function",
      "A variable defined outside a function",
      "A variable passed as a parameter"
    ],
    "answer": "A variable defined inside a function",
    "difficulty": "Medium",
    "explanation": "Local variables are defined inside a function and are only accessible within that function's scope."
  },
  {
    "question": "How do you start a switch statement in JavaScript?",
    "options": [
      "switch (expression) {",
      "switch { expression }",
      "case (expression):",
      "switch: expression {"
    ],
    "answer": "switch (expression) {",
    "difficulty": "Easy",
    "explanation": "A switch statement starts with 'switch (expression) {' followed by case clauses."
  },
  {
    "question": "What is required to complete a switch statement?",
    "options": [
      "A default case",
      "A break statement",
      "A case clause",
      "Both break and default"
    ],
    "answer": "Both break and default",
    "difficulty": "Medium",
    "explanation": "A switch statement typically includes 'break' to exit cases and a 'default' case for unmatched values."
  },
  {
    "question": "What is the difference between a while and a do...while loop?",
    "options": [
      "do...while executes at least once",
      "while executes at least once",
      "do...while uses a for loop",
      "They are identical"
    ],
    "answer": "do...while executes at least once",
    "difficulty": "Medium",
    "explanation": "A do...while loop executes its code block at least once before checking the condition."
  },
  {
    "question": "Where should JavaScript scripts be placed in an HTML file?",
    "options": [
      "Inside the <head> tag",
      "At the bottom of the <body> tag",
      "Anywhere in the HTML file",
      "In a separate CSS file"
    ],
    "answer": "At the bottom of the <body> tag",
    "difficulty": "Easy",
    "explanation": "Placing scripts at the bottom of <body> ensures the DOM is loaded before execution."
  },
  {
    "question": "How do you write a single-line comment in JavaScript?",
    "options": [
      "// Comment",
      "/* Comment */",
      "<!-- Comment -->",
      "# Comment"
    ],
    "answer": "// Comment",
    "difficulty": "Easy",
    "explanation": "Single-line comments in JavaScript start with '//'."
  },
  {
    "question": "How do you add a click event to a link in JavaScript?",
    "options": [
      "addEventListener('click', handler)",
      "onClick(handler)",
      "attachEvent('click', handler)",
      "eventClick(handler)"
    ],
    "answer": "addEventListener('click', handler)",
    "difficulty": "Medium",
    "explanation": "The 'addEventListener()' method attaches a click event handler to a link."
  },
  {
    "question": "How do you handle a button click event in JavaScript?",
    "options": [
      "button.addEventListener('click', handler)",
      "button.onClick(handler)",
      "button.event('click', handler)",
      "button.click(handler)"
    ],
    "answer": "button.addEventListener('click', handler)",
    "difficulty": "Medium",
    "explanation": "The 'addEventListener()' method is used to handle button click events."
  },
  {
    "question": "Which event is triggered when a mouse hovers over an element?",
    "options": [
      "mouseover",
      "click",
      "mousemove",
      "mouseout"
    ],
    "answer": "mouseover",
    "difficulty": "Easy",
    "explanation": "The 'mouseover' event is triggered when the mouse pointer enters an element."
  },
  {
    "question": "How do you handle a change event in a form field?",
    "options": [
      "addEventListener('change', handler)",
      "onChange(handler)",
      "field.change(handler)",
      "eventChange(handler)"
    ],
    "answer": "addEventListener('change', handler)",
    "difficulty": "Medium",
    "explanation": "The 'change' event is handled using 'addEventListener()' for form fields like inputs."
  },
  {
    "question": "How do you read the value of a text input field?",
    "options": [
      "input.value",
      "input.text",
      "input.content",
      "input.innerText"
    ],
    "answer": "input.value",
    "difficulty": "Easy",
    "explanation": "The 'value' property retrieves the current value of a text input field."
  },
  {
    "question": "How do you set the value of a text input field?",
    "options": [
      "input.value = 'new value'",
      "input.text = 'new value'",
      "input.setValue('new value')",
      "input.innerText = 'new value'"
    ],
    "answer": "input.value = 'new value'",
    "difficulty": "Easy",
    "explanation": "The 'value' property is used to set the value of a text input field."
  },
  {
    "question": "How do you set the text content of a paragraph element?",
    "options": [
      "p.textContent = 'text'",
      "p.value = 'text'",
      "p.innerHTML = 'text'",
      "Both p.textContent and p.innerHTML"
    ],
    "answer": "Both p.textContent and p.innerHTML",
    "difficulty": "Medium",
    "explanation": "Both 'textContent' and 'innerHTML' can set a paragraph's text, but 'innerHTML' allows HTML tags."
  },
  {
    "question": "How do you change the source of an image element?",
    "options": [
      "img.src = 'new.jpg'",
      "img.source = 'new.jpg'",
      "img.setSrc('new.jpg')",
      "img.image = 'new.jpg'"
    ],
    "answer": "img.src = 'new.jpg'",
    "difficulty": "Easy",
    "explanation": "The 'src' property sets the source URL of an image element."
  },
  {
    "question": "How do you swap an image by changing its class?",
    "options": [
      "img.className = 'new-class'",
      "img.class = 'new-class'",
      "img.setClass('new-class')",
      "img.style = 'new-class'"
    ],
    "answer": "img.className = 'new-class'",
    "difficulty": "Medium",
    "explanation": "The 'className' property changes an element's class, which can swap an image if styled via CSS."
  },
  {
    "question": "How do you set an element's inline style in JavaScript?",
    "options": [
      "element.style.property = 'value'",
      "element.setStyle('property', 'value')",
      "element.css('property', 'value')",
      "element.style = 'property: value'"
    ],
    "answer": "element.style.property = 'value'",
    "difficulty": "Easy",
    "explanation": "The 'style' property is used to set inline CSS properties, like 'element.style.color = 'red''."
  },
  {
    "question": "How do you select all elements by tag name?",
    "options": [
      "document.getElementsByTagName()",
      "document.querySelectorAll()",
      "document.getElementsByClassName()",
      "document.getElementById()"
    ],
    "answer": "document.getElementsByTagName()",
    "difficulty": "Easy",
    "explanation": "'getElementsByTagName()' selects all elements with the specified tag name."
  },
  {
    "question": "How do you select some elements by tag name using querySelectorAll?",
    "options": [
      "document.querySelectorAll('tag')",
      "document.getElementsByTag('tag')",
      "document.querySelector('tag')",
      "document.selectTag('tag')"
    ],
    "answer": "document.querySelectorAll('tag')",
    "difficulty": "Medium",
    "explanation": "'querySelectorAll('tag')' selects all elements with the specified tag name."
  },
  {
    "question": "What is the DOM in JavaScript?",
    "options": [
      "A programming interface for HTML documents",
      "A database for storing data",
      "A JavaScript library",
      "A type of loop"
    ],
    "answer": "A programming interface for HTML documents",
    "difficulty": "Easy",
    "explanation": "The DOM (Document Object Model) is a programming interface for manipulating HTML documents."
  },
  {
    "question": "What is the parentNode property in the DOM?",
    "options": [
      "The first child of an element",
      "The parent element of a node",
      "The next sibling of an element",
      "The root of the document"
    ],
    "answer": "The parent element of a node",
    "difficulty": "Medium",
    "explanation": "The 'parentNode' property returns the parent node of a given DOM element."
  },
  {
    "question": "How do you find the children of a DOM element?",
    "options": [
      "element.children",
      "element.childNodes",
      "element.getChildren()",
      "Both element.children and element.childNodes"
    ],
    "answer": "Both element.children and element.childNodes",
    "difficulty": "Medium",
    "explanation": "'children' returns HTML elements, while 'childNodes' includes all nodes (e.g., text nodes)."
  },
  {
    "question": "What is the nodeType property used for in the DOM?",
    "options": [
      "To get the element's ID",
      "To identify the type of node",
      "To count child nodes",
      "To set the node’s style"
    ],
    "answer": "To identify the type of node",
    "difficulty": "Medium",
    "explanation": "The 'nodeType' property returns a number indicating the type of node (e.g., 1 for elements, 3 for text)."
  },
  {
    "question": "How do you select an element by its class name in the DOM?",
    "options": [
      "document.getElementsByClassName()",
      "document.getElementById()",
      "document.querySelector('.class')",
      "Both getElementsByClassName and querySelector"
    ],
    "answer": "Both getElementsByClassName and querySelector",
    "difficulty": "Medium",
    "explanation": "Both methods can select elements by class; 'querySelector' uses CSS selector syntax."
  },
  {
    "question": "How do you get the tag name of a DOM element?",
    "options": [
      "element.tagName",
      "element.name",
      "element.type",
      "element.id"
    ],
    "answer": "element.tagName",
    "difficulty": "Easy",
    "explanation": "The 'tagName' property returns the tag name of a DOM element in uppercase."
  },
  {
    "question": "How do you count the number of child elements in a DOM node?",
    "options": [
      "element.children.length",
      "element.childNodes.length",
      "element.countChildren()",
      "Both children.length and childNodes.length"
    ],
    "answer": "Both children.length and childNodes.length",
    "difficulty": "Medium",
    "explanation": "'children.length' counts HTML elements, while 'childNodes.length' counts all nodes."
  },
  {
    "question": "How do you get an element’s attribute in the DOM?",
    "options": [
      "element.getAttribute('name')",
      "element.attribute('name')",
      "element.getAttr('name')",
      "element.name"
    ],
    "answer": "element.getAttribute('name')",
    "difficulty": "Easy",
    "explanation": "The 'getAttribute()' method retrieves the value of a specified attribute."
  },
  {
    "question": "How do you add a new node to the DOM?",
    "options": [
      "document.createElement()",
      "document.addNode()",
      "document.newElement()",
      "document.append()"
    ],
    "answer": "document.createElement()",
    "difficulty": "Medium",
    "explanation": "'createElement()' creates a new element node, which can then be added to the DOM."
  },
  {
    "question": "How do you insert a node before another in the DOM?",
    "options": [
      "parent.insertBefore(newNode, referenceNode)",
      "parent.appendChild(newNode)",
      "parent.replaceChild(newNode)",
      "parent.addBefore(newNode)"
    ],
    "answer": "parent.insertBefore(newNode, referenceNode)",
    "difficulty": "Medium",
    "explanation": "'insertBefore()' inserts a new node before a specified reference node."
  },
  {
    "question": "What is an object in JavaScript?",
    "options": [
      "A collection of properties",
      "A type of loop",
      "A function declaration",
      "An array of numbers"
    ],
    "answer": "A collection of properties",
    "difficulty": "Easy",
    "explanation": "An object is a data structure that stores key-value pairs, known as properties."
  },
  {
    "question": "How do you access an object’s property in JavaScript?",
    "options": [
      "object.property or object['property']",
      "object(property)",
      "object.getProperty()",
      "object::property"
    ],
    "answer": "object.property or object['property']",
    "difficulty": "Easy",
    "explanation": "Properties can be accessed using dot notation or bracket notation."
  },
  {
    "question": "What is a method in a JavaScript object?",
    "options": [
      "A function stored as a property",
      "A loop inside an object",
      "A variable inside an object",
      "A class definition"
    ],
    "answer": "A function stored as a property",
    "difficulty": "Medium",
    "explanation": "A method is a function assigned to an object’s property, allowing the object to perform actions."
  },
  {
    "question": "What is an object constructor in JavaScript?",
    "options": [
      "A function used to create objects",
      "A loop for creating objects",
      "A property of an object",
      "An array of objects"
    ],
    "answer": "A function used to create objects",
    "difficulty": "Medium",
    "explanation": "A constructor is a function used with the 'new' keyword to create and initialize objects."
  },
  {
    "question": "How do you add a method to an object constructor?",
    "options": [
      "Inside the constructor function",
      "Using a loop",
      "Using an array",
      "Using a prototype"
    ],
    "answer": "Both inside the constructor and using a prototype",
    "difficulty": "Medium",
    "explanation": "Methods can be defined inside the constructor or added to the prototype for shared functionality."
  },
  {
    "question": "What is the purpose of a prototype in JavaScript?",
    "options": [
      "To add shared properties/methods to objects",
      "To create loops",
      "To store arrays",
      "To define variables"
    ],
    "answer": "To add shared properties/methods to objects",
    "difficulty": "Medium",
    "explanation": "Prototypes allow objects created by a constructor to share properties and methods."
  },
  {
    "question": "How do you check if a property exists in an object?",
    "options": [
      "object.hasOwnProperty('property')",
      "object.exists('property')",
      "object.propertyExists('property')",
      "object.checkProperty('property')"
    ],
    "answer": "object.hasOwnProperty('property')",
    "difficulty": "Medium",
    "explanation": "'hasOwnProperty()' checks if an object has a specific property as its own, not inherited."
  },
  {
    "question": "How do you get the current URL of a webpage?",
    "options": [
      "window.location.href",
      "document.url",
      "window.url",
      "location.getURL()"
    ],
    "answer": "window.location.href",
    "difficulty": "Easy",
    "explanation": "'window.location.href' returns the full URL of the current webpage."
  },
  {
    "question": "How do you set a new URL for the current page?",
    "options": [
      "window.location.href = 'new-url'",
      "document.url = 'new-url'",
      "window.setURL('new-url')",
      "location.navigate('new-url')"
    ],
    "answer": "window.location.href = 'new-url'",
    "difficulty": "Medium",
    "explanation": "Setting 'window.location.href' navigates the browser to a new URL."
  },
  {
    "question": "How do you go back to the previous page in the browser?",
    "options": [
      "window.history.back()",
      "window.location.back()",
      "history.goBack()",
      "document.back()"
    ],
    "answer": "window.history.back()",
    "difficulty": "Medium",
    "explanation": "'window.history.back()' navigates to the previous page in the browser’s history."
  },
  {
    "question": "How do you make an element fill the browser window?",
    "options": [
      "element.style.width = '100vw'; element.style.height = '100vh'",
      "element.style.width = '100%'; element.style.height = '100%'",
      "element.setSize('full')",
      "element.style.fullscreen = true"
    ],
    "answer": "element.style.width = '100vw'; element.style.height = '100vh'",
    "difficulty": "Medium",
    "explanation": "Using '100vw' and '100vh' sets an element’s size to the full viewport width and height."
  },
  {
    "question": "How do you resize the browser window?",
    "options": [
      "window.resizeTo(width, height)",
      "window.setSize(width, height)",
      "window.resize(width, height)",
      "document.resize(width, height)"
    ],
    "answer": "window.resizeTo(width, height)",
    "difficulty": "Medium",
    "explanation": "'window.resizeTo()' sets the browser window to a specific width and height."
  },
  {
    "question": "How do you test for popup blockers in JavaScript?",
    "options": [
      "Check if window.open() returns null",
      "Use window.popupTest()",
      "Check document.popupBlocked",
      "Use window.isBlocked()"
    ],
    "answer": "Check if window.open() returns null",
    "difficulty": "Hard",
    "explanation": "If 'window.open()' returns null, it indicates a popup blocker prevented the window from opening."
  },
  {
    "question": "How do you validate a text field to ensure it’s not empty?",
    "options": [
      "if (input.value.trim() === '')",
      "if (input.text === '')",
      "if (input.value === null)",
      "if (input.empty())"
    ],
    "answer": "if (input.value.trim() === '')",
    "difficulty": "Medium",
    "explanation": "Use 'trim()' to remove whitespace and check if the input’s value is an empty string."
  },
  {
    "question": "How do you validate a dropdown selection?",
    "options": [
      "Check if select.value is not empty",
      "Check if select.selectedIndex >= 0",
      "Check if select.option is null",
      "Check if select.text is empty"
    ],
    "answer": "Check if select.value is not empty",
    "difficulty": "Medium",
    "explanation": "A dropdown’s 'value' property returns the selected option’s value; an empty string indicates no selection."
  },
  {
    "question": "How do you validate a radio button selection?",
    "options": [
      "Check if any radio button is checked",
      "Check if radio.value is not null",
      "Check if radio.selected is true",
      "Check if radio.checked is false"
    ],
    "answer": "Check if any radio button is checked",
    "difficulty": "Medium",
    "explanation": "Use the 'checked' property to verify if at least one radio button in a group is selected."
  },
  {
    "question": "How do you validate a ZIP code format (e.g., 12345)?",
    "options": [
      "/^\\d{5}$/.test(input.value)",
      "/^\\d{5}-\\d{4}$/.test(input.value)",
      "input.value.length === 5",
      "isZipCode(input.value)"
    ],
    "answer": "/^\\d{5}$/.test(input.value)",
    "difficulty": "Hard",
    "explanation": "A regular expression '/^\\d{5}$/' ensures the input is exactly five digits."
  },
  {
    "question": "How do you validate an email address format?",
    "options": [
      "/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)",
      "/^\\w+@\\w+\\.com$/.test(email)",
      "email.includes('@')",
      "email.validate()"
    ],
    "answer": "/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)",
    "difficulty": "Hard",
    "explanation": "A regular expression checks for a valid email format with a username, '@', domain, and top-level domain."
  },
  {
    "question": "What does a try...catch block do in JavaScript?",
    "options": [
      "Handles errors gracefully",
      "Repeats code",
      "Defines a function",
      "Creates an array"
    ],
    "answer": "Handles errors gracefully",
    "difficulty": "Medium",
    "explanation": "A try...catch block catches and handles exceptions (errors) that occur in the try block."
  },
  {
    "question": "How do you throw a custom error in JavaScript?",
    "options": [
      "throw new Error('message')",
      "throw 'message'",
      "error('message')",
      "raise new Error('message')"
    ],
    "answer": "throw new Error('message')",
    "difficulty": "Medium",
    "explanation": "The 'throw' statement with a new Error object creates a custom error with a message."
  },
  {
    "question": "How do you handle events directly in JavaScript?",
    "options": [
      "Using addEventListener()",
      "Using inline HTML events",
      "Using event attributes",
      "All of the above"
    ],
    "answer": "All of the above",
    "difficulty": "Medium",
    "explanation": "Events can be handled using 'addEventListener()', inline HTML (e.g., onclick), or event attributes."
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




