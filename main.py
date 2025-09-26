import streamlit as st
import random
from datetime import datetime
import uuid

quiz =[
  {
    "question": "What is the output of: `function test() { var x = 1; if (true) { var x = 2; } return x; } console.log(test());`?",
    "options": [
      "2",
      "1"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "'var' is function-scoped, so the inner 'var x = 2' reassigns the same variable, returning 2."
  },
  {
    "question": "What does: `let x = 10; { let x = 20; } console.log(x);` output?",
    "options": [
      "10",
      "20"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "'let' is block-scoped, so the inner 'let x = 20' doesn’t affect the outer x, logging 10."
  },
  {
    "question": "What is the output of: `function scope() { let x = 5; x = 10; return x; } console.log(scope());`?",
    "options": [
      "10",
      "5"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "The variable x is reassigned to 10 within the function scope, returning 10."
  },
  {
    "question": "What happens in: `function run() { 'use strict'; x = 1; } run();`?",
    "options": [
      "Throws ReferenceError",
      "Sets global x to 1"
    ],
    "answer": "Throws ReferenceError",
    "difficulty": "Medium",
    "explanation": "In strict mode, assigning to an undeclared variable throws a ReferenceError."
  },
  {
    "question": "What is the output of: `var x = 1; function test() { console.log(x); var x = 2; } test();`?",
    "options": [
      "undefined",
      "1"
    ],
    "answer": "undefined",
    "difficulty": "Medium",
    "explanation": "Due to hoisting, 'var x = 2' is declared but undefined when logged, shadowing the global x."
  },
  {
    "question": "Which validates a non-empty text field: `let input = document.querySelector('#text');`?",
    "options": [
      "if (input.value.trim() !== '')",
      "if (input.value === null)"
    ],
    "answer": "if (input.value.trim() !== '')",
    "difficulty": "Medium",
    "explanation": "'trim()' removes whitespace, and checking '!== ''' ensures the field isn’t empty."
  },
  {
    "question": "What does: `let input = document.querySelector('#text'); if (input.value.length >= 5) console.log('Valid');` do?",
    "options": [
      "Logs 'Valid' if input has 5+ characters",
      "Sets input value to 'Valid'"
    ],
    "answer": "Logs 'Valid' if input has 5+ characters",
    "difficulty": "Medium",
    "explanation": "The code checks if the input’s value length is >= 5, logging 'Valid'."
  },
  {
    "question": "What does: `let select = document.querySelector('#dropdown'); if (select.selectedIndex > -1) console.log('Selected');` do?",
    "options": [
      "Logs 'Selected' if dropdown has a selection",
      "Sets dropdown value"
    ],
    "answer": "Logs 'Selected' if dropdown has a selection",
    "difficulty": "Medium",
    "explanation": "'selectedIndex > -1' confirms a dropdown option is selected, logging 'Selected'."
  },
  {
    "question": "What does: `let radio = document.querySelector('input[name=group]:checked'); if (radio) console.log(radio.value);` do?",
    "options": [
      "Logs value of selected radio button",
      "Checks all radio buttons"
    ],
    "answer": "Logs value of selected radio button",
    "difficulty": "Medium",
    "explanation": "The code logs the value of the checked radio button, or nothing if none is selected."
  },
  {
    "question": "Which regex validates a 5-digit ZIP code: `let input = document.querySelector('#zip'); if (regex.test(input.value)) console.log('Valid');`?",
    "options": [
      "/^\\d{5}$/",
      "/^\\d{5}-\\d{4}$/"
    ],
    "answer": "/^\\d{5}$/",
    "difficulty": "Medium",
    "explanation": "'/^\\d{5}$/' matches exactly 5 digits, validating a basic ZIP code."
  },
  {
    "question": "What does: `let input = document.querySelector('#email'); if (/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(input.value)) console.log('Valid');` do?",
    "options": [
      "Logs 'Valid' for correct email format",
      "Sets email value"
    ],
    "answer": "Logs 'Valid' for correct email format",
    "difficulty": "Medium",
    "explanation": "The regex validates an email format, logging 'Valid' if it matches."
  },
  {
    "question": "What is the output of: `try { let x = undefined.x; } catch (e) { console.log(e.name); }`?",
    "options": [
      "TypeError",
      "ReferenceError"
    ],
    "answer": "TypeError",
    "difficulty": "Medium",
    "explanation": "Accessing a property on undefined throws a TypeError, caught and logged."
  },
  {
    "question": "What does: `try { throw new Error('Invalid'); } catch (e) { console.log(e.message); }` output?",
    "options": [
      "Invalid",
      "Error"
    ],
    "answer": "Invalid",
    "difficulty": "Medium",
    "explanation": "The thrown error’s message 'Invalid' is caught and logged."
  },
  {
    "question": "What does: `document.querySelector('.btn').addEventListener('click', () => console.log('Clicked'));` do?",
    "options": [
      "Logs 'Clicked' on button click",
      "Changes button text"
    ],
    "answer": "Logs 'Clicked' on button click",
    "difficulty": "Medium",
    "explanation": "'addEventListener()' binds a click handler that logs 'Clicked'."
  },
  {
    "question": "What is the output of: `let node = document.createElement('div'); console.log(node.nodeType);`?",
    "options": [
      "1",
      "3"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "An element node like a div has a 'nodeType' of 1."
  },
  {
    "question": "What does: `let elements = document.querySelectorAll('.test'); console.log(elements.length);` do?",
    "options": [
      "Logs number of elements with class 'test'",
      "Selects first element"
    ],
    "answer": "Logs number of elements with class 'test'",
    "difficulty": "Medium",
    "explanation": "'querySelectorAll()' returns a NodeList, and 'length' counts matching elements."
  },
  {
    "question": "What is the output of: `let elem = document.querySelector('p'); console.log(elem.tagName);` for a <p> element?",
    "options": [
      "P",
      "p"
    ],
    "answer": "P",
    "difficulty": "Medium",
    "explanation": "'tagName' returns the tag name in uppercase, so 'P'."
  },
  {
    "question": "What is the output of: `let div = document.createElement('div'); div.innerHTML = '<p>1</p><p>2</p>'; console.log(div.children.length);`?",
    "options": [
      "2",
      "1"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "'children.length' counts the two <p> elements."
  },
  {
    "question": "What does: `let elem = document.querySelector('#box'); elem.setAttribute('data-value', 'test'); console.log(elem.getAttribute('data-value'));` output?",
    "options": [
      "test",
      "undefined"
    ],
    "answer": "test",
    "difficulty": "Medium",
    "explanation": "'setAttribute()' sets the attribute, and 'getAttribute()' retrieves it, logging 'test'."
  },
  {
    "question": "What does: `let elem = document.querySelector('#box'); console.log(elem.attributes.length);` do?",
    "options": [
      "Logs number of attributes on #box",
      "Logs attribute values"
    ],
    "answer": "Logs number of attributes on #box",
    "difficulty": "Medium",
    "explanation": "'attributes.length' counts the number of attributes on the element."
  },
  {
    "question": "What does: `let div = document.createElement('div'); document.body.appendChild(div);` do?",
    "options": [
      "Appends new div to body",
      "Replaces body"
    ],
    "answer": "Appends new div to body",
    "difficulty": "Medium",
    "explanation": "'appendChild()' adds the div as the last child of the body."
  },
  {
    "question": "What does: `let p = document.createElement('p'); document.querySelector('#target').parentNode.insertBefore(p, document.querySelector('#target'));` do?",
    "options": [
      "Inserts new <p> before #target",
      "Inserts new <p> after #target"
    ],
    "answer": "Inserts new <p> before #target",
    "difficulty": "Medium",
    "explanation": "'insertBefore()' adds the <p> before the specified target."
  },
  {
    "question": "What is the output of: `let obj = { x: 10 }; console.log(obj.x);`?",
    "options": [
      "10",
      "undefined"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "The 'x' property is accessed using dot notation, logging 10."
  },
  {
    "question": "What does: `let obj = {}; obj.newProp = 42; console.log(obj.newProp);` output?",
    "options": [
      "42",
      "undefined"
    ],
    "answer": "42",
    "difficulty": "Medium",
    "explanation": "Adding 'newProp' to the object and accessing it logs 42."
  },
  {
    "question": "What is the output of: `let obj = { calc: function() { return 5; } }; console.log(obj.calc());`?",
    "options": [
      "5",
      "undefined"
    ],
    "answer": "5",
    "difficulty": "Medium",
    "explanation": "The 'calc' method returns 5 when called."
  },
  {
    "question": "What is the output of: `function User(name) { this.name = name; } let u = new User('Bob'); console.log(u.name);`?",
    "options": [
      "Bob",
      "undefined"
    ],
    "answer": "Bob",
    "difficulty": "Medium",
    "explanation": "The constructor sets 'name' to 'Bob', accessed as u.name."
  },
  {
    "question": "What does: `function Car() { this.drive = function() { return 'Driving'; }; } let c = new Car(); console.log(c.drive());` output?",
    "options": [
      "Driving",
      "undefined"
    ],
    "answer": "Driving",
    "difficulty": "Medium",
    "explanation": "The constructor defines the 'drive' method, which returns 'Driving'."
  },
  {
    "question": "What is the output of: `function Animal() { } Animal.prototype.speak = function() { return 'Bark'; }; let a = new Animal(); console.log(a.speak());`?",
    "options": [
      "Bark",
      "undefined"
    ],
    "answer": "Bark",
    "difficulty": "Medium",
    "explanation": "The 'speak' method on the prototype returns 'Bark'."
  },
  {
    "question": "What is the output of: `let obj = { x: 1 }; console.log(obj.hasOwnProperty('x'));`?",
    "options": [
      "true",
      "false"
    ],
    "answer": "true",
    "difficulty": "Medium",
    "explanation": "'hasOwnProperty()' returns true if 'x' is a direct property of the object."
  },
  {
    "question": "What does: `console.log(window.location.href);` do?",
    "options": [
      "Logs the current URL",
      "Navigates to a new URL"
    ],
    "answer": "Logs the current URL",
    "difficulty": "Medium",
    "explanation": "'window.location.href' returns the full URL of the current page."
  },
  {
    "question": "What does: `window.location.assign('https://example.com');` do?",
    "options": [
      "Navigates to https://example.com",
      "Reloads the page"
    ],
    "answer": "Navigates to https://example.com",
    "difficulty": "Medium",
    "explanation": "'location.assign()' loads a new URL in the current window."
  },
  {
    "question": "What does: `window.history.back();` do?",
    "options": [
      "Navigates to previous page",
      "Navigates to next page"
    ],
    "answer": "Navigates to previous page",
    "difficulty": "Medium",
    "explanation": "'history.back()' moves to the previous page in the browser’s history."
  },
  {
    "question": "What does: `document.body.style.height = '100vh';` do?",
    "options": [
      "Sets body height to full viewport",
      "Sets body width to full viewport"
    ],
    "answer": "Sets body height to full viewport",
    "difficulty": "Medium",
    "explanation": "'100vh' sets the body’s height to the full viewport height."
  },
  {
    "question": "What does: `window.resizeTo(800, 600);` do?",
    "options": [
      "Resizes window to 800x600 pixels",
      "Moves window to (800, 600)"
    ],
    "answer": "Resizes window to 800x600 pixels",
    "difficulty": "Medium",
    "explanation": "'window.resizeTo()' sets the browser window’s dimensions."
  },
  {
    "question": "What does: `let win = window.open(''); if (!win) console.log('Blocked');` do?",
    "options": [
      "Logs 'Blocked' if popup is blocked",
      "Opens a new window"
    ],
    "answer": "Logs 'Blocked' if popup is blocked",
    "difficulty": "Medium",
    "explanation": "'window.open()' returns null if a popup blocker prevents the window."
  },
  {
    "question": "What does: `let input = document.querySelector('#text'); if (/^[a-zA-Z]+$/.test(input.value)) console.log('Valid');` do?",
    "options": [
      "Logs 'Valid' if input is alphabetic",
      "Sets input value"
    ],
    "answer": "Logs 'Valid' if input is alphabetic",
    "difficulty": "Medium",
    "explanation": "The regex '/^[a-zA-Z]+$/' checks if the input contains only letters."
  },
  {
    "question": "What is the output of: `function test() { let x = 1; { let x = 2; } return x; } console.log(test());`?",
    "options": [
      "1",
      "2"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "The inner 'let x = 2' is block-scoped, so the outer x remains 1."
  },
  {
    "question": "What does: `let select = document.querySelector('#dropdown'); if (select.value !== '') console.log('Valid');` do?",
    "options": [
      "Logs 'Valid' if dropdown has non-empty value",
      "Sets dropdown value"
    ],
    "answer": "Logs 'Valid' if dropdown has non-empty value",
    "difficulty": "Medium",
    "explanation": "Checking 'value !== ''' ensures a non-empty dropdown selection."
  },
  {
    "question": "What does: `let radios = document.querySelectorAll('input[name=group]'); radios.forEach(r => r.checked = false);` do?",
    "options": [
      "Unchecks all radio buttons",
      "Checks all radio buttons"
    ],
    "answer": "Unchecks all radio buttons",
    "difficulty": "Medium",
    "explanation": "The code sets 'checked' to false for all radio buttons."
  },
  {
    "question": "What does: `let input = document.querySelector('#zip'); if (/^\\d{5}(-\\d{4})?$/.test(input.value)) console.log('Valid');` do?",
    "options": [
      "Logs 'Valid' for 5- or 9-digit ZIP",
      "Sets ZIP code value"
    ],
    "answer": "Logs 'Valid' for 5- or 9-digit ZIP",
    "difficulty": "Medium",
    "explanation": "The regex matches 5 digits or 5 digits plus a hyphen and 4 digits."
  },
  {
    "question": "What is the output of: `try { JSON.parse('invalid'); } catch (e) { console.log(e.name); }`?",
    "options": [
      "SyntaxError",
      "TypeError"
    ],
    "answer": "SyntaxError",
    "difficulty": "Medium",
    "explanation": "Invalid JSON in 'JSON.parse()' throws a SyntaxError, caught and logged."
  },
  {
    "question": "What does: `try { throw new Error('Fail'); } catch (e) { console.log(e.message); }` output?",
    "options": [
      "Fail",
      "Error"
    ],
    "answer": "Fail",
    "difficulty": "Medium",
    "explanation": "The thrown error’s message 'Fail' is caught and logged."
  },
  {
    "question": "What does: `document.querySelector('#input').addEventListener('input', () => console.log('Typing'));` do?",
    "options": [
      "Logs 'Typing' when input changes",
      "Changes input value"
    ],
    "answer": "Logs 'Typing' when input changes",
    "difficulty": "Medium",
    "explanation": "The 'input' event fires on value changes, logging 'Typing'."
  },
  {
    "question": "What is the output of: `let text = document.createTextNode('test'); console.log(text.nodeType);`?",
    "options": [
      "3",
      "1"
    ],
    "answer": "3",
    "difficulty": "Medium",
    "explanation": "A text node has a 'nodeType' of 3."
  },
  {
    "question": "What does: `let elements = document.getElementsByClassName('test'); console.log(elements.length);` do?",
    "options": [
      "Logs number of elements with class 'test'",
      "Selects first element"
    ],
    "answer": "Logs number of elements with class 'test'",
    "difficulty": "Medium",
    "explanation": "'getElementsByClassName()' returns a collection, and 'length' counts matches."
  },
  {
    "question": "What is the output of: `let img = document.createElement('img'); console.log(img.tagName);`?",
    "options": [
      "IMG",
      "img"
    ],
    "answer": "IMG",
    "difficulty": "Medium",
    "explanation": "'tagName' returns the tag name in uppercase, so 'IMG'."
  },
  {
    "question": "What does: `let div = document.querySelector('#box'); console.log(div.childNodes.length);` do?",
    "options": [
      "Logs number of all child nodes",
      "Logs number of element children"
    ],
    "answer": "Logs number of all child nodes",
    "difficulty": "Medium",
    "explanation": "'childNodes.length' counts all nodes, including text and comments."
  },
  {
    "question": "What does: `let elem = document.querySelector('#box'); if (elem.hasAttribute('data-test')) console.log('Has attribute');` do?",
    "options": [
      "Logs 'Has attribute' if data-test exists",
      "Sets data-test attribute"
    ],
    "answer": "Logs 'Has attribute' if data-test exists",
    "difficulty": "Medium",
    "explanation": "'hasAttribute()' checks if the element has the specified attribute."
  },
  {
    "question": "What does: `let elem = document.querySelector('#box'); elem.removeAttribute('data-test');` do?",
    "options": [
      "Removes data-test attribute",
      "Sets data-test to null"
    ],
    "answer": "Removes data-test attribute",
    "difficulty": "Medium",
    "explanation": "'removeAttribute()' removes the specified attribute."
  },
  {
    "question": "What does: `let span = document.createElement('span'); document.querySelector('#container').appendChild(span);` do?",
    "options": [
      "Appends new span to #container",
      "Replaces #container"
    ],
    "answer": "Appends new span to #container",
    "difficulty": "Medium",
    "explanation": "'appendChild()' adds the span as the last child of #container."
  },
  {
    "question": "What does: `let p = document.createElement('p'); document.querySelector('#target').parentNode.insertBefore(p, document.querySelector('#target').nextSibling);` do?",
    "options": [
      "Inserts new <p> after #target",
      "Inserts new <p> before #target"
    ],
    "answer": "Inserts new <p> after #target",
    "difficulty": "Medium",
    "explanation": "Using 'nextSibling' with 'insertBefore()' places the <p> after #target."
  },
  {
    "question": "What is the output of: `let obj = { y: 20 }; console.log(obj['y']);`?",
    "options": [
      "20",
      "undefined"
    ],
    "answer": "20",
    "difficulty": "Medium",
    "explanation": "Bracket notation accesses the 'y' property, logging 20."
  },
  {
    "question": "What does: `let obj = { x: 1 }; obj.x = 2; console.log(obj.x);` output?",
    "options": [
      "2",
      "1"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "Reassigning obj.x updates the property, logging 2."
  },
  {
    "question": "What is the output of: `let obj = { say: () => 'Hello' }; console.log(obj.say());`?",
    "options": [
      "Hello",
      "undefined"
    ],
    "answer": "Hello",
    "difficulty": "Medium",
    "explanation": "The 'say' method returns 'Hello' when called."
  },
  {
    "question": "What does: `function Person() { this.name = 'Alice'; } let p = new Person(); console.log(p.name);` output?",
    "options": [
      "Alice",
      "undefined"
    ],
    "answer": "Alice",
    "difficulty": "Medium",
    "explanation": "The constructor sets 'name' to 'Alice', accessed as p.name."
  },
  {
    "question": "What does: `function Dog() { this.bark = function() { return 'Woof'; }; } let d = new Dog(); console.log(d.bark());` output?",
    "options": [
      "Woof",
      "undefined"
    ],
    "answer": "Woof",
    "difficulty": "Medium",
    "explanation": "The constructor defines the 'bark' method, which returns 'Woof'."
  },
  {
    "question": "What is the output of: `function Cat() { } Cat.prototype.meow = function() { return 'Meow'; }; let c = new Cat(); console.log(c.meow());`?",
    "options": [
      "Meow",
      "undefined"
    ],
    "answer": "Meow",
    "difficulty": "Medium",
    "explanation": "The 'meow' method on the prototype returns 'Meow'."
  },
  {
    "question": "What does: `let obj = { x: 1 }; console.log('x' in obj);` output?",
    "options": [
      "true",
      "false"
    ],
    "answer": "true",
    "difficulty": "Medium",
    "explanation": "The 'in' operator returns true if 'x' exists in the object or its prototype."
  },
  {
    "question": "What does: `window.location.search = '?q=test';` do?",
    "options": [
      "Sets query string to '?q=test'",
      "Navigates to a new URL"
    ],
    "answer": "Sets query string to '?q=test'",
    "difficulty": "Medium",
    "explanation": "Setting 'location.search' updates the URL’s query string."
  },
  {
    "question": "What does: `window.history.forward();` do?",
    "options": [
      "Navigates to next page",
      "Navigates to previous page"
    ],
    "answer": "Navigates to next page",
    "difficulty": "Medium",
    "explanation": "'history.forward()' moves to the next page in the browser’s history."
  },
  {
    "question": "What does: `document.documentElement.style.width = '100vw';` do?",
    "options": [
      "Sets html width to full viewport",
      "Sets html height to full viewport"
    ],
    "answer": "Sets html width to full viewport",
    "difficulty": "Medium",
    "explanation": "'100vw' sets the html element’s width to the full viewport width."
  },
  {
    "question": "What does: `window.moveTo(100, 100);` do?",
    "options": [
      "Moves window to (100, 100)",
      "Resizes window"
    ],
    "answer": "Moves window to (100, 100)",
    "difficulty": "Medium",
    "explanation": "'window.moveTo()' repositions the browser window."
  },
  {
    "question": "What does: `let input = document.querySelector('#text'); if (/^\\d+$/.test(input.value)) console.log('Valid');` do?",
    "options": [
      "Logs 'Valid' if input is numeric",
      "Sets input value"
    ],
    "answer": "Logs 'Valid' if input is numeric",
    "difficulty": "Medium",
    "explanation": "The regex '/^\\d+$/' checks if the input contains only digits."
  },
  {
    "question": "What is the output of: `let x = 5; function test() { let x = 10; return x; } console.log(test(), x);`?",
    "options": [
      "10, 5",
      "5, 10"
    ],
    "answer": "10, 5",
    "difficulty": "Medium",
    "explanation": "The inner 'let x = 10' is function-scoped, so test() returns 10; outer x is 5."
  },
  {
    "question": "What does: `let select = document.querySelector('#dropdown'); if (select.options[select.selectedIndex].value === 'valid') console.log('Valid');` do?",
    "options": [
      "Logs 'Valid' if dropdown value is 'valid'",
      "Sets dropdown value"
    ],
    "answer": "Logs 'Valid' if dropdown value is 'valid'",
    "difficulty": "Medium",
    "explanation": "The code checks if the selected option’s value is 'valid', logging 'Valid'."
  },
  {
    "question": "What does: `let radio = document.querySelector('input[name=group]:checked'); if (radio) radio.value = 'selected';` do?",
    "options": [
      "Sets selected radio value to 'selected'",
      "Checks all radio buttons"
    ],
    "answer": "Sets selected radio value to 'selected'",
    "difficulty": "Medium",
    "explanation": "The code sets the value of the checked radio button to 'selected'."
  },
  {
    "question": "What does: `let input = document.querySelector('#zip'); if (/^\\d{9}$/.test(input.value)) console.log('Valid');` do?",
    "options": [
      "Logs 'Valid' for 9-digit ZIP",
      "Sets ZIP code value"
    ],
    "answer": "Logs 'Valid' for 9-digit ZIP",
    "difficulty": "Medium",
    "explanation": "The regex '/^\\d{9}$/' matches exactly 9 digits."
  },
  {
    "question": "What is the output of: `try { null.x; } catch (e) { console.log(e.name); }`?",
    "options": [
      "TypeError",
      "ReferenceError"
    ],
    "answer": "TypeError",
    "difficulty": "Medium",
    "explanation": "Accessing a property on null throws a TypeError, caught and logged."
  },
  {
    "question": "What does: `try { throw 'Custom error'; } catch (e) { console.log(e); }` output?",
    "options": [
      "Custom error",
      "Error"
    ],
    "answer": "Custom error",
    "difficulty": "Medium",
    "explanation": "The thrown string 'Custom error' is caught and logged."
  },
  {
    "question": "What does: `document.querySelector('#form').addEventListener('submit', (e) => { e.preventDefault(); console.log('Submitted'); });` do?",
    "options": [
      "Logs 'Submitted' and prevents form submission",
      "Submits the form"
    ],
    "answer": "Logs 'Submitted' and prevents form submission",
    "difficulty": "Medium",
    "explanation": "'preventDefault()' stops form submission, and 'Submitted' is logged."
  },
  {
    "question": "What is the output of: `let comment = document.createComment('test'); console.log(comment.nodeType);`?",
    "options": [
      "8",
      "1"
    ],
    "answer": "8",
    "difficulty": "Medium",
    "explanation": "A comment node has a 'nodeType' of 8."
  },
  {
    "question": "What does: `let elements = document.querySelectorAll('[data-test]'); console.log(elements.length);` do?",
    "options": [
      "Logs number of elements with data-test",
      "Sets data-test attribute"
    ],
    "answer": "Logs number of elements with data-test",
    "difficulty": "Medium",
    "explanation": "'querySelectorAll()' selects elements with data-test, and 'length' counts them."
  },
  {
    "question": "What does: `let div = document.querySelector('#box'); console.log(div.tagName);` output for a <div>?",
    "options": [
      "DIV",
      "div"
    ],
    "answer": "DIV",
    "difficulty": "Medium",
    "explanation": "'tagName' returns the tag name in uppercase, so 'DIV'."
  },
  {
    "question": "What does: `let div = document.querySelector('#box'); div.innerHTML = '<span>1</span>'; console.log(div.children.length);` output?",
    "options": [
      "1",
      "0"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "'children.length' counts the single <span> element."
  },
  {
    "question": "What does: `let elem = document.querySelector('#box'); elem.setAttribute('title', 'Tooltip'); console.log(elem.getAttribute('title'));` output?",
    "options": [
      "Tooltip",
      "undefined"
    ],
    "answer": "Tooltip",
    "difficulty": "Medium",
    "explanation": "'setAttribute()' sets the title, and 'getAttribute()' retrieves it."
  },
  {
    "question": "What does: `let elem = document.querySelector('#box'); console.log(Array.from(elem.attributes).map(attr => attr.name));` output?",
    "options": [
      "Array of attribute names",
      "Array of attribute values"
    ],
    "answer": "Array of attribute names",
    "difficulty": "Medium",
    "explanation": "'attributes' is a NamedNodeMap; mapping 'name' gives an array of attribute names."
  },
  {
    "question": "What does: `let div = document.createElement('div'); div.textContent = 'Hello'; document.body.appendChild(div);` do?",
    "options": [
      "Appends div with 'Hello' to body",
      "Replaces body content"
    ],
    "answer": "Appends div with 'Hello' to body",
    "difficulty": "Medium",
    "explanation": "'appendChild()' adds the div with 'Hello' to the body."
  },
  {
    "question": "What does: `let span = document.createElement('span'); document.querySelector('#target').parentNode.replaceChild(span, document.querySelector('#target'));` do?",
    "options": [
      "Replaces #target with new span",
      "Inserts span before #target"
    ],
    "answer": "Replaces #target with new span",
    "difficulty": "Medium",
    "explanation": "'replaceChild()' swaps #target with the new span."
  },
  {
    "question": "What does: `let obj = { x: 1 }; delete obj.x; console.log(obj.x);` output?",
    "options": [
      "undefined",
      "1"
    ],
    "answer": "undefined",
    "difficulty": "Medium",
    "explanation": "'delete' removes the 'x' property, so obj.x is undefined."
  },
  {
    "question": "What does: `let obj = { count: 5 }; console.log(obj['count']);` output?",
    "options": [
      "5",
      "undefined"
    ],
    "answer": "5",
    "difficulty": "Medium",
    "explanation": "Bracket notation accesses the 'count' property, logging 5."
  },
  {
    "question": "What does: `let obj = { add: function(a, b) { return a + b; } }; console.log(obj.add(2, 3));` output?",
    "options": [
      "5",
      "undefined"
    ],
    "answer": "5",
    "difficulty": "Medium",
    "explanation": "The 'add' method returns the sum of 2 and 3, which is 5."
  },
  {
    "question": "What does: `function Book(title) { this.title = title; } let b = new Book('JS'); console.log(b.title);` output?",
    "options": [
      "JS",
      "undefined"
    ],
    "answer": "JS",
    "difficulty": "Medium",
    "explanation": "The constructor sets 'title' to 'JS', accessed as b.title."
  },
  {
    "question": "What does: `function Vehicle() { this.move = () => 'Moving'; } let v = new Vehicle(); console.log(v.move());` output?",
    "options": [
      "Moving",
      "undefined"
    ],
    "answer": "Moving",
    "difficulty": "Medium",
    "explanation": "The constructor defines the 'move' method, which returns 'Moving'."
  },
  {
    "question": "What is the output of: `function Bird() { } Bird.prototype.fly = function() { return 'Flying'; }; let b = new Bird(); console.log(b.fly());`?",
    "options": [
      "Flying",
      "undefined"
    ],
    "answer": "Flying",
    "difficulty": "Medium",
    "explanation": "The 'fly' method on the prototype returns 'Flying'."
  },
  {
    "question": "What does: `let obj = { y: 2 }; console.log(Object.keys(obj).length);` output?",
    "options": [
      "1",
      "0"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "'Object.keys()' returns an array of property names, with length 1."
  },
  {
    "question": "What does: `window.location.replace('https://example.com');` do?",
    "options": [
      "Navigates to https://example.com without history",
      "Adds to history"
    ],
    "answer": "Navigates to https://example.com without history",
    "difficulty": "Medium",
    "explanation": "'location.replace()' navigates without creating a new history entry."
  },
  {
    "question": "What does: `let input = document.querySelector('#text'); if (input.value.length <= 10) console.log('Valid');` do?",
    "options": [
      "Logs 'Valid' if input has ≤10 characters",
      "Sets input value"
    ],
    "answer": "Logs 'Valid' if input has ≤10 characters",
    "difficulty": "Medium",
    "explanation": "The code checks if the input’s length is <= 10, logging 'Valid'."
  },
  {
    "question": "What does: `let select = document.querySelector('#dropdown'); if (select.selectedOptions.length > 0) console.log('Valid');` do?",
    "options": [
      "Logs 'Valid' if dropdown has selection",
      "Sets dropdown value"
    ],
    "answer": "Logs 'Valid' if dropdown has selection",
    "difficulty": "Medium",
    "explanation": "'selectedOptions.length' checks if an option is selected."
  },
  {
    "question": "What does: `let radio = document.querySelector('input[name=group]'); radio.checked = true;` do?",
    "options": [
      "Checks first radio button",
      "Unchecks radio button"
    ],
    "answer": "Checks first radio button",
    "difficulty": "Medium",
    "explanation": "Setting 'checked = true' selects the first radio button."
  },
  {
    "question": "What does: `let input = document.querySelector('#email'); if (/^\\w+@\\w+\\.\\w+$/.test(input.value)) console.log('Valid');` do?",
    "options": [
      "Logs 'Valid' for basic email format",
      "Sets email value"
    ],
    "answer": "Logs 'Valid' for basic email format",
    "difficulty": "Medium",
    "explanation": "The regex '/^\\w+@\\w+\\.\\w+$/' validates a simple email format."
  },
  {
    "question": "What does: `try { let x = y; } catch (e) { console.log(e.name); }` output?",
    "options": [
      "ReferenceError",
      "TypeError"
    ],
    "answer": "ReferenceError",
    "difficulty": "Medium",
    "explanation": "Accessing an undefined variable 'y' throws a ReferenceError."
  },
  {
    "question": "What does: `document.querySelector('#box').addEventListener('mouseover', () => console.log('Hovered'));` do?",
    "options": [
      "Logs 'Hovered' on mouseover",
      "Changes box content"
    ],
    "answer": "Logs 'Hovered' on mouseover",
    "difficulty": "Medium",
    "explanation": "The 'mouseover' event triggers the handler, logging 'Hovered'."
  },
  {
    "question": "What does: `let div = document.querySelector('#box'); div.innerHTML = '<!-- comment -->'; console.log(div.childNodes[0].nodeType);` output?",
    "options": [
      "8",
      "1"
    ],
    "answer": "8",
    "difficulty": "Medium",
    "explanation": "The first child is a comment node, with 'nodeType' 8."
  },
  {
    "question": "What does: `let elements = document.getElementsByTagName('p'); console.log(elements.length);` do?",
    "options": [
      "Logs number of <p> elements",
      "Selects first <p>"
    ],
    "answer": "Logs number of <p> elements",
    "difficulty": "Medium",
    "explanation": "'getElementsByTagName()' returns a collection of <p> elements, and 'length' counts them."
  }
]

# Cache shuffled quiz with a fixed key
@st.cache_data
def shuffle_quiz(_quiz, seed=42):
    random.seed(seed)  # Ensure consistent shuffling for caching
    shuffled = random.sample(_quiz, len(_quiz))
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = q["options"].copy()
        random.seed(seed + int(q["id"].replace("-", ""), 16))  # Unique seed per question
        random.shuffle(q["display_options"])
        q["labeled_answer"] = q["answer"]
    return shuffled

# Initialize session state with minimal data
if "initialized" not in st.session_state:
    if not quiz:
        st.error("Quiz list is empty! Please check the quiz data.")
        st.stop()
    st.session_state.update({
        "initialized": True,
        "quiz_data": shuffle_quiz(quiz),
        "score": 0,
        "current_q": 0,
        "start_time": None,
        "answers": [None] * len(quiz),
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 30 * len(quiz),  # 30 seconds per question
        "theme": "dark",
        "streak": 0,
        "max_streak": 0,
        "started": False,
        "paused": False,
        "pause_time": None
    })

# Theme toggle
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
    st.rerun()

# Timer logic
def update_timer():
    if not st.session_state.paused and st.session_state.start_time:
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        st.session_state.time_left = max(30 * len(quiz) - elapsed, 0)
        if st.session_state.time_left <= 0:
            st.session_state.show_results = True
            st.rerun()

# Pause/Resume quiz
def toggle_pause():
    if st.session_state.paused:
        pause_duration = (datetime.now() - st.session_state.pause_time).total_seconds()
        st.session_state.start_time += pause_duration
        st.session_state.paused = False
    else:
        st.session_state.paused = True
        st.session_state.pause_time = datetime.now()
    st.rerun()

# Reset quiz
def reset_quiz():
    st.session_state.update({
        "initialized": True,
        "quiz_data": shuffle_quiz(quiz),
        "score": 0,
        "current_q": 0,
        "start_time": None,
        "answers": [None] * len(quiz),
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 30 * len(quiz),
        "streak": 0,
        "max_streak": 0,
        "started": False,
        "paused": False,
        "pause_time": None
    })
    st.rerun()

# CSS for UI (minimized for performance)
st.markdown("""
<style>
:root {
    --bg-container: #2c2c54;
    --text-color: #ffffff;
    --button-bg: #6b21a8;
    --button-hover: #8b5cf6;
    --code-bg: #1e1e1e;
    --shadow: rgba(0,0,0,0.3);
}
[data-theme="light"] {
    --bg-container: #ffffff;
    --text-color: #1f2937;
    --button-bg: #4f46e5;
    --button-hover: #6366f1;
    --code-bg: #f1f5f9;
    --shadow: rgba(0,0,0,0.1);
}
.main-container {
    background: var(--bg-container);
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 10px var(--shadow);
    max-width: 700px;
    margin: 10px auto;
}
.stButton>button {
    background: var(--button-bg);
    color: var(--text-color);
    border: none;
    border-radius: 6px;
    padding: 8px;
    width: 100%;
    font-size: 13px;
    margin: 4px 0;
    cursor: pointer;
    transition: all 0.2s ease;
}
.stButton>button:hover:not(:disabled) {
    background: var(--button-hover);
}
.stButton>button:disabled {
    background: #6b7280;
    cursor: not-allowed;
}
.stButton>button:focus {
    outline: 2px solid #a855f7;
}
.selected-correct {
    background: #34c759 !important;
}
.selected-wrong {
    background: #ff3b30 !important;
}
.question-container {
    padding: 10px;
    border-radius: 6px;
}
.feedback-correct {
    color: #34c759;
    font-weight: 600;
    font-size: 14px;
    margin: 8px 0;
}
.feedback-wrong {
    color: #ff3b30;
    font-weight: 600;
    font-size: 14px;
    margin: 8px 0;
}
.progress-bar {
    background: #4b4b6b;
    border-radius: 6px;
    height: 8px;
    margin: 6px 0;
    position: relative;
}
.progress-fill {
    background: var(--button-bg);
    height: 100%;
    border-radius: 6px;
}
.progress-text {
    position: absolute;
    top: -16px;
    right: 0;
    color: var(--text-color);
    font-size: 10px;
}
.title {
    font-size: 24px;
    text-align: center;
    margin-bottom: 5px;
    color: var(--text-color);
}
.caption {
    text-align: center;
    color: #b0b0d0;
    font-size: 12px;
    margin-bottom: 10px;
}
.timer {
    font-size: 12px;
    color: #ff6b6b;
    font-weight: 600;
    text-align: center;
    margin-top: 6px;
}
.difficulty {
    font-size: 11px;
    color: #b0b0d0;
    margin-bottom: 6px;
}
.stCodeBlock, .stCodeBlock pre, .stCodeBlock code {
    background-color: var(--code-bg) !important;
    border-radius: 5px;
    padding: 8px;
    font-family: 'Consolas', monospace;
    font-size: 12px;
    border: 1px solid #4b4b6b;
    color: var(--text-color);
}
@media (max-width: 600px) {
    .main-container {
        padding: 10px;
        margin: 5px;
    }
    .title {
        font-size: 20px;
    }
    .stButton>button {
        font-size: 12px;
        padding: 6px;
    }
}
</style>
""", unsafe_allow_html=True)

# Main UI
try:
    st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}" role="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">🚀 JavaScript Quiz</h1>', unsafe_allow_html=True)
    st.markdown('<p class="caption">Test Your JavaScript Skills!</p>', unsafe_allow_html=True)

    # Theme toggle
    if st.button("🌙 Toggle Theme", key="theme_toggle"):
        toggle_theme()

    # Welcome screen
    if not st.session_state.started:
        st.markdown(f"""
        <div style="text-align: center;">
            <p style="color: var(--text-color); font-size: 14px;">Challenge yourself with {len(quiz)} JavaScript questions!</p>
            <p style="color: #b0b0d0;">{int(30 * len(quiz) / 60)} minutes, 2 points per correct answer.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start Quiz", key="start_quiz"):
            st.session_state.started = True
            st.session_state.start_time = datetime.now()
            st.rerun()
    else:
        # Timer
        if not st.session_state.show_results and not st.session_state.paused:
            update_timer()
            minutes = int(st.session_state.time_left // 60)
            seconds = int(st.session_state.time_left % 60)
            st.markdown(f'<div class="timer" role="timer">⏰ Time Left: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

        # Pause/Resume
        pause_label = "Pause Quiz" if not st.session_state.paused else "Resume Quiz"
        if st.button(pause_label, key="pause_quiz"):
            toggle_pause()

        if not st.session_state.quiz_data:
            st.error("No quiz questions available.")
            st.stop()

        # Progress bar
        progress = st.session_state.current_q / len(st.session_state.quiz_data)
        progress_percentage = progress * 100
        st.markdown(f"""
        <div class="progress-bar" role="progressbar" aria-valuenow="{progress_percentage:.1f}" aria-valuemin="0" aria-valuemax="100">
            <div class="progress-fill" style="width: {progress_percentage}%"></div>
            <div class="progress-text">{progress_percentage:.1f}%</div>
        </div>
        <div style="color: var(--text-color); font-size: 11px; text-align: center;">
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
                if "`" in q["question"]:
                    question_parts = q["question"].split("`")
                    question_text = question_parts[0].strip()
                    code_snippet = question_parts[1].strip() if len(question_parts) > 1 else ""
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{question_text}**")
                    if code_snippet:
                        st.code(code_snippet, language="javascript")
                else:
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{q['question']}**")

                # Option buttons
                for i, option in enumerate(q["display_options"]):
                    button_class = ""
                    if st.session_state.selected_option == option:
                        button_class = "selected-correct" if option == q["labeled_answer"] else "selected-wrong"
                    button_key = f"q_{q['id']}_{i}"
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
                        else:
                            st.session_state.streak = 0
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
                        st.markdown(f'<div style="color: var(--text-color); font-size: 12px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

        else:
            # Results
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 30 * len(quiz)) if st.session_state.start_time else 30 * len(quiz)
            total_possible_score = len(quiz) * 2
            accuracy = (st.session_state.score / total_possible_score) * 100 if total_possible_score > 0 else 0
            st.markdown('<div class="question-container" role="region" aria-label="Results">', unsafe_allow_html=True)
            st.markdown(f'<h2 style="color: #34c759; text-align: center;">🏆 Score: {st.session_state.score}/{total_possible_score}</h2>', unsafe_allow_html=True)
            st.markdown(f"""
            <h3>📊 Results</h3>
            <div style="color: var(--text-color); font-size: 13px;">
                - ⏱️ Time: {int(time_taken) // 60}m {int(time_taken) % 60}s<br>
                - 🎯 Accuracy: {accuracy:.1f}%<br>
                - ✅ Correct: {sum(1 for ans in st.session_state.answers if ans and ans["is_correct"])}<br>
                - ❌ Incorrect: {sum(1 for ans in st.session_state.answers if ans and not ans["is_correct"])}<br>
                - 🔥 Max Streak: {st.session_state.max_streak}
            </div>
            """, unsafe_allow_html=True)

            # Review Answers
            st.markdown('<h3>📝 Review Your Answers</h3>', unsafe_allow_html=True)
            for i, ans in enumerate(st.session_state.answers):
                if ans:
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})"
                    st.markdown(f"""
                    <div style="color: var(--text-color); margin-bottom: 6px;">
                        Question {i+1}: {ans["question"]}<br>
                        Your Answer: {ans["user_answer"]}<br>
                        {status}<br>
                        Explanation: {quiz[i]["explanation"]}
                    </div>
                    """, unsafe_allow_html=True)

            # Play Again
            if st.button("🔄 Play Again", key="play_again"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

except Exception as e:
    st.error(f"An error occurred: {str(e)}. Please try refreshing or running locally.")
    st.markdown("To run locally, save this code as `quiz_app.py` and run `streamlit run quiz_app.py`.")





