
import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 50 questions covering all specified topics
quiz = [
    {
        "question": "What does `alert('Hello!')` do in JavaScript?\n```javascript\nalert('Hello!');\n```",
        "options": ["Logs to console", "Displays a popup", "Returns 'Hello!'", "Nothing"],
        "answer": "Displays a popup",
        "difficulty": "Easy",
        "explanation": "The `alert()` function displays a popup dialog with the message 'Hello!' in the browser.",
        "hint": "Think about user interaction in the browser."
    },
    {
        "question": "What is the value of `str` after this code runs?\n```javascript\nlet str = 'Java';\nstr = str + 'Script';\n```",
        "options": ["'JavaScript'", "'Java Script'", "'Java'", "'Script'"],
        "answer": "'JavaScript'",
        "difficulty": "Easy",
        "explanation": "The `+` operator concatenates 'Java' with 'Script', resulting in 'JavaScript'.",
        "hint": "Consider how strings are combined."
    },
    {
        "question": "What is the value of `num` after this code runs?\n```javascript\nlet num = 15;\nnum = num - 5;\n```",
        "options": ["10", "5", "15", "NaN"],
        "answer": "10",
        "difficulty": "Easy",
        "explanation": "The subtraction operator `-` subtracts 5 from 15, resulting in 10.",
        "hint": "Evaluate the arithmetic operation."
    },
    {
        "question": "Which variable name is illegal in JavaScript?\n```javascript\nlet 2ndPlace = 'Winner';\nlet place2 = 'Winner';\nlet $place = 'Winner';\nlet _place = 'Winner';\n```",
        "options": ["2ndPlace", "place2", "$place", "_place"],
        "answer": "2ndPlace",
        "difficulty": "Easy",
        "explanation": "Variable names cannot start with a number, making `2ndPlace` illegal.",
        "hint": "Recall JavaScript variable naming rules."
    },
    {
        "question": "What is the result of this expression?\n```javascript\n10 % 3\n```",
        "options": ["3", "1", "0", "10"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "The modulo operator `%` returns the remainder of 10 divided by 3, which is 1.",
        "hint": "Perform the division and check the remainder."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = (2 + 3) * 4;\n```",
        "options": ["20", "14", "10", "8"],
        "answer": "20",
        "difficulty": "Easy",
        "explanation": "Parentheses ensure `2 + 3` is evaluated first, giving 5, then `5 * 4 = 20`.",
        "hint": "Check operator precedence with parentheses."
    },
    {
        "question": "What is logged when the user clicks 'Cancel'?\n```javascript\nlet result = prompt('Enter name');\nconsole.log(result);\n```",
        "options": ["null", "undefined", "''", "'Cancel'"],
        "answer": "null",
        "difficulty": "Medium",
        "explanation": "The `prompt()` function returns `null` when the user clicks 'Cancel'.",
        "hint": "Consider what `prompt()` returns on cancellation."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 8;\nif (x > 5) {\n  console.log('Greater');\n}\n```",
        "options": ["'Greater'", "Nothing", "'Less'", "Error"],
        "answer": "'Greater'",
        "difficulty": "Easy",
        "explanation": "The condition `x > 5` is true for `x = 8`, so 'Greater' is logged.",
        "hint": "Evaluate the condition in the `if` statement."
    },
    {
        "question": "What is the result of this comparison?\n```javascript\n'5' == 5\n```",
        "options": ["true", "false", "NaN", "Error"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The `==` operator performs type coercion, so '5' is converted to 5, making the comparison true.",
        "hint": "Consider loose equality in JavaScript."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 10;\nif (x < 5) {\n  console.log('Small');\n} else if (x > 8) {\n  console.log('Large');\n}\n```",
        "options": ["'Small'", "'Large'", "Nothing", "Error"],
        "answer": "'Large'",
        "difficulty": "Medium",
        "explanation": "The condition `x > 8` is true for `x = 10`, so 'Large' is logged.",
        "hint": "Check which `else if` condition is evaluated."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 6;\nif (x > 5 && x < 8) {\n  console.log('In range');\n}\n```",
        "options": ["'In range'", "Nothing", "'Out of range'", "Error"],
        "answer": "'In range'",
        "difficulty": "Medium",
        "explanation": "Both conditions `x > 5` and `x < 8` are true for `x = 6`, so 'In range' is logged.",
        "hint": "Evaluate the logical AND operator."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 5;\nif (x > 3) {\n  if (x < 7) {\n    console.log('Nested');\n  }\n}\n```",
        "options": ["'Nested'", "Nothing", "Error", "5"],
        "answer": "'Nested'",
        "difficulty": "Medium",
        "explanation": "Both conditions `x > 3` and `x < 7` are true for `x = 5`, so 'Nested' is logged.",
        "hint": "Evaluate nested `if` conditions."
    },
    {
        "question": "What is the value of `arr` after this code runs?\n```javascript\nlet arr = [1, 2, 3];\narr.push(4);\n```",
        "options": ["[1, 2, 3, 4]", "[1, 2, 3]", "[4, 1, 2, 3]", "[1, 2, 4, 3]"],
        "answer": "[1, 2, 3, 4]",
        "difficulty": "Easy",
        "explanation": "The `push()` method adds 4 to the end of the array.",
        "hint": "Consider what `push()` does to an array."
    },
    {
        "question": "What is the value of `arr` after this code runs?\n```javascript\nlet arr = [1, 2, 3];\narr.pop();\n```",
        "options": ["[1, 2]", "[1, 3]", "[2, 3]", "[1, 2, 3]"],
        "answer": "[1, 2]",
        "difficulty": "Easy",
        "explanation": "The `pop()` method removes the last element, resulting in `[1, 2]`.",
        "hint": "Consider what `pop()` does to an array."
    },
    {
        "question": "What is the value of `arr` after this code runs?\n```javascript\nlet arr = [1, 2, 3];\narr.splice(1, 1, 4);\n```",
        "options": ["[1, 4, 3]", "[1, 2, 4]", "[4, 2, 3]", "[1, 2, 3, 4]"],
        "answer": "[1, 4, 3]",
        "difficulty": "Medium",
        "explanation": "The `splice(1, 1, 4)` method removes 1 element at index 1 and inserts 4.",
        "hint": "Understand the `splice()` method parameters."
    },
    {
        "question": "What is logged to the console?\n```javascript\nfor (let i = 0; i < 3; i++) {\n  console.log(i);\n}\n```",
        "options": ["0, 1, 2", "1, 2, 3", "0, 1, 2, 3", "Nothing"],
        "answer": "0, 1, 2",
        "difficulty": "Medium",
        "explanation": "The `for` loop iterates from `i = 0` to `i = 2`, logging each value.",
        "hint": "Trace the loop iterations."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet arr = [1, 2, 3];\nfor (let i = 0; i < arr.length; i++) {\n  if (arr[i] === 2) {\n    break;\n  }\n  console.log(arr[i]);\n}\n```",
        "options": ["1", "1, 2", "1, 2, 3", "Nothing"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "The loop breaks when `arr[i] === 2`, so only `1` is logged.",
        "hint": "Consider the effect of `break` in the loop."
    },
    {
        "question": "What is logged to the console?\n```javascript\nfor (let i = 1; i <= 2; i++) {\n  for (let j = 1; j <= 2; j++) {\n    console.log(i);\n  }\n}\n```",
        "options": ["1, 1, 2, 2", "1, 2", "1, 2, 1, 2", "Nothing"],
        "answer": "1, 1, 2, 2",
        "difficulty": "Hard",
        "explanation": "The inner loop logs `i` twice for each outer loop iteration, resulting in 1, 1, 2, 2.",
        "hint": "Trace the nested loop iterations."
    },
    {
        "question": "What is the value of `str` after this code runs?\n```javascript\nlet str = 'hello';\nstr = str.toUpperCase();\n```",
        "options": ["'HELLO'", "'hello'", "'Hello'", "'hELLO'"],
        "answer": "'HELLO'",
        "difficulty": "Easy",
        "explanation": "The `toUpperCase()` method converts all characters to uppercase.",
        "hint": "Consider the effect of `toUpperCase()`."
    },
    {
        "question": "What is the value of `str` after this code runs?\n```javascript\nlet str = 'JavaScript';\nstr = str.substring(0, 4);\n```",
        "options": ["'Java'", "'Script'", "'JavaS'", "'JavaScript'"],
        "answer": "'Java'",
        "difficulty": "Medium",
        "explanation": "The `substring(0, 4)` method extracts characters from index 0 to 3, resulting in 'Java'.",
        "hint": "Check the indices used in `substring()`."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet str = 'Hello World';\nconsole.log(str.includes('World'));\n```",
        "options": ["true", "false", "'World'", "Error"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The `includes()` method checks if 'World' is a substring, returning `true`.",
        "hint": "Consider what `includes()` checks for."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet str = 'JavaScript';\nconsole.log(str.charAt(4));\n```",
        "options": ["'S'", "'s'", "'c'", "''"],
        "answer": "'S'",
        "difficulty": "Medium",
        "explanation": "The `charAt(4)` method returns the character at index 4, which is 'S'.",
        "hint": "Count the character position in the string."
    },
    {
        "question": "What is the value of `str` after this code runs?\n```javascript\nlet str = 'hello';\nstr = str.replace('h', 'H');\n```",
        "options": ["'Hello'", "'hello'", "'Hhello'", "'Helloo'"],
        "answer": "'Hello'",
        "difficulty": "Medium",
        "explanation": "The `replace()` method replaces the first 'h' with 'H', resulting in 'Hello'.",
        "hint": "Consider what `replace()` does with the first occurrence."
    },
    {
        "question": "What is the value of `num` after this code runs?\n```javascript\nlet num = Math.round(7.6);\n```",
        "options": ["7", "8", "7.6", "8.0"],
        "answer": "8",
        "difficulty": "Medium",
        "explanation": "The `Math.round()` function rounds 7.6 to the nearest integer, which is 8.",
        "hint": "Consider how `Math.round()` handles decimals."
    },
    {
        "question": "What is logged to the console?\n```javascript\nconsole.log(Math.random());\n```",
        "options": ["A number between 0 and 1", "A number between 1 and 10", "A whole number", "Nothing"],
        "answer": "A number between 0 and 1",
        "difficulty": "Easy",
        "explanation": "The `Math.random()` function returns a random number between 0 (inclusive) and 1 (exclusive).",
        "hint": "Consider the range of `Math.random()`."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = parseInt('123');\n```",
        "options": ["123", "'123'", "NaN", "Error"],
        "answer": "123",
        "difficulty": "Medium",
        "explanation": "The `parseInt()` function converts the string '123' to the number 123.",
        "hint": "Check how `parseInt()` converts strings."
    },
    {
        "question": "What is the value of `str` after this code runs?\n```javascript\nlet str = '123';\nstr = Number(str).toString();\n```",
        "options": ["'123'", "123", "'NaN'", "Error"],
        "answer": "'123'",
        "difficulty": "Medium",
        "explanation": "The `Number()` function converts '123' to 123, and `toString()` converts it back to '123'.",
        "hint": "Trace the conversion process."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = 3.14159;\nx = x.toFixed(2);\n```",
        "options": ["'3.14'", "3.14", "'3.14159'", "3"],
        "answer": "'3.14'",
        "difficulty": "Medium",
        "explanation": "The `toFixed(2)` method formats the number to 2 decimal places and returns it as a string, '3.14'.",
        "hint": "Check the return type of `toFixed()`."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet date = new Date('2025-06-28');\nconsole.log(date.getFullYear());\n```",
        "options": ["2025", "6", "28", "Error"],
        "answer": "2025",
        "difficulty": "Medium",
        "explanation": "The `getFullYear()` method returns the year of the date, which is 2025.",
        "hint": "Check what `getFullYear()` extracts."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet date = new Date('2025-06-28');\nconsole.log(date.getMonth());\n```",
        "options": ["5", "6", "28", "2025"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The `getMonth()` method returns the month (0-11), so June is 5.",
        "hint": "Remember months are zero-based in JavaScript."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet date = new Date('2025-06-28');\ndate.setFullYear(2026);\nconsole.log(date.getFullYear());\n```",
        "options": ["2025", "2026", "6", "28"],
        "answer": "2026",
        "difficulty": "Medium",
        "explanation": "The `setFullYear(2026)` method changes the year to 2026, and `getFullYear()` returns it.",
        "hint": "Check how `setFullYear()` modifies the date."
    },
    {
        "question": "What does this function return?\n```javascript\nfunction square(num) {\n  return num * num;\n}\nconsole.log(square(4));\n```",
        "options": ["16", "8", "4", "Error"],
        "answer": "16",
        "difficulty": "Easy",
        "explanation": "The function `square` returns `num * num`, so `square(4)` returns `4 * 4 = 16`.",
        "hint": "Evaluate the function's return value."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = 0;\nfunction increment(num) {\n  return num + 1;\n}\nx = increment(5);\n```",
        "options": ["6", "5", "1", "0"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "The function `increment` returns `num + 1`, so `increment(5)` returns 6, assigned to `x`.",
        "hint": "Check the function's parameter and return value."
    },
    {
        "question": "What is the value of `x` after this code runs?\n```javascript\nlet x = 10;\nfunction setX() {\n  let x = 20;\n}\nsetX();\n```",
        "options": ["10", "20", "undefined", "Error"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "The `x` inside `setX` is a local variable, so the global `x` remains 10.",
        "hint": "Consider variable scope in functions."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 3;\nswitch (x) {\n  case 3:\n    console.log('Three');\n    break;\n  default:\n    console.log('Other');\n}\n```",
        "options": ["'Three'", "'Other'", "Nothing", "Error"],
        "answer": "'Three'",
        "difficulty": "Medium",
        "explanation": "The `switch` statement matches `x = 3` to `case 3`, logging 'Three' and breaking.",
        "hint": "Trace the `switch` case execution."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet x = 5;\nswitch (x) {\n  case 3:\n    console.log('Three');\n    break;\n  case 5:\n    console.log('Five');\n}\n```",
        "options": ["'Three'", "'Five'", "Nothing", "'Three', 'Five'"],
        "answer": "'Five'",
        "difficulty": "Medium",
        "explanation": "The `switch` matches `x = 5` to `case 5`, logging 'Five'. No `break` causes fall-through, but no further cases apply.",
        "hint": "Check for fall-through behavior in `switch`."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet i = 0;\nwhile (i < 2) {\n  console.log(i);\n  i++;\n}\n```",
        "options": ["0, 1", "0, 1, 2", "1, 2", "Nothing"],
        "answer": "0, 1",
        "difficulty": "Medium",
        "explanation": "The `while` loop logs `i` and increments it until `i < 2` is false, logging 0 and 1.",
        "hint": "Trace the `while` loop iterations."
    },
    {
        "question": "What is logged to the console?\n```javascript\nlet i = 0;\ndo {\n  console.log(i);\n  i++;\n} while (i < 2);\n```",
        "options": ["0, 1", "0, 1, 2", "1, 2", "Nothing"],
        "answer": "0, 1",
        "difficulty": "Medium",
        "explanation": "The `do...while` loop logs `i` and increments it, continuing until `i < 2` is false, logging 0 and 1.",
        "hint": "Consider the guaranteed first iteration of `do...while`."
    },
    {
        "question": "Where should JavaScript code be placed in an HTML file to ensure it runs after the DOM is loaded?\n```html\n<script>...</script>\n```",
        "options": ["In the `<head>`", "At the end of `<body>`", "Before `<!DOCTYPE html>`", "Anywhere"],
        "answer": "At the end of `<body>`",
        "difficulty": "Medium",
        "explanation": "Placing `<script>` at the end of `<body>` ensures the DOM is fully loaded before execution.",
        "hint": "Think about DOM loading order."
    },
    {
        "question": "What is the purpose of this comment?\n```javascript\n// This is a comment\nlet x = 10;\n```",
        "options": ["Executes code", "Documents code", "Logs to console", "Defines a variable"],
        "answer": "Documents code",
        "difficulty": "Easy",
        "explanation": "Comments like `//` are used to document or explain code without affecting execution.",
        "hint": "Consider the role of comments in code."
    },
    {
        "question": "What does this code do?\n```javascript\ndocument.querySelector('a').onclick = function() { console.log('Clicked'); };\n```",
        "options": ["Logs 'Clicked' on page load", "Logs 'Clicked' when a link is clicked", "Changes the link text", "Nothing"],
        "answer": "Logs 'Clicked' when a link is clicked",
        "difficulty": "Medium",
        "explanation": "The `onclick` event handler logs 'Clicked' when the link is clicked.",
        "hint": "Check the event being assigned."
    },
    {
        "question": "What does this code do?\n```javascript\ndocument.querySelector('button').addEventListener('click', () => console.log('Button'));\n```",
        "options": ["Logs 'Button' on page load", "Logs 'Button' when clicked", "Changes button text", "Nothing"],
        "answer": "Logs 'Button' when clicked",
        "difficulty": "Medium",
        "explanation": "The `addEventListener` assigns a click event to the button, logging 'Button' when clicked.",
        "hint": "Consider how `addEventListener` works."
    },
    {
        "question": "What does this code do?\n```javascript\ndocument.querySelector('div').onmouseover = function() { console.log('Hover'); };\n```",
        "options": ["Logs 'Hover' on click", "Logs 'Hover' on mouseover", "Changes div text", "Nothing"],
        "answer": "Logs 'Hover' on mouseover",
        "difficulty": "Medium",
        "explanation": "The `onmouseover` event triggers when the mouse hovers over the div, logging 'Hover'.",
        "hint": "Check the mouse event type."
    },
    {
        "question": "What is the value of `value` after this code runs?\n```javascript\nlet value = document.querySelector('input').value;\n```",
        "options": ["The input's value", "undefined", "null", "The input element"],
        "answer": "The input's value",
        "difficulty": "Medium",
        "explanation": "The `value` property returns the current value of the input element.",
        "hint": "Consider what `value` retrieves from an input."
    },
    {
        "question": "What does this code do?\n```javascript\ndocument.querySelector('input').value = 'Hello';\n```",
        "options": ["Reads the input value", "Sets the input value to 'Hello'", "Logs 'Hello'", "Nothing"],
        "answer": "Sets the input value to 'Hello'",
        "difficulty": "Medium",
        "explanation": "Assigning to the `value` property sets the input element's value to 'Hello'.",
        "hint": "Check what assigning to `value` does."
    },
    {
        "question": "What does this code do?\n```javascript\ndocument.querySelector('p').innerText = 'New Text';\n```",
        "options": ["Logs 'New Text'", "Sets paragraph text to 'New Text'", "Reads paragraph text", "Nothing"],
        "answer": "Sets paragraph text to 'New Text'",
        "difficulty": "Medium",
        "explanation": "The `innerText` property sets the text content of the paragraph to 'New Text'.",
        "hint": "Consider what `innerText` modifies."
    },
    {
        "question": "What does this code do?\n```javascript\ndocument.querySelector('img').src = 'new.jpg';\n```",
        "options": ["Changes the image source", "Logs the image source", "Reads the image source", "Nothing"],
        "answer": "Changes the image source",
        "difficulty": "Medium",
        "explanation": "Assigning to the `src` property changes the image displayed to 'new.jpg'.",
        "hint": "Check what `src` modifies on an image."
    },
    {
        "question": "What does this code do?\n```javascript\ndocument.querySelector('img').className = 'active';\n```",
        "options": ["Adds a class to the image", "Removes a class", "Logs the class", "Nothing"],
        "answer": "Adds a class to the image",
        "difficulty": "Medium",
        "explanation": "The `className` property sets the class of the image to 'active'.",
        "hint": "Consider how `className` affects elements."
    },
    {
        "question": "What does this code do?\n```javascript\ndocument.querySelector('div').style.backgroundColor = 'blue';\n```",
        "options": ["Sets the div's background to blue", "Logs the background color", "Removes the background", "Nothing"],
        "answer": "Sets the div's background to blue",
        "difficulty": "Medium",
        "explanation": "The `style.backgroundColor` property sets the div's background color to blue.",
        "hint": "Check what `style` modifies."
    },
    {
        "question": "What does this code return?\n```javascript\ndocument.getElementsByTagName('p');\n```",
        "options": ["A single paragraph", "An array-like list of paragraphs", "The first paragraph", "Nothing"],
        "answer": "An array-like list of paragraphs",
        "difficulty": "Medium",
        "explanation": "The `getElementsByTagName()` method returns an HTMLCollection of all `<p>` elements.",
        "hint": "Consider what `getElementsByTagName` targets."
    },
    {
        "question": "What does this code do?\n```javascript\nlet paras = document.getElementsByTagName('p');\nparas[0].innerText = 'First';\n```",
        "options": ["Sets first paragraph text to 'First'", "Sets all paragraphs to 'First'", "Logs 'First'", "Nothing"],
        "answer": "Sets first paragraph text to 'First'",
        "difficulty": "Medium",
        "explanation": "The first `<p>` element in the HTMLCollection has its `innerText` set to 'First'.",
        "hint": "Check how indexing works with HTMLCollection."
    },
    {
        "question": "What is the DOM in JavaScript?",
        "options": ["A database", "A programming interface for HTML", "A JavaScript function", "A styling method"],
        "answer": "A programming interface for HTML",
        "difficulty": "Easy",
        "explanation": "The DOM (Document Object Model) is a programming interface for manipulating HTML and XML documents.",
        "hint": "Think about how JavaScript interacts with HTML."
    },
    {
        "question": "What is the parent of an element returned by `document.querySelector('p')`?\n```javascript\nlet p = document.querySelector('p');\n```",
        "options": ["The `<body>` element", "The element containing `<p>`", "The `<html>` element", "Nothing"],
        "answer": "The element containing `<p>`",
        "difficulty": "Medium",
        "explanation": "The parent is the element that directly contains the `<p>` element, accessed via `parentNode`.",
        "hint": "Consider the DOM tree structure."
    },
    {
        "question": "What does this code return?\n```javascript\ndocument.querySelector('div').children;\n```",
        "options": ["All child elements", "The first child", "The parent", "Nothing"],
        "answer": "All child elements",
        "difficulty": "Medium",
        "explanation": "The `children` property returns an HTMLCollection of all child elements of the div.",
        "hint": "Check what `children` retrieves in the DOM."
    },
    {
        "question": "What is the value of `node.nodeType` for a text node?\n```javascript\nlet node = document.createTextNode('text');\n```",
        "options": ["1", "3", "8", "11"],
        "answer": "3",
        "difficulty": "Hard",
        "explanation": "The `nodeType` property returns 3 for text nodes in the DOM.",
        "hint": "Recall DOM node type values."
    },
    {
        "question": "What does this code return?\n```javascript\ndocument.querySelectorAll('.class');\n```",
        "options": ["A single element", "A NodeList of elements", "The first element", "Nothing"],
        "answer": "A NodeList of elements",
        "difficulty": "Medium",
        "explanation": "The `querySelectorAll()` method returns a NodeList of all elements with the class 'class'.",
        "hint": "Check how `querySelectorAll` differs from `querySelector`."
    },
    {
        "question": "What does this code return?\n```javascript\ndocument.querySelector('div').tagName;\n```",
        "options": ["'div'", "'DIV'", "The div's class", "Nothing"],
        "answer": "'DIV'",
        "difficulty": "Medium",
        "explanation": "The `tagName` property returns the tag name of the element in uppercase, 'DIV'.",
        "hint": "Check what `tagName` returns."
    },
    {
        "question": "What does this code return?\n```javascript\ndocument.getElementsByTagName('p').length;\n```",
        "options": ["The number of `<p>` elements", "The first `<p>` element", "0", "Nothing"],
        "answer": "The number of `<p>` elements",
        "difficulty": "Medium",
        "explanation": "The `length` property of the HTMLCollection returns the number of `<p>` elements.",
        "hint": "Consider what `length` measures."
    },
    {
        "question": "What does this code do?\n```javascript\ndocument.querySelector('img').setAttribute('alt', 'Image');\n```",
        "options": ["Sets the image's alt attribute", "Gets the alt attribute", "Removes the alt attribute", "Nothing"],
        "answer": "Sets the image's alt attribute",
        "difficulty": "Medium",
        "explanation": "The `setAttribute()` method sets the 'alt' attribute of the image to 'Image'.",
        "hint": "Check what `setAttribute()` modifies."
    },
    {
        "question": "What does this code return?\n```javascript\ndocument.querySelector('img').getAttribute('src');\n```",
        "options": ["The image's src value", "The image element", "null", "Nothing"],
        "answer": "The image's src value",
        "difficulty": "Medium",
        "explanation": "The `getAttribute('src')` method returns the value of the image's src attribute.",
        "hint": "Check what `getAttribute()` retrieves."
    },
    {
        "question": "What does this code do?\n```javascript\nlet p = document.createElement('p');\ndocument.body.appendChild(p);\n```",
        "options": ["Adds a paragraph to `<body>`", "Removes a paragraph", "Logs the paragraph", "Nothing"],
        "answer": "Adds a paragraph to `<body>`",
        "difficulty": "Medium",
        "explanation": "The `createElement()` and `appendChild()` methods create and add a `<p>` element to `<body>`.",
        "hint": "Consider how elements are added to the DOM."
    },
    {
        "question": "What does this code do?\n```javascript\nlet div = document.querySelector('div');\nlet p = document.createElement('p');\ndiv.insertBefore(p, div.firstChild);\n```",
        "options": ["Inserts a paragraph as the first child", "Inserts a paragraph as the last child", "Removes the first child", "Nothing"],
        "answer": "Inserts a paragraph as the first child",
        "difficulty": "Hard",
        "explanation": "The `insertBefore()` method inserts the new `<p>` before the first child of the div.",
        "hint": "Check the parameters of `insertBefore()`."
    },
    {
        "question": "What is the value of `obj.name` after this code runs?\n```javascript\nlet obj = { name: 'John' };\n```",
        "options": ["'John'", "undefined", "null", "Error"],
        "answer": "'John'",
        "difficulty": "Easy",
        "explanation": "The `name` property of the object `obj` is set to 'John'.",
        "hint": "Check how object properties are accessed."
    },
    {
        "question": "What does this code return?\n```javascript\nlet obj = { greet: function() { return 'Hello'; } };\nconsole.log(obj.greet());\n```",
        "options": ["'Hello'", "undefined", "null", "Error"],
        "answer": "'Hello'",
        "difficulty": "Medium",
        "explanation": "The `greet` method of the object returns 'Hello' when called.",
        "hint": "Consider how object methods are invoked."
    },
    {
        "question": "What does this code do?\n```javascript\nfunction Person(name) {\n  this.name = name;\n}\nlet person = new Person('Alice');\n```",
        "options": ["Creates an object with a name property", "Logs 'Alice'", "Defines a function", "Nothing"],
        "answer": "Creates an object with a name property",
        "difficulty": "Medium",
        "explanation": "The `Person` constructor creates an object with a `name` property set to 'Alice'.",
        "hint": "Check how constructors work with `new`."
    },
    {
        "question": "What does this code do?\n```javascript\nfunction Person() {\n  this.greet = function() { return 'Hi'; };\n}\nlet p = new Person();\nconsole.log(p.greet());\n```",
        "options": ["Logs 'Hi'", "Logs 'Person'", "Creates a function", "Error"],
        "answer": "Logs 'Hi'",
        "difficulty": "Medium",
        "explanation": "The constructor assigns a `greet` method to the object, which returns 'Hi' when called.",
        "hint": "Consider how methods are defined in constructors."
    },
    {
        "question": "What does this code do?\n```javascript\nfunction Person() {}\nPerson.prototype.sayHello = function() { return 'Hello'; };\nlet p = new Person();\nconsole.log(p.sayHello());\n```",
        "options": ["Logs 'Hello'", "Logs 'Person'", "Error", "Nothing"],
        "answer": "Logs 'Hello'",
        "difficulty": "Hard",
        "explanation": "The `sayHello` method is added to the `Person` prototype, so `p.sayHello()` logs 'Hello'.",
        "hint": "Check how prototype methods are inherited."
    },
    {
        "question": "What does this code return?\n```javascript\nlet obj = { name: 'John' };\nconsole.log('name' in obj);\n```",
        "options": ["true", "false", "'John'", "Error"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The `in` operator checks if the 'name' property exists in `obj`, returning `true`.",
        "hint": "Consider how `in` checks for properties."
    }
]

# Cache shuffled quiz
@st.cache_data
def shuffle_quiz(_quiz):
    shuffled = random.sample(_quiz, len(_quiz))
    for i in range(len(shuffled) - 1):
        if i < len(shuffled) - 1 and shuffled[i]["difficulty"] == shuffled[i + 1]["difficulty"]:
            for j in range(i + 2, len(shuffled)):
                if shuffled[j]["difficulty"] != shuffled[i]["difficulty"]:
                    shuffled[i + 1], shuffled[j] = shuffled[j], shuffled[i + 1]
                    break
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        labeled_options = list(zip(q["options"], ["A", "B", "C", "D"]))
        random.shuffle(labeled_options)
        q["display_options"] = [f"{label}: {option}" for option, label in labeled_options]
        for option, label in labeled_options:
            if option == q["answer"]:
                q["labeled_answer"] = f"{label}: {option}"
                break
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
        "show_hint": False,
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
        "show_hint": False,
        "started": False
    })
    st.rerun()

# Skip question
def skip_question():
    st.session_state.answers[st.session_state.current_q] = {
        "question": st.session_state.quiz_data[st.session_state.current_q]["question"],
        "user_answer": "Skipped",
        "correct_answer": st.session_state.quiz_data[st.session_state.current_q]["labeled_answer"],
        "is_correct": False,
        "difficulty": st.session_state.quiz_data[st.session_state.current_q]["difficulty"]
    }
    st.session_state.score = max(0, st.session_state.score - 0.5)
    st.session_state.streak = 0
    if st.session_state.current_q < len(quiz) - 1:
        st.session_state.current_q += 1
    else:
        st.session_state.show_results = True
    st.session_state.selected_option = None
    st.session_state.feedback = None
    st.session_state.show_hint = False
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
        <p style="color: #b0b0d0;">30 minutes, 1-3 points per correct answer. Ready?</p>
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
                        disabled=st.session_state.selected_option is not None,
                        help="Select this option"
                    ):
                        original_option = option[3:]
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
                            points = {"Easy": 1, "Medium": 2, "Hard": 3}[q["difficulty"]]
                            st.session_state.score += points
                            st.session_state.streak += 1
                            if st.session_state.streak >= 3:
                                st.session_state.score += 0.5
                        else:
                            st.session_state.streak = 0
                        st.rerun()

                # Feedback
                if st.session_state.feedback:
                    if st.session_state.feedback["is_correct"]:
                        st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="color: var(--text-color); font-size: 14px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                # Hint button
                if st.button("💡 Show Hint", key="hint", disabled=st.session_state.show_hint or st.session_state.selected_option is not None):
                    st.session_state.show_hint = True
                    st.session_state.score = max(0, st.session_state.score - 0.25)
                    st.rerun()
                if st.session_state.show_hint:
                    st.markdown(f'<div style="color: #facc15; font-size: 14px;">Hint: {q["hint"]}</div>', unsafe_allow_html=True)

                # Navigation
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("⬅ Previous", disabled=st.session_state.current_q == 0):
                        if st.session_state.current_q > 0 and st.session_state.answers[st.session_state.current_q] and st.session_state.answers[st.session_state.current_q]["is_correct"]:
                            points = {"Easy": 1, "Medium": 2, "Hard": 3}[st.session_state.answers[st.session_state.current_q]["difficulty"]]
                            st.session_state.score -= points
                            if st.session_state.streak >= 3:
                                st.session_state.score -= 0.5
                        st.session_state.current_q -= 1
                        st.session_state.selected_option = None
                        st.session_state.feedback = None
                        st.session_state.show_hint = False
                        st.rerun()
                with col2:
                    if st.button("⏭️ Skip", key="skip"):
                        skip_question()
                with col3:
                    if st.session_state.current_q < len(quiz) - 1:
                        if st.button("➡️ Next", disabled=st.session_state.selected_option is None):
                            st.session_state.current_q += 1
                            st.session_state.selected_option = None
                            st.session_state.feedback = None
                            st.session_state.show_hint = False
                            st.rerun()
                    else:
                        if st.button("🏁 Finish", disabled=st.session_state.selected_option is None):
                            st.session_state.show_results = True
                            st.rerun()

                # Reset quiz button
                if st.button("🔄 Reset Quiz", key="reset"):
                    reset_quiz()

                st.markdown("</div>", unsafe_allow_html=True)

        else:
            # Results
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 1800)
            total_possible_score = sum({"Easy": 1, "Medium": 2, "Hard": 3}[q["difficulty"]] for q in quiz)
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
                - ⏭️ Skipped: {sum(1 for ans in st.session_state.answers if ans and ans["user_answer"] == "Skipped")}<br>
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
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})" if ans["user_answer"] != "Skipped" else "⏭️ Skipped"
                    st.markdown(f'<div style="color: var(--text-color);">Question {i+1}: {ans["question"]}<br>Your Answer: {ans["user_answer"]}<br>{status}<br>Explanation: {quiz[i]["explanation"]}</div>', unsafe_allow_html=True)

            # Reset button
            if st.button("🔄 Play Again", key="play_again"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
