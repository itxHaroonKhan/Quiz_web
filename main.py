


import streamlit as st
import random
from datetime import datetime
import uuid


# Quiz data with 67 questions covering specified JavaScript topics
quiz =[
  {
    "question": "What is the scope of a variable declared with 'let' inside a block?",
    "options": [
      "Function scope",
      "Global scope",
      "Block scope",
      "Module scope"
    ],
    "answer": "Block scope",
    "difficulty": "Medium",
    "explanation": "Variables declared with 'let' are limited to the block (e.g., {}) in which they are defined."
  },
  {
    "question": "What happens to a 'var' variable declared inside a function?",
    "options": [
      "It is block-scoped",
      "It is function-scoped",
      "It becomes global",
      "It is module-scoped"
    ],
    "answer": "It is function-scoped",
    "difficulty": "Medium",
    "explanation": "'var' variables are scoped to the function they are declared in, not the block."
  },
  {
    "question": "What is the output of: { let x = 10; } console.log(typeof x);?",
    "options": [
      "number",
      "undefined",
      "ReferenceError",
      "null"
    ],
    "answer": "undefined",
    "difficulty": "Medium",
    "explanation": "'let x' is block-scoped, so x is undefined outside the block."
  },
  {
    "question": "What is a closure in JavaScript?",
    "options": [
      "A function with its own scope",
      "A function that retains access to its outer scope’s variables",
      "A function that runs immediately",
      "A function with no parameters"
    ],
    "answer": "A function that retains access to its outer scope’s variables",
    "difficulty": "Medium",
    "explanation": "A closure is a function that remembers its outer variables even after the outer function has finished executing."
  },
  {
    "question": "What does this closure do: function outer() { let x = 5; return function() { return x++; } } let fn = outer(); console.log(fn());?",
    "options": [
      "5",
      "6",
      "undefined",
      "Error"
    ],
    "answer": "5",
    "difficulty": "Medium",
    "explanation": "The inner function retains access to x and returns its value (5) before incrementing it."
  },
  {
    "question": "What is the output of: let name = 'Alice'; let str = `Hello, ${name}!`; console.log(str);?",
    "options": [
      "Hello, Alice!",
      "Hello, ${name}!",
      "Hello, name!",
      "Error"
    ],
    "answer": "Hello, Alice!",
    "difficulty": "Medium",
    "explanation": "Template literals use backticks (`) and ${} to embed expressions, evaluating to 'Hello, Alice!'."
  },
  {
    "question": "How do you include a multi-line string using template literals?",
    "options": [
      "`Line1\\nLine2`",
      "`Line1\nLine2`",
      "'Line1\nLine2'",
      "`Line1 Line2`"
    ],
    "answer": "`Line1\nLine2`",
    "difficulty": "Medium",
    "explanation": "Template literals allow multi-line strings without escaping, using \\n for newlines."
  },
  {
    "question": "What does let {a, b} = {a: 1, b: 2}; assign to a and b?",
    "options": [
      "a = 1, b = 2",
      "a = undefined, b = undefined",
      "a = {a: 1}, b = {b: 2}",
      "Error"
    ],
    "answer": "a = 1, b = 2",
    "difficulty": "Medium",
    "explanation": "Destructuring assigns properties a and b to variables of the same name."
  },
  {
    "question": "What is the result of: let [x, y] = [10, 20, 30];?",
    "options": [
      "x = 10, y = 20",
      "x = 10, y = 30",
      "x = [10, 20], y = 30",
      "Error"
    ],
    "answer": "x = 10, y = 20",
    "difficulty": "Medium",
    "explanation": "Array destructuring assigns the first two elements to x and y, ignoring the rest."
  },
  {
    "question": "What is the output of: function greet(name = 'Guest') { return `Hi, ${name}`; } console.log(greet());?",
    "options": [
      "Hi, Guest",
      "Hi, undefined",
      "Hi, ",
      "Error"
    ],
    "answer": "Hi, Guest",
    "difficulty": "Medium",
    "explanation": "Default parameters assign 'Guest' to name when no argument is provided."
  },
  {
    "question": "How do you use the rest parameter in a function?",
    "options": [
      "function sum(...numbers) { return numbers.reduce((a, b) => a + b); }",
      "function sum(numbers...) { return numbers.reduce((a, b) => a + b); }",
      "function sum(*numbers) { return numbers.reduce((a, b) => a + b); }",
      "function sum(numbers) { return numbers.reduce((a, b) => a + b); }"
    ],
    "answer": "function sum(...numbers) { return numbers.reduce((a, b) => a + b); }",
    "difficulty": "Medium",
    "explanation": "The rest parameter (...numbers) collects all arguments into an array."
  },
  {
    "question": "What does the spread operator do in: let arr = [...[1, 2], 3];?",
    "options": [
      "Creates [1, 2, 3]",
      "Creates [1, 2, [3]]",
      "Creates [[1, 2], 3]",
      "Throws an error"
    ],
    "answer": "Creates [1, 2, 3]",
    "difficulty": "Medium",
    "explanation": "The spread operator (...) flattens the array [1, 2] and adds 3, forming [1, 2, 3]."
  },
  {
    "question": "What is the output of: const fn = (x) => x * 2; console.log(fn(5));?",
    "options": [
      "10",
      "5",
      "undefined",
      "Error"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "Arrow functions provide concise syntax; this one multiplies x by 2, returning 10."
  },
  {
    "question": "What is the difference between arrow functions and regular functions regarding 'this'?",
    "options": [
      "Arrow functions inherit 'this' from their lexical scope",
      "Arrow functions have their own 'this'",
      "Arrow functions cannot use 'this'",
      "No difference"
    ],
    "answer": "Arrow functions inherit 'this' from their lexical scope",
    "difficulty": "Medium",
    "explanation": "Arrow functions do not bind their own 'this' and use the enclosing scope’s 'this'."
  },
  {
    "question": "What does this enhanced object literal do: let x = 1; let obj = {x, method() { return this.x; }}; console.log(obj.method());?",
    "options": [
      "1",
      "undefined",
      "method",
      "Error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "Enhanced object literals allow shorthand property (x) and method syntax, returning x = 1."
  },
  {
    "question": "What is the purpose of a for..of loop?",
    "options": [
      "To iterate over iterable objects like arrays",
      "To iterate over object properties",
      "To create a function",
      "To loop over numbers"
    ],
    "answer": "To iterate over iterable objects like arrays",
    "difficulty": "Medium",
    "explanation": "The for..of loop iterates over values of iterable objects like arrays or strings."
  },
  {
    "question": "What does this for..of loop do: let arr = [1, 2, 3]; for (let x of arr) { console.log(x); }?",
    "options": [
      "Logs 1, 2, 3",
      "Logs 0, 1, 2",
      "Logs [1, 2, 3]",
      "Logs nothing"
    ],
    "answer": "Logs 1, 2, 3",
    "difficulty": "Medium",
    "explanation": "The for..of loop iterates over each element in the array, logging 1, 2, 3."
  },
  {
    "question": "What is a generator function in JavaScript?",
    "options": [
      "A function that can pause and resume execution",
      "A function that runs once",
      "A function with no return value",
      "A function that creates arrays"
    ],
    "answer": "A function that can pause and resume execution",
    "difficulty": "Medium",
    "explanation": "Generator functions use 'function*' and 'yield' to pause and resume, returning an iterator."
  },
  {
    "question": "What does this generator do: function* gen() { yield 1; yield 2; } let g = gen(); console.log(g.next().value);?",
    "options": [
      "1",
      "2",
      "undefined",
      "Error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "The generator yields 1 first; calling g.next().value returns 1."
  },
  {
    "question": "How do you export a function in a JavaScript module?",
    "options": [
      "export function myFunc() {}",
      "module.export = myFunc()",
      "export.myFunc = function() {}",
      "function export myFunc() {}"
    ],
    "answer": "export function myFunc() {}",
    "difficulty": "Medium",
    "explanation": "The 'export' keyword makes a function available for import in other modules."
  },
  {
    "question": "How do you import a named function from a module?",
    "options": [
      "import { myFunc } from './module.js';",
      "import myFunc from './module.js';",
      "require('./module.js').myFunc;",
      "import * as myFunc from './module.js';"
    ],
    "answer": "import { myFunc } from './module.js';",
    "difficulty": "Medium",
    "explanation": "Named imports use curly braces to specify the function name from the module."
  },
  {
    "question": "What does new Map([[1, 'one'], [2, 'two']]).get(1) return?",
    "options": [
      "'one'",
      "1",
      "'two'",
      "undefined"
    ],
    "answer": "'one'",
    "difficulty": "Medium",
    "explanation": "The Map object stores key-value pairs; get(1) retrieves the value 'one'."
  },
  {
    "question": "How do you add a key-value pair to a Map?",
    "options": [
      "map.set(key, value)",
      "map.add(key, value)",
      "map.put(key, value)",
      "map[key] = value"
    ],
    "answer": "map.set(key, value)",
    "difficulty": "Medium",
    "explanation": "The 'set()' method adds or updates a key-value pair in a Map."
  },
  {
    "question": "What does [1, 2, 3].map(x => x * 2) return?",
    "options": [
      "[2, 4, 6]",
      "[1, 2, 3]",
      "[1, 4, 9]",
      "Error"
    ],
    "answer": "[2, 4, 6]",
    "difficulty": "Medium",
    "explanation": "The 'map()' method applies the function to each element, doubling the values."
  },
  {
    "question": "What does [1, 2, 3, 4].filter(x => x % 2 === 0) return?",
    "options": [
      "[2, 4]",
      "[1, 3]",
      "[1, 2, 3, 4]",
      "[]"
    ],
    "answer": "[2, 4]",
    "difficulty": "Medium",
    "explanation": "'filter()' returns a new array with elements that pass the test (even numbers)."
  },
  {
    "question": "What is a higher-order function?",
    "options": [
      "A function that takes or returns a function",
      "A function with no parameters",
      "A function that runs once",
      "A function with multiple returns"
    ],
    "answer": "A function that takes or returns a function",
    "difficulty": "Medium",
    "explanation": "Higher-order functions either accept functions as arguments or return functions."
  },
  {
    "question": "What does this higher-order function do: function apply(fn, x) { return fn(x); } console.log(apply(x => x * 2, 5));?",
    "options": [
      "10",
      "5",
      "undefined",
      "Error"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "The function applies the provided function (x => x * 2) to x = 5, returning 10."
  },
  {
    "question": "What is a callback function?",
    "options": [
      "A function passed as an argument to another function",
      "A function that returns a value",
      "A function that runs immediately",
      "A function with no scope"
    ],
    "answer": "A function passed as an argument to another function",
    "difficulty": "Medium",
    "explanation": "Callbacks are functions passed to another function to be executed later."
  },
  {
    "question": "What does setTimeout(() => console.log('Hi'), 1000) do?",
    "options": [
      "Logs 'Hi' after 1 second",
      "Logs 'Hi' immediately",
      "Logs 'Hi' every second",
      "Throws an error"
    ],
    "answer": "Logs 'Hi' after 1 second",
    "difficulty": "Medium",
    "explanation": "'setTimeout' executes the callback after a 1000ms delay."
  },
  {
    "question": "What is the output of: let p = new Promise((resolve) => resolve('Done')); p.then(console.log);?",
    "options": [
      "Done",
      "undefined",
      "Promise",
      "Error"
    ],
    "answer": "Done",
    "difficulty": "Medium",
    "explanation": "The Promise resolves with 'Done', and the then() method logs it."
  },
  {
    "question": "What happens if a Promise rejects without a catch?",
    "options": [
      "An uncaught error is thrown",
      "The Promise resolves",
      "Nothing happens",
      "The Promise retries"
    ],
    "answer": "An uncaught error is thrown",
    "difficulty": "Medium",
    "explanation": "Unhandled Promise rejections trigger an error in the console."
  },
  {
    "question": "What does 2 ** 3 evaluate to?",
    "options": [
      "8",
      "6",
      "9",
      "Error"
    ],
    "answer": "8",
    "difficulty": "Medium",
    "explanation": "The exponentiation operator (**) raises 2 to the power of 3, resulting in 8."
  },
  {
    "question": "What is the output of: class MyClass { constructor(x) { this.x = x; } } let obj = new MyClass(5); console.log(obj.x);?",
    "options": [
      "5",
      "undefined",
      "MyClass",
      "Error"
    ],
    "answer": "5",
    "difficulty": "Medium",
    "explanation": "The class constructor sets the x property, which is accessed as obj.x."
  },
  {
    "question": "What does let x = true ? 'Yes' : 'No'; assign to x?",
    "options": [
      "Yes",
      "No",
      "true",
      "Error"
    ],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "The ternary operator evaluates true, assigning 'Yes' to x."
  },
  {
    "question": "What does obj?.prop return if obj is undefined?",
    "options": [
      "undefined",
      "null",
      "Error",
      "prop"
    ],
    "answer": "undefined",
    "difficulty": "Medium",
    "explanation": "Optional chaining (?.) returns undefined if obj is undefined, avoiding an error."
  },
  {
    "question": "What is the output of: let x = 10; function test() { let x = 20; console.log(x); } test();?",
    "options": [
      "20",
      "10",
      "undefined",
      "Error"
    ],
    "answer": "20",
    "difficulty": "Medium",
    "explanation": "The 'let x' inside the function creates a new block-scoped variable, shadowing the outer x."
  },
  {
    "question": "What does this closure return: function makeCounter() { let count = 0; return () => count++; } let counter = makeCounter(); console.log(counter());?",
    "options": [
      "0",
      "1",
      "undefined",
      "Error"
    ],
    "answer": "0",
    "difficulty": "Medium",
    "explanation": "The closure returns the current count (0) and then increments it."
  },
  {
    "question": "What is the output of: let x = 2; console.log(`Square: ${x * x}`);?",
    "options": [
      "Square: 4",
      "Square: 2",
      "Square: ${x * x}",
      "Error"
    ],
    "answer": "Square: 4",
    "difficulty": "Medium",
    "explanation": "Template literals evaluate ${x * x} as 4, resulting in 'Square: 4'."
  },
  {
    "question": "What does let [a, ...rest] = [1, 2, 3, 4]; assign to rest?",
    "options": [
      "[2, 3, 4]",
      "[1, 2, 3]",
      "[3, 4]",
      "Error"
    ],
    "answer": "[2, 3, 4]",
    "difficulty": "Medium",
    "explanation": "The rest parameter in destructuring collects remaining elements into an array."
  },
  {
    "question": "What does function add(a, b = 10) { return a + b; } return when called as add(5);?",
    "options": [
      "15",
      "5",
      "10",
      "Error"
    ],
    "answer": "15",
    "difficulty": "Medium",
    "explanation": "The default parameter b = 10 is used, so add(5) returns 5 + 10 = 15."
  },
  {
    "question": "What does function collect(...args) { return args.length; } return when called as collect(1, 2, 3);?",
    "options": [
      "3",
      "1",
      "[1, 2, 3]",
      "Error"
    ],
    "answer": "3",
    "difficulty": "Medium",
    "explanation": "The rest parameter collects all arguments into an array, and length returns 3."
  },
  {
    "question": "What does let obj = { ...{a: 1}, b: 2 }; create?",
    "options": [
      "{a: 1, b: 2}",
      "{a: 1}",
      "{b: 2}",
      "Error"
    ],
    "answer": "{a: 1, b: 2}",
    "difficulty": "Medium",
    "explanation": "The spread operator copies properties from one object and adds b: 2."
  },
  {
    "question": "What does const fn = () => 'Hello'; console.log(fn()); return?",
    "options": [
      "Hello",
      "undefined",
      "fn",
      "Error"
    ],
    "answer": "Hello",
    "difficulty": "Medium",
    "explanation": "The arrow function returns 'Hello' when called."
  },
  {
    "question": "What is the output of: let obj = { [key]: value } where key = 'x' and value = 10?",
    "options": [
      "{x: 10}",
      "{key: value}",
      "undefined",
      "Error"
    ],
    "answer": "{x: 10}",
    "difficulty": "Medium",
    "explanation": "Computed property names in enhanced object literals evaluate [key] to x."
  },
  {
    "question": "What does for (let c of 'abc') { console.log(c); } output?",
    "options": [
      "a, b, c",
      "abc",
      "0, 1, 2",
      "Error"
    ],
    "answer": "a, b, c",
    "difficulty": "Medium",
    "explanation": "The for..of loop iterates over each character in the string 'abc'."
  },
  {
    "question": "What does function* range() { for (let i = 0; i < 3; i++) yield i; } let r = range(); console.log(r.next().value); return?",
    "options": [
      "0",
      "1",
      "undefined",
      "Error"
    ],
    "answer": "0",
    "difficulty": "Medium",
    "explanation": "The generator yields 0 first; next().value retrieves it."
  },
  {
    "question": "What does export default function myFunc() {} allow?",
    "options": [
      "Importing without curly braces",
      "Importing with curly braces",
      "Multiple default exports",
      "No imports"
    ],
    "answer": "Importing without curly braces",
    "difficulty": "Medium",
    "explanation": "Default exports allow importing the function without specifying a name in curly braces."
  },
  {
    "question": "What does new Map().set('key', 'value').get('key') return?",
    "options": [
      "value",
      "key",
      "undefined",
      "Error"
    ],
    "answer": "value",
    "difficulty": "Medium",
    "explanation": "'set()' adds the key-value pair, and 'get()' retrieves 'value' for 'key'."
  },
  {
    "question": "What does [1, 2, 3].reduce((a, b) => a + b, 0) return?",
    "options": [
      "6",
      "3",
      "[1, 2, 3]",
      "Error"
    ],
    "answer": "6",
    "difficulty": "Medium",
    "explanation": "'reduce()' sums the array elements starting with initial value 0, resulting in 6."
  },
  {
    "question": "What does function higher(fn) { return fn(10); } console.log(higher(x => x + 5)); return?",
    "options": [
      "15",
      "10",
      "5",
      "Error"
    ],
    "answer": "15",
    "difficulty": "Medium",
    "explanation": "The higher-order function calls the provided function with 10, returning 10 + 5 = 15."
  },
  {
    "question": "What does [1, 2, 3].forEach(x => console.log(x)) do?",
    "options": [
      "Logs 1, 2, 3",
      "Returns [1, 2, 3]",
      "Logs nothing",
      "Throws an error"
    ],
    "answer": "Logs 1, 2, 3",
    "difficulty": "Medium",
    "explanation": "'forEach()' executes the callback for each element, logging 1, 2, 3."
  },
  {
    "question": "What does Promise.resolve(42).then(x => x * 2) return?",
    "options": [
      "A Promise resolving to 84",
      "84",
      "42",
      "Error"
    ],
    "answer": "A Promise resolving to 84",
    "difficulty": "Medium",
    "explanation": "'then()' chains a transformation, returning a new Promise that resolves to 42 * 2."
  },
  {
    "question": "What is the output of: console.log(5 ** 2);?",
    "options": [
      "25",
      "10",
      "5",
      "Error"
    ],
    "answer": "25",
    "difficulty": "Medium",
    "explanation": "The exponentiation operator (**) computes 5 raised to the power of 2, yielding 25."
  },
  {
    "question": "What does class Point { constructor(x, y) { this.x = x; this.y = y; } } let p = new Point(3, 4); console.log(p.x); return?",
    "options": [
      "3",
      "4",
      "undefined",
      "Error"
    ],
    "answer": "3",
    "difficulty": "Medium",
    "explanation": "The constructor sets x to 3, which is accessed as p.x."
  },
  {
    "question": "What does let x = 10 > 5 ? 'Big' : 'Small'; assign to x?",
    "options": [
      "Big",
      "Small",
      "true",
      "Error"
    ],
    "answer": "Big",
    "difficulty": "Medium",
    "explanation": "The ternary operator evaluates 10 > 5 as true, assigning 'Big' to x."
  },
  {
    "question": "What does obj?.method?.() return if obj is null?",
    "options": [
      "undefined",
      "null",
      "Error",
      "method"
    ],
    "answer": "undefined",
    "difficulty": "Medium",
    "explanation": "Optional chaining (?.) stops evaluation at null, returning undefined."
  },
  {
    "question": "What is the output of: function outer() { let x = 1; function inner() { x++; return x; } return inner; } let fn = outer(); console.log(fn());?",
    "options": [
      "2",
      "1",
      "undefined",
      "Error"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "The closure increments x from 1 to 2 and returns it."
  },
  {
    "question": "What does `Sum: ${2 + 3}` evaluate to?",
    "options": [
      "Sum: 5",
      "Sum: 2 + 3",
      "5",
      "Error"
    ],
    "answer": "Sum: 5",
    "difficulty": "Medium",
    "explanation": "Template literals evaluate the expression ${2 + 3} to 5."
  },
  {
    "question": "What does let {x: a, y: b} = {x: 10, y: 20}; assign to a and b?",
    "options": [
      "a = 10, b = 20",
      "a = undefined, b = undefined",
      "a = x, b = y",
      "Error"
    ],
    "answer": "a = 10, b = 20",
    "difficulty": "Medium",
    "explanation": "Destructuring renames properties x and y to variables a and b."
  },
  {
    "question": "What does function multiply(a, b = 2) { return a * b; } return when called as multiply(3);?",
    "options": [
      "6",
      "3",
      "2",
      "Error"
    ],
    "answer": "6",
    "difficulty": "Medium",
    "explanation": "The default parameter b = 2 is used, so multiply(3) returns 3 * 2 = 6."
  },
  {
    "question": "What does function args(...values) { return values[0]; } return when called as args(1, 2, 3);?",
    "options": [
      "1",
      "3",
      "[1, 2, 3]",
      "Error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "The rest parameter collects arguments into an array; values[0] returns 1."
  },
  {
    "question": "What does let arr = [1, ...[2, 3], 4]; create?",
    "options": [
      "[1, 2, 3, 4]",
      "[1, [2, 3], 4]",
      "[2, 3, 4]",
      "Error"
    ],
    "answer": "[1, 2, 3, 4]",
    "difficulty": "Medium",
    "explanation": "The spread operator flattens [2, 3] into the new array."
  },
  {
    "question": "What does const fn = x => x + 1; console.log(fn(9)); return?",
    "options": [
      "10",
      "9",
      "undefined",
      "Error"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "The arrow function adds 1 to x, returning 10 for x = 9."
  },
  {
    "question": "What does let obj = { prop: 'value', getProp() { return this.prop; } }; console.log(obj.getProp()); return?",
    "options": [
      "value",
      "prop",
      "undefined",
      "Error"
    ],
    "answer": "value",
    "difficulty": "Medium",
    "explanation": "The enhanced object literal method getProp returns the prop value."
  },
  {
    "question": "What does for (let x of new Set([1, 1, 2])) { console.log(x); } output?",
    "options": [
      "1, 2",
      "1, 1, 2",
      "1",
      "Error"
    ],
    "answer": "1, 2",
    "difficulty": "Medium",
    "explanation": "The for..of loop iterates over unique values in the Set, logging 1, 2."
  },
  {
    "question": "What does function* gen() { yield* [1, 2]; } let g = gen(); console.log(g.next().value); return?",
    "options": [
      "1",
      "2",
      "undefined",
      "Error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "'yield*' delegates to the iterable, yielding 1 first."
  },
  {
    "question": "What does import * as mod from './module.js'; do?",
    "options": [
      "Imports all exports as an object",
      "Imports only the default export",
      "Imports nothing",
      "Throws an error"
    ],
    "answer": "Imports all exports as an object",
    "difficulty": "Medium",
    "explanation": "The * as mod syntax imports all exports into an object named mod."
  },
  {
    "question": "What does new Map().has('key') return if no key is set?",
    "options": [
      "false",
      "true",
      "undefined",
      "Error"
    ],
    "answer": "false",
    "difficulty": "Medium",
    "explanation": "'has()' returns false if the key does not exist in the Map."
  },
  {
    "question": "What does [1, 2, 3].every(x => x > 0) return?",
    "options": [
      "true",
      "false",
      "[1, 2, 3]",
      "Error"
    ],
    "answer": "true",
    "difficulty": "Medium",
    "explanation": "'every()' returns true if all elements pass the test (x > 0)."
  },
  {
    "question": "What does function compose(f, g) { return x => f(g(x)); } do?",
    "options": [
      "Combines two functions",
      "Adds two functions",
      "Returns a single function",
      "Throws an error"
    ],
    "answer": "Combines two functions",
    "difficulty": "Medium",
    "explanation": "The higher-order function composes f and g, applying g then f to x."
  },
  {
    "question": "What does setInterval(() => console.log('Tick'), 1000) do?",
    "options": [
      "Logs 'Tick' every second",
      "Logs 'Tick' once",
      "Logs 'Tick' after 1 second",
      "Throws an error"
    ],
    "answer": "Logs 'Tick' every second",
    "difficulty": "Medium",
    "explanation": "'setInterval' repeatedly calls the callback every 1000ms."
  },
  {
    "question": "What does Promise.reject('Error').catch(err => console.log(err)); do?",
    "options": [
      "Logs 'Error'",
      "Logs undefined",
      "Throws an error",
      "Logs nothing"
    ],
    "answer": "Logs 'Error'",
    "difficulty": "Medium",
    "explanation": "The catch() method handles the rejected Promise, logging 'Error'."
  },
  {
    "question": "What does 4 ** 0.5 evaluate to?",
    "options": [
      "2",
      "4",
      "1",
      "Error"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "The exponentiation operator computes the square root (4 ** 0.5 = 2)."
  },
  {
    "question": "What does class Animal { speak() { return 'Sound'; } } let a = new Animal(); console.log(a.speak()); return?",
    "options": [
      "Sound",
      "undefined",
      "Animal",
      "Error"
    ],
    "answer": "Sound",
    "difficulty": "Medium",
    "explanation": "The speak method returns 'Sound' for the Animal instance."
  },
  {
    "question": "What does let x = null ?? 'default'; assign to x?",
    "options": [
      "default",
      "null",
      "undefined",
      "Error"
    ],
    "answer": "default",
    "difficulty": "Medium",
    "explanation": "The nullish coalescing operator (??) assigns 'default' if x is null or undefined."
  },
  {
    "question": "What does arr?.[0] return if arr is undefined?",
    "options": [
      "undefined",
      "null",
      "Error",
      "0"
    ],
    "answer": "undefined",
    "difficulty": "Medium",
    "explanation": "Optional chaining (?.) returns undefined if arr is undefined."
  },
  {
    "question": "What is the output of: function outer() { let x = 10; return function() { return x; } } let fn = outer(); console.log(fn());?",
    "options": [
      "10",
      "undefined",
      "Error",
      "null"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "The closure retains access to x, returning its value (10)."
  },
  {
    "question": "What does `Result: ${10 > 5 ? 'Yes' : 'No'}` evaluate to?",
    "options": [
      "Result: Yes",
      "Result: No",
      "Result: true",
      "Error"
    ],
    "answer": "Result: Yes",
    "difficulty": "Medium",
    "explanation": "The ternary operator in the template literal evaluates to 'Yes' since 10 > 5."
  },
  {
    "question": "What does let [first, , third] = [1, 2, 3]; assign to first and third?",
    "options": [
      "first = 1, third = 3",
      "first = 1, third = 2",
      "first = undefined, third = undefined",
      "Error"
    ],
    "answer": "first = 1, third = 3",
    "difficulty": "Medium",
    "explanation": "Destructuring skips the second element, assigning 1 to first and 3 to third."
  },
  {
    "question": "What does function greet({name = 'User'} = {}) { return name; } return when called as greet();?",
    "options": [
      "User",
      "undefined",
      "null",
      "Error"
    ],
    "answer": "User",
    "difficulty": "Medium",
    "explanation": "The default parameter provides an empty object with name = 'User' if no argument is passed."
  },
  {
    "question": "What does function sum(...nums) { return nums.reduce((a, b) => a + b, 0); } return for sum(1, 2, 3);?",
    "options": [
      "6",
      "1",
      "[1, 2, 3]",
      "Error"
    ],
    "answer": "6",
    "difficulty": "Medium",
    "explanation": "The rest parameter collects arguments into an array, and reduce sums them to 6."
  },
  {
    "question": "What does let obj = {...{x: 1, y: 2}, z: 3}; create?",
    "options": [
      "{x: 1, y: 2, z: 3}",
      "{x: 1, y: 2}",
      "{z: 3}",
      "Error"
    ],
    "answer": "{x: 1, y: 2, z: 3}",
    "difficulty": "Medium",
    "explanation": "The spread operator copies x and y, and z: 3 is added to the new object."
  },
  {
    "question": "What does const double = x => x * 2; console.log(double(3)); return?",
    "options": [
      "6",
      "3",
      "undefined",
      "Error"
    ],
    "answer": "6",
    "difficulty": "Medium",
    "explanation": "The arrow function multiplies x by 2, returning 6 for x = 3."
  },
  {
    "question": "What does let obj = { ['prop' + 1]: 'value' }; console.log(obj.prop1); return?",
    "options": [
      "value",
      "undefined",
      "prop1",
      "Error"
    ],
    "answer": "value",
    "difficulty": "Medium",
    "explanation": "Computed property names evaluate 'prop' + 1 to prop1, assigning 'value'."
  },
  {
    "question": "What does for (let x of new Map([[1, 'a'], [2, 'b']])) { console.log(x); } output?",
    "options": [
      "[1, 'a'], [2, 'b']",
      "1, 2",
      "'a', 'b'",
      "Error"
    ],
    "answer": "[1, 'a'], [2, 'b']",
    "difficulty": "Medium",
    "explanation": "The for..of loop iterates over Map entries, logging key-value pairs as arrays."
  },
  {
    "question": "What does function* gen() { yield 1; return 2; } let g = gen(); console.log(g.next().value); return?",
    "options": [
      "1",
      "2",
      "undefined",
      "Error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "The generator yields 1 first; next().value retrieves it."
  },
  {
    "question": "What does export { x, y } from './module.js'; do?",
    "options": [
      "Re-exports x and y from another module",
      "Imports x and y",
      "Defines x and y",
      "Throws an error"
    ],
    "answer": "Re-exports x and y from another module",
    "difficulty": "Medium",
    "explanation": "The syntax re-exports named exports from another module."
  },
  {
    "question": "What does new Map([['a', 1]]).size return?",
    "options": [
      "1",
      "0",
      "undefined",
      "Error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "The 'size' property returns the number of key-value pairs in the Map."
  },
  {
    "question": "What does [1, 2, 3].some(x => x > 2) return?",
    "options": [
      "true",
      "false",
      "[1, 2, 3]",
      "Error"
    ],
    "answer": "true",
    "difficulty": "Medium",
    "explanation": "'some()' returns true if at least one element (3) passes the test."
  },
  {
    "question": "What does function wrap(fn) { return (...args) => fn(args); } console.log(wrap(x => x.length)(1, 2, 3)); return?",
    "options": [
      "3",
      "1",
      "[1, 2, 3]",
      "Error"
    ],
    "answer": "3",
    "difficulty": "Medium",
    "explanation": "The higher-order function wraps fn, passing args as an array, returning its length."
  },
  {
    "question": "What does [1, 2].forEach((x, i) => console.log(i, x)); output?",
    "options": [
      "0 1, 1 2",
      "1 2, 2 1",
      "1, 2",
      "Error"
    ],
    "answer": "0 1, 1 2",
    "difficulty": "Medium",
    "explanation": "'forEach()' passes the index and element to the callback, logging pairs."
  },
  {
    "question": "What does Promise.all([Promise.resolve(1), Promise.resolve(2)]).then(console.log); do?",
    "options": [
      "Logs [1, 2]",
      "Logs 1, 2",
      "Logs nothing",
      "Throws an error"
    ],
    "answer": "Logs [1, 2]",
    "difficulty": "Medium",
    "explanation": "Promise.all resolves with an array of resolved values, logging [1, 2]."
  },
  {
    "question": "What does 3 ** 3 evaluate to?",
    "options": [
      "27",
      "9",
      "6",
      "Error"
    ],
    "answer": "27",
    "difficulty": "Medium",
    "explanation": "The exponentiation operator computes 3 raised to the power of 3, yielding 27."
  },
  {
    "question": "What does class MyClass { static x = 5; } console.log(MyClass.x); return?",
    "options": [
      "5",
      "undefined",
      "MyClass",
      "Error"
    ],
    "answer": "5",
    "difficulty": "Medium",
    "explanation": "Static properties are accessed directly on the class, returning 5."
  },
  {
    "question": "What does let x = false ? 'On' : 'Off'; assign to x?",
    "options": [
      "Off",
      "On",
      "false",
      "Error"
    ],
    "answer": "Off",
    "difficulty": "Medium",
    "explanation": "The ternary operator evaluates false, assigning 'Off' to x."
  },
  {
    "question": "What does obj?.nested?.prop return if nested is undefined?",
    "options": [
      "undefined",
      "null",
      "Error",
      "prop"
    ],
    "answer": "undefined",
    "difficulty": "Medium",
    "explanation": "Optional chaining stops at undefined, returning undefined."
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









