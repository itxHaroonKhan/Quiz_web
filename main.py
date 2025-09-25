


import streamlit as st
import random
from datetime import datetime
import uuid

quiz = [
  {
    "question": "What is the output of this code: `function scopeTest() { var x = 1; if (true) { var x = 2; } return x; } console.log(scopeTest());`?",
    "options": [
      "2",
      "1",
      "undefined",
      "ReferenceError"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "'var' is function-scoped, so the inner 'var x = 2' reassigns the same variable, resulting in 2 being returned."
  },
  {
    "question": "What does this jQuery code do: `$(function() { let x = 10; $('.btn').click(function() { let x = 20; console.log(x); }); });` when the button is clicked?",
    "options": [
      "Logs 20",
      "Logs 10",
      "Logs undefined",
      "Throws an error"
    ],
    "answer": "Logs 20",
    "difficulty": "Medium",
    "explanation": "'let x = 20' inside the click handler is block-scoped, so it logs 20, not the outer x (10)."
  },
  {
    "question": "What is the output of: `function test() { let x = 5; { let x = 10; } return x; } console.log(test());`?",
    "options": [
      "5",
      "10",
      "undefined",
      "Error"
    ],
    "answer": "5",
    "difficulty": "Medium",
    "explanation": "The inner 'let x = 10' is block-scoped and doesn’t affect the outer 'let x = 5', so 5 is returned."
  },
  {
    "question": "What does this jQuery code do: `$('#input').val().length >= 3 ? $('#input').addClass('valid') : $('#input').removeClass('valid');`?",
    "options": [
      "Adds or removes 'valid' class based on input length",
      "Sets the input value to 'valid'",
      "Checks if the input is empty",
      "Triggers an event"
    ],
    "answer": "Adds or removes 'valid' class based on input length",
    "difficulty": "Medium",
    "explanation": "The ternary operator checks if the input’s value length is >= 3, adding or removing the 'valid' class accordingly."
  },
  {
    "question": "How do you validate a text field for non-empty input using JavaScript?",
    "options": [
      "if (document.getElementById('input').value.trim() !== '')",
      "if (document.getElementById('input').value === null)",
      "if (document.getElementById('input').length > 0)",
      "if (document.getElementById('input').text !== '')"
    ],
    "answer": "if (document.getElementById('input').value.trim() !== '')",
    "difficulty": "Medium",
    "explanation": "'trim()' removes whitespace, and checking '!== ''' ensures the input isn’t empty."
  },
  {
    "question": "What does this jQuery code do: `$('select#dropdown').val() !== '' ? console.log('Selected') : console.log('Not selected');`?",
    "options": [
      "Logs 'Selected' if dropdown has a value, else 'Not selected'",
      "Sets the dropdown value",
      "Triggers a change event",
      "Checks if dropdown is visible"
    ],
    "answer": "Logs 'Selected' if dropdown has a value, else 'Not selected'",
    "difficulty": "Medium",
    "explanation": "'val()' gets the dropdown’s value; the ternary operator logs based on whether it’s non-empty."
  },
  {
    "question": "How do you check if a radio button is selected using JavaScript?",
    "options": [
      "if (document.querySelector('input[name=group]:checked'))",
      "if (document.getElementsByName('group').checked)",
      "if (document.querySelector('input.group').value)",
      "if (document.getRadio('group').selected)"
    ],
    "answer": "if (document.querySelector('input[name=group]:checked'))",
    "difficulty": "Medium",
    "explanation": "'querySelector' with ':checked' returns the selected radio button or null if none is selected."
  },
  {
    "question": "What is the output of: `$('input[name=group]:checked').length > 0 ? console.log('Checked') : console.log('Not checked');`?",
    "options": [
      "Logs 'Checked' if a radio button is selected, else 'Not checked'",
      "Logs the value of the radio button",
      "Triggers a click event",
      "Throws an error if no radio is selected"
    ],
    "answer": "Logs 'Checked' if a radio button is selected, else 'Not checked'",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'length' checks if a radio button is selected, logging accordingly."
  },
  {
    "question": "What regex validates a ZIP code like 12345 or 12345-6789 in JavaScript?",
    "options": [
      "/^\\d{5}(-\\d{4})?$/",
      "/^\\d{5}$/",
      "/^\\d{5}-\\d{4}$/",
      "/^\\d{9}$/"
    ],
    "answer": "/^\\d{5}(-\\d{4})?$/",
    "difficulty": "Medium",
    "explanation": "The regex matches 5 digits with an optional hyphen and 4 digits."
  },
  {
    "question": "What does this jQuery code do: `$('#email').val().match(/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/) ? $('#email').addClass('valid') : $('#email').removeClass('valid');`?",
    "options": [
      "Validates email and toggles 'valid' class",
      "Sets email field value",
      "Triggers email field event",
      "Clears email field"
    ],
    "answer": "Validates email and toggles 'valid' class",
    "difficulty": "Medium",
    "explanation": "The regex checks for a valid email format, adding or removing the 'valid' class."
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
    "explanation": "Accessing a property on undefined throws a TypeError, caught and logged as 'TypeError'."
  },
  {
    "question": "What does this code do: `try { throw new Error('Invalid input'); } catch (e) { console.log(e.message); }`?",
    "options": [
      "Logs 'Invalid input'",
      "Logs 'Error'",
      "Throws an error",
      "Logs undefined"
    ],
    "answer": "Logs 'Invalid input'",
    "difficulty": "Medium",
    "explanation": "The thrown error’s message is caught and logged as 'Invalid input'."
  },
  {
    "question": "What does this jQuery code do: `$('.btn').on('click', function() { alert('Button clicked'); });`?",
    "options": [
      "Shows an alert on button click",
      "Changes button text",
      "Disables the button",
      "Redirects the page"
    ],
    "answer": "Shows an alert on button click",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'on' method binds a click event handler to show an alert."
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
    "question": "What does this jQuery code do: `$('.test').first().text('New text');`?",
    "options": [
      "Sets the first element with class 'test' to 'New text'",
      "Sets all elements with class 'test' to 'New text'",
      "Appends 'New text' to the first element",
      "Removes the first element"
    ],
    "answer": "Sets the first element with class 'test' to 'New text'",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'first()' selects the first matching element, and 'text()' sets its text content."
  },
  {
    "question": "What does `document.querySelector('div').tagName` return for a <div> element?",
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
    "question": "What is the output of: `let div = document.createElement('div'); div.innerHTML = '<p>1</p><p>2</p>'; console.log(div.children.length);`?",
    "options": [
      "2",
      "1",
      "0",
      "undefined"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "'children.length' counts the two <p> elements as child elements, excluding text nodes."
  },
  {
    "question": "What does this jQuery code do: `$('#box').attr('data-value', 'test');`?",
    "options": [
      "Sets the 'data-value' attribute of #box to 'test'",
      "Gets the 'data-value' attribute",
      "Removes the 'data-value' attribute",
      "Adds a class 'test' to #box"
    ],
    "answer": "Sets the 'data-value' attribute of #box to 'test'",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'attr()' sets the specified attribute to the given value."
  },
  {
    "question": "What is the output of: `let elem = document.createElement('img'); elem.setAttribute('src', 'image.jpg'); console.log(elem.getAttribute('src'));`?",
    "options": [
      "image.jpg",
      "undefined",
      "img",
      "Error"
    ],
    "answer": "image.jpg",
    "difficulty": "Medium",
    "explanation": "'setAttribute()' sets the 'src' attribute, and 'getAttribute()' retrieves it."
  },
  {
    "question": "What does this jQuery code do: `$('<div>Hello</div>').appendTo('#container');`?",
    "options": [
      "Appends a new div with 'Hello' to #container",
      "Replaces #container with a new div",
      "Prepends a div to #container",
      "Removes #container"
    ],
    "answer": "Appends a new div with 'Hello' to #container",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'appendTo()' adds the new div as the last child of #container."
  },
  {
    "question": "What does this code do: `let newNode = document.createElement('p'); document.querySelector('#target').parentNode.insertBefore(newNode, document.querySelector('#target'));`?",
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
    "question": "What does this jQuery code do: `let obj = { name: 'Test' }; $('#output').text(obj.name);`?",
    "options": [
      "Sets #output’s text to 'Test'",
      "Sets #output’s value to 'Test'",
      "Appends 'Test' to #output",
      "Removes #output"
    ],
    "answer": "Sets #output’s text to 'Test'",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'text()' sets the text content of #output to the object’s 'name' property."
  },
  {
    "question": "What is the output of: `let obj = { greet() { return 'Hello'; } }; console.log(obj.greet());`?",
    "options": [
      "Hello",
      "undefined",
      "greet",
      "Error"
    ],
    "answer": "Hello",
    "difficulty": "Medium",
    "explanation": "'greet' is a method that returns 'Hello' when called."
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
    "explanation": "The 'drive' method is added to the prototype, so c.drive() returns 'Driving'."
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
    "question": "What does this jQuery code do: `$('#link').attr('href', 'new-url');`?",
    "options": [
      "Sets the href of #link to 'new-url'",
      "Gets the href of #link",
      "Removes the href attribute",
      "Triggers a click on #link"
    ],
    "answer": "Sets the href of #link to 'new-url'",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'attr()' sets the href attribute to 'new-url'."
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
    "question": "What does this jQuery code do: `$(window).on('popstate', function() { console.log('Navigated'); });`?",
    "options": [
      "Logs 'Navigated' on history navigation",
      "Reloads the page",
      "Triggers a popstate event",
      "Opens a new window"
    ],
    "answer": "Logs 'Navigated' on history navigation",
    "difficulty": "Medium",
    "explanation": "The 'popstate' event fires on forward/back navigation, logging 'Navigated'."
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
    "question": "What does this jQuery code do: `$(window).resize(function() { $('#box').css('width', '50vw'); });`?",
    "options": [
      "Sets #box width to 50% of viewport on window resize",
      "Resizes the window",
      "Sets #box height to 50vw",
      "Triggers a resize event"
    ],
    "answer": "Sets #box width to 50% of viewport on window resize",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'resize' event handler sets #box’s width to '50vw' when the window resizes."
  },
  {
    "question": "What is the output of: `let popup = window.open(''); if (!popup) console.log('Blocked');`?",
    "options": [
      "Logs 'Blocked' if popup is blocked",
      "Opens a new window",
      "Logs 'Blocked' always",
      "Throws an error"
    ],
    "answer": "Logs 'Blocked' if popup is blocked",
    "difficulty": "Medium",
    "explanation": "'window.open()' returns null if a popup blocker prevents the window, triggering the log."
  },
  {
    "question": "What does this jQuery code do: `$('#input').on('input', function() { $(this).val().length >= 5 ? $(this).addClass('valid') : $(this).removeClass('valid'); });`?",
    "options": [
      "Toggles 'valid' class based on input length >= 5",
      "Sets input value to 'valid'",
      "Clears the input",
      "Triggers a keypress event"
    ],
    "answer": "Toggles 'valid' class based on input length >= 5",
    "difficulty": "Medium",
    "explanation": "The 'input' event checks the input’s length, adding/removing 'valid' accordingly."
  },
  {
    "question": "What is the output of: `function test() { let x = 1; if (true) { x = 2; } return x; } console.log(test());`?",
    "options": [
      "2",
      "1",
      "undefined",
      "Error"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "Since there’s no new 'let' in the if block, 'x = 2' reassigns the outer x, returning 2."
  },
  {
    "question": "What does this jQuery code do: `$('select#dropdown').change(function() { $(this).val() !== 'default' ? console.log('Valid') : console.log('Invalid'); });`?",
    "options": [
      "Logs 'Valid' or 'Invalid' based on dropdown selection",
      "Sets dropdown value to 'Valid'",
      "Triggers a change event",
      "Hides the dropdown"
    ],
    "answer": "Logs 'Valid' or 'Invalid' based on dropdown selection",
    "difficulty": "Medium",
    "explanation": "The 'change' event checks if the dropdown’s value isn’t 'default', logging accordingly."
  },
  {
    "question": "What does this code do: `let radios = document.querySelectorAll('input[name=group]'); radios.forEach(r => r.checked = false);`?",
    "options": [
      "Unchecks all radio buttons in the group",
      "Checks all radio buttons",
      "Gets the values of radio buttons",
      "Removes radio buttons"
    ],
    "answer": "Unchecks all radio buttons in the group",
    "difficulty": "Medium",
    "explanation": "The code loops through radio buttons and sets 'checked' to false, unchecking them."
  },
  {
    "question": "What does this jQuery code do: `$('input[name=zip]').val().match(/^\\d{5}$/) ? $('#zip').addClass('valid') : $('#zip').removeClass('valid');`?",
    "options": [
      "Validates a 5-digit ZIP code and toggles 'valid' class",
      "Sets ZIP code value",
      "Triggers a keypress event",
      "Clears the ZIP field"
    ],
    "answer": "Validates a 5-digit ZIP code and toggles 'valid' class",
    "difficulty": "Medium",
    "explanation": "The regex checks for a 5-digit ZIP, adding/removing the 'valid' class."
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
    "question": "What does this jQuery code do: `try { throw new Error('Fail'); } catch (e) { $('#error').text(e.message); }`?",
    "options": [
      "Sets #error’s text to 'Fail'",
      "Logs 'Fail' to console",
      "Throws an error",
      "Clears #error"
    ],
    "answer": "Sets #error’s text to 'Fail'",
    "difficulty": "Medium",
    "explanation": "The thrown error’s message is caught and set as the text of #error using jQuery."
  },
  {
    "question": "What does this code do: `document.querySelector('.btn').addEventListener('mouseover', () => console.log('Hovered'));`?",
    "options": [
      "Logs 'Hovered' when the button is moused over",
      "Logs 'Hovered' on click",
      "Changes button text",
      "Hides the button"
    ],
    "answer": "Logs 'Hovered' when the button is moused over",
    "difficulty": "Medium",
    "explanation": "'addEventListener()' binds a handler to the 'mouseover' event."
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
    "question": "What does this jQuery code do: `$('[data-test]').first().addClass('active');`?",
    "options": [
      "Adds 'active' class to the first element with data-test attribute",
      "Adds 'active' to all elements with data-test",
      "Sets data-test to 'active'",
      "Removes the first element"
    ],
    "answer": "Adds 'active' class to the first element with data-test attribute",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'first()' selects the first matching element, and 'addClass()' applies 'active'."
  },
  {
    "question": "What is the output of: `let p = document.createElement('p'); console.log(p.tagName);`?",
    "options": [
      "P",
      "p",
      "Paragraph",
      "undefined"
    ],
    "answer": "P",
    "difficulty": "Medium",
    "explanation": "'tagName' returns the tag name in uppercase, so 'P' for a <p> element."
  },
  {
    "question": "What does this jQuery code do: `$('#container').children().length > 0 ? $('#container').addClass('has-content') : $('#container').removeClass('has-content');`?",
    "options": [
      "Toggles 'has-content' class based on child elements",
      "Counts all nodes in #container",
      "Adds content to #container",
      "Removes #container"
    ],
    "answer": "Toggles 'has-content' class based on child elements",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'children()' counts HTML child elements, toggling the class accordingly."
  },
  {
    "question": "What does this code do: `let img = document.createElement('img'); img.setAttribute('alt', 'desc'); console.log(img.getAttribute('alt'));`?",
    "options": [
      "Logs 'desc'",
      "Logs 'img'",
      "Logs undefined",
      "Throws an error"
    ],
    "answer": "Logs 'desc'",
    "difficulty": "Medium",
    "explanation": "'setAttribute()' sets the 'alt' attribute, and 'getAttribute()' retrieves it."
  },
  {
    "question": "What does this jQuery code do: `$('#box').removeAttr('data-value');`?",
    "options": [
      "Removes the 'data-value' attribute from #box",
      "Sets 'data-value' to null",
      "Gets 'data-value'",
      "Adds 'data-value' class"
    ],
    "answer": "Removes the 'data-value' attribute from #box",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'removeAttr()' removes the specified attribute."
  },
  {
    "question": "What does this code do: `let div = document.createElement('div'); document.body.appendChild(div);`?",
    "options": [
      "Appends a new div to the body",
      "Replaces the body with a div",
      "Creates a div without adding it",
      "Throws an error"
    ],
    "answer": "Appends a new div to the body",
    "difficulty": "Medium",
    "explanation": "'appendChild()' adds the new div as the last child of the body."
  },
  {
    "question": "What does this jQuery code do: `$('<p>New</p>').insertAfter('#target');`?",
    "options": [
      "Inserts a new <p> after #target",
      "Inserts a new <p> before #target",
      "Replaces #target with a <p>",
      "Appends a <p> to #target"
    ],
    "answer": "Inserts a new <p> after #target",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'insertAfter()' places the new <p> after the #target element."
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
    "question": "What does this jQuery code do: `let obj = { value: 10 }; $('#output').data('value', obj.value);`?",
    "options": [
      "Sets #output’s data-value to 10",
      "Sets #output’s text to 10",
      "Appends 10 to #output",
      "Removes #output"
    ],
    "answer": "Sets #output’s data-value to 10",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'data()' sets a data attribute, storing the object’s value."
  },
  {
    "question": "What does this code do: `let obj = { calc: function() { return 2 * 2; } }; console.log(obj.calc());`?",
    "options": [
      "Logs 4",
      "Logs undefined",
      "Logs 'calc'",
      "Throws an error"
    ],
    "answer": "Logs 4",
    "difficulty": "Medium",
    "explanation": "The 'calc' method returns the result of 2 * 2, which is 4."
  },
  {
    "question": "What does this jQuery code do: `function User(name) { this.name = name; } let u = new User('Bob'); $('#name').text(u.name);`?",
    "options": [
      "Sets #name’s text to 'Bob'",
      "Sets #name’s value to 'Bob'",
      "Appends 'Bob' to #name",
      "Throws an error"
    ],
    "answer": "Sets #name’s text to 'Bob'",
    "difficulty": "Medium",
    "explanation": "The constructor sets 'name', and jQuery’s 'text()' sets #name’s text to 'Bob'."
  },
  {
    "question": "What does this code do: `function Animal() { } Animal.prototype.speak = function() { return 'Sound'; }; let a = new Animal(); console.log(a.speak());`?",
    "options": [
      "Logs 'Sound'",
      "Logs undefined",
      "Logs 'Animal'",
      "Throws an error"
    ],
    "answer": "Logs 'Sound'",
    "difficulty": "Medium",
    "explanation": "The 'speak' method on the prototype returns 'Sound' for the instance."
  },
  {
    "question": "What does this jQuery code do: `let obj = { x: 1 }; if ('x' in obj) { $('#output').text('Has x'); }`?",
    "options": [
      "Sets #output’s text to 'Has x'",
      "Sets #output’s value to 'x'",
      "Logs 'Has x' to console",
      "Throws an error"
    ],
    "answer": "Sets #output’s text to 'Has x'",
    "difficulty": "Medium",
    "explanation": "The 'in' operator checks for 'x', and jQuery’s 'text()' sets #output’s text."
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
    "question": "What does this jQuery code do: `$(window).on('popstate', () => $('#status').text('Navigated'));`?",
    "options": [
      "Sets #status text to 'Navigated' on history navigation",
      "Reloads the page",
      "Triggers a popstate event",
      "Opens a new window"
    ],
    "answer": "Sets #status text to 'Navigated' on history navigation",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'on' binds a handler to 'popstate', updating #status on navigation."
  },
  {
    "question": "What does this code do: `document.documentElement.style.width = '100vw';`?",
    "options": [
      "Sets html element width to full viewport",
      "Sets html element height to full viewport",
      "Hides the html element",
      "Scrolls the page"
    ],
    "answer": "Sets html element width to full viewport",
    "difficulty": "Medium",
    "explanation": "'100vw' sets the html element’s width to the full viewport width."
  },
  {
    "question": "What does this jQuery code do: `$(window).on('resize', () => $('#box').css('height', '50vh'));`?",
    "options": [
      "Sets #box height to 50% of viewport on resize",
      "Resizes the window",
      "Sets #box width to 50vh",
      "Triggers a resize event"
    ],
    "answer": "Sets #box height to 50% of viewport on resize",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'resize' event sets #box’s height to '50vh' when the window resizes."
  },
  {
    "question": "What does this code do: `let win = window.open(''); if (!win) $('#status').text('Popup blocked');`?",
    "options": [
      "Sets #status text to 'Popup blocked' if popup fails",
      "Opens a new window",
      "Logs 'Popup blocked' to console",
      "Throws an error"
    ],
    "answer": "Sets #status text to 'Popup blocked' if popup fails",
    "difficulty": "Medium",
    "explanation": "'window.open()' returns null if blocked, and jQuery sets #status text."
  },
  {
    "question": "What does this jQuery code do: `$('#input').on('input', function() { /^[a-zA-Z]+$/.test($(this).val()) ? $(this).addClass('valid') : $(this).removeClass('valid'); });`?",
    "options": [
      "Toggles 'valid' class if input is alphabetic",
      "Sets input value to alphabetic",
      "Clears the input",
      "Triggers a keypress event"
    ],
    "answer": "Toggles 'valid' class if input is alphabetic",
    "difficulty": "Medium",
    "explanation": "The regex checks for letters, and jQuery toggles the 'valid' class."
  },
  {
    "question": "What is the output of: `function test() { var x = 10; { var x = 20; } return x; } console.log(test());`?",
    "options": [
      "20",
      "10",
      "undefined",
      "Error"
    ],
    "answer": "20",
    "difficulty": "Medium",
    "explanation": "'var' is function-scoped, so the inner 'var x = 20' reassigns the variable, returning 20."
  },
  {
    "question": "What does this jQuery code do: `$('select').on('change', function() { $(this).val() !== '' ? $('#status').text('Selected') : $('#status').text('Empty'); });`?",
    "options": [
      "Sets #status text based on dropdown selection",
      "Sets dropdown value",
      "Triggers a change event",
      "Hides the dropdown"
    ],
    "answer": "Sets #status text based on dropdown selection",
    "difficulty": "Medium",
    "explanation": "jQuery checks the dropdown’s value and updates #status text."
  },
  {
    "question": "What does this code do: `document.querySelector('input[name=group]:checked') ? console.log('Selected') : console.log('Not selected');`?",
    "options": [
      "Logs 'Selected' or 'Not selected' based on radio button",
      "Checks all radio buttons",
      "Sets radio button value",
      "Removes radio buttons"
    ],
    "answer": "Logs 'Selected' or 'Not selected' based on radio button",
    "difficulty": "Medium",
    "explanation": "'querySelector' checks for a selected radio button, logging accordingly."
  },
  {
    "question": "What does this jQuery code do: `$('#zip').on('input', function() { $(this).val().match(/^\\d{9}$/) ? $(this).addClass('valid') : $(this).removeClass('valid'); });`?",
    "options": [
      "Validates a 9-digit ZIP code and toggles 'valid' class",
      "Sets ZIP code value",
      "Triggers a keypress event",
      "Clears the ZIP field"
    ],
    "answer": "Validates a 9-digit ZIP code and toggles 'valid' class",
    "difficulty": "Medium",
    "explanation": "The regex checks for 9 digits, and jQuery toggles the 'valid' class."
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
    "question": "What does this jQuery code do: `try { throw new Error('Error'); } catch (e) { $('#error').text(e.message); }`?",
    "options": [
      "Sets #error’s text to 'Error'",
      "Logs 'Error' to console",
      "Throws an error",
      "Clears #error"
    ],
    "answer": "Sets #error’s text to 'Error'",
    "difficulty": "Medium",
    "explanation": "The thrown error’s message is caught and set as #error’s text."
  },
  {
    "question": "What does this jQuery code do: `$('.box').on('dblclick', function() { $(this).toggleClass('active'); });`?",
    "options": [
      "Toggles 'active' class on double-click",
      "Adds 'active' class on click",
      "Removes 'active' class",
      "Triggers a click event"
    ],
    "answer": "Toggles 'active' class on double-click",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'toggleClass()' adds or removes 'active' on double-click."
  },
  {
    "question": "What is the output of: `let div = document.createElement('div'); console.log(div.nodeType);`?",
    "options": [
      "1",
      "3",
      "8",
      "9"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "An element node like a div has a 'nodeType' of 1."
  },
  {
    "question": "What does this jQuery code do: `$('.test[data-value="1"]').addClass('selected');`?",
    "options": [
      "Adds 'selected' class to elements with data-value='1'",
      "Sets data-value to 'selected'",
      "Removes elements with data-value='1'",
      "Triggers an event"
    ],
    "answer": "Adds 'selected' class to elements with data-value='1'",
    "difficulty": "Medium",
    "explanation": "jQuery selects elements with the specified data attribute and adds 'selected'."
  },
  {
    "question": "What does this code do: `let elem = document.querySelector('#box'); elem.parentNode.removeChild(elem);`?",
    "options": [
      "Removes #box from the DOM",
      "Hides #box",
      "Replaces #box",
      "Appends #box"
    ],
    "answer": "Removes #box from the DOM",
    "difficulty": "Medium",
    "explanation": "'removeChild()' removes the specified element from its parent."
  },
  {
    "question": "What does this jQuery code do: `$('#box').attr('title') ? $('#box').removeAttr('title') : $('#box').attr('title', 'Tooltip');`?",
    "options": [
      "Toggles the 'title' attribute on #box",
      "Sets 'title' to 'Tooltip' always",
      "Removes #box",
      "Gets the 'title' value"
    ],
    "answer": "Toggles the 'title' attribute on #box",
    "difficulty": "Medium",
    "explanation": "If 'title' exists, it’s removed; otherwise, it’s set to 'Tooltip'."
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
    "question": "What does this jQuery code do: `let obj = { count: 5 }; $('#count').text(obj.count);`?",
    "options": [
      "Sets #count’s text to 5",
      "Sets #count’s value to 5",
      "Appends 5 to #count",
      "Removes #count"
    ],
    "answer": "Sets #count’s text to 5",
    "difficulty": "Medium",
    "explanation": "jQuery’s 'text()' sets #count’s text to the object’s 'count' property."
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
    "question": "What does this jQuery code do: `$('#form').on('submit', function(e) { e.preventDefault(); $('#status').text('Submitted'); });`?",
    "options": [
      "Prevents form submission and sets #status to 'Submitted'",
      "Submits the form",
      "Clears the form",
      "Triggers a click event"
    ],
    "answer": "Prevents form submission and sets #status to 'Submitted'",
    "difficulty": "Medium",
    "explanation": "'preventDefault()' stops the form submission, and 'text()' updates #status."
  },
  {
    "question": "What does this code do: `document.querySelector('#input').value = 'test'; console.log(document.querySelector('#input').value);`?",
    "options": [
      "Logs 'test'",
      "Logs undefined",
      "Logs 'input'",
      "Throws an error"
    ],
    "answer": "Logs 'test'",
    "difficulty": "Medium",
    "explanation": "The code sets the input’s value to 'test' and logs it."
  },
  {
    "question": "What does this jQuery code do: `$('input[name=email]').on('input', function() { $(this).val().match(/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/) ? $(this).addClass('valid') : $(this).removeClass('valid'); });`?",
    "options": [
      "Validates email and toggles 'valid' class",
      "Sets email value",
      "Triggers a keypress event",
      "Clears the email field"
    ],
    "answer": "Validates email and toggles 'valid' class",
    "difficulty": "Medium",
    "explanation": "The regex validates the email, and jQuery toggles the 'valid' class."
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












