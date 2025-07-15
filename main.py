Here's the complete corrected code for your JavaScript quiz application:

```python
import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 50 questions covering all specified topics, options without a, b, c, d labels
quiz = [
    {
        "question": "How do you convert a string to lowercase and then capitalize only its first letter?\n```javascript\nlet str = 'JAVASCRIPT';\n```",
        "options": ["str.toLowerCase()[0].toUpperCase() + str.slice(1)", "str.toLowerCase().charAt(0).toUpperCase() + str.slice(1)", "str[0].toUpperCase() + str.toLowerCase().slice(1)", "str.toLowerCase().replace(str[0], str[0].toUpperCase())"],
        "answer": "str.toLowerCase().charAt(0).toUpperCase() + str.slice(1)",
        "difficulty": "Medium",
        "explanation": "Convert the string to lowercase with `toLowerCase()`, use `charAt(0)` to get the first character, capitalize it with `toUpperCase()`, and append the rest with `slice(1)`."
    },
    {
        "question": "How do you extract the last 3 characters of a string?\n```javascript\nlet str = 'JavaScript';\n```",
        "options": ["str.substring(str.length - 3)", "str.slice(-3)", "str.substr(-3)", "All of the above"],
        "answer": "All of the above",
        "difficulty": "Medium",
        "explanation": "`substring(str.length - 3)`, `slice(-3)`, and `substr(-3)` all return the last 3 characters ('ipt') of the string."
    },
    {
        "question": "How do you find the index of the first occurrence of 'Script' in a string?\n```javascript\nlet str = 'JavaScript is fun';\n```",
        "options": ["str.find('Script')", "str.indexOf('Script')", "str.search('Script')", "Both str.indexOf('Script') and str.search('Script')"],
        "answer": "Both str.indexOf('Script') and str.search('Script')",
        "difficulty": "Medium",
        "explanation": "`indexOf()` and `search()` both return the starting index (4) of 'Script'. `search()` can also use regex."
    },
    {
        "question": "How do you safely access the character at index 10 of a string that may be shorter?\n```javascript\nlet str = 'JavaScript';\n```",
        "options": ["str[10] || ''", "str.charAt(10)", "str.at(10) || ''", "Both str[10] || '' and str.at(10) || ''"],
        "answer": "Both str[10] || '' and str.at(10) || ''",
        "difficulty": "Medium",
        "explanation": "`str[10]` returns `undefined` if out of bounds, and `at(10)` returns `undefined`, so both can be safely handled with a fallback like `|| ''`. `charAt(10)` returns an empty string."
    },
    {
        "question": "How do you replace only the first 'a' with 'b' in a string case-insensitively?\n```javascript\nlet str = 'JavaScript';\n```",
        "options": ["str.replace('a', 'b')", "str.replace(/a/i, 'b')", "str.replaceAll('a', 'b')", "str.replace(/a/, 'b')"],
        "answer": "str.replace(/a/i, 'b')",
        "difficulty": "Medium",
        "explanation": "`replace(/a/i, 'b')` uses a regex with the `i` flag to replace the first 'a' or 'A' with 'b'."
    },
    {
        "question": "How do you round 3.14159 to the nearest tenth?",
        "options": ["Math.round(3.14159 * 10) / 10", "Math.floor(3.14159 * 10) / 10", "Math.ceil(3.14159 * 10) / 10", "Math.trunc(3.14159 * 10) / 10"],
        "answer": "Math.round(3.14159 * 10) / 10",
        "difficulty": "Medium",
        "explanation": "Multiply by 10, use `Math.round()` to round to the nearest integer, then divide by 10 to get 3.1."
    },
    {
        "question": "How do you generate a random integer between 1 and 10?",
        "options": ["Math.random() * 10", "Math.floor(Math.random() * 10) + 1", "Math.ceil(Math.random() * 10)", "Math.round(Math.random() * 10)"],
        "answer": "Math.floor(Math.random() * 10) + 1",
        "difficulty": "Medium",
        "explanation": "`Math.random() * 10` gives a number from 0 to <10, `Math.floor()` makes it an integer (0-9), and `+ 1` shifts it to 1-10."
    },
    {
        "question": "How do you convert '123.45' to a number with integer and decimal parts?",
        "options": ["parseInt('123.45')", "parseFloat('123.45')", "Number('123.45')", "Both parseFloat('123.45') and Number('123.45')"],
        "answer": "Both parseFloat('123.45') and Number('123.45')",
        "difficulty": "Medium",
        "explanation": "Both `parseFloat('123.45')` and `Number('123.45')` return 123.45, preserving the decimal part."
    },
    {
        "question": "How do you convert a number to a string with a leading zero if less than 10?\n```javascript\nlet num = 5;\n```",
        "options": ["num.toString().padStart(2, '0')", "num.toString(2)", "String(num).padEnd(2, '0')", "num + '0'"],
        "answer": "num.toString().padStart(2, '0')",
        "difficulty": "Medium",
        "explanation": "`padStart(2, '0')` adds a leading zero to make the string '05' if the number is single-digit."
    },
    {
        "question": "How do you format a number to exactly 3 decimal places as a number?\n```javascript\nlet num = 3.14159;\n```",
        "options": ["Number(num.toFixed(3))", "num.toPrecision(3)", "Math.round(num * 1000) / 1000", "Both Number(num.toFixed(3)) and Math.round(num * 1000) / 1000"],
        "answer": "Both Number(num.toFixed(3)) and Math.round(num * 1000) / 1000",
        "difficulty": "Medium",
        "explanation": "`toFixed(3)` returns a string with 3 decimals, converted back with `Number()`. `Math.round(num * 1000) / 1000` achieves the same numerically."
    },
    {
        "question": "How do you get the current date in 'YYYY-MM-DD' format?",
        "options": ["new Date().toISOString().split('T')[0]", "new Date().toDateString()", "new Date().format('YYYY-MM-DD')", "new Date().getDate()"],
        "answer": "new Date().toISOString().split('T')[0]",
        "difficulty": "Medium",
        "explanation": "`toISOString()` returns a string like '2025-07-14T...', and `split('T')[0]` extracts '2025-07-14'."
    },
    {
        "question": "How do you extract the day of the week from a Date object?\n```javascript\nlet date = new Date('2025-07-14');\n```",
        "options": ["date.getDay()", "date.getDate()", "date.getWeekday()", "date.day()"],
        "answer": "date.getDay()",
        "difficulty": "Medium",
        "explanation": "`getDay()` returns the day of the week (0-6, Sunday to Saturday)."
    },
    {
        "question": "How do you create a Date object for 2025-12-31 at 23:59:59?",
        "options": ["new Date('2025-12-31 23:59:59')", "new Date(2025, 11, 31, 23, 59, 59)", "new Date(2025, 12, 31, 23, 59, 59)", "Both new Date('2025-12-31 23:59:59') and new Date(2025, 11, 31, 23, 59, 59)"],
        "answer": "Both new Date('2025-12-31 23:59:59') and new Date(2025, 11, 31, 23, 59, 59)",
        "difficulty": "Medium",
        "explanation": "Both the string format and the constructor with 0-based month (11 for December) work."
    },
    {
        "question": "How do you add one month to a Date object?\n```javascript\nlet date = new Date('2025-07-14');\n```",
        "options": ["date.setMonth(date.getMonth() + 1)", "date.addMonth(1)", "date.setMonth(1)", "date.month += 1"],
        "answer": "date.setMonth(date.getMonth() + 1)",
        "difficulty": "Medium",
        "explanation": "`setMonth()` with `getMonth() + 1` increments the month, handling year rollovers."
    },
    {
        "question": "How do you write a function that accepts variable arguments?\n```javascript\nfunction sum(...numbers) {}\n```",
        "options": ["Use the rest parameter syntax", "Use arguments object", "Both Use the rest parameter syntax and Use arguments object", "Use a fixed parameter list"],
        "answer": "Both Use the rest parameter syntax and Use arguments object",
        "difficulty": "Medium",
        "explanation": "The rest parameter (`...numbers`) or the `arguments` object can handle variable arguments."
    },
    {
        "question": "How do you pass an object as a parameter and access its properties?\n```javascript\nfunction process({name}) {}\n```",
        "options": ["process({name: 'John'})", "process('John')", "process.name('John')", "process({name: 'John'}.name)"],
        "answer": "process({name: 'John'})",
        "difficulty": "Medium",
        "explanation": "Destructuring in the parameter allows direct access to the `name` property of the passed object."
    },
    {
        "question": "How do you return multiple values from a function?",
        "options": ["return [val1, val2]", "return {val1, val2}", "return val1, val2", "Both return [val1, val2] and return {val1, val2}"],
        "answer": "Both return [val1, val2] and return {val1, val2}",
        "difficulty": "Medium",
        "explanation": "Returning an array or object allows multiple values to be returned and destructured by the caller."
    },
    {
        "question": "How do you avoid global variable conflicts in a function?\n```javascript\nlet x = 10;\nfunction myFunc() {\n  let x = 20;\n}\n```",
        "options": ["Use `let` or `const` inside the function", "Use `var` globally", "Avoid naming variables", "Use globalThis.x"],
        "answer": "Use `let` or `const` inside the function",
        "difficulty": "Medium",
        "explanation": "Declaring variables with `let` or `const` inside a function creates local scope, avoiding global conflicts."
    },
    {
        "question": "How do you structure a switch statement to handle multiple cases?\n```javascript\nlet value = 2;\nswitch(value) {}\n```",
        "options": ["switch(value) { case 1: case 2: return 'Low'; }", "switch(value) { case 1, 2: return 'Low'; }", "switch(value) { case 1 || 2: return 'Low'; }", "switch(value) { case [1, 2]: return 'Low'; }"],
        "answer": "switch(value) { case 1: case 2: return 'Low'; }",
        "difficulty": "Medium",
        "explanation": "Multiple cases can share the same block by listing them sequentially without breaks."
    },
    {
        "question": "How do you ensure a switch statement handles an unexpected value?\n```javascript\nswitch(value) {}\n```",
        "options": ["Add a default case", "Add a break statement", "Use a try-catch", "Add an else clause"],
        "answer": "Add a default case",
        "difficulty": "Medium",
        "explanation": "A `default` case handles values not matched by any `case`."
    },
    {
        "question": "How do you prevent an infinite while loop?\n```javascript\nlet i = 0;\nwhile (i < 5) {}\n```",
        "options": ["Increment i inside the loop", "Use break", "Both Increment i inside the loop and Use break", "Set i outside the loop"],
        "answer": "Both Increment i inside the loop and Use break",
        "difficulty": "Medium",
        "explanation": "Incrementing the loop variable (`i++`) or using `break` ensures the condition eventually becomes false."
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
        "question": "How do you write a multi-line comment that explains a function's purpose?",
        "options": ["/* Comment */", "// Comment", "# Comment", "<!-- Comment -->"],
        "answer": "/* Comment */",
        "difficulty": "Medium",
        "explanation": "Multi-line comments use `/* */` to document code, such as a function's purpose."
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
        "question": "How do you validate an input field's value before reading it?\n```javascript\nlet input = document.querySelector('input');\n```",
        "options": ["if (input.value)", "if (input.value !== '')", "if (input.checkValidity())", "Both if (input.value !== '') and if (input.checkValidity())"],
        "answer": "Both if (input.value !== '') and if (input.checkValidity())",
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
        "question": "How do you update a paragraph's HTML content safely?\n```javascript\nlet p = document.querySelector('p');\n```",
        "options": ["p.innerHTML = '<b>Text</b>'", "p.textContent = '<b>Text</b>'", "p.innerText = '<b>Text</b>'", "p.setHTML('<b>Text</b>')"],
        "answer": "p.innerHTML = '<b>Text</b>'",
        "difficulty": "Medium",
        "explanation": "`innerHTML` sets HTML content, but use with caution to avoid XSS; `textContent` escapes HTML."
    },
    {
        "question": "How do you toggle an image's visibility using styles?\n```javascript\nlet img = document.querySelector('img');\n```",
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
        "question": "How do you filter out non-element nodes from a node's children?\n```javascript\nlet parent = document.querySelector('div');\n```",
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
        "question": "How do you get the value of an element's attribute?\n```javascript\nlet el = document.querySelector('input');\n```",
        "options": ["el.getAttribute('value')", "el.attributes.value", "el.value", "Both el.getAttribute('value') and el.value"],
        "answer": "Both el.getAttribute('value') and el.value",
        "difficulty": "Medium",
        "explanation": "`getAttribute('value')` gets the attribute value; `value` directly accesses the input's current value."
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
        "question": "How do you add a method to a constructor's prototype?\n```javascript\nfunction Person() {}\n```",
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
