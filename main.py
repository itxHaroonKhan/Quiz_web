import streamlit as st
import random
from datetime import datetime
import uuid

quiz =[
    {
        "question": "How do you write a nested for loop to iterate over a 2D array in JavaScript?",
        "options": [
            "for (let i = 0; i < array.length; i++) { for (let j = 0; j < array[i].length; j++) { } }",
            "for (let i = 0; i < array; i++) { for (let j = 0; j < array[i]; j++) { } }",
            "for (let i in array) { for (let j in array[i]) { } }",
            "for (let i of array) { for (let j of array) { } }"
        ],
        "answer": "for (let i = 0; i < array.length; i++) { for (let j = 0; j < array[i].length; j++) { } }",
        "difficulty": "Medium",
        "explanation": "A nested for loop uses two indices: `i` for rows and `j` for columns, accessing each element as `array[i][j]`."
    },
    {
        "question": "What is the purpose of a nested for loop in JavaScript?",
        "options": [
            "To iterate over multiple dimensions of data",
            "To repeat a single loop multiple times",
            "To create a function inside another function",
            "To replace a while loop"
        ],
        "answer": "To iterate over multiple dimensions of data",
        "difficulty": "Easy",
        "explanation": "Nested for loops are used to process multi-dimensional data, like 2D arrays, by iterating over each dimension."
    },
    {
        "question": "How many times will the inner loop execute in `for (let i = 0; i < 3; i++) { for (let j = 0; j < 2; j++) { } }`?",
        "options": [
            "6 times",
            "3 times",
            "2 times",
            "5 times"
        ],
        "answer": "6 times",
        "difficulty": "Medium",
        "explanation": "The outer loop runs 3 times, and the inner loop runs 2 times per outer iteration, so 3 * 2 = 6 total iterations."
    },
    {
        "question": "What does the `toLowerCase()` method do in JavaScript?",
        "options": [
            "Converts a string to lowercase",
            "Converts a string to uppercase",
            "Capitalizes the first letter",
            "Removes spaces from a string"
        ],
        "answer": "Converts a string to lowercase",
        "difficulty": "Easy",
        "explanation": "`toLowerCase()` converts all characters in a string to lowercase, e.g., 'HELLO' becomes 'hello'."
    },
    {
        "question": "How do you convert the first letter of a string to uppercase in JavaScript?",
        "options": [
            "string.charAt(0).toUpperCase() + string.slice(1)",
            "string.toUpperCase(0)",
            "string.capitalize()",
            "string[0].toUpperCase() + string.substring(1)"
        ],
        "answer": "string.charAt(0).toUpperCase() + string.slice(1)",
        "difficulty": "Medium",
        "explanation": "To capitalize the first letter, use `charAt(0).toUpperCase()` for the first character and `slice(1)` for the rest."
    },
    {
        "question": "What is the result of `'Hello'.length` in JavaScript?",
        "options": [
            "5",
            "4",
            "6",
            "0"
        ],
        "answer": "5",
        "difficulty": "Easy",
        "explanation": "The `length` property returns the number of characters in a string, so `'Hello'.length` returns 5."
    },
    {
        "question": "How do you extract characters from index 1 to 3 in a string?",
        "options": [
            "string.slice(1, 4)",
            "string.substring(1, 3)",
            "string.substr(1, 3)",
            "string.cut(1, 3)"
        ],
        "answer": "string.slice(1, 4)",
        "difficulty": "Medium",
        "explanation": "`slice(1, 4)` extracts characters from index 1 up to (but not including) index 4, giving 3 characters."
    },
    {
        "question": "Which method extracts a substring based on a starting index and length?",
        "options": [
            "string.substr(start, length)",
            "string.slice(start, length)",
            "string.substring(start, length)",
            "string.extract(start, length)"
        ],
        "answer": "string.substr(start, length)",
        "difficulty": "Medium",
        "explanation": "`substr(start, length)` extracts `length` characters starting from `start`. Note: `substr` is deprecated."
    },
    {
        "question": "How do you check if a string contains the substring 'test'?",
        "options": [
            "string.includes('test')",
            "string.contains('test')",
            "string.has('test')",
            "string.find('test')"
        ],
        "answer": "string.includes('test')",
        "difficulty": "Easy",
        "explanation": "`includes('test')` returns `true` if the string contains 'test', otherwise `false`."
    },
    {
        "question": "What does `string.indexOf('text')` return if 'text' is not found?",
        "options": [
            "-1",
            "0",
            "null",
            "undefined"
        ],
        "answer": "-1",
        "difficulty": "Medium",
        "explanation": "`indexOf('text')` returns -1 if the substring 'text' is not found in the string."
    },
    {
        "question": "How do you find the character at index 2 in a string?",
        "options": [
            "string.charAt(2)",
            "string.getChar(2)",
            "string.char(2)",
            "string.atIndex(2)"
        ],
        "answer": "string.charAt(2)",
        "difficulty": "Easy",
        "explanation": "`charAt(2)` returns the character at index 2. Alternatively, `string[2]` also works."
    },
    {
        "question": "What is the modern way to access a character at a specific index in a string?",
        "options": [
            "string.at(index)",
            "string.charAt(index)",
            "string[index]",
            "string.get(index)"
        ],
        "answer": "string.at(index)",
        "difficulty": "Medium",
        "explanation": "`at(index)` is a modern method to access a character at a given index, supporting negative indices."
    },
    {
        "question": "How do you replace the first occurrence of 'a' with 'b' in a string?",
        "options": [
            "string.replace('a', 'b')",
            "string.replaceAll('a', 'b')",
            "string.swap('a', 'b')",
            "string.change('a', 'b')"
        ],
        "answer": "string.replace('a', 'b')",
        "difficulty": "Medium",
        "explanation": "`replace('a', 'b')` replaces only the first occurrence of 'a' with 'b'."
    },
    {
        "question": "How do you replace all occurrences of 'x' with 'y' in a string?",
        "options": [
            "string.replaceAll('x', 'y')",
            "string.replace('x', 'y')",
            "string.update('x', 'y')",
            "string.modify('x', 'y')"
        ],
        "answer": "string.replaceAll('x', 'y')",
        "difficulty": "Medium",
        "explanation": "`replaceAll('x', 'y')` replaces all instances of 'x' with 'y' in the string."
    },
    {
        "question": "What does `Math.round(3.7)` return in JavaScript?",
        "options": [
            "4",
            "3",
            "3.7",
            "4.0"
        ],
        "answer": "4",
        "difficulty": "Easy",
        "explanation": "`Math.round(3.7)` rounds 3.7 to the nearest integer, which is 4."
    },
    {
        "question": "How do you round a number down to the nearest integer?",
        "options": [
            "Math.floor(number)",
            "Math.round(number)",
            "Math.ceil(number)",
            "Math.trunc(number)"
        ],
        "answer": "Math.floor(number)",
        "difficulty": "Easy",
        "explanation": "`Math.floor(number)` rounds a number down to the nearest integer, e.g., 3.9 becomes 3."
    },
    {
        "question": "How do you round a number up to the nearest integer?",
        "options": [
            "Math.ceil(number)",
            "Math.round(number)",
            "Math.floor(number)",
            "Math.trunc(number)"
        ],
        "answer": "Math.ceil(number)",
        "difficulty": "Easy",
        "explanation": "`Math.ceil(number)` rounds a number up to the nearest integer, e.g., 3.1 becomes 4."
    },
    {
        "question": "What does `Math.random()` return in JavaScript?",
        "options": [
            "A number between 0 and 1",
            "A number between 1 and 10",
            "An integer between 0 and 100",
            "A random integer"
        ],
        "answer": "A number between 0 and 1",
        "difficulty": "Easy",
        "explanation": "`Math.random()` returns a random floating-point number between 0 (inclusive) and 1 (exclusive)."
    },
    {
        "question": "How do you generate a random integer between 1 and 10?",
        "options": [
            "Math.floor(Math.random() * 10) + 1",
            "Math.random() * 10",
            "Math.round(Math.random() * 10)",
            "Math.floor(Math.random() * 10)"
        ],
        "answer": "Math.floor(Math.random() * 10) + 1",
        "difficulty": "Medium",
        "explanation": "`Math.random() * 10` generates a number from 0 to 9.999..., `Math.floor` rounds it down, and `+ 1` shifts to 1–10."
    },
    {
        "question": "How do you convert the string '456' to an integer?",
        "options": [
            "parseInt('456')",
            "parseFloat('456')",
            "Number.parse('456')",
            "toInt('456')"
        ],
        "answer": "parseInt('456')",
        "difficulty": "Medium",
        "explanation": "`parseInt('456')` converts the string '456' to the integer 456."
    },
    {
        "question": "How do you convert the string '12.34' to a decimal number?",
        "options": [
            "parseFloat('12.34')",
            "parseInt('12.34')",
            "toFloat('12.34')",
            "Number.toDecimal('12.34')"
        ],
        "answer": "parseFloat('12.34')",
        "difficulty": "Medium",
        "explanation": "`parseFloat('12.34')` converts the string '12.34' to the floating-point number 12.34."
    },
    {
        "question": "How do you convert a number to a string in JavaScript?",
        "options": [
            "number.toString()",
            "number.toStr()",
            "convertToString(number)",
            "number.string()"
        ],
        "answer": "number.toString()",
        "difficulty": "Easy",
        "explanation": "`toString()` converts a number to a string, e.g., 123 becomes '123'."
    },
    {
        "question": "How do you convert a string to a number using the unary plus operator?",
        "options": [
            "+string",
            "string++",
            "++string",
            "-string"
        ],
        "answer": "+string",
        "difficulty": "Medium",
        "explanation": "The unary plus operator `+` converts a string to a number, e.g., +'123' returns 123."
    },
    {
        "question": "How do you format a number to exactly 3 decimal places?",
        "options": [
            "number.toFixed(3)",
            "number.toPrecision(3)",
            "number.round(3)",
            "number.limit(3)"
        ],
        "answer": "number.toFixed(3)",
        "difficulty": "Medium",
        "explanation": "`toFixed(3)` formats a number to 3 decimal places, returning a string, e.g., 3.14159 becomes '3.142'."
    },
    {
        "question": "What does `number.toPrecision(4)` do?",
        "options": [
            "Formats a number to 4 significant digits",
            "Formats a number to 4 decimal places",
            "Rounds a number to 4 integers",
            "Converts a number to a string with 4 characters"
        ],
        "answer": "Formats a number to 4 significant digits",
        "difficulty": "Medium",
        "explanation": "`toPrecision(4)` formats a number to 4 significant digits, e.g., 123.456 becomes '123.5'."
    },
    {
        "question": "How do you get the current date and time in JavaScript?",
        "options": [
            "new Date()",
            "Date.now()",
            "Date.getCurrent()",
            "new DateTime()"
        ],
        "answer": "new Date()",
        "difficulty": "Easy",
        "explanation": "`new Date()` creates a Date object representing the current date and time."
    },
    {
        "question": "What does `Date.now()` return?",
        "options": [
            "A timestamp in milliseconds",
            "A Date object",
            "The current date as a string",
            "The current time in seconds"
        ],
        "answer": "A timestamp in milliseconds",
        "difficulty": "Medium",
        "explanation": "`Date.now()` returns the number of milliseconds since January 1, 1970 (Unix epoch)."
    },
    {
        "question": "How do you extract the month from a Date object?",
        "options": [
            "date.getMonth()",
            "date.getDate()",
            "date.month()",
            "date.getMonthNumber()"
        ],
        "answer": "date.getMonth()",
        "difficulty": "Medium",
        "explanation": "`getMonth()` returns the month (0–11) of a Date object, where 0 is January."
    },
    {
        "question": "How do you get the day of the week from a Date object?",
        "options": [
            "date.getDay()",
            "date.getWeekday()",
            "date.day()",
            "date.getWeekDay()"
        ],
        "answer": "date.getDay()",
        "difficulty": "Medium",
        "explanation": "`getDay()` returns the day of the week (0–6), where 0 is Sunday."
    },
    {
        "question": "How do you create a Date object for March 10, 2023?",
        "options": [
            "new Date(2023, 2, 10)",
            "new Date(2023, 3, 10)",
            "new Date('2023-03-10')",
            "new Date('March 10, 2023')"
        ],
        "answer": "new Date(2023, 2, 10)",
        "difficulty": "Medium",
        "explanation": "`new Date(2023, 2, 10)` creates a Date for March 10, 2023, as months are 0-based."
    },
    {
        "question": "How do you create a Date object for a specific time on January 1, 2025?",
        "options": [
            "new Date(2025, 0, 1, 14, 30)",
            "new Date(2025, 1, 1, 14, 30)",
            "new Date('2025-01-01 14:30')",
            "new Date('January 1, 2025 14:30')"
        ],
        "answer": "new Date(2025, 0, 1, 14, 30)",
        "difficulty": "Medium",
        "explanation": "`new Date(2025, 0, 1, 14, 30)` creates a Date for January 1, 2025, at 2:30 PM."
    },
    {
        "question": "How do you set the month of a Date object to July?",
        "options": [
            "date.setMonth(6)",
            "date.setMonth(7)",
            "date.updateMonth(6)",
            "date.changeMonth(7)"
        ],
        "answer": "date.setMonth(6)",
        "difficulty": "Medium",
        "explanation": "`setMonth(6)` sets the month to July, as months are 0-based (0 = January, 6 = July)."
    },
    {
        "question": "How do you add one day to a Date object?",
        "options": [
            "date.setDate(date.getDate() + 1)",
            "date.addDay(1)",
            "date.setDay(date.getDay() + 1)",
            "date.updateDate(1)"
        ],
        "answer": "date.setDate(date.getDate() + 1)",
        "difficulty": "Medium",
        "explanation": "`setDate(date.getDate() + 1)` increments the day of the month by 1."
    },
    {
        "question": "How do you define an arrow function in JavaScript?",
        "options": [
            "const myFunc = () => {}",
            "function myFunc() => {}",
            "const myFunc = function() => {}",
            "arrow myFunc() {}"
        ],
        "answer": "const myFunc = () => {}",
        "difficulty": "Medium",
        "explanation": "Arrow functions are defined using the `=>` syntax, e.g., `const myFunc = () => {}`."
    },
    {
        "question": "What is a function expression in JavaScript?",
        "options": [
            "A function assigned to a variable",
            "A named function declaration",
            "A function inside a loop",
            "A function with no parameters"
        ],
        "answer": "A function assigned to a variable",
        "difficulty": "Medium",
        "explanation": "A function expression assigns an anonymous function to a variable, e.g., `const myFunc = function() {}`."
    },
    {
        "question": "How do you pass multiple parameters to a function?",
        "options": [
            "function myFunc(a, b, c) {}",
            "function myFunc(a; b; c) {}",
            "function myFunc[a, b, c] {}",
            "function myFunc {a, b, c}"
        ],
        "answer": "functionseye myFunc(a, b, c) {}",
        "difficulty": "Easy",
        "explanation": "Multiple parameters are passed in the parentheses, separated by commas, e.g., `myFunc(a, b, c)`."
    },
    {
        "question": "What happens if you call a function without passing required parameters?",
        "options": [
            "The missing parameters are `undefined`",
            "The function throws an error",
            "The function returns `null`",
            "The function skips execution"
        ],
        "answer": "The missing parameters are `undefined`",
        "difficulty": "Medium",
        "explanation": "If a parameter is not provided, it is set to `undefined` inside the function."
    },
    {
        "question": "How do you return multiple values from a function?",
        "options": [
            "return [value1, value2]",
            "return value1, value2",
            "return {value1, value2}",
            "return value1; value2"
        ],
        "answer": "return [value1, value2]",
        "difficulty": "Medium",
        "explanation": "Multiple values can be returned as an array or object, e.g., `return [value1, value2]`."
    },
    {
        "question": "What is the purpose of the `return` statement in a function?",
        "options": [
            "To send a value back and stop execution",
            "To declare a variable",
            "To loop through a function",
            "To call another function"
        ],
        "answer": "To send a value back and stop execution",
        "difficulty": "Easy",
        "explanation": "The `return` statement sends a value back to the caller and terminates the function."
    },
    {
        "question": "What is a global variable in JavaScript?",
        "options": [
            "A variable declared outside any function",
            "A variable inside a function",
            "A variable passed to a function",
            "A variable with a fixed value"
        ],
        "answer": "A variable declared outside any function",
        "difficulty": "Medium",
        "explanation": "Global variables are declared outside functions and are accessible everywhere in the code."
    },
    {
        "question": "What happens if a local variable has the same name as a global variable?",
        "options": [
            "The local variable takes precedence",
            "The global variable takes precedence",
            "An error is thrown",
            "Both variables are merged"
        ],
        "answer": "The local variable takes precedence",
        "difficulty": "Medium",
        "explanation": "Inside a function, a local variable shadows a global variable with the same name."
    },
    {
        "question": "How do you declare a variable as global inside a function?",
        "options": [
            "Declare it without `let`, `const`, or `var`",
            "Use `global var`",
            "Use$Ruse `let global`",
            "Use `const global`"
        ],
        "answer": "Declare it without `let`, `const`, or `var`",
        "difficulty": "Medium",
        "explanation": "Omitting `let`, `const`, or `var` makes a variable global, but this is not recommended."
    },
    {
        "question": "What is the purpose of a `switch` statement in JavaScript?",
        "options": [
            "To compare a rapporte multiple values",
            "To execute a loop",
            "To declare a function",
            "To handle events"
        ],
        "answer": "To compare multiple values",
        "difficulty": "Easy",
        "explanation": "A `switch` statement evaluates an expression and executes different code blocks based on its value."
    },
    {
        "question": "How do you write a `case` clause in a switch statement?",
        "options": [
            "case value:",
            "when value:",
            "if value:",
            "match value:"
        ],
        "answer": "case value:",
        "difficulty": "Easy",
        "explanation": "A `case` clause in a `switch` statement is written as `case value:`, followed by code to execute."
    },
    {
        "question": "What is the role of the `break` statement in a switch case?",
        "options": [
            "Stops the execution of the case block",
            "Continues to the next case",
            "Returns a value from the switch",
            "Declares a new case"
        ],
        "answer": "Stops the execution of the case block",
        "difficulty": "Medium",
        "explanation": "The `break` statement exits the current case block, preventing fall-through to the next case."
    },
    {
        "question": "How do you write a `default` case in a switch statement?",
        "options": [
            "default:",
            "else:",
            "otherwise:",
            "defaultCase:"
        ],
        "answer": "default:",
        "difficulty": "Easy",
        "explanation": "The `default:` case handles any value that doesn't match other cases in a `switch` statement."
    },
    {
        "question": "What happens if you omit a `break` statement in a switch case?",
        "options": [
            "The next case will also execute",
            "The switch statement will stop",
            "An error will occur",
            "The function will return"
        ],
        "answer": "The next case will also execute",
        "difficulty": "Medium",
        "explanation": "Without a `break`, execution continues to the next case (fall-through behavior)."
    },
    {
        "question": "How do you start a switch statement with a string variable `color`?",
        "options": [
            "switch (color) {",
            "case (color) {",
            "if (color) {",
            "match (color) {"
        ],
        "answer": "switch (color) {",
        "difficulty": "Easy",
        "explanation": "A `switch` statement starts with `switch (expression)`, where `color` is the expression to evaluate."
    },
    {
        "question": "What is the result of `'JavaScript'.toUpperCase()`?",
        "options": [
            "JAVASCRIPT",
            "javascript",
            "JavaScript",
            "JAVAScript"
        ],
        "answer": "JAVASCRIPT",
        "difficulty": "Easy",
        "explanation": "`toUpperCase()` converts all characters in a string to uppercase."
    },
    {
        "question": "How do you extract the last 3 characters of a string?",
        "options": [
            "string.slice(-3)",
            "string.substring(-3)",
            "string.substr(-3)",
            "string.last(3)"
        ],
        "answer": "string.slice(-3)",
        "difficulty": "Medium",
        "explanation": "`slice(-3)` extracts the last 3 characters by starting from the 3rd-to-last index."
    },
    {
        "question": "What does `string.includes('')` return for an empty string?",
        "options": [
            "true",
            "false",
            "null",
            "undefined"
        ],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "An empty string is considered a substring of any string, so `includes('')` returns `true`."
    },
    {
        "question": "What does `Math.trunc(5.7)` return?",
        "options": [
            "5",
            "6",
            "5.7",
            "6.0"
        ],
        "answer": "5",
        "difficulty": "Easy",
        "explanation": "`Math.trunc(5.7)` removes the decimal part, returning the integer 5."
    },
    {
        "question": "How do you generate a random integer between 0 and 99?",
        "options": [
            "Math.floor(Math.random() * 100)",
            "Math.random() * 100",
            "Math.round(Math.random() * 100)",
            "Math.floor(Math.random() * 99) + 1"
        ],
        "answer": "Math.floor(Math.random() * 100)",
        "difficulty": "Medium",
        "explanation": "`Math.random() * 100` generates a number from 0 to 99.999..., and `Math.floor` rounds it down to 0–99."
    },
    {
        "question": "How do you convert the string 'true' to a boolean?",
        "options": [
            "JSON.parse('true')",
            "Boolean('true')",
            "parseBool('true')",
            "String.toBoolean('true')"
        ],
        "answer": "JSON.parse('true')",
        "difficulty": "Medium",
        "explanation": "`JSON.parse('true')` converts the string 'true' to the boolean value `true`."
    },
    {
        "question": "What does `Number('123.45')` return?",
        "options": [
            "123.45",
            "123",
            "123.45.0",
            "124"
        ],
        "answer": "123.45",
        "difficulty": "Easy",
        "explanation": "`Number('123.45')` converts the string '123.45' to the number 123.45."
    },
    {
        "question": "How do you get the current hour from a Date object?",
        "options": [
            "date.getHours()",
            "date.getHour()",
            "date.hour()",
            "date.getTime().hour"
        ],
        "answer": "date.getHours()",
        "difficulty": "Medium",
        "explanation": "`getHours()` returns the hour (0–23) of a Date object."
    },
    {
        "question": "How do you set the hours of a Date object to 15 (3 PM)?",
        "options": [
            "date.setHours(15)",
            "date.setHour(15)",
            "date.updateHours(15)",
            "date.changeHours(15)"
        ],
        "answer": "date.setHours(15)",
        "difficulty": "Medium",
        "explanation": "`setHours(15)` sets the hour of a Date object to 15 (3 PM)."
    },
    {
        "question": "What is an anonymous function in JavaScript?",
        "options": [
            "A function without a name",
            "A function that returns nothing",
            "A function inside another function",
            "A function with default parameters"
        ],
        "answer": "A function without a name",
        "difficulty": "Medium",
        "explanation": "An anonymous function is a function without a name, often used in function expressions or as callbacks."
    },
    {
        "question": "How do you call a function with a default parameter value?",
        "options": [
            "function myFunc(x = 0) { return x; } myFunc();",
            "function myFunc(x) { return x; } myFunc(0);",
            "function myFunc(x) { return x; } myFunc();",
            "function myFunc(x = 0) { return x; } myFunc(0);"
        ],
        "answer": "function myFunc(x = 0) { return x; } myFunc();",
        "difficulty": "Medium",
        "explanation": "A default parameter assigns a value if none is provided, so `myFunc()` returns 0."
    },
    {
        "question": "What does a function return if no `return` statement is used?",
        "options": [
            "undefined",
            "null",
            "0",
            "false"
        ],
        "answer": "undefined",
        "difficulty": "Medium",
        "explanation": "A function without a `return` statement implicitly returns `undefined`."
    },
    {
        "question": "What is the scope of a variable declared with `let` inside a function?",
        "options": [
            "Function scope",
            "Global scope",
            "Block scope",
            "Module scope"
        ],
        "answer": "Block scope",
        "difficulty": "Medium",
        "explanation": "Variables declared with `let` inside a function have block scope, limited to the block they are defined in."
    },
    {
        "question": "How do you ensure a variable is not global in a function?",
        "options": [
            "Use `let` or `const`",
            "Use `var`",
            "Omit any keyword",
            "Use `global`"
        ],
        "answer": "Use `let` or `const`",
        "difficulty": "Medium",
        "explanation": "Using `let` or `const` ensures a variable is scoped to the block or function, not global."
    },
    {
        "question": "What is the purpose of the `default` case in a switch statement?",
        "options": [
            "To handle unmatched values",
            "To set a default value",
            "To start the switch",
            "To end the switch"
        ],
        "answer": "To handle unmatched values",
        "difficulty": "Easy",
        "explanation": "The `default` case executes when no other case matches the switch expression."
    },
    {
        "question": "How do you write a switch statement with multiple cases for the same action?",
        "options": [
            "case 'a': case 'b': code;",
            "case 'a', 'b': code;",
            "case 'a' || 'b': code;",
            "case 'a' && 'b': code;"
        ],
        "answer": "case 'a': case 'b': code;",
        "difficulty": "Medium",
        "explanation": "Multiple `case` labels without `break` statements share the same code block (fall-through)."
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
        "time_left": 3600,  # 60 minutes
        "theme": "dark",
        "streak": 0,
        "started": False,
        "max_streak": 0
    })

