


import streamlit as st
import random
from datetime import datetime
import uuid


# Quiz data with 67 questions covering specified JavaScript topics
quiz =[
  {
    "question": "What happens if a while loop's condition is initially false?",
    "options": [
      "The loop executes once",
      "The loop skips entirely",
      "The loop throws an error",
      "The loop runs indefinitely"
    ],
    "answer": "The loop skips entirely",
    "difficulty": "Medium",
    "explanation": "If the condition in a while loop is false initially, the loop body is not executed."
  },
  {
    "question": "How do you prevent an infinite while loop?",
    "options": [
      "Using a counter or condition update",
      "Using a return statement",
      "Using a function declaration",
      "Using an array"
    ],
    "answer": "Using a counter or condition update",
    "difficulty": "Medium",
    "explanation": "Updating a counter or condition inside the loop ensures it eventually becomes false."
  },
  {
    "question": "What is the output of: let i = 5; while (i > 0) { console.log(i); i -= 2; }?",
    "options": [
      "5 3 1",
      "5 4 3 2 1",
      "4 2 0",
      "5 3"
    ],
    "answer": "5 3 1",
    "difficulty": "Medium",
    "explanation": "The loop logs i and decrements by 2 until i > 0 is false, outputting 5, 3, 1."
  },
  {
    "question": "How do you use a while loop to sum numbers from 1 to 5?",
    "options": [
      "let sum = 0, i = 1; while (i <= 5) { sum += i; i++; }",
      "let sum = 0; while (i < 5) { sum += i; }",
      "let sum = 0, i = 1; while (i < 5) { sum += i; }",
      "let sum = 0, i = 0; while (i <= 5) { sum += i; i++; }"
    ],
    "answer": "let sum = 0, i = 1; while (i <= 5) { sum += i; i++; }",
    "difficulty": "Medium",
    "explanation": "The loop adds numbers from 1 to 5, incrementing i each time, resulting in sum = 15."
  },
  {
    "question": "What does the 'continue' statement do in a while loop?",
    "options": [
      "Exits the loop",
      "Skips to the next iteration",
      "Restarts the loop",
      "Pauses execution"
    ],
    "answer": "Skips to the next iteration",
    "difficulty": "Medium",
    "explanation": "The 'continue' statement skips the rest of the current iteration and checks the condition again."
  },
  {
    "question": "What is the result of: if (5 > 3) { console.log('Yes'); } else { console.log('No'); }?",
    "options": [
      "Yes",
      "No",
      "Nothing is logged",
      "Error"
    ],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "Since 5 > 3 is true, the if block executes, logging 'Yes'."
  },
  {
    "question": "Which comparison operator checks for inequality with type conversion?",
    "options": [
      "==",
      "===",
      "!=",
      "!=="
    ],
    "answer": "!=",
    "difficulty": "Medium",
    "explanation": "The '!=' operator checks for inequality, converting types if necessary."
  },
  {
    "question": "What is the output of: if (false) { console.log('A'); } else if (true) { console.log('B'); } else { console.log('C'); }?",
    "options": [
      "A",
      "B",
      "C",
      "Nothing is logged"
    ],
    "answer": "B",
    "difficulty": "Medium",
    "explanation": "The else if (true) block executes because the first condition is false and the second is true."
  },
  {
    "question": "How do you test multiple conditions using && in an if statement?",
    "options": [
      "if (a > 0 && b < 10) { code }",
      "if (a > 0 + b < 10) { code }",
      "if (a > 0, b < 10) { code }",
      "if (a > 0 || b < 10) { code }"
    ],
    "answer": "if (a > 0 && b < 10) { code }",
    "difficulty": "Medium",
    "explanation": "The '&&' operator requires both conditions to be true for the if block to execute."
  },
  {
    "question": "What is the output of: if (x > 10) { if (x < 20) { console.log('Range'); } } when x = 15?",
    "options": [
      "Range",
      "Nothing is logged",
      "Error",
      "undefined"
    ],
    "answer": "Range",
    "difficulty": "Medium",
    "explanation": "The nested if checks if x is between 10 and 20; since x = 15, 'Range' is logged."
  },
  {
    "question": "How do you initialize an array with specific values?",
    "options": [
      "let arr = [1, 2, 3];",
      "let arr = {1, 2, 3};",
      "let arr = (1, 2, 3);",
      "let arr = <1, 2, 3>;"
    ],
    "answer": "let arr = [1, 2, 3];",
    "difficulty": "Medium",
    "explanation": "Arrays are initialized with square brackets containing comma-separated values."
  },
  {
    "question": "What does arr.push(4, 5) do to an array?",
    "options": [
      "Adds 4 and 5 to the start",
      "Adds 4 and 5 to the end",
      "Removes 4 and 5",
      "Replaces elements with 4 and 5"
    ],
    "answer": "Adds 4 and 5 to the end",
    "difficulty": "Medium",
    "explanation": "The 'push()' method appends multiple elements to the end of an array."
  },
  {
    "question": "What does arr.shift() return?",
    "options": [
      "The last element",
      "The first element",
      "The array length",
      "Nothing"
    ],
    "answer": "The first element",
    "difficulty": "Medium",
    "explanation": "'shift()' removes and returns the first element, shifting others left."
  },
  {
    "question": "What does arr.splice(2, 1, 'new') do?",
    "options": [
      "Removes 1 element at index 2 and adds 'new'",
      "Adds 'new' at index 2",
      "Removes 'new' from index 2",
      "Extracts 1 element at index 2"
    ],
    "answer": "Removes 1 element at index 2 and adds 'new'",
    "difficulty": "Medium",
    "explanation": "'splice(2, 1, 'new')' removes 1 element at index 2 and inserts 'new'."
  },
  {
    "question": "What is the output of: for (let i = 0; i < 3; i++) { console.log(i * 2); }?",
    "options": [
      "0 2 4",
      "0 1 2",
      "2 4 6",
      "0 2 6"
    ],
    "answer": "0 2 4",
    "difficulty": "Medium",
    "explanation": "The loop multiplies i by 2 for i = 0, 1, 2, logging 0, 2, 4."
  },
  {
    "question": "How do you use a flag in a for loop?",
    "options": [
      "Set a boolean to track a condition",
      "Use a counter variable",
      "Use a loop label",
      "Use a function"
    ],
    "answer": "Set a boolean to track a condition",
    "difficulty": "Medium",
    "explanation": "A flag is a boolean variable used to track a condition, like finding an element."
  },
  {
    "question": "What does this nested loop do: for (let i = 0; i < 2; i++) { for (let j = 0; j < 2; j++) { console.log(i, j); } }?",
    "options": [
      "Logs pairs (0,0), (0,1), (1,0), (1,1)",
      "Logs pairs (0,0), (1,1)",
      "Logs pairs (0,1), (1,0)",
      "Logs i and j separately"
    ],
    "answer": "Logs pairs (0,0), (0,1), (1,0), (1,1)",
    "difficulty": "Medium",
    "explanation": "The nested loop iterates over all combinations of i and j, logging each pair."
  },
  {
    "question": "What does 'hello'.toLowerCase() return?",
    "options": [
      "HELLO",
      "hello",
      "Hello",
      "hELLO"
    ],
    "answer": "hello",
    "difficulty": "Medium",
    "explanation": "'toLowerCase()' converts all characters in a string to lowercase."
  },
  {
    "question": "What is the value of 'javascript'.length?",
    "options": [
      "9",
      "10",
      "8",
      "11"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "The 'length' property counts the characters in 'javascript', which is 10."
  },
  {
    "question": "What does 'hello world'.indexOf('world') return?",
    "options": [
      "6",
      "5",
      "0",
      "-1"
    ],
    "answer": "6",
    "difficulty": "Medium",
    "explanation": "'indexOf()' returns the starting index of 'world', which is 6 (after 'hello ')."
  },
  {
    "question": "What does 'test'.charAt(1) return?",
    "options": [
      "e",
      "t",
      "s",
      "undefined"
    ],
    "answer": "e",
    "difficulty": "Medium",
    "explanation": "'charAt(1)' returns the character at index 1, which is 'e' in 'test'."
  },
  {
    "question": "What does 'hello'.replace('l', 'p') return?",
    "options": [
      "heplo",
      "hepplo",
      "hello",
      "hallo"
    ],
    "answer": "heplo",
    "difficulty": "Medium",
    "explanation": "'replace()' replaces the first 'l' with 'p', resulting in 'heplo'."
  },
  {
    "question": "What does Math.round(3.6) return?",
    "options": [
      "4",
      "3",
      "3.6",
      "4.0"
    ],
    "answer": "4",
    "difficulty": "Medium",
    "explanation": "'Math.round()' rounds 3.6 to the nearest integer, which is 4."
  },
  {
    "question": "How do you generate a random integer between 1 and 10?",
    "options": [
      "Math.floor(Math.random() * 10) + 1",
      "Math.random() * 10",
      "Math.ceil(Math.random() * 10)",
      "Math.round(Math.random() * 10)"
    ],
    "answer": "Math.floor(Math.random() * 10) + 1",
    "difficulty": "Medium",
    "explanation": "'Math.random() * 10' gives 0 to 9.999, 'Math.floor' rounds down, and +1 shifts to 1-10."
  },
  {
    "question": "What does parseInt('123abc') return?",
    "options": [
      "123",
      "NaN",
      "123abc",
      "undefined"
    ],
    "answer": "123",
    "difficulty": "Medium",
    "explanation": "'parseInt()' parses a string to an integer until a non-numeric character is found."
  },
  {
    "question": "What does (456).toString() return?",
    "options": [
      "456",
      "'456'",
      "456.0",
      "undefined"
    ],
    "answer": "'456'",
    "difficulty": "Medium",
    "explanation": "'toString()' converts the number 456 to the string '456'."
  },
  {
    "question": "What does (3.14159).toFixed(2) return?",
    "options": [
      "'3.14'",
      "3.14",
      "'3.14159'",
      "3.142"
    ],
    "answer": "'3.14'",
    "difficulty": "Medium",
    "explanation": "'toFixed(2)' formats the number to 2 decimal places, returning '3.14' as a string."
  },
  {
    "question": "What does new Date().getTime() return?",
    "options": [
      "Current timestamp in milliseconds",
      "Current date as a string",
      "Current year",
      "Current time in seconds"
    ],
    "answer": "Current timestamp in milliseconds",
    "difficulty": "Medium",
    "explanation": "'getTime()' returns the number of milliseconds since January 1, 1970."
  },
  {
    "question": "What does new Date().getMonth() return?",
    "options": [
      "0 to 11",
      "1 to 12",
      "Month name",
      "Current day"
    ],
    "answer": "0 to 11",
    "difficulty": "Medium",
    "explanation": "'getMonth()' returns the month as a number from 0 (January) to 11 (December)."
  },
  {
    "question": "How do you create a Date object for January 15, 2023?",
    "options": [
      "new Date('2023-01-15')",
      "new Date('01-15-2023')",
      "new Date(2023, 1, 15)",
      "new Date(2023, 0, 15)"
    ],
    "answer": "new Date('2023-01-15')",
    "difficulty": "Medium",
    "explanation": "'new Date('2023-01-15')' or 'new Date(2023, 0, 15)' creates a Date for January 15, 2023."
  },
  {
    "question": "What does date.setMonth(5) do?",
    "options": [
      "Sets the month to June",
      "Sets the month to May",
      "Sets the day to 5",
      "Sets the year to 5"
    ],
    "answer": "Sets the month to June",
    "difficulty": "Medium",
    "explanation": "'setMonth(5)' sets the month to June (0-based indexing: 0=January, 5=June)."
  },
  {
    "question": "What is the output of: function add(a, b) { return a + b; } console.log(add(2, 3));?",
    "options": [
      "5",
      "23",
      "undefined",
      "Error"
    ],
    "answer": "5",
    "difficulty": "Medium",
    "explanation": "The function 'add' returns the sum of 2 and 3, which is 5."
  },
  {
    "question": "How do you pass multiple parameters to a function?",
    "options": [
      "function name(a, b, c) {}",
      "function name(a; b; c) {}",
      "function name(a b c) {}",
      "function name(a + b + c) {}"
    ],
    "answer": "function name(a, b, c) {}",
    "difficulty": "Medium",
    "explanation": "Multiple parameters are defined in the function declaration, separated by commas."
  },
  {
    "question": "What does this function return: function square(num) { return num * num; } when called with square(4)?",
    "options": [
      "16",
      "8",
      "4",
      "undefined"
    ],
    "answer": "16",
    "difficulty": "Medium",
    "explanation": "The function multiplies 4 by 4, returning 16."
  },
  {
    "question": "What is the scope of a variable declared with 'let' inside a function?",
    "options": [
      "Local to the function",
      "Global",
      "Block-scoped",
      "Both local and block-scoped"
    ],
    "answer": "Both local and block-scoped",
    "difficulty": "Medium",
    "explanation": "'let' variables are block-scoped and local to the function they’re declared in."
  },
  {
    "question": "What does this switch statement do: switch (day) { case 1: console.log('Monday'); break; default: console.log('Other'); } when day = 2?",
    "options": [
      "Logs 'Monday'",
      "Logs 'Other'",
      "Logs nothing",
      "Throws an error"
    ],
    "answer": "Logs 'Other'",
    "difficulty": "Medium",
    "explanation": "Since day = 2 doesn’t match case 1, the default case logs 'Other'."
  },
  {
    "question": "How do you ensure a switch case stops execution?",
    "options": [
      "Use break",
      "Use return",
      "Use continue",
      "Use exit"
    ],
    "answer": "Use break",
    "difficulty": "Medium",
    "explanation": "The 'break' statement prevents fall-through to the next case."
  },
  {
    "question": "What does a do...while loop guarantee?",
    "options": [
      "At least one execution",
      "No executions",
      "Infinite executions",
      "Conditional execution"
    ],
    "answer": "At least one execution",
    "difficulty": "Medium",
    "explanation": "A do...while loop executes its body at least once before checking the condition."
  },
  {
    "question": "What is the output of: let i = 0; do { console.log(i); i++; } while (i < 2);?",
    "options": [
      "0 1",
      "1 2",
      "0",
      "1"
    ],
    "answer": "0 1",
    "difficulty": "Medium",
    "explanation": "The loop executes twice, logging 0 and 1, as i increments until i < 2 is false."
  },
  {
    "question": "Why place scripts at the bottom of the <body> tag?",
    "options": [
      "To ensure DOM is fully loaded",
      "To improve CSS rendering",
      "To reduce file size",
      "To avoid function hoisting"
    ],
    "answer": "To ensure DOM is fully loaded",
    "difficulty": "Medium",
    "explanation": "Scripts at the bottom run after the DOM is parsed, preventing access errors."
  },
  {
    "question": "How do you write a multi-line comment in JavaScript?",
    "options": [
      "/* Comment */",
      "// Comment",
      "<!-- Comment -->",
      "# Comment"
    ],
    "answer": "/* Comment */",
    "difficulty": "Medium",
    "explanation": "Multi-line comments are enclosed in '/*' and '*/'."
  },
  {
    "question": "How do you attach a click event to a link using addEventListener?",
    "options": [
      "link.addEventListener('click', func)",
      "link.onClick(func)",
      "link.event('click', func)",
      "link.click(func)"
    ],
    "answer": "link.addEventListener('click', func)",
    "difficulty": "Medium",
    "explanation": "'addEventListener()' binds a function to the 'click' event of a link."
  },
  {
    "question": "What does button.addEventListener('click', () => alert('Clicked')) do?",
    "options": [
      "Shows an alert when the button is clicked",
      "Changes the button’s text",
      "Disables the button",
      "Redirects the page"
    ],
    "answer": "Shows an alert when the button is clicked",
    "difficulty": "Medium",
    "explanation": "The event listener triggers an alert when the button is clicked."
  },
  {
    "question": "What does the 'mouseout' event do?",
    "options": [
      "Triggers when the mouse leaves an element",
      "Triggers when the mouse clicks",
      "Triggers when the mouse moves",
      "Triggers when the mouse enters"
    ],
    "answer": "Triggers when the mouse leaves an element",
    "difficulty": "Medium",
    "explanation": "'mouseout' fires when the mouse pointer exits an element."
  },
  {
    "question": "How do you handle a form input’s 'input' event?",
    "options": [
      "input.addEventListener('input', handler)",
      "input.onInput(handler)",
      "input.event('input', handler)",
      "input.change(handler)"
    ],
    "answer": "input.addEventListener('input', handler)",
    "difficulty": "Medium",
    "explanation": "The 'input' event fires on every change to the input’s value."
  },
  {
    "question": "What is input.value for a text field with 'hello' entered?",
    "options": [
      "'hello'",
      "hello",
      "undefined",
      "null"
    ],
    "answer": "'hello'",
    "difficulty": "Medium",
    "explanation": "The 'value' property returns the string entered in the text field."
  },
  {
    "question": "How do you set a text field’s value to 'test'?",
    "options": [
      "input.value = 'test'",
      "input.text = 'test'",
      "input.setValue('test')",
      "input.innerText = 'test'"
    ],
    "answer": "input.value = 'test'",
    "difficulty": "Medium",
    "explanation": "Assigning to 'value' sets the text field’s content to 'test'."
  },
  {
    "question": "What does p.textContent = 'New text' do?",
    "options": [
      "Sets the paragraph’s text",
      "Sets the paragraph’s HTML",
      "Clears the paragraph",
      "Adds a class"
    ],
    "answer": "Sets the paragraph’s text",
    "difficulty": "Medium",
    "explanation": "'textContent' sets the text content of a paragraph, ignoring HTML tags."
  },
  {
    "question": "How do you change an image’s source to 'new.jpg'?",
    "options": [
      "img.src = 'new.jpg'",
      "img.source = 'new.jpg'",
      "img.setSrc('new.jpg')",
      "img.image = 'new.jpg'"
    ],
    "answer": "img.src = 'new.jpg'",
    "difficulty": "Medium",
    "explanation": "The 'src' property sets the image’s source URL."
  },
  {
    "question": "How do you toggle an image’s class to swap its appearance?",
    "options": [
      "img.classList.toggle('new-class')",
      "img.className = 'new-class'",
      "img.setClass('new-class')",
      "img.style.class = 'new-class'"
    ],
    "answer": "img.classList.toggle('new-class')",
    "difficulty": "Medium",
    "explanation": "'classList.toggle()' adds or removes a class, useful for swapping styles."
  },
  {
    "question": "How do you set an element’s background color to blue?",
    "options": [
      "element.style.backgroundColor = 'blue'",
      "element.style.background = 'blue'",
      "element.setStyle('background', 'blue')",
      "element.css('backgroundColor', 'blue')"
    ],
    "answer": "element.style.backgroundColor = 'blue'",
    "difficulty": "Medium",
    "explanation": "The 'style.backgroundColor' property sets the inline background color."
  },
  {
    "question": "What does document.getElementsByTagName('div') return?",
    "options": [
      "A live HTMLCollection of divs",
      "An array of divs",
      "A single div element",
      "A NodeList of divs"
    ],
    "answer": "A live HTMLCollection of divs",
    "difficulty": "Medium",
    "explanation": "'getElementsByTagName()' returns a live HTMLCollection of elements with the tag 'div'."
  },
  {
    "question": "How do you select all paragraphs using querySelectorAll?",
    "options": [
      "document.querySelectorAll('p')",
      "document.getElementsByTagName('p')",
      "document.querySelector('p')",
      "Both querySelectorAll and getElementsByTagName"
    ],
    "answer": "Both querySelectorAll and getElementsByTagName",
    "difficulty": "Medium",
    "explanation": "Both methods select all <p> elements; 'querySelectorAll' returns a static NodeList."
  },
  {
    "question": "What does the DOM represent?",
    "options": [
      "A tree structure of HTML elements",
      "A JavaScript function",
      "A CSS stylesheet",
      "A database"
    ],
    "answer": "A tree structure of HTML elements",
    "difficulty": "Medium",
    "explanation": "The DOM is a tree-like representation of HTML elements for manipulation."
  },
  {
    "question": "What does element.parentNode return?",
    "options": [
      "The parent element",
      "The first child",
      "The next sibling",
      "The document root"
    ],
    "answer": "The parent element",
    "difficulty": "Medium",
    "explanation": "'parentNode' returns the parent node of an element in the DOM."
  },
  {
    "question": "What does element.children include?",
    "options": [
      "Only HTML element children",
      "All nodes including text",
      "Only text nodes",
      "Only comment nodes"
    ],
    "answer": "Only HTML element children",
    "difficulty": "Medium",
    "explanation": "'children' returns a collection of HTML element children, excluding text or comments."
  },
  {
    "question": "What does node.nodeType === 3 indicate?",
    "options": [
      "Text node",
      "Element node",
      "Comment node",
      "Document node"
    ],
    "answer": "Text node",
    "difficulty": "Medium",
    "explanation": "A 'nodeType' of 3 indicates a text node in the DOM."
  },
  {
    "question": "How do you select an element with id 'test' using querySelector?",
    "options": [
      "document.querySelector('#test')",
      "document.getElementById('test')",
      "document.querySelector('.test')",
      "Both querySelector and getElementById"
    ],
    "answer": "Both querySelector and getElementById",
    "difficulty": "Medium",
    "explanation": "Both methods select an element by ID; 'querySelector' uses CSS selector syntax."
  },
  {
    "question": "What does element.tagName return for a <div>?",
    "options": [
      "DIV",
      "div",
      "Div",
      "undefined"
    ],
    "answer": "DIV",
    "difficulty": "Medium",
    "explanation": "'tagName' returns the tag name in uppercase, so 'DIV' for a <div> element."
  },
  {
    "question": "How do you count all child nodes of an element?",
    "options": [
      "element.childNodes.length",
      "element.children.length",
      "element.nodeCount()",
      "element.getNodes()"
    ],
    "answer": "element.childNodes.length",
    "difficulty": "Medium",
    "explanation": "'childNodes.length' counts all nodes, including text and comments."
  },
  {
    "question": "How do you set an attribute on an element?",
    "options": [
      "element.setAttribute('name', 'value')",
      "element.attribute = 'value'",
      "element.name = 'value'",
      "element.setAttr('name', 'value')"
    ],
    "answer": "element.setAttribute('name', 'value')",
    "difficulty": "Medium",
    "explanation": "'setAttribute()' sets the value of a specified attribute on an element."
  },
  {
    "question": "How do you create a new <div> element?",
    "options": [
      "document.createElement('div')",
      "document.newElement('div')",
      "document.create('div')",
      "document.addElement('div')"
    ],
    "answer": "document.createElement('div')",
    "difficulty": "Medium",
    "explanation": "'createElement('div')' creates a new <div> element node."
  },
  {
    "question": "How do you insert a node after an existing node?",
    "options": [
      "parent.insertBefore(newNode, referenceNode.nextSibling)",
      "parent.appendChild(newNode)",
      "parent.insertAfter(newNode)",
      "parent.addNode(newNode)"
    ],
    "answer": "parent.insertBefore(newNode, referenceNode.nextSibling)",
    "difficulty": "Medium",
    "explanation": "'insertBefore()' with 'nextSibling' inserts a node after the reference node."
  },
  {
    "question": "What is the output of: let obj = { x: 1 }; console.log(obj.x);?",
    "options": [
      "1",
      "undefined",
      "x",
      "Error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "The 'x' property of the object is accessed using dot notation, logging 1."
  },
  {
    "question": "How do you add a property to an existing object?",
    "options": [
      "obj.newProp = 'value'",
      "obj.addProp('value')",
      "obj.set('newProp', 'value')",
      "obj.createProp('value')"
    ],
    "answer": "obj.newProp = 'value'",
    "difficulty": "Medium",
    "explanation": "Properties are added using dot notation or bracket notation, e.g., obj['newProp'] = 'value'."
  },
  {
    "question": "What does this do: let obj = { greet() { return 'Hello'; } }; console.log(obj.greet());?",
    "options": [
      "Logs 'Hello'",
      "Logs undefined",
      "Logs greet",
      "Throws an error"
    ],
    "answer": "Logs 'Hello'",
    "difficulty": "Medium",
    "explanation": "'greet' is a method that returns 'Hello' when called."
  },
  {
    "question": "What is the output of: function Person(name) { this.name = name; } let p = new Person('Alice'); console.log(p.name);?",
    "options": [
      "Alice",
      "Person",
      "undefined",
      "Error"
    ],
    "answer": "Alice",
    "difficulty": "Medium",
    "explanation": "The constructor sets the 'name' property, which is accessed as p.name."
  },
  {
    "question": "How do you add a method to a constructor’s prototype?",
    "options": [
      "Constructor.prototype.method = function() {}",
      "Constructor.method = function() {}",
      "Constructor.addMethod(function() {})",
      "Constructor.setMethod(function() {})"
    ],
    "answer": "Constructor.prototype.method = function() {}",
    "difficulty": "Medium",
    "explanation": "Methods added to the prototype are shared by all instances of the constructor."
  },
  {
    "question": "What does obj.hasOwnProperty('prop') check?",
    "options": [
      "If prop exists on obj directly",
      "If prop exists in the prototype",
      "If prop is a method",
      "If prop is undefined"
    ],
    "answer": "If prop exists on obj directly",
    "difficulty": "Medium",
    "explanation": "'hasOwnProperty()' checks if a property is defined directly on the object."
  },
  {
    "question": "What does window.location.assign('new-url') do?",
    "options": [
      "Navigates to a new URL",
      "Reloads the page",
      "Opens a new window",
      "Changes the page title"
    ],
    "answer": "Navigates to a new URL",
    "difficulty": "Medium",
    "explanation": "'location.assign()' loads a new URL in the current window."
  },
  {
    "question": "What does window.history.forward() do?",
    "options": [
      "Navigates to the next page in history",
      "Reloads the current page",
      "Opens a new tab",
      "Goes back one page"
    ],
    "answer": "Navigates to the next page in history",
    "difficulty": "Medium",
    "explanation": "'history.forward()' moves to the next page in the browser’s history."
  },
  {
    "question": "How do you set an element to full viewport height?",
    "options": [
      "element.style.height = '100vh'",
      "element.style.height = '100%'",
      "element.setHeight('full')",
      "element.style.height = '100vw'"
    ],
    "answer": "element.style.height = '100vh'",
    "difficulty": "Medium",
    "explanation": "'100vh' sets the element’s height to the full viewport height."
  },
  {
    "question": "What does window.moveTo(100, 100) do?",
    "options": [
      "Moves the window to coordinates (100, 100)",
      "Resizes the window",
      "Scrolls the window",
      "Opens a new window"
    ],
    "answer": "Moves the window to coordinates (100, 100)",
    "difficulty": "Medium",
    "explanation": "'window.moveTo()' repositions the browser window to the specified coordinates."
  },
  {
    "question": "How do you check if a popup was blocked?",
    "options": [
      "if (!window.open('url'))",
      "if (window.isBlocked())",
      "if (window.popup === null)",
      "if (document.popupBlocked)"
    ],
    "answer": "if (!window.open('url'))",
    "difficulty": "Medium",
    "explanation": "'window.open()' returns null if a popup blocker prevents the window from opening."
  },
  {
    "question": "How do you validate that a text field contains at least 3 characters?",
    "options": [
      "if (input.value.length >= 3)",
      "if (input.text.length >= 3)",
      "if (input.value >= 3)",
      "if (input.length >= 3)"
    ],
    "answer": "if (input.value.length >= 3)",
    "difficulty": "Medium",
    "explanation": "Check the 'length' of 'input.value' to ensure at least 3 characters."
  },
  {
    "question": "How do you ensure a dropdown has a valid selection?",
    "options": [
      "if (select.selectedIndex > -1)",
      "if (select.value === null)",
      "if (select.option === '')",
      "if (select.selected === false)"
    ],
    "answer": "if (select.selectedIndex > -1)",
    "difficulty": "Medium",
    "explanation": "'selectedIndex > -1' confirms a valid option is selected."
  },
  {
    "question": "How do you check if a radio button group has a selection?",
    "options": [
      "document.querySelector('input[name=group]:checked')",
      "document.getElementByName('group').checked",
      "document.querySelector('input.group:checked')",
      "document.getRadio('group').selected"
    ],
    "answer": "document.querySelector('input[name=group]:checked')",
    "difficulty": "Medium",
    "explanation": "The selector checks if any radio button in the group is checked."
  },
  {
    "question": "What regex validates a 5-digit ZIP code with optional -1234?",
    "options": [
      "/^\\d{5}(-\\d{4})?$/",
      "/^\\d{5}$/",
      "/^\\d{5}-\\d{4}$/",
      "/^\\d{9}$/"
    ],
    "answer": "/^\\d{5}(-\\d{4})?$/",
    "difficulty": "Medium",
    "explanation": "The regex allows 5 digits with an optional hyphen and 4 digits."
  },
  {
    "question": "What does try { let x = y; } catch (e) { console.log(e.name); } log?",
    "options": [
      "ReferenceError",
      "TypeError",
      "SyntaxError",
      "undefined"
    ],
    "answer": "ReferenceError",
    "difficulty": "Medium",
    "explanation": "Accessing undefined variable 'y' throws a ReferenceError, caught by the catch block."
  },
  {
    "question": "What does throw new Error('Invalid input') do?",
    "options": [
      "Throws a custom error",
      "Logs a message",
      "Stops the loop",
      "Returns a value"
    ],
    "answer": "Throws a custom error",
    "difficulty": "Medium",
    "explanation": "'throw new Error()' creates and throws a custom error with the message 'Invalid input'."
  },
  {
    "question": "How do you handle a double-click event on an element?",
    "options": [
      "element.addEventListener('dblclick', handler)",
      "element.onDoubleClick(handler)",
      "element.event('dblclick', handler)",
      "element.doubleClick(handler)"
    ],
    "answer": "element.addEventListener('dblclick', handler)",
    "difficulty": "Medium",
    "explanation": "The 'dblclick' event is handled using 'addEventListener()'."
  },
  {
    "question": "What does 'hello world'.slice(0, 5) return?",
    "options": [
      "hello",
      "world",
      "hello ",
      "he"
    ],
    "answer": "hello",
    "difficulty": "Medium",
    "explanation": "'slice(0, 5)' extracts characters from index 0 to 4, returning 'hello'."
  },
  {
    "question": "What does Math.floor(7.8) return?",
    "options": [
      "7",
      "8",
      "7.8",
      "8.0"
    ],
    "answer": "7",
    "difficulty": "Medium",
    "explanation": "'Math.floor()' rounds down to the nearest integer, so 7.8 becomes 7."
  },
  {
    "question": "What does parseFloat('12.34abc') return?",
    "options": [
      "12.34",
      "NaN",
      "12.34abc",
      "12"
    ],
    "answer": "12.34",
    "difficulty": "Medium",
    "explanation": "'parseFloat()' parses a string to a floating-point number until a non-numeric character."
  },
  {
    "question": "What does new Date().getDate() return?",
    "options": [
      "Day of the month (1-31)",
      "Day of the week (0-6)",
      "Month (0-11)",
      "Year"
    ],
    "answer": "Day of the month (1-31)",
    "difficulty": "Medium",
    "explanation": "'getDate()' returns the day of the month for a Date object."
  },
  {
    "question": "What does arr.pop() do?",
    "options": [
      "Removes and returns the last element",
      "Removes and returns the first element",
      "Adds an element to the end",
      "Reverses the array"
    ],
    "answer": "Removes and returns the last element",
    "difficulty": "Medium",
    "explanation": "'pop()' removes the last element from an array and returns it."
  },
  {
    "question": "What does document.querySelector('input[type=text]') select?",
    "options": [
      "The first text input",
      "All text inputs",
      "The first input element",
      "All elements with type=text"
    ],
    "answer": "The first text input",
    "difficulty": "Medium",
    "explanation": "'querySelector()' returns the first element matching the CSS selector."
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







