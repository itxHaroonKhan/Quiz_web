import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Quiz data - Enhanced with more questions
quiz =[
    {
        "question": "What is the output of: ```javascript\nfunction test() { var x = 1; if (true) { var x = 2; } console.log(x); }\ntest();```",
        "options": ["1", "2", "undefined", "ReferenceError"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "'var' is function-scoped, so the inner 'var x = 2' reassigns the same variable, logging 2.",
        "category": "Variable Scoping"
    },
    {
        "question": "What is the output of: ```javascript\nlet x = 10; { let x = 20; } console.log(x);```",
        "options": ["10", "20", "undefined", "Error"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "'let' is block-scoped, so the inner 'let x = 20' creates a new variable, and the outer x remains 10.",
        "category": "Variable Scoping"
    },
    {
        "question": "What happens when a variable is declared with 'const' in a block?",
        "options": ["Global scope", "Block scope", "Function scope", "Causes an error"],
        "answer": "Block scope",
        "difficulty": "Easy",
        "explanation": "'const' is block-scoped, so the variable is only accessible within the block.",
        "category": "Variable Scoping"
    },
    {
        "question": "What is the output of: ```javascript\nfunction example() { console.log(x); var x = 5; }\nexample();```",
        "options": ["5", "undefined", "ReferenceError", "null"],
        "answer": "undefined",
        "difficulty": "Medium",
        "explanation": "Due to hoisting, 'var x' is declared but not initialized, so it logs 'undefined'.",
        "category": "Variable Scoping"
    },
    {
        "question": "What is the scope of a variable declared without a keyword in a function?",
        "options": ["Block scope", "Function scope", "Global scope", "Module scope"],
        "answer": "Global scope",
        "difficulty": "Medium",
        "explanation": "Without 'var', 'let', or 'const', a variable is implicitly global.",
        "category": "Variable Scoping"
    },
    {
        "question": "What is the output of: ```javascript\n{ var x = 1; } console.log(x);``` in non-strict mode?",
        "options": ["1", "undefined", "ReferenceError", "null"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "In non-strict mode, 'var' declarations in a block are hoisted to the global or function scope.",
        "category": "Variable Scoping"
    },
    {
        "question": "What is the output of: ```javascript\nfunction foo() { if (false) { let x = 1; } console.log(x); }\nfoo();```",
        "options": ["1", "undefined", "ReferenceError", "null"],
        "answer": "ReferenceError",
        "difficulty": "Medium",
        "explanation": "'let' is block-scoped, so 'x' is not accessible outside the 'if' block, causing a ReferenceError.",
        "category": "Variable Scoping"
    },
    {
        "question": "What is the output of: ```javascript\nvar x = 10; function test() { var x = 20; console.log(x); }\ntest(); console.log(x);```",
        "options": ["20, 10", "10, 20", "20, 20", "ReferenceError"],
        "answer": "20, 10",
        "difficulty": "Medium",
        "explanation": "The inner 'var x' is function-scoped, so 'test' logs 20, while the outer 'x' remains 10.",
        "category": "Variable Scoping"
    },
    {
        "question": "What is the output of: ```javascript\nlet x = 5; function test() { console.log(x); let x = 10; }\ntest();```",
        "options": ["5", "10", "undefined", "ReferenceError"],
        "answer": "ReferenceError",
        "difficulty": "Hard",
        "explanation": "'let' declarations are hoisted but not initialized, causing a temporal dead zone error.",
        "category": "Variable Scoping"
    },
    {
        "question": "What is the output of: ```javascript\nconst x = 1; { const x = 2; console.log(x); } console.log(x);```",
        "options": ["2, 1", "1, 2", "2, 2", "ReferenceError"],
        "answer": "2, 1",
        "difficulty": "Medium",
        "explanation": "'const' is block-scoped, so the inner 'x' is separate from the outer 'x'.",
        "category": "Variable Scoping"
    },
    {
        "question": "How do you validate a drop-down menu has a selected option?",
        "options": ["select.value !== ''", "select.selectedIndex !== -1", "select.options === null", "select.text !== undefined"],
        "answer": "select.selectedIndex !== -1",
        "difficulty": "Easy",
        "explanation": "'selectedIndex' is -1 when no option is selected, making it a reliable check.",
        "category": "Form validation: drop-downs"
    },
    {
        "question": "What does select.options[select.selectedIndex].value return?",
        "options": ["Selected option’s text", "Selected option’s value", "Selected index", "Entire select element"],
        "answer": "Selected option’s value",
        "difficulty": "Medium",
        "explanation": "It retrieves the 'value' attribute of the selected option.",
        "category": "Form validation: drop-downs"
    },
    {
        "question": "How do you get the text of a selected drop-down option?",
        "options": ["select.options[select.selectedIndex].text", "select.value.text", "select.text", "select.options.text"],
        "answer": "select.options[select.selectedIndex].text",
        "difficulty": "Medium",
        "explanation": "The 'text' property of the selected option returns its visible text.",
        "category": "Form validation: drop-downs"
    },
    {
        "question": "How do you ensure a drop-down has a valid selection?",
        "options": ["Check select.value.length > 0", "Check select.selectedIndex > 0", "Check select.options.length", "Check select.value !== 'default'"],
        "answer": "Check select.value !== 'default'",
        "difficulty": "Medium",
        "explanation": "A common approach is to set a 'default' value for the first option and check against it.",
        "category": "Form validation: drop-downs"
    },
    {
        "question": "What happens if select.selectedIndex is -1?",
        "options": ["No option is selected", "First option is selected", "Last option is selected", "Error occurs"],
        "answer": "No option is selected",
        "difficulty": "Easy",
        "explanation": "'selectedIndex' is -1 when no option is selected in a drop-down.",
        "category": "Form validation: drop-downs"
    },
    {
        "question": "How do you check if a radio button group has a selection?",
        "options": ["document.querySelector('input[name=group]:checked')", "document.getElementById('group').checked", "document.getElementsByName('group').value", "document.querySelector('input[type=radio]').value"],
        "answer": "document.querySelector('input[name=group]:checked')",
        "difficulty": "Medium",
        "explanation": "Using ':checked' selects the checked radio button in the group, or null if none is selected.",
        "category": "Form validation: radio buttons"
    },
    {
        "question": "How do you get the value of a selected radio button?",
        "options": ["document.querySelector('input[type=radio]:checked').value", "document.getElementById('radio').value", "document.getElementsByName('radio').value", "document.querySelector('input[type=radio]').value"],
        "answer": "document.querySelector('input[type=radio]:checked').value",
        "difficulty": "Medium",
        "explanation": "':checked' selects the radio button that is currently selected, and '.value' gets its value.",
        "category": "Form validation: radio buttons"
    },
    {
        "question": "What happens if no radio button is selected in a group?",
        "options": ["First radio’s value is returned", "null is returned", "undefined is returned", "An error occurs"],
        "answer": "null is returned",
        "difficulty": "Medium",
        "explanation": "If no radio button is checked, 'querySelector(':checked')' returns null.",
        "category": "Form validation: radio buttons"
    },
    {
        "question": "How do you loop through radio buttons to check for a selection?",
        "options": ["Use document.getElementsByName('group') and check .checked", "Use document.querySelectorAll('input') and check .value", "Use document.getElementsByClassName('radio')", "Use document.getElementById('group')"],
        "answer": "Use document.getElementsByName('group') and check .checked",
        "difficulty": "Medium",
        "explanation": "Radio buttons with the same 'name' are grouped, and '.checked' indicates selection.",
        "category": "Form validation: radio buttons"
    },
    {
        "question": "What does document.getElementsByName('group')[0].checked return?",
        "options": ["true if first radio is checked", "The value of the first radio", "The name of the group", "null"],
        "answer": "true if first radio is checked",
        "difficulty": "Easy",
        "explanation": "'.checked' returns true if the radio button is selected, false otherwise.",
        "category": "Form validation: radio buttons"
    },
    {
        "question": "Which regex validates a US ZIP code (5 digits or 5+4)?",
        "options": ["/^\\d{5}(-\\d{4})?$/", "/^\\d{5}$/", "/^\\d{5}-\\d{4}$/", "/^[0-9]{5,9}$/"],
        "answer": "/^\\d{5}(-\\d{4})?$/",
        "difficulty": "Medium",
        "explanation": "This pattern allows 5 digits optionally followed by a hyphen and 4 digits.",
        "category": "Form validation: ZIP codes"
    },
    {
        "question": "What does the regex /^\\d{5}$/ validate?",
        "options": ["5-digit ZIP code", "5 or 9-digit ZIP code", "Any numeric string", "ZIP with letters"],
        "answer": "5-digit ZIP code",
        "difficulty": "Easy",
        "explanation": "The pattern matches exactly 5 digits, suitable for basic US ZIP codes.",
        "category": "Form validation: ZIP codes"
    },
    {
        "question": "What does the regex /^\\d{5}-\\d{4}$/ validate?",
        "options": ["5-digit ZIP code", "9-digit ZIP code", "5 or 9-digit ZIP code", "Any ZIP code"],
        "answer": "9-digit ZIP code",
        "difficulty": "Medium",
        "explanation": "This pattern requires 5 digits, a hyphen, and 4 digits, matching ZIP+4 format.",
        "category": "Form validation: ZIP codes"
    },
    {
        "question": "How do you test if a ZIP code input matches a regex?",
        "options": ["regex.test(input.value)", "input.match(regex)", "regex.exec(input)", "input.validate(regex)"],
        "answer": "regex.test(input.value)",
        "difficulty": "Medium",
        "explanation": "'regex.test()' returns true if the input string matches the regex pattern.",
        "category": "Form validation: ZIP codes"
    },
    {
        "question": "What does /^\\d{5}(-\\d{4})?$/ allow in a ZIP code?",
        "options": ["5 digits or 5+4 digits", "Only 5 digits", "Only 9 digits", "Any digits"],
        "answer": "5 digits or 5+4 digits",
        "difficulty": "Medium",
        "explanation": "The optional '(-\\d{4})?' allows either a 5-digit or 5+4-digit ZIP code.",
        "category": "Form validation: ZIP codes"
    },
    {
        "question": "Which regex is best for validating an email address?",
        "options": ["/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/", "/^\\w+@\\w+\\.\\w+$/", "/^[a-zA-Z0-9]+@[a-zA-Z0-9]+\\.[a-zA-Z]{2}$/", "/^.*@.*\\..*$/"],
        "answer": "/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/",
        "difficulty": "Hard",
        "explanation": "This regex supports common email formats with a valid domain and TLD.",
        "category": "Form validation: email"
    },
    {
        "question": "What happens if an email input fails custom regex validation?",
        "options": ["Form submission stops", "Browser shows an error", "Nothing, unless handled", "Input is cleared"],
        "answer": "Nothing, unless handled",
        "difficulty": "Medium",
        "explanation": "Custom regex validation requires JavaScript to handle invalid input explicitly.",
        "category": "Form validation: email"
    },
    {
        "question": "How do you validate an email using HTML5?",
        "options": ["<input type='email'>", "<input type='text' pattern='email'>", "<input type='email' regex='...'>", "<input type='text' validate='email'>"],
        "answer": "<input type='email'>",
        "difficulty": "Easy",
        "explanation": "The 'email' input type triggers browser-native email validation.",
        "category": "Form validation: email"
    },
    {
        "question": "What does input.checkValidity() do for an email input?",
        "options": ["Checks if the input matches email format", "Clears the input", "Submits the form", "Returns the input’s value"],
        "answer": "Checks if the input matches email format",
        "difficulty": "Medium",
        "explanation": "'checkValidity()' returns true if the input meets HTML5 validation rules.",
        "category": "Form validation: email"
    },
    {
        "question": "What does /^\\w+@\\w+\\.\\w+$/ miss in email validation?",
        "options": ["Special characters like ._%+-", "Multiple domain levels", "TLD length validation", "All of the above"],
        "answer": "All of the above",
        "difficulty": "Hard",
        "explanation": "This simple regex misses special characters, subdomains, and longer TLDs.",
        "category": "Form validation: email"
    },
    {
        "question": "What does a 'try...catch' block do?",
        "options": ["Declares variables", "Handles errors", "Loops through arrays", "Defines functions"],
        "answer": "Handles errors",
        "difficulty": "Easy",
        "explanation": "'try...catch' catches exceptions thrown in the 'try' block and handles them in 'catch'.",
        "category": "Exceptions: try and catch"
    },
    {
        "question": "What is logged in: ```javascript\ntry { throw new Error('Oops'); } catch (e) { console.log(e.message); }```",
        "options": ["Oops", "Error", "undefined", "null"],
        "answer": "Oops",
        "difficulty": "Medium",
        "explanation": "The error’s message 'Oops' is caught and logged in the 'catch' block.",
        "category": "Exceptions: try and catch"
    },
    {
        "question": "What happens if no error is thrown in a 'try' block?",
        "options": ["Catch block is skipped", "Catch block runs", "Error occurs", "Try block loops"],
        "answer": "Catch block is skipped",
        "difficulty": "Easy",
        "explanation": "If no exception occurs, the 'catch' block is not executed.",
        "category": "Exceptions: try and catch"
    },
    {
        "question": "What does 'finally' do in a try...catch...finally block?",
        "options": ["Runs after try or catch", "Catches errors", "Throws errors", "Loops the try block"],
        "answer": "Runs after try or catch",
        "difficulty": "Medium",
        "explanation": "The 'finally' block executes regardless of whether an error was thrown or caught.",
        "category": "Exceptions: try and catch"
    },
    {
        "question": "What does the 'throw' statement do?",
        "options": ["Exits a function", "Throws an exception", "Logs a message", "Declares a variable"],
        "answer": "Throws an exception",
        "difficulty": "Easy",
        "explanation": "'throw' creates and throws a custom exception for error handling.",
        "category": "Exceptions: throw"
    },
    {
        "question": "What is thrown in: ```javascript\nthrow 'CustomError';```?",
        "options": ["A string", "An Error object", "A function", "A variable"],
        "answer": "A string",
        "difficulty": "Medium",
        "explanation": "'throw' can throw any value, like a string, which is caught in a 'catch' block.",
        "category": "Exceptions: throw"
    },
    {
        "question": "What is the output of: ```javascript\ntry { throw 42; } catch (e) { console.log(e); }```",
        "options": ["42", "Error", "undefined", "null"],
        "answer": "42",
        "difficulty": "Medium",
        "explanation": "'throw 42' throws the number 42, which is caught and logged.",
        "category": "Exceptions: throw"
    },
    {
        "question": "How do you add a click event listener to a button?",
        "options": ["button.addEventListener('click', handler)", "button.onClick(handler)", "button.attachEvent('click', handler)", "button.event('click', handler)"],
        "answer": "button.addEventListener('click', handler)",
        "difficulty": "Easy",
        "explanation": "'addEventListener' attaches an event handler for the specified event.",
        "category": "Handling events within JavaScript"
    },
    {
        "question": "What does 'event.preventDefault()' do?",
        "options": ["Stops event propagation", "Prevents default action", "Removes event listener", "Logs the event"],
        "answer": "Prevents default action",
        "difficulty": "Medium",
        "explanation": "'preventDefault()' stops the browser’s default action, like form submission.",
        "category": "Handling events within JavaScript"
    },
    {
        "question": "What does 'event.stopPropagation()' do?",
        "options": ["Prevents default action", "Stops event bubbling", "Removes the event", "Triggers the event"],
        "answer": "Stops event bubbling",
        "difficulty": "Medium",
        "explanation": "'stopPropagation()' prevents the event from bubbling up to parent elements.",
        "category": "Handling events within JavaScript"
    },
    {
        "question": "What is the nodeType of a comment in the DOM?",
        "options": ["1", "3", "8", "9"],
        "answer": "8",
        "difficulty": "Medium",
        "explanation": "Comment nodes have a nodeType of 8, while elements are 1 and text nodes are 3.",
        "category": "The DOM: Junk artifacts and nodeType"
    },
    {
        "question": "What is a 'junk artifact' in the DOM?",
        "options": ["A text node", "A comment node", "An element node", "A script node"],
        "answer": "A comment node",
        "difficulty": "Medium",
        "explanation": "Comment nodes (nodeType 8) are considered junk artifacts as they don’t affect rendering.",
        "category": "The DOM: Junk artifacts and nodeType"
    },
    {
        "question": "What is the nodeType of a text node?",
        "options": ["1", "3", "8", "9"],
        "answer": "3",
        "difficulty": "Easy",
        "explanation": "Text nodes have a nodeType of 3 in the DOM.",
        "category": "The DOM: Junk artifacts and nodeType"
    },
    {
        "question": "How do you select an element by ID?",
        "options": ["document.querySelector('#id')", "document.getElementById('id')", "document.getElementsByClassName('id')", "Both A and B"],
        "answer": "Both A and B",
        "difficulty": "Easy",
        "explanation": "Both 'getElementById' and 'querySelector' can select an element by ID.",
        "category": "The DOM: More ways to target elements"
    },
    {
        "question": "How do you select all elements with class 'example'?",
        "options": ["document.querySelectorAll('.example')", "document.getElementsByClassName('example')", "document.getElementsByTagName('example')", "Both A and B"],
        "answer": "Both A and B",
        "difficulty": "Medium",
        "explanation": "Both methods return collections of elements with the specified class.",
        "category": "The DOM: More ways to target elements"
    },
    {
        "question": "What does element.tagName return for a <p> element?",
        "options": ["p", "P", "<p>", "null"],
        "answer": "P",
        "difficulty": "Easy",
        "explanation": "'tagName' returns the tag name in uppercase, like 'P' for a <p> element.",
        "category": "The DOM: Getting a target's name"
    },
    {
        "question": "What is the difference between element.tagName and element.nodeName?",
        "options": ["They are identical", "tagName is lowercase", "nodeName includes text nodes", "tagName is for attributes"],
        "answer": "They are identical",
        "difficulty": "Medium",
        "explanation": "For elements, 'tagName' and 'nodeName' both return the uppercase tag name.",
        "category": "The DOM: Getting a target's name"
    },
    {
        "question": "How do you count all <div> elements in a document?",
        "options": ["document.getElementsByTagName('div').length", "document.querySelector('div').count", "document.getElementsByClassName('div').length", "document.querySelectorAll('div').count"],
        "answer": "document.getElementsByTagName('div').length",
        "difficulty": "Easy",
        "explanation": "'getElementsByTagName' returns an HTMLCollection, and '.length' counts the elements.",
        "category": "The DOM: Counting elements"
    },
    {
        "question": "What does document.querySelectorAll('p').length return?",
        "options": ["Number of <p> elements", "Number of all elements", "Number of classes", "Number of attributes"],
        "answer": "Number of <p> elements",
        "difficulty": "Easy",
        "explanation": "'querySelectorAll('p')' returns a NodeList, and '.length' counts the <p> elements.",
        "category": "The DOM: Counting elements"
    },
    {
        "question": "How do you check if an element has an attribute?",
        "options": ["element.hasAttribute('attr')", "element.getAttribute('attr')", "element.attribute('attr')", "element.checkAttribute('attr')"],
        "answer": "element.hasAttribute('attr')",
        "difficulty": "Easy",
        "explanation": "'hasAttribute' returns true if the element has the specified attribute.",
        "category": "The DOM: Attributes"
    },
    {
        "question": "How do you set an attribute on an element?",
        "options": ["element.setAttribute('name', 'value')", "element.attribute('name', 'value')", "element.name = 'value'", "element.addAttribute('name', 'value')"],
        "answer": "element.setAttribute('name', 'value')",
        "difficulty": "Easy",
        "explanation": "'setAttribute' sets or updates an attribute’s value on an element.",
        "category": "The DOM: Attributes"
    },
    {
        "question": "How do you get all attribute names of an element?",
        "options": ["element.getAttributeNames()", "element.attributes.map(attr => attr.name)", "Array.from(element.attributes).map(attr => attr.name)", "Both A and C"],
        "answer": "Both A and C",
        "difficulty": "Medium",
        "explanation": "'getAttributeNames()' or mapping 'element.attributes' returns an array of attribute names.",
        "category": "The DOM: Attribute names and values"
    },
    {
        "question": "What does element.getAttribute('id') return if no ID exists?",
        "options": ["''", "null", "undefined", "Error"],
        "answer": "null",
        "difficulty": "Medium",
        "explanation": "'getAttribute' returns null if the specified attribute doesn’t exist.",
        "category": "The DOM: Attribute names and values"
    },
    {
        "question": "How do you create a new DOM element?",
        "options": ["document.createElement('tag')", "document.newElement('tag')", "document.createNode('tag')", "document.addElement('tag')"],
        "answer": "document.createElement('tag')",
        "difficulty": "Easy",
        "explanation": "'createElement' creates a new DOM element with the specified tag.",
        "category": "The DOM: Adding nodes"
    },
    {
        "question": "What does document.createElement('span') return?",
        "options": ["A new span element", "A text node", "A comment node", "An attribute"],
        "answer": "A new span element",
        "difficulty": "Easy",
        "explanation": "'createElement('span')' returns a new <span> element, not yet in the DOM.",
        "category": "The DOM: Adding nodes"
    },
    {
        "question": "How do you append a node to an element’s children?",
        "options": ["element.appendChild(node)", "element.addChild(node)", "element.insertChild(node)", "element.append(node)"],
        "answer": "element.appendChild(node)",
        "difficulty": "Easy",
        "explanation": "'appendChild' adds a node as the last child of the element.",
        "category": "The DOM: Inserting nodes"
    },
    {
        "question": "How do you insert a node before an existing child?",
        "options": ["parent.insertBefore(newNode, existingNode)", "parent.insertChild(newNode, existingNode)", "parent.addBefore(newNode, existingNode)", "parent.prepend(newNode)"],
        "answer": "parent.insertBefore(newNode, existingNode)",
        "difficulty": "Medium",
        "explanation": "'insertBefore' inserts a new node before the specified existing child.",
        "category": "The DOM: Inserting nodes"
    },
    {
        "question": "What is a JavaScript object?",
        "options": ["A collection of properties", "A function", "A variable", "A DOM element"],
        "answer": "A collection of properties",
        "difficulty": "Easy",
        "explanation": "Objects are collections of key-value pairs, where values can be data or functions.",
        "category": "Objects"
    },
    {
        "question": "How do you access an object’s property?",
        "options": ["object.property or object['property']", "object.getProperty()", "object(property)", "object->property"],
        "answer": "object.property or object['property']",
        "difficulty": "Easy",
        "explanation": "Properties are accessed using dot or bracket notation.",
        "category": "Objects: Properties"
    },
    {
        "question": "How do you add a method to an object?",
        "options": ["object.method = function() {}", "object.addMethod(function)", "object.method(function)", "object.setMethod()"],
        "answer": "object.method = function() {}",
        "difficulty": "Easy",
        "explanation": "A method is added by assigning a function to an object property.",
        "category": "Objects: Methods"
    },
    {
        "question": "What is a constructor in JavaScript?",
        "options": ["A function to create objects", "A loop", "An event handler", "A variable"],
        "answer": "A function to create objects",
        "difficulty": "Medium",
        "explanation": "Constructors are functions used with 'new' to create and initialize objects.",
        "category": "Objects: Constructors"
    },
    {
        "question": "What is the output of: ```javascript\nfunction Person(name) { this.name = name; }\nlet p = new Person('Alice');\nconsole.log(p.name);```",
        "options": ["Alice", "Person", "undefined", "null"],
        "answer": "Alice",
        "difficulty": "Medium",
        "explanation": "The constructor sets the 'name' property, and 'new' creates an object with it.",
        "category": "Objects: Constructors"
    },
    {
        "question": "How do you add a method to a constructor’s prototype?",
        "options": ["Constructor.prototype.method = function() {}", "Constructor.method = function() {}", "Constructor.addMethod()", "Constructor.setMethod()"],
        "answer": "Constructor.prototype.method = function() {}",
        "difficulty": "Medium",
        "explanation": "Prototype methods are shared by all instances of the constructor.",
        "category": "Objects: Constructors for methods"
    },
    {
        "question": "What is a prototype in JavaScript?",
        "options": ["An object for inheritance", "A function", "A variable", "A DOM node"],
        "answer": "An object for inheritance",
        "difficulty": "Medium",
        "explanation": "Prototypes allow objects to inherit properties and methods from another object.",
        "category": "Objects: Prototypes"
    },
    {
        "question": "How do you check if an object has a property?",
        "options": ["'property' in object", "object.hasProperty('property')", "object.propertyExists('property')", "object.getProperty('property')"],
        "answer": "'property' in object",
        "difficulty": "Medium",
        "explanation": "The 'in' operator checks for a property in an object or its prototype chain.",
        "category": "Objects: Checking for properties and methods"
    },
    {
        "question": "How do you check if a property is directly on an object?",
        "options": ["object.hasOwnProperty('property')", "object.owns('property')", "object.property('property')", "'property' in object"],
        "answer": "object.hasOwnProperty('property')",
        "difficulty": "Medium",
        "explanation": "'hasOwnProperty' checks for properties directly on the object, not inherited.",
        "category": "Objects: Checking for properties and methods"
    },
    {
        "question": "How do you get the current URL of a page?",
        "options": ["window.location.href", "document.url", "window.url", "document.location"],
        "answer": "window.location.href",
        "difficulty": "Easy",
        "explanation": "'window.location.href' returns the full URL of the current page.",
        "category": "Browser control: Getting and setting the URL"
    },
    {
        "question": "How do you navigate to a new URL?",
        "options": ["window.location.href = 'new-url'", "window.url = 'new-url'", "document.location('new-url')", "window.setUrl('new-url')"],
        "answer": "window.location.href = 'new-url'",
        "difficulty": "Easy",
        "explanation": "Assigning to 'window.location.href' navigates to the new URL.",
        "category": "Browser control: Getting and setting the URL"
    },
    {
        "question": "What does window.location.assign('new-url') do?",
        "options": ["Navigates to a new URL", "Reloads the page", "Clears the URL", "Opens a popup"],
        "answer": "Navigates to a new URL",
        "difficulty": "Medium",
        "explanation": "'assign' navigates to a new URL, similar to setting 'href'.",
        "category": "Browser control: Getting and setting the URL another way"
    },
    {
        "question": "How do you go back in browser history?",
        "options": ["window.history.back()", "window.back()", "window.history.prev()", "window.location.back()"],
        "answer": "window.history.back()",
        "difficulty": "Easy",
        "explanation": "'window.history.back()' navigates to the previous page in history.",
        "category": "Browser control: Forward and reverse"
    },
    {
        "question": "How do you go forward in browser history?",
        "options": ["window.history.forward()", "window.forward()", "window.history.next()", "window.location.forward()"],
        "answer": "window.history.forward()",
        "difficulty": "Easy",
        "explanation": "'window.history.forward()' navigates to the next page in history.",
        "category": "Browser control: Forward and reverse"
    },
    {
        "question": "How do you set the entire page content?",
        "options": ["document.body.innerHTML = 'content'", "window.content = 'content'", "document.write('content')", "Both A and C"],
        "answer": "Both A and C",
        "difficulty": "Medium",
        "explanation": "Both 'innerHTML' and 'document.write' can set the page’s content.",
        "category": "Browser control: Filling the window with content"
    },
    {
        "question": "How do you resize a browser window?",
        "options": ["window.resizeTo(width, height)", "window.setSize(width, height)", "window.size(width, height)", "document.resize(width, height)"],
        "answer": "window.resizeTo(width, height)",
        "difficulty": "Medium",
        "explanation": "'window.resizeTo' resizes the browser window to specified dimensions.",
        "category": "Browser control: Controlling the window's size and location"
    },
    {
        "question": "How do you move a window to a position?",
        "options": ["window.moveTo(x, y)", "window.setPosition(x, y)", "window.location(x, y)", "window.move(x, y)"],
        "answer": "window.moveTo(x, y)",
        "difficulty": "Medium",
        "explanation": "'window.moveTo' moves the browser window to the specified coordinates.",
        "category": "Browser control: Controlling the window's size and location"
    },
    {
        "question": "How do you detect a popup blocker?",
        "options": ["Check if window.open() returns null", "Check window.popupBlocked", "Check document.popup", "Check window.isBlocked"],
        "answer": "Check if window.open() returns null",
        "difficulty": "Medium",
        "explanation": "If 'window.open()' returns null, the popup was blocked.",
        "category": "Browser control: Testing for popup blockers"
    },
    {
        "question": "How do you validate a text field is not empty?",
        "options": ["input.value.trim() !== ''", "input.text !== ''", "input.value.length > 0", "Both A and C"],
        "answer": "Both A and C",
        "difficulty": "Easy",
        "explanation": "Both checks validate a non-empty field, with 'trim()' handling whitespace.",
        "category": "Form validation: text fields"
    },
    {
        "question": "What does input.value.trim() do?",
        "options": ["Removes whitespace from both ends", "Converts to lowercase", "Removes special characters", "Checks for numbers"],
        "answer": "Removes whitespace from both ends",
        "difficulty": "Easy",
        "explanation": "'trim()' removes leading and trailing whitespace from a string.",
        "category": "Form validation: text fields"
    }
]

# Enhanced CSS with better styling
st.markdown("""
<style>
:root {
    --primary: #6b21a8;
    --primary-hover: #8b5cf6;
    --success: #34c759;
    --danger: #ff3b30;
    --warning: #ff9500;
    --info: #007aff;
    --dark: #1a1a3b;
    --light: #f3e8ff;
}

body {
    background: linear-gradient(135deg, var(--dark) 0%, #2c2c54 100%);
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

[data-theme="light"] {
    --bg-gradient: linear-gradient(135deg, #e0e7ff 0%, #f3e8ff 100%);
    --text-color: #1f2937;
    --card-bg: #ffffff;
}

[data-theme="dark"] {
    --bg-gradient: linear-gradient(135deg, #1a1a3b 0%, #2c2c54 100%);
    --text-color: #ffffff;
    --card-bg: #2c2c54;
}

.main-container {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    margin: 1rem auto;
    max-width: 900px;
    color: var(--text-color);
}

.title {
    text-align: center;
    font-size: 2.5rem;
    background: linear-gradient(90deg, var(--primary), var(--info));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: var(--text-color);
    opacity: 0.8;
    margin-bottom: 2rem;
}

.stButton>button {
    background: var(--primary);
    color: white;
    border: none;
    border-radius: 0.75rem;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s ease;
    margin: 0.5rem 0;
    width: 100%;
}

.stButton>button:hover {
    background: var(--primary-hover);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.option-button {
    background: rgba(107, 33, 168, 0.1) !important;
    border: 2px solid var(--primary) !important;
    color: var(--text-color) !important;
}

.option-button:hover {
    background: var(--primary) !important;
    color: white !important;
}

.selected-correct {
    background: var(--success) !important;
    color: white !important;
    border: 2px solid var(--success) !important;
}

.selected-wrong {
    background: var(--danger) !important;
    color: white !important;
    border: 2px solid var(--danger) !important;
}

.difficulty-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.8rem;
    font-weight: bold;
    margin: 0.5rem 0;
}

.easy { background: var(--success); color: white; }
.medium { background: var(--warning); color: white; }
.hard { background: var(--danger); color: white; }

.category-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.8rem;
    background: var(--info);
    color: white;
    margin-left: 0.5rem;
}

.progress-container {
    background: rgba(255,255,255,0.1);
    border-radius: 1rem;
    padding: 1rem;
    margin: 1rem 0;
}

.progress-bar {
    background: rgba(255,255,255,0.2);
    border-radius: 0.5rem;
    height: 0.75rem;
    margin: 0.5rem 0;
    overflow: hidden;
}

.progress-fill {
    background: linear-gradient(90deg, var(--primary), var(--info));
    height: 100%;
    border-radius: 0.5rem;
    transition: width 0.3s ease;
}

.streak-counter {
    background: linear-gradient(135deg, #ff6b6b, #ffa726);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    font-weight: bold;
    text-align: center;
    margin: 0.5rem 0;
}

.timer-display {
    font-size: 1.5rem;
    font-weight: bold;
    text-align: center;
    background: rgba(255,255,255,0.1);
    padding: 0.5rem;
    border-radius: 0.5rem;
    margin: 0.5rem 0;
}

.feedback-box {
    padding: 1rem;
    border-radius: 0.5rem;
    margin: 1rem 0;
    font-weight: bold;
}

.correct-feedback {
    background: rgba(52, 199, 89, 0.2);
    border: 2px solid var(--success);
    color: var(--success);
}

.wrong-feedback {
    background: rgba(255, 59, 48, 0.2);
    border: 2px solid var(--danger);
    color: var(--danger);
}

.results-container {
    text-align: center;
    padding: 2rem;
}

.score-display {
    font-size: 3rem;
    font-weight: bold;
    background: linear-gradient(90deg, var(--primary), var(--info));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 1rem 0;
}

.achievement-badge {
    background: linear-gradient(135deg, #ffd700, #ffa726);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    font-weight: bold;
    margin: 0.5rem;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
def initialize_session_state():
    if "quiz_data" not in st.session_state:
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
            "theme": "dark",
            "streak": 0,
            "max_streak": 0,
            "started": False,
            "paused": False,
            "pause_time": None,
            "quiz_duration": 3600
        })

def shuffle_quiz(_quiz):
    shuffled = random.sample(_quiz, len(_quiz))
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = q["options"].copy()
        random.shuffle(q["display_options"])
        q["labeled_answer"] = q["answer"]
    return shuffled

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

def update_timer():
    if not st.session_state.paused and st.session_state.start_time:
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        st.session_state.time_left = max(st.session_state.quiz_duration - elapsed, 0)
        if st.session_state.time_left <= 0:
            st.session_state.show_results = True

def toggle_pause():
    if st.session_state.paused:
        pause_duration = (datetime.now() - st.session_state.pause_time).total_seconds()
        st.session_state.start_time += timedelta(seconds=pause_duration)
        st.session_state.paused = False
    else:
        st.session_state.paused = True
        st.session_state.pause_time = datetime.now()

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
        "time_left": st.session_state.quiz_duration,
        "streak": 0,
        "max_streak": 0,
        "started": False,
        "paused": False,
        "pause_time": None
    })

def get_achievement(score, max_streak, total_questions):
    percentage = (score / (total_questions * 2)) * 100
    if percentage >= 90 and max_streak >= total_questions:
        return "JavaScript Master 🏆"
    elif percentage >= 80:
        return "Expert Developer 💻"
    elif percentage >= 70:
        return "Skilled Programmer ⚡"
    elif percentage >= 60:
        return "Good Learner 📚"
    else:
        return "Keep Practicing 🌱"

# Main application
def main():
    initialize_session_state()
    
    st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="title">🚀 JavaScript Mastery Quiz</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Test your JavaScript skills with interactive coding challenges!</p>', unsafe_allow_html=True)
    
    # Theme toggle
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🌓 Toggle Theme"):
            toggle_theme()
            st.rerun()
    
    # Welcome screen
    if not st.session_state.started:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h2>📋 Quiz Overview</h2>
            <p><strong>10 Questions</strong> • <strong>60 Minutes</strong> • <strong>2 Points per Question</strong></p>
            <p>Categories: Variables, DOM, Error Handling, Browser API, and more!</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎯 Start Quiz", use_container_width=True):
            st.session_state.started = True
            st.session_state.start_time = datetime.now()
            st.rerun()
    else:
        # Timer and controls
        if not st.session_state.show_results:
            update_timer()
            
            # Timer display
            minutes = int(st.session_state.time_left // 60)
            seconds = int(st.session_state.time_left % 60)
            timer_color = "🔴" if st.session_state.time_left < 300 else "🟡" if st.session_state.time_left < 900 else "🟢"
            st.markdown(f'<div class="timer-display">{timer_color} {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)
            
            # Control buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                pause_label = "⏸️ Pause" if not st.session_state.paused else "▶️ Resume"
                if st.button(pause_label, use_container_width=True):
                    toggle_pause()
                    st.rerun()
            with col2:
                if st.button("🔄 Restart", use_container_width=True):
                    reset_quiz()
                    st.rerun()
            with col3:
                if st.button("🏁 Submit", use_container_width=True):
                    st.session_state.show_results = True
                    st.rerun()
        
        # Progress section
        total_questions = len(st.session_state.quiz_data)
        current_q = min(st.session_state.current_q, total_questions - 1)
        progress = ((current_q + 1) / total_questions) * 100
        
        st.markdown(f"""
        <div class="progress-container">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span>Question {current_q + 1} of {total_questions}</span>
                <span>Score: {st.session_state.score}/{total_questions * 2}</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress}%"></div>
            </div>
            <div style="display: flex; justify-content: space-between; margin-top: 0.5rem;">
                <span>Progress: {progress:.1f}%</span>
                <div class="streak-counter">🔥 Streak: {st.session_state.streak}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.show_results:
            # Question display
            q = st.session_state.quiz_data[current_q]
            
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 0.75rem; margin: 1rem 0;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="difficulty-badge {q['difficulty'].lower()}">{q['difficulty']}</span>
                    <span class="category-badge">{q['category']}</span>
                </div>
                {q['question']}
            </div>
            """, unsafe_allow_html=True)
            
            # Options
            for option in q["display_options"]:
                button_class = "option-button"
                if st.session_state.selected_option == option:
                    button_class = "selected-correct" if option == q["answer"] else "selected-wrong"
                
                if st.button(option, key=f"option_{q['id']}_{option}", use_container_width=True):
                    st.session_state.selected_option = option
                    is_correct = option == q["answer"]
                    st.session_state.feedback = {
                        "message": f"{'✅ Correct!' if is_correct else '❌ Incorrect'} {q['explanation']}",
                        "type": "correct" if is_correct else "wrong"
                    }
                    
                    if is_correct:
                        st.session_state.score += 2
                        st.session_state.streak += 1
                        st.session_state.max_streak = max(st.session_state.streak, st.session_state.max_streak)
                    else:
                        st.session_state.streak = 0
                    
                    st.session_state.answers[current_q] = option
                    st.rerun()
            
            # Feedback
            if st.session_state.feedback:
                feedback_class = "correct-feedback" if st.session_state.feedback["type"] == "correct" else "wrong-feedback"
                st.markdown(f'<div class="feedback-box {feedback_class}">{st.session_state.feedback["message"]}</div>', unsafe_allow_html=True)
            
            # Navigation buttons
            col1, col2 = st.columns(2)
            with col1:
                if current_q > 0 and st.button("⬅️ Previous", use_container_width=True):
                    st.session_state.current_q -= 1
                    st.session_state.selected_option = st.session_state.answers[st.session_state.current_q]
                    st.session_state.feedback = None
                    st.rerun()
            with col2:
                if st.session_state.selected_option and st.button("Next ➡️", use_container_width=True):
                    st.session_state.current_q += 1
                    if st.session_state.current_q >= total_questions:
                        st.session_state.show_results = True
                    else:
                        st.session_state.selected_option = st.session_state.answers[st.session_state.current_q]
                        st.session_state.feedback = None
                    st.rerun()
        else:
            # Results screen
            achievement = get_achievement(st.session_state.score, st.session_state.max_streak, total_questions)
            
            st.markdown(f"""
            <div class="results-container">
                <h2>🎉 Quiz Completed!</h2>
                <div class="score-display">{st.session_state.score}/{total_questions * 2}</div>
                <div class="achievement-badge">{achievement}</div>
                <p>Maximum Streak: 🔥 {st.session_state.max_streak}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Detailed results
            st.markdown("### 📊 Detailed Results")
            for i, (q, ans) in enumerate(zip(st.session_state.quiz_data, st.session_state.answers)):
                is_correct = ans == q["answer"]
                result_icon = "✅" if is_correct else "❌"
                
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 0.5rem; margin: 0.5rem 0;">
                    <div style="display: flex; justify-content: space-between;">
                        <strong>Question {i + 1} {result_icon}</strong>
                        <span class="difficulty-badge {q['difficulty'].lower()}">{q['difficulty']}</span>
                    </div>
                    {q['question']}
                    <p><strong>Your Answer:</strong> <span style="color: {'var(--success)' if is_correct else 'var(--danger)'}">{ans or "Not answered"}</span></p>
                    <p><strong>Correct Answer:</strong> {q['answer']}</p>
                    <p><em>{q['explanation']}</em></p>
                </div>
                """, unsafe_allow_html=True)
            
            if st.button("🔄 Take Quiz Again", use_container_width=True):
                reset_quiz()
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