# Theme toggle
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# Timer logic
def update_timer():
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.session_state.time_left = max(3600 - elapsed, 0)
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
        "time_left": 3600,
        "streak": 0,
        "max_streak": 0,
        "started": False
    })
    st.rerun()
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
st.markdown('<h1 class="title">🚀 DOM Mastery Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript DOM Skills!</p>', unsafe_allow_html=True)

# Theme toggle button
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen
if not st.session_state.started:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: var(--text); font-size: 18px;">Test your DOM skills with 30 comprehensive questions!</p>
        <p style="color: var(--text-light);">60 minutes, 2 points per correct answer. Ready?</p>
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
        <div class="progress-container">
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress_percentage}%"></div>
                <div class="progress-text">{progress_percentage}%</div>
            </div>
            <div style="color: var(--text); font-size: 13px; text-align: center;">
                Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
            </div>
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
                    if "```javascript" in q["question"]:
                        language = "javascript"
                        question_parts = q["question"].split("```javascript\n")
                    else:
                        language = "html"
                        question_parts = q["question"].split("```html\n")
                    
                    question_text = question_parts[0].strip()
                    code_snippet = question_parts[1].split("```")[0].strip()
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{question_text}**")
                    st.code(code_snippet, language=language)
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
                            st.session_state.score += 2  # 2 points for correct answer
                            st.session_state.streak += 1
                            if st.session_state.streak > st.session_state.max_streak:
                                st.session_state.max_streak = st.session_state.streak
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
                        st.markdown(f'<div style="color: var(--text); font-size: 14px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

        else:
            # Results
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 3600)
            total_possible_score = len(quiz) * 2  # 2 points per question
            accuracy = (st.session_state.score / total_possible_score) * 100 if total_possible_score > 0 else 0
            st.markdown('<div class="results-container">', unsafe_allow_html=True)
            st.markdown(f'<div class="score-display">{st.session_state.score}/{total_possible_score}</div>', unsafe_allow_html=True)
            st.markdown(f"""
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-value">⏱️ {int(time_taken) // 60}m {int(time_taken) % 60}s</div>
                    <div class="stat-label">Time Taken</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">🎯 {accuracy:.1f}%</div>
                    <div class="stat-label">Accuracy</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">✅ {sum(1 for ans in st.session_state.answers if ans and ans["is_correct"])}</div>
                    <div class="stat-label">Correct</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">❌ {sum(1 for ans in st.session_state.answers if ans and not ans["is_correct"])}</div>
                    <div class="stat-label">Incorrect</div>
                </div>
            </div>
            <div style="text-align: center; margin: 1.5rem 0;">
                <div style="font-size: 1.2rem; color: var(--text);">🔥 Max Streak: {st.session_state.max_streak}</div>
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
            st.markdown('<h3 style="color: var(--text); margin-bottom: 1rem;">📝 Review Your Answers</h3>', unsafe_allow_html=True)
            for i, ans in enumerate(st.session_state.answers):
                if ans:
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})"
                    st.markdown(f"""
                    <div style="background: var(--card-bg); padding: 1rem; border-radius: 12px; margin-bottom: 1rem; box-shadow: var(--shadow);">
                        <div style="font-weight: 600; color: var(--text); margin-bottom: 0.5rem;">Question {i+1}: {ans["question"]}</div>
                        <div style="margin-bottom: 0.25rem;">Your Answer: {ans["user_answer"]}</div>
                        <div style="margin-bottom: 0.5rem; color: {'var(--correct)' if ans["is_correct"] else 'var(--wrong)'}">{status}</div>
                        <div style="font-size: 0.9rem; color: var(--text-light); padding: 0.75rem; background: rgba(168, 85, 247, 0.05); border-radius: 8px;">
                            Explanation: {quiz[i]["explanation"]}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

            # Play Again button
            if st.button("🔄 Play Again", key="play_again"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
