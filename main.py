
import streamlit as st
import random
from datetime import datetime
import uuid





quiz = [
    {
        "question": "What is the output of: function test() { var x = 1; if (true) { var x = 2; } return x; } console.log(test());",
        "options": ["2", "1", "undefined", "ReferenceError"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "The 'var' keyword is function-scoped, so the inner 'var x = 2' reassigns the same variable, returning 2."
    },
    {
        "question": "What does this code output: let x = 10; { let x = 20; } console.log(x);",
        "options": ["10", "20", "undefined", "Error"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "The 'let' keyword is block-scoped, so the inner 'let x = 20' does not affect the outer x, logging 10."
    },
    {
        "question": "What is the output of: function scope() { let x = 5; if (true) { x = 15; } return x; } console.log(scope());",
        "options": ["15", "5", "undefined", "Error"],
        "answer": "15",
        "difficulty": "Medium",
        "explanation": "Without a new 'let' in the if block, 'x = 15' reassigns the outer x, returning 15."
    },
    {
        "question": "What happens in: function test() { console.log(x); var x = 1; } test();",
        "options": ["Logs undefined", "Logs 1", "ReferenceError", "TypeError"],
        "answer": "Logs undefined",
        "difficulty": "Medium",
        "explanation": "Due to hoisting, 'var x' is declared but not initialized when logged, so it outputs undefined."
    },
    {
        "question": "What is the output of: const x = 10; { const x = 20; } console.log(x);",
        "options": ["10", "20", "undefined", "Error"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "The 'const' keyword is block-scoped, so the inner 'const x = 20' does not affect the outer x."
    },
    {
        "question": "What is the output of: function test() { console.log(x); let x = 1; } test();",
        "options": ["ReferenceError", "undefined", "1", "null"],
        "answer": "ReferenceError",
        "difficulty": "Medium",
        "explanation": "The 'let x' variable is in the temporal dead zone until declared, causing a ReferenceError."
    },
    {
        "question": "What does this code output: var x = 5; function test() { console.log(x); var x = 10; } test();",
        "options": ["undefined", "5", "10", "Error"],
        "answer": "undefined",
        "difficulty": "Medium",
        "explanation": "Inside the function, 'var x' is hoisted, shadowing the outer x, and logs undefined before assignment."
    },
    {
        "question": "What is the output of: let x = 1; { x = 2; let x = 3; } console.log(x);",
        "options": ["1", "2", "3", "ReferenceError"],
        "answer": "ReferenceError",
        "difficulty": "Medium",
        "explanation": "Assigning to x in the block before 'let x = 3' causes a ReferenceError due to the temporal dead zone."
    },
    {
        "question": "What does this code output: var x = 1; function test() { console.log(x); x = 2; } test(); console.log(x);",
        "options": ["1, 2", "undefined, 1", "1, 1", "2, 2"],
        "answer": "1, 2",
        "difficulty": "Medium",
        "explanation": "The function accesses the global x (1), then reassigns it to 2, affecting the global variable."
    },
    {
        "question": "What is the output of: function test() { let x = 1; { let x = 2; } return x; } console.log(test());",
        "options": ["1", "2", "undefined", "Error"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "The inner 'let x = 2' is block-scoped and doesn’t affect the outer x, returning 1."
    },
    {
        "question": "How do you validate a text field to ensure it is not empty?",
        "options": [
            "if (document.getElementById('input').value.trim() !== '')",
            "if (document.getElementById('input').value === null)",
            "if (document.getElementById('input').length > 0)",
            "if (document.getElementById('input').text !== '')"
        ],
        "answer": "if (document.getElementById('input').value.trim() !== '')",
        "difficulty": "Medium",
        "explanation": "The 'trim()' method removes whitespace, and checking '!== ''' ensures the field is not empty."
    },
    {
        "question": "What does this code do: let input = document.getElementById('text'); if (input.value.length >= 5) console.log('Valid');",
        "options": [
            "Logs 'Valid' if text input has 5 or more characters",
            "Logs 'Valid' if input is empty",
            "Throws an error",
            "Logs the input value"
        ],
        "answer": "Logs 'Valid' if text input has 5 or more characters",
        "difficulty": "Medium",
        "explanation": "Checks if the input’s value length is at least 5, logging 'Valid' if true."
    },
    {
        "question": "What does this code do: let input = document.getElementById('text'); if (/^[a-zA-Z]+$/.test(input.value)) console.log('Alphabetic');",
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
        "question": "What does this code do: let input = document.getElementById('text'); if (input.value.length <= 10) console.log('Valid length');",
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
        "question": "What does this code do: let input = document.getElementById('text'); if (/^\\d+$/.test(input.value)) console.log('Numbers');",
        "options": [
            "Logs 'Numbers' if input is digits only",
            "Logs the input value",
            "Sets the input value",
            "Throws an error"
        ],
        "answer": "Logs 'Numbers' if input is digits only",
        "difficulty": "Medium",
        "explanation": "The regex '/^\\d+$/' checks for digits, logging 'Numbers' if matched."
    },
    {
        "question": "What does this code do: let input = document.getElementById('text'); input.value = input.value.trim(); console.log(input.value);",
        "options": [
            "Logs the trimmed input value",
            "Logs the original input value",
            "Clears the input",
            "Throws an error"
        ],
        "answer": "Logs the trimmed input value",
        "difficulty": "Medium",
        "explanation": "The 'trim()' method removes leading/trailing whitespace, and the result is logged."
    },
    {
        "question": "What does this code do: let input = document.getElementById('text'); if (input.value !== '') console.log('Not empty');",
        "options": [
            "Logs 'Not empty' if input has any characters",
            "Logs the input value",
            "Sets the input value",
            "Throws an error"
        ],
        "answer": "Logs 'Not empty' if input has any characters",
        "difficulty": "Medium",
        "explanation": "Checks if the input’s value is non-empty, logging 'Not empty'."
    },
    {
        "question": "What does this code do: let input = document.getElementById('text'); if (/^[A-Z]/.test(input.value)) console.log('Starts with uppercase');",
        "options": [
            "Logs 'Starts with uppercase' if input starts with an uppercase letter",
            "Logs the input value",
            "Sets the input value",
            "Throws an error"
        ],
        "answer": "Logs 'Starts with uppercase' if input starts with an uppercase letter",
        "difficulty": "Medium",
        "explanation": "The regex '/^[A-Z]/' checks if the input starts with an uppercase letter."
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
        "explanation": "The 'selectedIndex > -1' condition confirms an option is selected in the dropdown."
    },
    {
        "question": "What does this code do: let select = document.getElementById('dropdown'); if (select.value !== '') console.log('Selected');",
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
        "question": "What does this code do: let select = document.getElementById('dropdown'); if (select.options[select.selectedIndex].value !== 'default') console.log('Valid');",
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
        "question": "What does this code do: let select = document.getElementById('dropdown'); if (select.selectedOptions.length > 0) console.log('Selected');",
        "options": [
            "Logs 'Selected' if an option is chosen",
            "Logs the number of options",
            "Sets the dropdown value",
            "Throws an error"
        ],
        "answer": "Logs 'Selected' if an option is chosen",
        "difficulty": "Medium",
        "explanation": "The 'selectedOptions.length' property checks if any options are selected."
    },
    {
        "question": "What does this code do: let select = document.getElementById('dropdown'); console.log(select.options[select.selectedIndex].text);",
        "options": [
            "Logs the text of the selected option",
            "Logs the value of the selected option",
            "Sets the selected option",
            "Throws an error"
        ],
        "answer": "Logs the text of the selected option",
        "difficulty": "Medium",
        "explanation": "The 'options[selectedIndex].text' property retrieves the display text of the selected option."
    },
    {
        "question": "What does this code do: let select = document.getElementById('dropdown'); select.value = 'option1'; console.log(select.value);",
        "options": [
            "Logs 'option1' after setting dropdown value",
            "Logs the previous value",
            "Clears the dropdown",
            "Throws an error"
        ],
        "answer": "Logs 'option1' after setting dropdown value",
        "difficulty": "Medium",
        "explanation": "Sets the dropdown’s value to 'option1' and logs it."
    },
    {
        "question": "What does this code do: let select = document.getElementById('dropdown'); if (select.options.length > 1) console.log('Multiple options');",
        "options": [
            "Logs 'Multiple options' if dropdown has more than one option",
            "Logs the number of options",
            "Sets the dropdown value",
            "Throws an error"
        ],
        "answer": "Logs 'Multiple options' if dropdown has more than one option",
        "difficulty": "Medium",
        "explanation": "Checks if the dropdown has multiple options using 'options.length'."
    },
    {
        "question": "What does this code do: let select = document.getElementById('dropdown'); select.disabled = true;",
        "options": [
            "Disables the dropdown",
            "Enables the dropdown",
            "Clears the dropdown",
            "Throws an error"
        ],
        "answer": "Disables the dropdown",
        "difficulty": "Medium",
        "explanation": "Setting 'disabled = true' prevents user interaction with the dropdown."
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
        "question": "What does this code do: let radio = document.querySelector('input[name=group]:checked'); console.log(radio ? radio.value : 'None');",
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
        "question": "What does this code do: let radios = document.querySelectorAll('input[name=group]'); radios.forEach(r => r.checked = false);",
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
        "question": "What does this code do: let radio = document.querySelector('input[name=group]:checked'); radio ? radio.checked = true : console.log('None');",
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
        "question": "What does this code do: let radios = document.getElementsByName('group'); console.log(radios[0].value);",
        "options": [
            "Logs the value of the first radio button",
            "Logs the checked radio’s value",
            "Sets the first radio’s value",
            "Throws an error"
        ],
        "answer": "Logs the value of the first radio button",
        "difficulty": "Medium",
        "explanation": "Accesses the first radio button’s value using 'getElementsByName()'."
    },
    {
        "question": "What does this code do: let radio = document.querySelector('input[name=group]'); radio.checked = true;",
        "options": [
            "Checks the first radio button in the group",
            "Unchecks the radio button",
            "Logs the radio value",
            "Throws an error"
        ],
        "answer": "Checks the first radio button in the group",
        "difficulty": "Medium",
        "explanation": "Sets 'checked = true' on the first radio button selected by the query."
    },
    {
        "question": "What does this code do: let radios = document.querySelectorAll('input[name=group]'); console.log(radios.length);",
        "options": [
            "Logs the number of radio buttons in the group",
            "Logs the checked radio’s value",
            "Sets the radio values",
            "Throws an error"
        ],
        "answer": "Logs the number of radio buttons in the group",
        "difficulty": "Medium",
        "explanation": "The 'querySelectorAll()' method returns a collection, and 'length' counts the radio buttons."
    },
    {
        "question": "What does this code do: let radio = document.querySelector('input[name=group]:checked'); console.log(radio?.value);",
        "options": [
            "Logs the checked radio’s value or undefined",
            "Logs 'None' always",
            "Sets the radio value",
            "Throws an error"
        ],
        "answer": "Logs the checked radio’s value or undefined",
        "difficulty": "Medium",
        "explanation": "The optional chaining '?.' logs the value if a radio is checked, else undefined."
    },
    {
        "question": "What regex validates a 5-digit ZIP code?",
        "options": ["/^\\d{5}$/", "/^\\d{5}-\\d{4}$/", "/^\\d{9}$/", "/^\\d{5}(-\\d{4})?$/"],
        "answer": "/^\\d{5}$/",
        "difficulty": "Medium",
        "explanation": "The regex '/^\\d{5}$/' ensures exactly 5 digits, suitable for a basic ZIP code."
    },
    {
        "question": "What does this code do: let zip = document.getElementById('zip').value; if (/^\\d{5}$/.test(zip)) console.log('Valid ZIP');",
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
        "question": "What does this code do: let zip = document.getElementById('zip').value; if (/^\\d{5}(-\\d{4})?$/.test(zip)) console.log('Valid');",
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
        "question": "What does this code do: let zip = document.getElementById('zip').value; if (/^\\d{9}$/.test(zip)) console.log('Valid 9-digit ZIP');",
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
        "question": "What does this code do: let zip = document.getElementById('zip').value; if (zip.length === 5 && /^\\d+$/.test(zip)) console.log('Valid');",
        "options": [
            "Logs 'Valid' for a 5-digit ZIP code",
            "Logs the ZIP value",
            "Sets the ZIP value",
            "Throws an error"
        ],
        "answer": "Logs 'Valid' for a 5-digit ZIP code",
        "difficulty": "Medium",
        "explanation": "Checks length and digit-only regex for a 5-digit ZIP, logging 'Valid'."
    },
    {
        "question": "What regex validates a 5-digit or 9-digit ZIP code with optional hyphen?",
        "options": ["/^\\d{5}(-\\d{4})?$/", "/^\\d{5}$/", "/^\\d{9}$/", "/^\\d{5,9}$/"],
        "answer": "/^\\d{5}(-\\d{4})?$/",
        "difficulty": "Medium",
        "explanation": "The regex '/^\\d{5}(-\\d{4})?$/' matches 5 digits or 5+4 with an optional hyphen."
    },
    {
        "question": "What does this code do: let zip = document.getElementById('zip').value; if (/^[0-9]{5}$/.test(zip)) console.log('Valid');",
        "options": [
            "Logs 'Valid' for a 5-digit ZIP code",
            "Logs the ZIP value",
            "Sets the ZIP value",
            "Throws an error"
        ],
        "answer": "Logs 'Valid' for a 5-digit ZIP code",
        "difficulty": "Medium",
        "explanation": "The regex '/^[0-9]{5}$/' matches exactly 5 digits, logging 'Valid'."
    },
    {
        "question": "What does this code do: let zip = document.getElementById('zip').value; zip = zip.replace(/[^\\d]/g, ''); console.log(zip);",
        "options": [
            "Logs the ZIP with non-digits removed",
            "Logs the original ZIP",
            "Sets the ZIP value",
            "Throws an error"
        ],
        "answer": "Logs the ZIP with non-digits removed",
        "difficulty": "Medium",
        "explanation": "The 'replace(/[^\\d]/g, '')' removes non-digit characters from the ZIP."
    },
    {
        "question": "What regex validates an email address?",
        "options": ["/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/", "/^\\w+@\\w+\\.com$/", "/^[^\\s@]+@[^\\s@]+$/", "/^\\w+\\.\\w+@\\w+$/"],
        "answer": "/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/",
        "difficulty": "Medium",
        "explanation": "This regex ensures a valid email format with username, @, domain, and top-level domain."
    },
    {
        "question": "What does this code do: let email = document.getElementById('email').value; if (/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) console.log('Valid');",
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
        "question": "What does this code do: let email = document.getElementById('email').value; if (email.includes('@')) console.log('Has @');",
        "options": [
            "Logs 'Has @' if email contains '@'",
            "Logs the email value",
            "Sets the email value",
            "Throws an error"
        ],
        "answer": "Logs 'Has @' if email contains '@'",
        "difficulty": "Medium",
        "explanation": "The 'includes()' method checks for '@' in the email string."
    },
    {
        "question": "What does this code do: let email = document.getElementById('email').value; if (/^[^\\s@]+@[^\\s@]+\\.[a-zA-Z]{2,}$/.test(email)) console.log('Valid');",
        "options": [
            "Logs 'Valid' for email with 2+ letter TLD",
            "Logs the email value",
            "Sets the email value",
            "Throws an error"
        ],
        "answer": "Logs 'Valid' for email with 2+ letter TLD",
        "difficulty": "Medium",
        "explanation": "The regex requires a top-level domain of at least 2 letters."
    },
    {
        "question": "What does this code do: let email = document.getElementById('email').value; if (email.split('@').length === 2) console.log('One @');",
        "options": [
            "Logs 'One @' if email has exactly one '@'",
            "Logs the email value",
            "Sets the email value",
            "Throws an error"
        ],
        "answer": "Logs 'One @' if email has exactly one '@'",
        "difficulty": "Medium",
        "explanation": "Splitting on '@' and checking length ensures exactly one '@'."
    },
    {
        "question": "What does this code do: let email = document.getElementById('email').value; if (/\\.com$/.test(email)) console.log('Ends with .com');",
        "options": [
            "Logs 'Ends with .com' if email ends with '.com'",
            "Logs the email value",
            "Sets the email value",
            "Throws an error"
        ],
        "answer": "Logs 'Ends with .com' if email ends with '.com'",
        "difficulty": "Medium",
        "explanation": "The regex '/\\.com$/' checks if the email ends with '.com'."
    },
    {
        "question": "What does this code do: let email = document.getElementById('email').value; if (email.length > 5) console.log('Long enough');",
        "options": [
            "Logs 'Long enough' if email is more than 5 characters",
            "Logs the email value",
            "Sets the email value",
            "Throws an error"
        ],
        "answer": "Logs 'Long enough' if email is more than 5 characters",
        "difficulty": "Medium",
        "explanation": "Checks if the email string length is greater than 5."
    },
    {
        "question": "What does this code do: let email = document.getElementById('email').value; email = email.toLowerCase(); console.log(email);",
        "options": [
            "Logs the email in lowercase",
            "Logs the original email",
            "Sets the email value",
            "Throws an error"
        ],
        "answer": "Logs the email in lowercase",
        "difficulty": "Medium",
        "explanation": "The 'toLowerCase()' method converts the email to lowercase."
    },
    {
        "question": "What is the output of: try { let x = undefined.x; } catch (e) { console.log(e.name); }",
        "options": ["TypeError", "ReferenceError", "SyntaxError", "undefined"],
        "answer": "TypeError",
        "difficulty": "Medium",
        "explanation": "Accessing a property on undefined throws a TypeError, caught and logged as 'TypeError'."
    },
    {
        "question": "What does this code do: try { throw new Error('Invalid'); } catch (e) { console.log(e.message); }",
        "options": ["Logs 'Invalid'", "Logs 'Error'", "Throws an error", "Logs undefined"],
        "answer": "Logs 'Invalid'",
        "difficulty": "Medium",
        "explanation": "The thrown error’s message is caught and logged as 'Invalid'."
    },
    {
        "question": "What is the output of: try { JSON.parse('invalid'); } catch (e) { console.log(e.name); }",
        "options": ["SyntaxError", "TypeError", "ReferenceError", "undefined"],
        "answer": "SyntaxError",
        "difficulty": "Medium",
        "explanation": "Invalid JSON in 'JSON.parse()' throws a SyntaxError, caught and logged."
    },
    {
        "question": "What does this code do: try { null.x; } catch (e) { console.log(e.name); }",
        "options": ["TypeError", "ReferenceError", "SyntaxError", "undefined"],
        "answer": "TypeError",
        "difficulty": "Medium",
        "explanation": "Accessing a property on null throws a TypeError, caught and logged."
    },
    {
        "question": "What does this code do: try { let x = 1 / 0; } catch (e) { console.log('Error'); }",
        "options": ["Nothing, no error is thrown", "Logs 'Error'", "Throws an error", "Logs undefined"],
        "answer": "Nothing, no error is thrown",
        "difficulty": "Medium",
        "explanation": "Dividing by zero in JavaScript returns Infinity, not an error."
    },
    {
        "question": "What does this code do: try { document.getElementById('none').value; } catch (e) { console.log(e.name); }",
        "options": ["TypeError", "ReferenceError", "SyntaxError", "undefined"],
        "answer": "TypeError",
        "difficulty": "Medium",
        "explanation": "Accessing 'value' on a null element (non-existent ID) throws a TypeError."
    },
    {
        "question": "What is the output of: try { throw new TypeError('Test'); } catch (e) { console.log(e.name); }",
        "options": ["TypeError", "ReferenceError", "SyntaxError", "Test"],
        "answer": "TypeError",
        "difficulty": "Medium",
        "explanation": "The thrown TypeError’s name is caught and logged as 'TypeError'."
    },
    {
        "question": "What does this code do: try { let x = y; } catch (e) { console.log(e.name); }",
        "options": ["ReferenceError", "TypeError", "SyntaxError", "undefined"],
        "answer": "ReferenceError",
        "difficulty": "Medium",
        "explanation": "Accessing an undeclared variable 'y' throws a ReferenceError."
    },
    {
        "question": "What does this code do: try { throw 'Custom error'; } catch (e) { console.log(e); }",
        "options": ["Logs 'Custom error'", "Logs undefined", "Throws an error", "Logs 'Error'"],
        "answer": "Logs 'Custom error'",
        "difficulty": "Medium",
        "explanation": "The 'throw' statement throws a string, which is caught and logged."
    },
    {
        "question": "What does this code do: try { throw { message: 'Custom' }; } catch (e) { console.log(e.message); }",
        "options": ["Logs 'Custom'", "Logs undefined", "Throws an error", "Logs 'Error'"],
        "answer": "Logs 'Custom'",
        "difficulty": "Medium",
        "explanation": "The thrown object’s 'message' property is caught and logged."
    },
    {
        "question": "What does this code do: try { throw new Error('Test'); } catch (e) { console.log(e.message); }",
        "options": ["Logs 'Test'", "Logs undefined", "Throws an error", "Logs 'Error'"],
        "answer": "Logs 'Test'",
        "difficulty": "Medium",
        "explanation": "The thrown error’s message is caught and logged as 'Test'."
    },
    {
        "question": "What does this code do: try { throw new SyntaxError('Bad syntax'); } catch (e) { console.log(e.name); }",
        "options": ["SyntaxError", "TypeError", "ReferenceError", "Bad syntax"],
        "answer": "SyntaxError",
        "difficulty": "Medium",
        "explanation": "The thrown SyntaxError’s name is caught and logged as 'SyntaxError'."
    },
    {
        "question": "What does this code do: try { throw 42; } catch (e) { console.log(e); }",
        "options": ["Logs 42", "Logs undefined", "Throws an error", "Logs 'Error'"],
        "answer": "Logs 42",
        "difficulty": "Medium",
        "explanation": "The 'throw' statement can throw any value, including a number, which is caught and logged."
    },
    {
        "question": "What does this code do: try { throw null; } catch (e) { console.log(e); }",
        "options": ["Logs null", "Logs undefined", "Throws an error", "Logs 'Error'"],
        "answer": "Logs null",
        "difficulty": "Medium",
        "explanation": "The 'throw' statement throws null, which is caught and logged."
    },
    {
        "question": "What does this code do: try { throw new Error(''); } catch (e) { console.log(e.message); }",
        "options": ["Logs empty string", "Logs undefined", "Throws an error", "Logs 'Error'"],
        "answer": "Logs empty string",
        "difficulty": "Medium",
        "explanation": "The thrown error has an empty message, which is caught and logged."
    },
    {
        "question": "What does this code do: try { throw new Error('Failed'); } catch (e) { console.log('Caught'); }",
        "options": ["Logs 'Caught'", "Logs 'Failed'", "Throws an error", "Logs undefined"],
        "answer": "Logs 'Caught'",
        "difficulty": "Medium",
        "explanation": "The error is caught, and 'Caught' is logged instead of the error message."
    },
    {
        "question": "What does this code do: document.getElementById('btn').addEventListener('click', () => console.log('Clicked'));",
        "options": ["Logs 'Clicked' on button click", "Changes button text", "Disables the button", "Redirects the page"],
        "answer": "Logs 'Clicked' on button click",
        "difficulty": "Medium",
        "explanation": "The 'addEventListener()' method binds a handler to the button’s click event."
    },
    {
        "question": "What does this code do: document.getElementById('input').addEventListener('keypress', () => console.log('Key pressed'));",
        "options": ["Logs 'Key pressed' on keypress", "Logs the key value", "Clears the input", "Triggers a click event"],
        "answer": "Logs 'Key pressed' on keypress",
        "difficulty": "Medium",
        "explanation": "The 'addEventListener()' method binds a handler to the 'keypress' event."
    },
    {
        "question": "What does this code do: document.getElementById('input').addEventListener('submit', e => e.preventDefault());",
        "options": ["Prevents form submission", "Submits the form", "Logs the form data", "Throws an error"],
        "answer": "Prevents form submission",
        "difficulty": "Medium",
        "explanation": "The 'preventDefault()' method stops the form’s default submission behavior."
    },
    {
        "question": "What does this code do: document.addEventListener('click', e => console.log(e.target.tagName));",
        "options": ["Logs the tag name of the clicked element", "Logs the event type", "Logs the click coordinates", "Throws an error"],
        "answer": "Logs the tag name of the clicked element",
        "difficulty": "Medium",
        "explanation": "The 'e.target.tagName' property returns the tag name of the clicked element."
    },
    {
        "question": "What does this code do: document.getElementById('input').addEventListener('change', () => console.log('Changed'));",
        "options": ["Logs 'Changed' when input value changes", "Logs the input value", "Clears the input", "Throws an error"],
        "answer": "Logs 'Changed' when input value changes",
        "difficulty": "Medium",
        "explanation": "The 'change' event fires when the input’s value changes."
    },
    {
        "question": "What does this code do: document.addEventListener('keydown', e => console.log(e.key));",
        "options": ["Logs the key pressed", "Logs the event type", "Logs the key code", "Throws an error"],
        "answer": "Logs the key pressed",
        "difficulty": "Medium",
        "explanation": "The 'e.key' property returns the value of the pressed key."
    },
    {
        "question": "What does this code do: document.getElementById('btn').addEventListener('mouseover', () => console.log('Hovered'));",
        "options": ["Logs 'Hovered' on mouseover", "Logs the button’s text", "Changes the button’s style", "Throws an error"],
        "answer": "Logs 'Hovered' on mouseover",
        "difficulty": "Medium",
        "explanation": "The 'mouseover' event fires when the mouse enters the button."
    },
    {
        "question": "What does this code do: document.addEventListener('click', e => console.log(e.clientX));",
        "options": ["Logs the x-coordinate of the click", "Logs the clicked element", "Logs the event type", "Throws an error"],
        "answer": "Logs the x-coordinate of the click",
        "difficulty": "Medium",
        "explanation": "The 'e.clientX' property returns the x-coordinate of the click relative to the viewport."
    },
    {
        "question": "What does this code do: document.getElementById('input').addEventListener('focus', () => console.log('Focused'));",
        "options": ["Logs 'Focused' when input is focused", "Logs the input value", "Clears the input", "Throws an error"],
        "answer": "Logs 'Focused' when input is focused",
        "difficulty": "Medium",
        "explanation": "The 'focus' event fires when the input gains focus."
    },
    {
        "question": "What does this code do: document.getElementById('btn').addEventListener('click', e => e.stopPropagation());",
        "options": ["Prevents event bubbling", "Prevents default action", "Logs the event", "Throws an error"],
        "answer": "Prevents event bubbling",
        "difficulty": "Medium",
        "explanation": "The 'stopPropagation()' method stops the event from bubbling up the DOM."
    },
    {
        "question": "What is the output of: let node = document.createTextNode('test'); console.log(node.nodeType);",
        "options": ["3", "1", "8", "9"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "A text node has a 'nodeType' of 3 in the DOM."
    },
    {
        "question": "What is the output of: let comment = document.createComment('test'); console.log(comment.nodeType);",
        "options": ["8", "1", "3", "9"],
        "answer": "8",
        "difficulty": "Medium",
        "explanation": "A comment node has a 'nodeType' of 8 in the DOM."
    },
    {
        "question": "What is the output of: let div = document.createElement('div'); console.log(div.nodeType);",
        "options": ["1", "3", "8", "9"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "An element node like a div has a 'nodeType' of 1."
    },
    {
        "question": "What is the output of: let doc = document; console.log(doc.nodeType);",
        "options": ["9", "1", "3", "8"],
        "answer": "9",
        "difficulty": "Medium",
        "explanation": "The document node has a 'nodeType' of 9."
    },
    {
        "question": "What is the output of: let attr = document.createAttribute('id'); console.log(attr.nodeType);",
        "options": ["2", "1", "3", "8"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "An attribute node has a 'nodeType' of 2."
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
        "explanation": "The 'querySelectorAll()' method uses CSS selector syntax to select all elements with class 'test'."
    },
    {
        "question": "What does this code do: let elements = document.querySelectorAll('[data-test]'); console.log(elements.length);",
        "options": [
            "Logs the number of elements with data-test attribute",
            "Logs the data-test values",
            "Selects one element",
            "Throws an error"
        ],
        "answer": "Logs the number of elements with data-test attribute",
        "difficulty": "Medium",
        "explanation": "The 'querySelectorAll()' method selects elements with 'data-test', and 'length' counts them."
    },
    {
        "question": "What does this code do: let element = document.querySelector('#box'); console.log(element);",
        "options": [
            "Logs the element with id 'box'",
            "Logs undefined if no element",
            "Selects all elements",
            "Throws an error"
        ],
        "answer": "Logs the element with id 'box'",
        "difficulty": "Medium",
        "explanation": "The 'querySelector()' method returns the element with id 'box' or null if not found."
    },
    {
        "question": "What does this code do: let elements = document.getElementsByTagName('p'); console.log(elements.length);",
        "options": [
            "Logs the number of <p> elements",
            "Logs the first <p> element",
            "Selects one <p> element",
            "Throws an error"
        ],
        "answer": "Logs the number of <p> elements",
        "difficulty": "Medium",
        "explanation": "The 'getElementsByTagName()' method returns a collection of <p> elements, and 'length' counts them."
    },
    {
        "question": "What does this code do: let element = document.getElementsByClassName('test')[0]; console.log(element);",
        "options": [
            "Logs the first element with class 'test'",
            "Logs all elements with class 'test'",
            "Selects no elements",
            "Throws an error"
        ],
        "answer": "Logs the first element with class 'test'",
        "difficulty": "Medium",
        "explanation": "The 'getElementsByClassName()' method returns a collection, and [0] accesses the first element."
    },
    {
        "question": "What is the output of: let div = document.createElement('div'); console.log(div.tagName);",
        "options": ["DIV", "div", "Div", "undefined"],
        "answer": "DIV",
        "difficulty": "Medium",
        "explanation": "The 'tagName' property returns the tag name in uppercase, so 'DIV' for a <div> element."
    },
    {
        "question": "What does this code do: let p = document.createElement('p'); console.log(p.tagName);",
        "options": ["Logs 'P'", "Logs 'p'", "Logs undefined", "Throws an error"],
        "answer": "Logs 'P'",
        "difficulty": "Medium",
        "explanation": "The 'tagName' property returns the tag name in uppercase, so 'P' for a <p> element."
    },
    {
        "question": "What does this code do: let button = document.createElement('button'); console.log(button.tagName);",
        "options": ["Logs 'BUTTON'", "Logs 'button'", "Logs undefined", "Throws an error"],
        "answer": "Logs 'BUTTON'",
        "difficulty": "Medium",
        "explanation": "The 'tagName' property returns the tag name in uppercase, so 'BUTTON' for a <button> element."
    },
    {
        "question": "What does this code do: let div = document.createElement('div'); div.innerHTML = '<p>1</p><p>2</p>'; console.log(div.children.length);",
        "options": ["Logs 2", "Logs 1", "Logs 0", "Throws an error"],
        "answer": "Logs 2",
        "difficulty": "Medium",
        "explanation": "The 'children.length' property counts the two <p> elements, excluding text nodes."
    },
    {
        "question": "What does this code do: let div = document.createElement('div'); div.innerHTML = 'Text'; console.log(div.childNodes.length);",
        "options": ["Logs 1", "Logs 0", "Logs 2", "Throws an error"],
        "answer": "Logs 1",
        "difficulty": "Medium",
        "explanation": "The 'childNodes.length' property counts the text node created by 'Text'."
    },
    {
        "question": "What does this code do: let div = document.createElement('div'); div.appendChild(document.createTextNode('Test')); console.log(div.childNodes.length);",
        "options": ["Logs 1", "Logs 0", "Logs 2", "Throws an error"],
        "answer": "Logs 1",
        "difficulty": "Medium",
        "explanation": "Appending a text node results in one child node, counted by 'childNodes.length'."
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
        "explanation": "The 'hasAttribute()' method returns true if the element has the specified attribute."
    },
    {
        "question": "What does this code do: let img = document.createElement('img'); img.setAttribute('src', 'image.jpg'); console.log(img.getAttribute('src'));",
        "options": ["Logs 'image.jpg'", "Logs undefined", "Logs 'img'", "Throws an error"],
        "answer": "Logs 'image.jpg'",
        "difficulty": "Medium",
        "explanation": "The 'setAttribute()' method sets the 'src', and 'getAttribute()' retrieves it."
    },
    {
        "question": "What does this code do: let elem = document.createElement('div'); elem.setAttribute('id', 'box'); console.log(elem.id);",
        "options": ["Logs 'box'", "Logs undefined", "Logs 'div'", "Throws an error"],
        "answer": "Logs 'box'",
        "difficulty": "Medium",
        "explanation": "The 'setAttribute()' method sets the 'id', and the 'id' property retrieves it."
    },
    {
        "question": "What does this code do: let elem = document.createElement('img'); elem.removeAttribute('src'); console.log(elem.hasAttribute('src'));",
        "options": ["Logs false", "Logs true", "Logs undefined", "Throws an error"],
        "answer": "Logs false",
        "difficulty": "Medium",
        "explanation": "The 'removeAttribute()' method removes the 'src', so 'hasAttribute()' returns false."
    },
    {
        "question": "What does this code do: let elem = document.querySelector('#box'); console.log(elem.getAttribute('data-value'));",
        "options": [
            "Logs the value of data-value attribute",
            "Logs undefined if no attribute",
            "Sets the data-value attribute",
            "Throws an error"
        ],
        "answer": "Logs the value of data-value attribute",
        "difficulty": "Medium",
        "explanation": "The 'getAttribute()' method returns the 'data-value' or null if it doesn’t exist."
    },
    {
        "question": "What does this code do: let elem = document.createElement('span'); document.body.appendChild(elem);",
        "options": [
            "Appends a new span to the body",
            "Replaces the body with a span",
            "Creates a span without adding it",
            "Throws an error"
        ],
        "answer": "Appends a new span to the body",
        "difficulty": "Medium",
        "explanation": "The 'appendChild()' method adds the new span as the last child of the body."
    },
    {
        "question": "What does this code do: let div = document.createElement('div'); div.textContent = 'Hello'; document.body.appendChild(div);",
        "options": [
            "Appends a div with 'Hello' to the body",
            "Replaces the body",
            "Creates a div without adding it",
            "Throws an error"
        ],
        "answer": "Appends a div with 'Hello' to the body",
        "difficulty": "Medium",
        "explanation": "The 'textContent' property sets the text, and 'appendChild()' adds the div."
    },
    {
        "question": "What does this code do: let div = document.createElement('div'); document.body.appendChild(div); div.textContent = 'Test';",
        "options": [
            "Appends a div with 'Test' to the body",
            "Replaces the body",
            "Creates a div without adding it",
            "Throws an error"
        ],
        "answer": "Appends a div with 'Test' to the body",
        "difficulty": "Medium",
        "explanation": "The 'appendChild()' method adds the div, and 'textContent' sets its text."
    },
    {
        "question": "What does this code do: let p = document.createElement('p'); document.querySelector('#target').parentNode.insertBefore(p, document.querySelector('#target'));",
        "options": [
            "Inserts a new <p> before #target",
            "Inserts a new <p> after #target",
            "Replaces #target with a <p>",
            "Appends a <p> to #target"
        ],
        "answer": "Inserts a new <p> before #target",
        "difficulty": "Medium",
        "explanation": "The 'insertBefore()' method adds the new node before the specified reference node."
    },
    {
        "question": "What does this code do: let p = document.createElement('p'); let target = document.querySelector('#target'); target.parentNode.insertBefore(p, target.nextSibling);",
        "options": [
            "Inserts a new <p> after #target",
            "Inserts a new <p> before #target",
            "Replaces #target",
            "Appends a <p> to #target"
        ],
        "answer": "Inserts a new <p> after #target",
        "difficulty": "Medium",
        "explanation": "The 'insertBefore()' method with 'nextSibling' inserts the <p> after #target."
    },
    {
        "question": "What does this code do: let div = document.createElement('div'); document.querySelector('#container').appendChild(div);",
        "options": [
            "Appends a div to #container",
            "Replaces #container",
            "Creates a div without adding it",
            "Throws an error"
        ],
        "answer": "Appends a div to #container",
        "difficulty": "Medium",
        "explanation": "The 'appendChild()' method adds the div as the last child of #container."
    },
    {
        "question": "What is the output of: let obj = { x: 5 }; console.log(obj.x);",
        "options": ["5", "undefined", "x", "Error"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The 'x' property is accessed using dot notation, logging its value, 5."
    },
    {
        "question": "What does this code do: let obj = {}; obj.newProp = 42; console.log(obj.newProp);",
        "options": ["Logs 42", "Logs undefined", "Logs 'newProp'", "Throws an error"],
        "answer": "Logs 42",
        "difficulty": "Medium",
        "explanation": "Adding 'newProp' to the object and accessing it logs its value, 42."
    },
    {
        "question": "What does this code do: let obj = { x: 10 }; obj.x = 20; console.log(obj.x);",
        "options": ["Logs 20", "Logs 10", "Logs undefined", "Throws an error"],
        "answer": "Logs 20",
        "difficulty": "Medium",
        "explanation": "Reassigning 'obj.x' updates the property, logging 20."
    },
    {
        "question": "What does this code do: let obj = { calc: function() { return 2 * 2; } }; console.log(obj.calc());",
        "options": ["4", "undefined", "calc", "Error"],
        "answer": "4",
        "difficulty": "Medium",
        "explanation": "The 'calc' method returns the result of 2 * 2, which is 4."
    },
    {
        "question": "What does this code do: let obj = { greet() { return 'Hi'; } }; console.log(obj.greet());",
        "options": ["Logs 'Hi'", "Logs undefined", "Logs 'greet'", "Throws an error"],
        "answer": "Logs 'Hi'",
        "difficulty": "Medium",
        "explanation": "The 'greet' method returns 'Hi' when called."
    },
    {
        "question": "What does this code do: let obj = { x: 1, y: 2 }; console.log(Object.keys(obj).length);",
        "options": ["Logs 2", "Logs 1", "Logs undefined", "Throws an error"],
        "answer": "Logs 2",
        "difficulty": "Medium",
        "explanation": "The 'Object.keys()' method returns an array of property names, and 'length' counts them."
    },
    {
        "question": "What does this code do: function Person(name) { this.name = name; } let p = new Person('Alice'); console.log(p.name);",
        "options": ["Logs 'Alice'", "Logs 'Person'", "Logs undefined", "Throws an error"],
        "answer": "Logs 'Alice'",
        "difficulty": "Medium",
        "explanation": "The constructor sets the 'name' property, accessed as p.name."
    },
    {
        "question": "What does this code do: function User(name) { this.name = name; } let u = new User('Bob'); console.log(u.name);",
        "options": ["Logs 'Bob'", "Logs 'User'", "Logs undefined", "Throws an error"],
        "answer": "Logs 'Bob'",
        "difficulty": "Medium",
        "explanation": "The constructor sets 'name', accessed as u.name."
    },
    {
        "question": "What does this code do: function Car() { } Car.prototype.drive = function() { return 'Driving'; }; let c = new Car(); console.log(c.drive());",
        "options": ["Logs 'Driving'", "Logs undefined", "Logs 'Car'", "Throws an error"],
        "answer": "Logs 'Driving'",
        "difficulty": "Medium",
        "explanation": "The 'drive' method on the prototype returns 'Driving' for the instance."
    },
    {
        "question": "What does this code do: function Animal() { } Animal.prototype.speak = function() { return 'Woof'; }; let a = new Animal(); console.log(a.speak());",
        "options": ["Logs 'Woof'", "Logs undefined", "Logs 'Animal'", "Throws an error"],
        "answer": "Logs 'Woof'",
        "difficulty": "Medium",
        "explanation": "The 'speak' method on the prototype returns 'Woof'."
    },
    {
        "question": "What does this code do: function Shape() { } Shape.prototype.getType = function() { return 'Shape'; }; let s = new Shape(); console.log(s.getType());",
        "options": ["Logs 'Shape'", "Logs undefined", "Logs 'getType'", "Throws an error"],
        "answer": "Logs 'Shape'",
        "difficulty": "Medium",
        "explanation": "The 'getType' method on the prototype returns 'Shape'."
    },
    {
        "question": "What is the output of: let obj = { x: 1 }; console.log(obj.hasOwnProperty('x'));",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The 'hasOwnProperty()' method returns true if 'x' is a direct property of the object."
    },
    {
        "question": "What does this code do: let obj = { x: 1 }; console.log('x' in obj);",
        "options": ["Logs true", "Logs false", "Logs undefined", "Throws an error"],
        "answer": "Logs true",
        "difficulty": "Medium",
        "explanation": "The 'in' operator returns true if 'x' exists in the object."
    },
    {
        "question": "What does this code do: window.location.href = 'https://example.com';",
        "options": ["Navigates to https://example.com", "Reloads the current page", "Opens a new tab", "Changes the page title"],
        "answer": "Navigates to https://example.com",
        "difficulty": "Medium",
        "explanation": "Setting 'location.href' navigates to the specified URL."
    },
    {
        "question": "What does this code do: window.location.pathname = '/new';",
        "options": ["Navigates to /new on the current domain", "Reloads the page", "Opens a new tab", "Changes the query string"],
        "answer": "Navigates to /new on the current domain",
        "difficulty": "Medium",
        "explanation": "Setting 'location.pathname' navigates to the new path."
    },
    {
        "question": "What does this code do: window.location.assign('https://example.com');",
        "options": ["Navigates to https://example.com", "Reloads the current page", "Opens a new tab", "Changes the page title"],
        "answer": "Navigates to https://example.com",
        "difficulty": "Medium",
        "explanation": "The 'location.assign()' method loads a new URL in the current window."
    },
    {
        "question": "What does this code do: window.location.replace('https://example.com');",
        "options": ["Navigates to https://example.com without history", "Adds to history", "Reloads the page", "Opens a new tab"],
        "answer": "Navigates to https://example.com without history",
        "difficulty": "Medium",
        "explanation": "The 'location.replace()' method navigates without adding to browser history."
    },
    {
        "question": "What does this code do: window.history.back();",
        "options": ["Navigates to the previous page", "Navigates to the next page", "Reloads the page", "Opens a new tab"],
        "answer": "Navigates to the previous page",
        "difficulty": "Medium",
        "explanation": "The 'history.back()' method moves to the previous page in the browser’s history."
    },
    {
        "question": "What does this code do: window.history.forward();",
        "options": ["Navigates to the next page", "Navigates to the previous page", "Reloads the page", "Opens a new tab"],
        "answer": "Navigates to the next page",
        "difficulty": "Medium",
        "explanation": "The 'history.forward()' method moves to the next page in the browser’s history."
    },
    {
        "question": "What does this code do: document.body.style.height = '100vh';",
        "options": ["Sets body height to full viewport height", "Sets body width to full viewport", "Hides the body", "Scrolls the body"],
        "answer": "Sets body height to full viewport height",
        "difficulty": "Medium",
        "explanation": "Setting '100vh' sets the body’s height to the full viewport height."
    },
    {
        "question": "What does this code do: document.documentElement.style.width = '100vw';",
        "options": ["Sets html element width to full viewport", "Sets height to full viewport", "Hides the html element", "Scrolls the page"],
        "answer": "Sets html element width to full viewport",
        "difficulty": "Medium",
        "explanation": "Setting '100vw' sets the html element’s width to the full viewport."
    },
    {
        "question": "What does this code do: window.resizeTo(800, 600);",
        "options": ["Resizes the window to 800x600 pixels", "Moves the window to (800, 600)", "Scrolls the window", "Sets the viewport size"],
        "answer": "Resizes the window to 800x600 pixels",
        "difficulty": "Medium",
        "explanation": "The 'window.resizeTo()' method sets the browser window’s dimensions."
    },
    {
        "question": "What does this code do: window.moveTo(100, 100);",
        "options": ["Moves the window to (100, 100)", "Resizes the window", "Scrolls the window", "Opens a new window"],
        "answer": "Moves the window to (100, 100)",
        "difficulty": "Medium",
        "explanation": "The 'window.moveTo()' method repositions the browser window to the coordinates."
    },
    {
        "question": "What does this code do: let win = window.open(''); if (!win) console.log('Blocked');",
        "options": ["Logs 'Blocked' if popup is blocked", "Opens a new window", "Logs 'Blocked' always", "Throws an error"],
        "answer": "Logs 'Blocked' if popup is blocked",
        "difficulty": "Medium",
        "explanation": "The 'window.open()' method returns null if a popup blocker prevents the window."
    },
    {
        "question": "What does this code do: let win = window.open('https://example.com'); console.log(!!win);",
        "options": ["Logs true if window opens, false if blocked", "Logs the window object", "Logs undefined", "Throws an error"],
        "answer": "Logs true if window opens, false if blocked",
        "difficulty": "Medium",
        "explanation": "The '!!win' converts the window object to a boolean, false if blocked."
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



