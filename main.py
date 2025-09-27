
import streamlit as st
import random
from datetime import datetime
import uuid






quiz = [
  {
    "question": "What is the output of: `function test() { var x = 1; if (true) { var x = 2; } return x; } console.log(test());`?",
    "options": [
      "2",
      "1",
      "undefined",
      "ReferenceError"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "'var' is function-scoped, so the inner 'var x = 2' reassigns the same variable, returning 2."
  },
  {
    "question": "What does this code output: `let x = 10; { let x = 20; } console.log(x);`?",
    "options": [
      "10",
      "20",
      "undefined",
      "Error"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "'let' is block-scoped, so the inner 'let x = 20' doesn’t affect the outer x, logging 10."
  },
  {
    "question": "What is the output of: `function scope() { let x = 5; if (true) { x = 15; } return x; } console.log(scope());`?",
    "options": [
      "15",
      "5",
      "undefined",
      "Error"
    ],
    "answer": "15",
    "difficulty": "Medium",
    "explanation": "Without a new 'let' in the if block, 'x = 15' reassigns the outer x, returning 15."
  },
  {
    "question": "What happens in: `function test() { console.log(x); var x = 1; } test();`?",
    "options": [
      "Logs undefined",
      "Logs 1",
      "ReferenceError",
      "TypeError"
    ],
    "answer": "Logs undefined",
    "difficulty": "Medium",
    "explanation": "Due to hoisting, 'var x' is declared but not initialized when logged, so it’s undefined."
  },
  {
    "question": "What is the output of: `const x = 10; { const x = 20; } console.log(x);`?",
    "options": [
      "10",
      "20",
      "undefined",
      "Error"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "'const' is block-scoped, so the inner 'const x = 20' doesn’t affect the outer x."
  },
  {
    "question": "How do you validate a text field for non-empty input?",
    "options": [
      "if (document.getElementById('input').value.trim() !== '')",
      "if (document.getElementById('input').value === null)",
      "if (document.getElementById('input').length > 0)",
      "if (document.getElementById('input').text !== '')"
    ],
    "answer": "if (document.getElementById('input').value.trim() !== '')",
    "difficulty": "Medium",
    "explanation": "'trim()' removes whitespace, and checking '!== ''' ensures the field isn’t empty."
  },
  {
    "question": "What does this code do: `let input = document.getElementById('text'); if (input.value.length >= 5) console.log('Valid');`?",
    "options": [
      "Logs 'Valid' if text input has 5+ characters",
      "Logs 'Valid' if input is empty",
      "Throws an error",
      "Logs the input value"
    ],
    "answer": "Logs 'Valid' if text input has 5+ characters",
    "difficulty": "Medium",
    "explanation": "Checks if the input’s value length is at least 5, logging 'Valid' if true."
  },
  {
    "question": "How do you check if a dropdown has a selected option?",
    "options": [
      "if (document.getElementById('dropdown').selectedIndex > -1)",
      "if (document.getElementById('dropdown').value === null)",
      "if (document.getElementById('dropdown').option !== '')",
      "if (document.getElementById('dropdown').selected === true)"
    ],
    "answer": "if (document.getElementById('dropdown').selectedIndex > -1)",
    "difficulty": "Medium",
    "explanation": "'selectedIndex > -1' confirms an option is selected in the dropdown."
  },
  {
    "question": "What does this code do: `let select = document.getElementById('dropdown'); if (select.value !== '') console.log('Selected');`?",
    "options": [
      "Logs 'Selected' if dropdown has a non-empty value",
      "Logs the dropdown’s value",
      "Sets the dropdown’s value",
      "Throws an error"
    ],
    "answer": "Logs 'Selected' if dropdown has a non-empty value",
    "difficulty": "Medium",
    "explanation": "Checks if the dropdown’s value is non-empty, logging 'Selected' if true."
  },
  {
    "question": "How do you validate a radio button group selection?",
    "options": [
      "if (document.querySelector('input[name=group]:checked'))",
      "if (document.getElementsByName('group').checked)",
      "if (document.querySelector('input.group').value)",
      "if (document.getRadio('group').selected)"
    ],
    "answer": "if (document.querySelector('input[name=group]:checked'))",
    "difficulty": "Medium",
    "explanation": "The selector returns the checked radio button or null if none is selected."
  },
  {
    "question": "What does this code do: `let radio = document.querySelector('input[name=group]:checked'); console.log(radio ? radio.value : 'None');`?",
    "options": [
      "Logs the checked radio’s value or 'None'",
      "Logs 'None' always",
      "Sets the radio’s value",
      "Throws an error"
    ],
    "answer": "Logs the checked radio’s value or 'None'",
    "difficulty": "Medium",
    "explanation": "If a radio is checked, its value is logged; otherwise, 'None' is logged."
  },
  {
    "question": "What regex validates a 5-digit ZIP code?",
    "options": [
      "/^\\d{5}$/",
      "/^\\d{5}-\\d{4}$/",
      "/^\\d{9}$/",
      "/^\\d{5}(-\\d{4})?$/"
    ],
    "answer": "/^\\d{5}$/",
    "difficulty": "Medium",
    "explanation": "'/^\\d{5}$/' ensures exactly 5 digits, suitable for a basic ZIP code."
  },
  {
    "question": "What does this code do: `let zip = document.getElementById('zip').value; if (/^\\d{5}$/.test(zip)) console.log('Valid ZIP');`?",
    "options": [
      "Logs 'Valid ZIP' for a 5-digit ZIP code",
      "Logs the ZIP code value",
      "Sets the ZIP code value",
      "Throws an error"
    ],
    "answer": "Logs 'Valid ZIP' for a 5-digit ZIP code",
    "difficulty": "Medium",
    "explanation": "The regex tests for exactly 5 digits, logging 'Valid ZIP' if matched."
  },
  {
    "question": "What regex validates an email address?",
    "options": [
      "/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/",
      "/^\\w+@\\w+\\.com$/",
      "/^[^\\s@]+@[^\\s@]+$/",
      "/^\\w+\\.\\w+@\\w+$/"
    ],
    "answer": "/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/",
    "difficulty": "Medium",
    "explanation": "This regex ensures a valid email format with username, @, domain, and top-level domain."
  },
  {
    "question": "What does this code do: `let email = document.getElementById('email').value; if (/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) console.log('Valid');`?",
    "options": [
      "Logs 'Valid' for a valid email format",
      "Logs the email value",
      "Sets the email value",
      "Throws an error"
    ],
    "answer": "Logs 'Valid' for a valid email format",
    "difficulty": "Medium",
    "explanation": "The regex validates the email format, logging 'Valid' if it matches."
  },
  {
    "question": "What is the output of: `try { let x = undefined.x; } catch (e) { console.log(e.name); }`?",
    "options": [
      "TypeError",
      "ReferenceError",
      "SyntaxError",
      "undefined"
    ],
    "answer": "TypeError",
    "difficulty": "Medium",
    "explanation": "Accessing a property on undefined throws a TypeError, caught and logged."
  },
  {
    "question": "What does this code do: `try { throw new Error('Invalid'); } catch (e) { console.log(e.message); }`?",
    "options": [
      "Logs 'Invalid'",
      "Logs 'Error'",
      "Throws an error",
      "Logs undefined"
    ],
    "answer": "Logs 'Invalid'",
    "difficulty": "Medium",
    "explanation": "The thrown error’s message is caught and logged as 'Invalid'."
  },
  {
    "question": "What does this code do: `document.getElementById('btn').addEventListener('click', () => console.log('Clicked'));`?",
    "options": [
      "Logs 'Clicked' on button click",
      "Changes button text",
      "Disables the button",
      "Redirects the page"
    ],
    "answer": "Logs 'Clicked' on button click",
    "difficulty": "Medium",
    "explanation": "'addEventListener()' binds a handler to the button’s click event."
  },
  {
    "question": "What is the output of: `let node = document.createTextNode('test'); console.log(node.nodeType);`?",
    "options": [
      "3",
      "1",
      "8",
      "9"
    ],
    "answer": "3",
    "difficulty": "Medium",
    "explanation": "A text node has a 'nodeType' of 3 in the DOM."
  },
  {
    "question": "How do you select all elements with class 'test'?",
    "options": [
      "document.querySelectorAll('.test')",
      "document.getElementById('test')",
      "document.querySelector('test')",
      "document.getElementsByTagName('test')"
    ],
    "answer": "document.querySelectorAll('.test')",
    "difficulty": "Medium",
    "explanation": "'querySelectorAll()' uses CSS selector syntax to select all elements with class 'test'."
  },
  {
    "question": "What is the output of: `let div = document.createElement('div'); console.log(div.tagName);`?",
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
    "question": "What does this code do: `let div = document.createElement('div'); div.innerHTML = '<p>1</p><p>2</p>'; console.log(div.children.length);`?",
    "options": [
      "Logs 2",
      "Logs 1",
      "Logs 0",
      "Throws an error"
    ],
    "answer": "Logs 2",
    "difficulty": "Medium",
    "explanation": "'children.length' counts the two <p> elements, excluding text nodes."
  },
  {
    "question": "What does this code do: `let img = document.createElement('img'); img.setAttribute('src', 'image.jpg'); console.log(img.getAttribute('src'));`?",
    "options": [
      "Logs 'image.jpg'",
      "Logs undefined",
      "Logs 'img'",
      "Throws an error"
    ],
    "answer": "Logs 'image.jpg'",
    "difficulty": "Medium",
    "explanation": "'setAttribute()' sets the 'src', and 'getAttribute()' retrieves it."
  },
  {
    "question": "How do you check if an element has an attribute?",
    "options": [
      "element.hasAttribute('name')",
      "element.getAttribute('name')",
      "element.attribute('name')",
      "element.checkAttribute('name')"
    ],
    "answer": "element.hasAttribute('name')",
    "difficulty": "Medium",
    "explanation": "'hasAttribute()' returns true if the element has the specified attribute."
  },
  {
    "question": "What does this code do: `let elem = document.createElement('span'); document.body.appendChild(elem);`?",
    "options": [
      "Appends a new span to the body",
      "Replaces the body with a span",
      "Creates a span without adding it",
      "Throws an error"
    ],
    "answer": "Appends a new span to the body",
    "difficulty": "Medium",
    "explanation": "'appendChild()' adds the new span as the last child of the body."
  },
  {
    "question": "What does this code do: `let p = document.createElement('p'); document.querySelector('#target').parentNode.insertBefore(p, document.querySelector('#target'));`?",
    "options": [
      "Inserts a new <p> before #target",
      "Inserts a new <p> after #target",
      "Replaces #target with a <p>",
      "Appends a <p> to #target"
    ],
    "answer": "Inserts a new <p> before #target",
    "difficulty": "Medium",
    "explanation": "'insertBefore()' adds the new node before the specified reference node."
  },
  {
    "question": "What is the output of: `let obj = { x: 5 }; console.log(obj.x);`?",
    "options": [
      "5",
      "undefined",
      "x",
      "Error"
    ],
    "answer": "5",
    "difficulty": "Medium",
    "explanation": "The 'x' property is accessed using dot notation, logging its value, 5."
  },
  {
    "question": "What does this code do: `let obj = {}; obj.newProp = 42; console.log(obj.newProp);`?",
    "options": [
      "Logs 42",
      "Logs undefined",
      "Logs 'newProp'",
      "Throws an error"
    ],
    "answer": "Logs 42",
    "difficulty": "Medium",
    "explanation": "Adding 'newProp' to the object and accessing it logs its value, 42."
  },
  {
    "question": "What is the output of: `let obj = { calc: function() { return 2 * 2; } }; console.log(obj.calc());`?",
    "options": [
      "4",
      "undefined",
      "calc",
      "Error"
    ],
    "answer": "4",
    "difficulty": "Medium",
    "explanation": "The 'calc' method returns the result of 2 * 2, which is 4."
  },
  {
    "question": "What does this code do: `function Person(name) { this.name = name; } let p = new Person('Alice'); console.log(p.name);`?",
    "options": [
      "Logs 'Alice'",
      "Logs 'Person'",
      "Logs undefined",
      "Throws an error"
    ],
    "answer": "Logs 'Alice'",
    "difficulty": "Medium",
    "explanation": "The constructor sets the 'name' property, accessed as p.name."
  },
  {
    "question": "What does this code do: `function Car() { } Car.prototype.drive = function() { return 'Driving'; }; let c = new Car(); console.log(c.drive());`?",
    "options": [
      "Logs 'Driving'",
      "Logs undefined",
      "Logs 'Car'",
      "Throws an error"
    ],
    "answer": "Logs 'Driving'",
    "difficulty": "Medium",
    "explanation": "The 'drive' method on the prototype returns 'Driving' for the instance."
  },
  {
    "question": "What is the output of: `let obj = { x: 1 }; console.log(obj.hasOwnProperty('x'));`?",
    "options": [
      "true",
      "false",
      "undefined",
      "Error"
    ],
    "answer": "true",
    "difficulty": "Medium",
    "explanation": "'hasOwnProperty()' returns true if 'x' is a direct property of the object."
  },
  {
    "question": "What does this code do: `window.location.href = 'https://example.com';`?",
    "options": [
      "Navigates to https://example.com",
      "Reloads the current page",
      "Opens a new tab",
      "Changes the page title"
    ],
    "answer": "Navigates to https://example.com",
    "difficulty": "Medium",
    "explanation": "Setting 'location.href' navigates to the specified URL."
  },
  {
    "question": "What does this code do: `window.location.assign('https://example.com');`?",
    "options": [
      "Navigates to https://example.com",
      "Reloads the current page",
      "Opens a new tab",
      "Changes the page title"
    ],
    "answer": "Navigates to https://example.com",
    "difficulty": "Medium",
    "explanation": "'location.assign()' loads a new URL in the current window."
  },
  {
    "question": "What does this code do: `window.history.back();`?",
    "options": [
      "Navigates to the previous page",
      "Navigates to the next page",
      "Reloads the page",
      "Opens a new tab"
    ],
    "answer": "Navigates to the previous page",
    "difficulty": "Medium",
    "explanation": "'history.back()' moves to the previous page in the browser’s history."
  },
  {
    "question": "What does this code do: `document.body.style.height = '100vh';`?",
    "options": [
      "Sets body height to full viewport height",
      "Sets body width to full viewport",
      "Hides the body",
      "Scrolls the body"
    ],
    "answer": "Sets body height to full viewport height",
    "difficulty": "Medium",
    "explanation": "'100vh' sets the body’s height to the full viewport height."
  },
  {
    "question": "What does this code do: `window.resizeTo(800, 600);`?",
    "options": [
      "Resizes the window to 800x600 pixels",
      "Moves the window to (800, 600)",
      "Scrolls the window",
      "Sets the viewport size"
    ],
    "answer": "Resizes the window to 800x600 pixels",
    "difficulty": "Medium",
    "explanation": "'window.resizeTo()' sets the browser window’s dimensions."
  },
  {
    "question": "What does this code do: `let win = window.open(''); if (!win) console.log('Blocked');`?",
    "options": [
      "Logs 'Blocked' if popup is blocked",
      "Opens a new window",
      "Logs 'Blocked' always",
      "Throws an error"
    ],
    "answer": "Logs 'Blocked' if popup is blocked",
    "difficulty": "Medium",
    "explanation": "'window.open()' returns null if a popup blocker prevents the window."
  },
  {
    "question": "What does this code do: `let input = document.getElementById('text'); if (/^[a-zA-Z]+$/.test(input.value)) console.log('Alphabetic');`?",
    "options": [
      "Logs 'Alphabetic' if input is letters only",
      "Logs the input value",
      "Sets the input value",
      "Throws an error"
    ],
    "answer": "Logs 'Alphabetic' if input is letters only",
    "difficulty": "Medium",
    "explanation": "The regex '/^[a-zA-Z]+$/' checks for alphabetic characters, logging if matched."
  },
  {
    "question": "What is the output of: `function test() { console.log(x); let x = 1; } test();`?",
    "options": [
      "ReferenceError",
      "undefined",
      "1",
      "null"
    ],
    "answer": "ReferenceError",
    "difficulty": "Medium",
    "explanation": "'let x' is in the temporal dead zone until declared, causing a ReferenceError."
  },
  {
    "question": "What does this code do: `let select = document.getElementById('dropdown'); if (select.options[select.selectedIndex].value !== 'default') console.log('Valid');`?",
    "options": [
      "Logs 'Valid' if dropdown value isn’t 'default'",
      "Sets dropdown value",
      "Logs the selected index",
      "Throws an error"
    ],
    "answer": "Logs 'Valid' if dropdown value isn’t 'default'",
    "difficulty": "Medium",
    "explanation": "Checks if the selected option’s value isn’t 'default', logging 'Valid'."
  },
  {
    "question": "What does this code do: `let radios = document.querySelectorAll('input[name=group]'); radios.forEach(r => r.checked = false);`?",
    "options": [
      "Unchecks all radio buttons in the group",
      "Checks all radio buttons",
      "Gets radio values",
      "Removes radio buttons"
    ],
    "answer": "Unchecks all radio buttons in the group",
    "difficulty": "Medium",
    "explanation": "Loops through radio buttons, setting 'checked' to false."
  },
  {
    "question": "What does this code do: `let zip = document.getElementById('zip').value; if (/^\\d{5}(-\\d{4})?$/.test(zip)) console.log('Valid');`?",
    "options": [
      "Logs 'Valid' for 5-digit or 5+4 ZIP code",
      "Logs the ZIP value",
      "Sets the ZIP value",
      "Throws an error"
    ],
    "answer": "Logs 'Valid' for 5-digit or 5+4 ZIP code",
    "difficulty": "Medium",
    "explanation": "The regex matches 5 digits or 5+4 digits with a hyphen, logging 'Valid'."
  },
  {
    "question": "What is the output of: `try { JSON.parse('invalid'); } catch (e) { console.log(e.name); }`?",
    "options": [
      "SyntaxError",
      "TypeError",
      "ReferenceError",
      "undefined"
    ],
    "answer": "SyntaxError",
    "difficulty": "Medium",
    "explanation": "Invalid JSON in 'JSON.parse()' throws a SyntaxError, caught and logged."
  },
  {
    "question": "What does this code do: `try { throw 'Custom error'; } catch (e) { console.log(e); }`?",
    "options": [
      "Logs 'Custom error'",
      "Logs undefined",
      "Throws an error",
      "Logs 'Error'"
    ],
    "answer": "Logs 'Custom error'",
    "difficulty": "Medium",
    "explanation": "'throw' throws a string, which is caught and logged."
  },
  {
    "question": "What does this code do: `document.getElementById('input').addEventListener('keypress', () => console.log('Key pressed'));`?",
    "options": [
      "Logs 'Key pressed' on keypress",
      "Logs the key value",
      "Clears the input",
      "Triggers a click event"
    ],
    "answer": "Logs 'Key pressed' on keypress",
    "difficulty": "Medium",
    "explanation": "'addEventListener()' binds a handler to the 'keypress' event."
  },
  {
    "question": "What is the output of: `let comment = document.createComment('test'); console.log(comment.nodeType);`?",
    "options": [
      "8",
      "1",
      "3",
      "9"
    ],
    "answer": "8",
    "difficulty": "Medium",
    "explanation": "A comment node has a 'nodeType' of 8 in the DOM."
  },
  {
    "question": "What does this code do: `let elements = document.querySelectorAll('[data-test]'); console.log(elements.length);`?",
    "options": [
      "Logs the number of elements with data-test attribute",
      "Logs the data-test values",
      "Selects one element",
      "Throws an error"
    ],
    "answer": "Logs the number of elements with data-test attribute",
    "difficulty": "Medium",
    "explanation": "'querySelectorAll()' selects elements with 'data-test', and 'length' counts them."
  },
  {
    "question": "What does this code do: `let p = document.createElement('p'); console.log(p.tagName);`?",
    "options": [
      "Logs 'P'",
      "Logs 'p'",
      "Logs undefined",
      "Throws an error"
    ],
    "answer": "Logs 'P'",
    "difficulty": "Medium",
    "explanation": "'tagName' returns the tag name in uppercase, so 'P' for a <p> element."
  },
  {
    "question": "What does this code do: `let div = document.createElement('div'); div.innerHTML = 'Text'; console.log(div.childNodes.length);`?",
    "options": [
      "Logs 1",
      "Logs 0",
      "Logs 2",
      "Throws an error"
    ],
    "answer": "Logs 1",
    "difficulty": "Medium",
    "explanation": "'childNodes.length' counts the text node created by 'Text'."
  },
  {
    "question": "What does this code do: `let elem = document.createElement('div'); elem.setAttribute('id', 'box'); console.log(elem.id);`?",
    "options": [
      "Logs 'box'",
      "Logs undefined",
      "Logs 'div'",
      "Throws an error"
    ],
    "answer": "Logs 'box'",
    "difficulty": "Medium",
    "explanation": "'setAttribute()' sets the 'id', and the 'id' property retrieves it."
  },
  {
    "question": "What does this code do: `let elem = document.createElement('img'); elem.removeAttribute('src'); console.log(elem.hasAttribute('src'));`?",
    "options": [
      "Logs false",
      "Logs true",
      "Logs undefined",
      "Throws an error"
    ],
    "answer": "Logs false",
    "difficulty": "Medium",
    "explanation": "'removeAttribute()' removes the 'src', so 'hasAttribute()' returns false."
  },
  {
    "question": "What does this code do: `let div = document.createElement('div'); div.textContent = 'Hello'; document.body.appendChild(div);`?",
    "options": [
      "Appends a div with 'Hello' to the body",
      "Replaces the body",
      "Creates a div without adding it",
      "Throws an error"
    ],
    "answer": "Appends a div with 'Hello' to the body",
    "difficulty": "Medium",
    "explanation": "'textContent' sets the text, and 'appendChild()' adds the div."
  },
  {
    "question": "What does this code do: `let p = document.createElement('p'); let target = document.querySelector('#target'); target.parentNode.insertBefore(p, target.nextSibling);`?",
    "options": [
      "Inserts a new <p> after #target",
      "Inserts a new <p> before #target",
      "Replaces #target",
      "Appends a <p> to #target"
    ],
    "answer": "Inserts a new <p> after #target",
    "difficulty": "Medium",
    "explanation": "'insertBefore()' with 'nextSibling' inserts the <p> after #target."
  },
  {
    "question": "What does this code do: `let obj = { a: 1, b: 2 }; console.log(obj['b']);`?",
    "options": [
      "Logs 2",
      "Logs 'b'",
      "Logs undefined",
      "Throws an error"
    ],
    "answer": "Logs 2",
    "difficulty": "Medium",
    "explanation": "Bracket notation accesses the 'b' property, logging its value, 2."
  },
  {
    "question": "What does this code do: `let obj = { x: 10 }; obj.x = 20; console.log(obj.x);`?",
    "options": [
      "Logs 20",
      "Logs 10",
      "Logs undefined",
      "Throws an error"
    ],
    "answer": "Logs 20",
    "difficulty": "Medium",
    "explanation": "Reassigning 'obj.x' updates the property, logging 20."
  },
  {
    "question": "What does this code do: `let obj = { greet() { return 'Hi'; } }; console.log(obj.greet());`?",
    "options": [
      "Logs 'Hi'",
      "Logs undefined",
      "Logs 'greet'",
      "Throws an error"
    ],
    "answer": "Logs 'Hi'",
    "difficulty": "Medium",
    "explanation": "The 'greet' method returns 'Hi' when called."
  },
  {
    "question": "What does this code do: `function User(name) { this.name = name; } let u = new User('Bob'); console.log(u.name);`?",
    "options": [
      "Logs 'Bob'",
      "Logs 'User'",
      "Logs undefined",
      "Throws an error"
    ],
    "answer": "Logs 'Bob'",
    "difficulty": "Medium",
    "explanation": "The constructor sets 'name', accessed as u.name."
  },
  {
    "question": "What does this code do: `function Animal() { } Animal.prototype.speak = function() { return 'Woof'; }; let a = new Animal(); console.log(a.speak());`?",
    "options": [
      "Logs 'Woof'",
      "Logs undefined",
      "Logs 'Animal'",
      "Throws an error"
    ],
    "answer": "Logs 'Woof'",
    "difficulty": "Medium",
    "explanation": "The 'speak' method on the prototype returns 'Woof'."
  },
  {
    "question": "What does this code do: `let obj = { x: 1 }; console.log('x' in obj);`?",
    "options": [
      "Logs true",
      "Logs false",
      "Logs undefined",
      "Throws an error"
    ],
    "answer": "Logs true",
    "difficulty": "Medium",
    "explanation": "The 'in' operator returns true if 'x' exists in the object."
  },
  {
    "question": "What does this code do: `console.log(window.location.search);`?",
    "options": [
      "Logs the URL’s query string",
      "Logs the full URL",
      "Logs the domain",
      "Logs the path"
    ],
    "answer": "Logs the URL’s query string",
    "difficulty": "Medium",
    "explanation": "'location.search' returns the query string, starting with '?'."
  },
  {
    "question": "What does this code do: `window.location.replace('https://example.com');`?",
    "options": [
      "Navigates to https://example.com without history",
      "Adds to history",
      "Reloads the page",
      "Opens a new tab"
    ],
    "answer": "Navigates to https://example.com without history",
    "difficulty": "Medium",
    "explanation": "'location.replace()' navigates without adding to browser history."
  },
  {
    "question": "What does this code do: `window.history.forward();`?",
    "options": [
      "Navigates to the next page",
      "Navigates to the previous page",
      "Reloads the page",
      "Opens a new tab"
    ],
    "answer": "Navigates to the next page",
    "difficulty": "Medium",
    "explanation": "'history.forward()' moves to the next page in the browser’s history."
  },
  {
    "question": "What does this code do: `document.documentElement.style.width = '100vw';`?",
    "options": [
      "Sets html element width to full viewport",
      "Sets height to full viewport",
      "Hides the html element",
      "Scrolls the page"
    ],
    "answer": "Sets html element width to full viewport",
    "difficulty": "Medium",
    "explanation": "'100vw' sets the html element’s width to the full viewport."
  },
  {
    "question": "What does this code do: `window.moveTo(100, 100);`?",
    "options": [
      "Moves the window to (100, 100)",
      "Resizes the window",
      "Scrolls the window",
      "Opens a new window"
    ],
    "answer": "Moves the window to (100, 100)",
    "difficulty": "Medium",
    "explanation": "'window.moveTo()' repositions the browser window to the coordinates."
  },
  {
    "question": "What does this code do: `let input = document.getElementById('text'); if (input.value.length <= 10) console.log('Valid length');`?",
    "options": [
      "Logs 'Valid length' if input is 10 or fewer characters",
      "Logs the input value",
      "Sets the input value",
      "Throws an error"
    ],
    "answer": "Logs 'Valid length' if input is 10 or fewer characters",
    "difficulty": "Medium",
    "explanation": "Checks if the input’s length is <= 10, logging 'Valid length'."
  },
  {
    "question": "What is the output of: `function test() { let x = 1; { let x = 2; { let x = 3; } } return x; } console.log(test());`?",
    "options": [
      "1",
      "2",
      "3",
      "Error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "Each 'let x' is block-scoped; the outermost x remains 1."
  },
  {
    "question": "What does this code do: `let select = document.getElementById('dropdown'); if (select.selectedOptions.length > 0) console.log('Selected');`?",
    "options": [
      "Logs 'Selected' if an option is chosen",
      "Logs the number of options",
      "Sets the dropdown value",
      "Throws an error"
    ],
    "answer": "Logs 'Selected' if an option is chosen",
    "difficulty": "Medium",
    "explanation": "'selectedOptions.length' checks if any options are selected."
  },
  {
    "question": "What does this code do: `let radio = document.querySelector('input[name=group]:checked'); radio ? radio.checked = true : console.log('None');`?",
    "options": [
      "Logs 'None' if no radio is checked",
      "Checks all radio buttons",
      "Logs the radio value",
      "Throws an error"
    ],
    "answer": "Logs 'None' if no radio is checked",
    "difficulty": "Medium",
    "explanation": "If no radio is checked, 'radio' is null, logging 'None'."
  },
  {
    "question": "What does this code do: `let zip = document.getElementById('zip').value; if (/^\\d{9}$/.test(zip)) console.log('Valid 9-digit ZIP');`?",
    "options": [
      "Logs 'Valid 9-digit ZIP' for 9 digits",
      "Logs the ZIP value",
      "Sets the ZIP value",
      "Throws an error"
    ],
    "answer": "Logs 'Valid 9-digit ZIP' for 9 digits",
    "difficulty": "Medium",
    "explanation": "The regex '/^\\d{9}$/' matches exactly 9 digits."
  },
  {
    "question": "What is the output of: `try { null.x; } catch (e) { console.log(e.name); }`?",
    "options": [
      "TypeError",
      "ReferenceError",
      "SyntaxError",
      "undefined"
    ],
    "answer": "TypeError",
    "difficulty": "Medium",
    "explanation": "Accessing a property on null throws a TypeError, caught and logged."
  },
  {
    "question": "What does this code do: `try { throw { message: 'Custom' }; } catch (e) { console.log(e.message); }`?",
    "options": [
      "Logs 'Custom'",
      "Logs undefined",
      "Throws an error",
      "Logs 'Error'"
    ],
    "answer": "Logs 'Custom'",
    "difficulty": "Medium",
    "explanation": "The thrown object’s 'message' property is caught and logged."
  },
  {
    "question": "What does this code do: `document.getElementById('input').addEventListener('submit', e => e.preventDefault());`?",
    "options": [
      "Prevents form submission",
      "Submits the form",
      "Logs the form data",
      "Throws an error"
    ],
    "answer": "Prevents form submission",
    "difficulty": "Medium",
    "explanation": "'preventDefault()' stops the form’s default submission behavior."
  },
  {
    "question": "What does this code do: `let div = document.createElement('div'); console.log(div.nodeType);`?",
    "options": [
      "Logs 1",
      "Logs 3",
      "Logs 8",
      "Throws an error"
    ],
    "answer": "Logs 1",
    "difficulty": "Medium",
    "explanation": "An element node like a div has a 'nodeType' of 1."
  },
  {
    "question": "What does this code do: `let elements = document.getElementsByTagName('p'); console.log(elements.length);`?",
    "options": [
      "Logs the number of <p> elements",
      "Logs the first <p> element",
      "Selects one <p> element",
      "Throws an error"
    ],
    "answer": "Logs the number of <p> elements",
    "difficulty": "Medium",
    "explanation": "'getElementsByTagName()' returns a collection of <p> elements, and 'length' counts them."
  },
  {
    "question": "What does this code do: `let elem = document.querySelector('#box'); console.log(elem.getAttribute('data-value'));`?",
    "options": [
      "Logs the value of data-value attribute",
      "Logs undefined if no attribute",
      "Sets the data-value attribute",
      "Throws an error"
    ],
    "answer": "Logs the value of data-value attribute",
    "difficulty": "Medium",
    "explanation": "'getAttribute()' returns the 'data-value' or null if it doesn’t exist."
  },
  {
    "question": "What does this code do: `let div = document.createElement('div'); document.body.appendChild(div); div.textContent = 'Test';`?",
    "options": [
      "Appends a div with 'Test' to the body",
      "Replaces the body",
      "Creates a div without adding it",
      "Throws an error"
    ],
    "answer": "Appends a div with 'Test' to the body",
    "difficulty": "Medium",
    "explanation": "'appendChild()' adds the div, and 'textContent' sets its text."
  },
  {
    "question": "What does this code do: `let obj = { x: 1 }; delete obj.x; console.log(obj.x);`?",
    "options": [
      "Logs undefined",
      "Logs 1",
      "Throws an error",
      "Logs 'x'"
    ],
    "answer": "Logs undefined",
    "difficulty": "Medium",
    "explanation": "'delete' removes the 'x' property, so accessing obj.x returns undefined."
  },
  {
    "question": "What does this code do: `let obj = { x: 10 }; obj.y = 20; console.log(obj.y);`?",
    "options": [
      "Logs 20",
      "Logs 10",
      "Logs undefined",
      "Throws an error"
    ],
    "answer": "Logs 20",
    "difficulty": "Medium",
    "explanation": "Adding 'y' to the object and accessing it logs 20."
  },
  {
    "question": "What does this code do: `window.location.pathname = '/new';`?",
    "options": [
      "Navigates to /new on the current domain",
      "Reloads the page",
      "Opens a new tab",
      "Changes the query string"
    ],
    "answer": "Navigates to /new on the current domain",
    "difficulty": "Medium",
    "explanation": "Setting 'location.pathname' navigates to the new path."
  },
  {
    "question": "What does this code do: `let input = document.getElementById('text'); if (/^\\d+$/.test(input.value)) console.log('Numbers');`?",
    "options": [
      "Logs 'Numbers' if input is digits only",
      "Logs the input value",
      "Sets the input value",
      "Throws an error"
    ],
    "answer": "Logs 'Numbers' if input is digits only",
    "difficulty": "Medium",
    "explanation": "The regex '/^\\d+$/' checks for digits, logging 'Numbers' if matched."
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
    if not quiz:
        st.error("Quiz list is empty! Please check the quiz data.")
        st.stop()
    st.session_state.update({
        "quiz_data": shuffle_quiz(quiz),
        "score": 0,
        "current_q": 0,
        "start_time": None,  # Set when quiz starts
        "answers": [None] * len(quiz),
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 3600,  # 60 minutes
        "theme": "dark",
        "streak": 0,
        "max_streak": 0,
        "started": False,
        "paused": False,
        "pause_time": None
    })
    st.write(f"Initialized quiz with {len(st.session_state.quiz_data)} questions")

# Theme toggle
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# Timer logic
def update_timer():
    if not st.session_state.paused and st.session_state.start_time:
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        st.session_state.time_left = max(3600 - elapsed, 0)
        if st.session_state.time_left <= 0:
            st.session_state.show_results = True

# Pause/Resume quiz
def toggle_pause():
    if st.session_state.paused:
        # Resume: adjust start_time to account for pause duration
        pause_duration = (datetime.now() - st.session_state.pause_time).total_seconds()
        st.session_state.start_time += pause_duration
        st.session_state.paused = False
    else:
        # Pause
        st.session_state.paused = True
        st.session_state.pause_time = datetime.now()
    st.rerun()

# Reset quiz
def reset_quiz():
    st.session_state.update({
        "quiz_data": shuffle_quiz(quiz),
        "score": 0,
        "current_q": 0,
        "start_time": None,
        "answers": [None] * len(quiz),
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 3600,
        "streak": 0,
        "max_streak": 0,
        "started": False,
        "paused": False,
        "pause_time": None
    })

# CSS for enhanced UI (added ARIA attributes and improved code block styling)
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
.stButton>button:hover:not(:disabled) {
    background: var(--button-hover);
    transform: scale(1.05);
    box-shadow: 0 4px 12px var(--shadow);
}
.stButton>button:disabled {
    background: #6b7280;
    cursor: not-allowed;
    transform: scale(1);
}
.stButton>button:focus {
    outline: 2px solid #a855f7;
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
.stCodeBlock, .stCodeBlock pre, .stCodeBlock code {
    background-color: var(--code-bg) !important;
    border-radius: 8px;
    padding: 15px;
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 14px;
    line-height: 1.5;
    border: 1px solid #4b4b6b;
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
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}" role="main">', unsafe_allow_html=True)
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
    if not st.session_state.show_results and not st.session_state.paused:
        update_timer()
        minutes = int(st.session_state.time_left // 60)
        seconds = int(st.session_state.time_left % 60)
        st.markdown(f'<div class="timer" role="timer">⏰ Time Left: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

    # Pause/Resume button
    pause_label = "Pause Quiz" if not st.session_state.paused else "Resume Quiz"
    if st.button(pause_label, key="pause_quiz"):
        toggle_pause()

    if not st.session_state.quiz_data:
        st.error("No quiz questions available.")
        st.stop()
    else:
        # Progress bar
        progress = st.session_state.current_q / len(st.session_state.quiz_data)
        progress_percentage = progress * 100  # Keep as float for precision
        st.markdown(f"""
        <div class="progress-bar" role="progressbar" aria-valuenow="{progress_percentage}" aria-valuemin="0" aria-valuemax="100">
            <div class="progress-fill" style="width: {progress_percentage}%"></div>
            <div class="progress-text">{progress_percentage:.1f}%</div>
        </div>
        <div style="color: var(--text-color); font-size: 13px; text-align: center;">
            Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
        </div>
        """, unsafe_allow_html=True)

        if not st.session_state.show_results:
            with st.container():
                st.markdown('<div class="question-container" role="region" aria-label="Question">', unsafe_allow_html=True)
                q = st.session_state.quiz_data[st.session_state.current_q]

                # Display difficulty and streak
                st.markdown(f'<div class="difficulty">Difficulty: {q["difficulty"]} | Streak: 🔥 {st.session_state.streak}</div>', unsafe_allow_html=True)

                # Split question into text and code
                if "```javascript" in q["question"]:
                    question_parts = q["question"].split("```javascript
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
                    button_key = f"q_{q['id']}_{i}"  # Unique key using question ID
                    if st.button(
                        option,
                        key=button_key,
                        disabled=st.session_state.selected_option is not None or st.session_state.paused,
                        help=f"Select option {i + 1}"
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
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 3600) if st.session_state.start_time else 3600
            total_possible_score = len(quiz) * 2
            accuracy = (st.session_state.score / total_possible_score) * 100 if total_possible_score > 0 else 0
            st.markdown('<div class="question-container" role="region" aria-label="Results">', unsafe_allow_html=True)
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
                    if (typeof confetti === 'function') {
                        confetti({
                            particleCount: 100,
                            spread: 70,
                            origin: { y: 0.6 }
                        });
                    }
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
                st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

