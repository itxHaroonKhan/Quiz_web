
import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 67 questions covering specified JavaScript topics
quiz = [
  {
    "question": "What is a Function Declaration in JavaScript?",
    "options": [
      "A function that is stored in a variable",
      "A named function defined using the 'function' keyword",
      "A function immediately executed after creation",
      "An anonymous function passed as an argument"
    ],
    "answer": "A named function defined using the 'function' keyword",
    "difficulty": "Easy",
    "explanation": "Function Declarations are named functions created using the 'function' keyword and are hoisted."
  },
  {
    "question": "Which syntax is used to create an Arrow Function?",
    "options": [
      "function() => {}",
      "() => {}",
      "=> function() {}",
      "function => () {}"
    ],
    "answer": "() => {}",
    "difficulty": "Easy",
    "explanation": "Arrow functions use the '() => {}' syntax introduced in ES6."
  },
  {
    "question": "What is an Immediately Invoked Function Expression (IIFE)?",
    "options": [
      "A function that runs when an event occurs",
      "A function that runs only once after page load",
      "A function that is executed immediately after being defined",
      "A function that calls itself recursively"
    ],
    "answer": "A function that is executed immediately after being defined",
    "difficulty": "Medium",
    "explanation": "IIFEs are functions wrapped in parentheses and immediately invoked to create isolated scopes."
  },
  {
    "question": "What does the 'this' keyword refer to inside a function defined in an object method?",
    "options": [
      "The global object",
      "The object itself",
      "Undefined",
      "The function itself"
    ],
    "answer": "The object itself",
    "difficulty": "Medium",
    "explanation": "'this' inside an object method refers to the object owning that method."
  },
  {
    "question": "How do you define a constructor function in JavaScript?",
    "options": [
      "function Person() { this.name = 'Name'; }",
      "let Person = () => { this.name = 'Name'; }",
      "class Person { name = 'Name'; }",
      "function Person => { this.name = 'Name'; }"
    ],
    "answer": "function Person() { this.name = 'Name'; }",
    "difficulty": "Medium",
    "explanation": "Constructor functions are defined like normal functions but used with 'new' to create objects."
  },
  {
    "question": "What is the primary use of the 'prototype' property in JavaScript?",
    "options": [
      "To add properties and methods to all instances of an object",
      "To create a new object",
      "To inherit variables from another function",
      "To execute functions asynchronously"
    ],
    "answer": "To add properties and methods to all instances of an object",
    "difficulty": "Medium",
    "explanation": "The prototype allows sharing methods and properties among all instances created by a constructor."
  },
  {
    "question": "What is a callback function?",
    "options": [
      "A function that is called immediately when defined",
      "A function passed as an argument to another function to be called later",
      "A function that returns another function",
      "A function that can only be used inside classes"
    ],
    "answer": "A function passed as an argument to another function to be called later",
    "difficulty": "Easy",
    "explanation": "Callbacks enable asynchronous programming by allowing functions to be called after an operation finishes."
  },
  {
    "question": "How do you define an asynchronous function in JavaScript?",
    "options": [
      "function async() {}",
      "async function myFunc() {}",
      "function* myFunc() {}",
      "await function myFunc() {}"
    ],
    "answer": "async function myFunc() {}",
    "difficulty": "Medium",
    "explanation": "The 'async' keyword before a function allows it to use 'await' for asynchronous operations."
  },
  {
    "question": "What is the output of this code?\n\n```js\nfunction test() {\n  console.log(this);\n}\ntest();\n```",
    "options": [
      "The global object (window in browser)",
      "undefined",
      "The test function itself",
      "An error"
    ],
    "answer": "The global object (window in browser)",
    "difficulty": "Medium",
    "explanation": "In non-strict mode, 'this' inside a normal function points to the global object."
  },
  {
    "question": "Which of these is NOT a function type in JavaScript?",
    "options": [
      "Generator function",
      "Arrow function",
      "Class function",
      "Recursive function"
    ],
    "answer": "Class function",
    "difficulty": "Easy",
    "explanation": "Classes have methods, but 'Class function' is not a standard function type."
  },
  {
    "question": "What does the 'bind' method do in JavaScript?",
    "options": [
      "Executes a function immediately",
      "Creates a new function with a fixed 'this' value",
      "Combines two functions into one",
      "Pauses function execution"
    ],
    "answer": "Creates a new function with a fixed 'this' value",
    "difficulty": "Medium",
    "explanation": "The 'bind' method creates a new function with its 'this' keyword set to the provided value."
  },
  {
    "question": "What is the purpose of the 'call' method in JavaScript?",
    "options": [
      "To invoke a function with a specified 'this' value and arguments",
      "To create a new object",
      "To loop through an array",
      "To define a new function"
    ],
    "answer": "To invoke a function with a specified 'this' value and arguments",
    "difficulty": "Medium",
    "explanation": "'call' invokes a function with a given 'this' value and individual arguments."
  },
  {
    "question": "What does the 'apply' method do in JavaScript?",
    "options": [
      "Executes a function with arguments as an array",
      "Adds a new property to an object",
      "Clones an object",
      "Defines a recursive function"
    ],
    "answer": "Executes a function with arguments as an array",
    "difficulty": "Medium",
    "explanation": "'apply' is similar to 'call' but accepts arguments as an array."
  },
  {
    "question": "What is the output of this code?\n\n```js\nconst obj = {\n  value: 42,\n  getValue: function() { return this.value; }\n};\nconsole.log(obj.getValue());\n```",
    "options": [
      "42",
      "undefined",
      "null",
      "An error"
    ],
    "answer": "42",
    "difficulty": "Easy",
    "explanation": "'this' refers to 'obj', so 'getValue' returns the 'value' property of 'obj'."
  },
  {
    "question": "What is a higher-order function in JavaScript?",
    "options": [
      "A function that takes another function as an argument or returns a function",
      "A function that runs faster than others",
      "A function defined inside a class",
      "A function that is called only once"
    ],
    "answer": "A function that takes another function as an argument or returns a function",
    "difficulty": "Medium",
    "explanation": "Higher-order functions either accept functions as arguments or return functions."
  },
  {
    "question": "What does the following code return?\n\n```js\nfunction outer() {\n  let x = 10;\n  return function inner() { return x; };\n}\nconst fn = outer();\nconsole.log(fn());\n```",
    "options": [
      "10",
      "undefined",
      "null",
      "An error"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "The inner function retains access to 'x' via closure, so it returns 10."
  },
  {
    "question": "What is the purpose of the 'new' keyword in JavaScript?",
    "options": [
      "To create a new variable",
      "To instantiate an object from a constructor function",
      "To declare a new function",
      "To reset an object's properties"
    ],
    "answer": "To instantiate an object from a constructor function",
    "difficulty": "Easy",
    "explanation": "'new' creates a new object and sets its prototype to the constructor's prototype."
  },
  {
    "question": "Which method is used to create a shallow copy of an object?",
    "options": [
      "Object.assign()",
      "Object.create()",
      "Object.defineProperty()",
      "Object.keys()"
    ],
    "answer": "Object.assign()",
    "difficulty": "Medium",
    "explanation": "'Object.assign()' copies enumerable own properties from one or more source objects to a target object."
  },
  {
    "question": "What is the output of this code?\n\n```js\nconst arr = [1, 2, 3];\narr.forEach(item => console.log(item * 2));\n```",
    "options": [
      "2, 4, 6",
      "[2, 4, 6]",
      "undefined",
      "An error"
    ],
    "answer": "2, 4, 6",
    "difficulty": "Easy",
    "explanation": "'forEach' iterates over the array, and the arrow function logs each item multiplied by 2."
  },
  {
    "question": "What is a Generator function in JavaScript?",
    "options": [
      "A function that generates random numbers",
      "A function that can pause and resume its execution",
      "A function that runs asynchronously",
      "A function that creates objects"
    ],
    "answer": "A function that can pause and resume its execution",
    "difficulty": "Medium",
    "explanation": "Generator functions, defined with 'function*', use 'yield' to pause and resume execution."
  },
  {
421
    "question": "What does the 'Object.keys()' method return?",
    "options": [
      "An array of an object's enumerable property names",
      "An array of an object's values",
      "A new object with copied properties",
      "The prototype of the object"
    ],
    "answer": "An array of an object's enumerable property names",
    "difficulty": "Easy",
    "explanation": "'Object.keys()' returns an array containing the names of an object's enumerable properties."
  },
  {
    "question": "What is the purpose of the 'map' method in JavaScript?",
    "options": [
      "To create a new array with transformed elements",
      "To loop through an array without returning anything",
      "To filter elements from an array",
      "To sort an array"
    ],
    "answer": "To create a new array with transformed elements",
    "difficulty": "Easy",
    "explanation": "'map' applies a function to each array element and returns a new array with the results."
  },
  {
    "question": "What does the following code return?\n\n```js\nconst numbers = [1, 2, 3];\nconst doubled = numbers.map(n => n * 2);\nconsole.log(doubled);\n```",
    "options": [
      "[2, 4, 6]",
      "[1, 2, 3]",
      "2, 4, 6",
      "An error"
    ],
    "answer": "[2, 4, 6]",
    "difficulty": "Easy",
    "explanation": "'map' creates a new array with each element doubled."
  },
  {
    "question": "What is the difference between 'let' and 'const' in function scope?",
    "options": [
      "'let' allows reassignment, 'const' does not",
      "'const' allows reassignment, 'let' does not",
      "'let' is block-scoped, 'const' is not",
      "'const' is hoisted, 'let' is not"
    ],
    "answer": "'let' allows reassignment, 'const' does not",
    "difficulty": "Easy",
    "explanation": "'let' allows variable reassignment, while 'const' prevents it after initial declaration."
  },
  {
    "question": "What is a closure in JavaScript?",
    "options": [
      "A function that closes over variables from its outer scope",
      "A function that runs only once",
      "A function that has no parameters",
      "A function that returns an object"
    ],
    "answer": "A function that closes over variables from its outer scope",
    "difficulty": "Medium",
    "explanation": "Closures allow inner functions to access variables from their outer scope even after the outer function finishes."
  },
  {
    "question": "What is the output of this code?\n\n```js\nfunction example() {\n  return () => { console.log('Hello'); };\n}\nconst fn = example();\nfn();\n```",
    "options": [
      "Hello",
      "undefined",
      "null",
      "An error"
    ],
    "answer": "Hello",
    "difficulty": "Medium",
    "explanation": "The inner arrow function is returned and executed, logging 'Hello'."
  },
  {
    "question": "What does the 'reduce' method do in JavaScript?",
    "options": [
      "Reduces an array to a single value by applying a function",
      "Removes elements from an array",
      "Sorts an array in descending order",
      "Creates a new array with filtered elements"
    ],
    "answer": "Reduces an array to a single value by applying a function",
    "difficulty": "Medium",
    "explanation": "'reduce' applies a function to an accumulator and each array element to produce a single value."
  },
  {
    "question": "What is the output of this code?\n\n```js\nconst nums = [1, 2, 3];\nconst sum = nums.reduce((acc, curr) => acc + curr, 0);\nconsole.log(sum);\n```",
    "options": [
      "6",
      "[1, 2, 3]",
      "0",
      "An error"
    ],
    "answer": "6",
    "difficulty": "Medium",
    "explanation": "'reduce' sums all elements in the array starting with an initial accumulator value of 0."
  },
  {
    "question": "What does 'Object.create()' do in JavaScript?",
    "options": [
      "Creates a new object with the specified prototype",
      "Clones an existing object",
      "Creates a new array",
      "Defines a new function"
    ],
    "answer": "Creates a new object with the specified prototype",
    "difficulty": "Medium",
    "explanation": "'Object.create()' creates a new object with the specified prototype object and properties."
  },
  {
    "question": "What is the purpose of the 'filter' method in JavaScript?",
    "options": [
      "To create a new array with elements that pass a test",
      "To transform each element in an array",
      "To sort an array",
      "To reduce an array to a single value"
    ],
    "answer": "To create a new array with elements that pass a test",
    "difficulty": "Easy",
    "explanation": "'filter' creates a new array with elements that return true for the provided function."
  },
  {
    "question": "What is the output of this code?\n\n```js\nconst nums = [1, 2, 3, 4];\nconst evens = nums.filter(n => n % 2 === 0);\nconsole.log(evens);\n```",
    "options": [
      "[2, 4]",
      "[1, 3]",
      "[1, 2, 3, 4]",
      "An error"
    ],
    "answer": "[2, 4]",
    "difficulty": "Easy",
    "explanation": "'filter' creates a new array with only even numbers from the original array."
  },
  {
    "question": "What does the 'Object.defineProperty()' method do?",
    "options": [
      "Defines a new property or modifies an existing one on an object",
      "Creates a new object",
      "Deletes a property from an object",
      "Returns an array of object properties"
    ],
    "answer": "Defines a new property or modifies an existing one on an object",
    "difficulty": "Medium",
    "explanation": "'Object.defineProperty()' allows precise control over property attributes like writability."
  },
  {
    "question": "What is a pure function in JavaScript?",
    "options": [
      "A function that always returns the same output for the same input and has no side effects",
      "A function that modifies global variables",
      "A function that runs asynchronously",
      "A function that returns another function"
    ],
    "answer": "A function that always returns the same output for the same input and has no side effects",
    "difficulty": "Medium",
    "explanation": "Pure functions are predictable, producing consistent outputs without modifying external state."
  },
  {
    "question": "What is the output of this code?\n\n```js\nconst obj = {};\nObject.defineProperty(obj, 'prop', { value: 42, writable: false });\nobj.prop = 100;\nconsole.log(obj.prop);\n```",
    "options": [
      "42",
      "100",
      "undefined",
      "An error"
    ],
    "answer": "42",
    "difficulty": "Medium",
    "explanation": "'writable: false' prevents 'prop' from being reassigned, so it remains 42."
  },
  {
    "question": "What does the 'some' method do in JavaScript?",
    "options": [
      "Checks if at least one element in an array passes a test",
      "Returns a new array with transformed elements",
      "Sums all elements in an array",
      "Filters out duplicate elements"
    ],
    "answer": "Checks if at least one element in an array passes a test",
    "difficulty": "Medium",
    "explanation": "'some' returns true if at least one element satisfies the provided function."
  },
  {
    "question": "What is the output of this code?\n\n```js\nconst nums = [1, 2, 3];\nconst hasEven = nums.some(n => n % 2 === 0);\nconsole.log(hasEven);\n```",
    "options": [
      "true",
      "false",
      "[2]",
      "An error"
    ],
    "answer": "true",
    "difficulty": "Easy",
    "explanation": "'some' returns true because at least one element (2) is even."
  },
  {
    "question": "What is the purpose of the 'every' method in JavaScript?",
    "options": [
      "Checks if all elements in an array pass a test",
      "Transforms each element in an array",
      "Reduces an array to a single value",
      "Sorts an array"
    ],
    "answer": "Checks if all elements in an array pass a test",
    "difficulty": "Medium",
    "explanation": "'every' returns true if all elements satisfy the provided function."
  },
  {
    "question": "What is the output of this code?\n\n```js\nconst nums = [2, 4, 6];\nconst allEven = nums.every(n => n % 2 === 0);\nconsole.log(allEven);\n```",
    "options": [
      "true",
      "false",
      "[2, 4, 6]",
      "An error"
    ],
    "answer": "true",
    "difficulty": "Easy",
    "explanation": "'every' returns true because all elements are even."
  },
  {
    "question": "What does the 'Object.freeze()' method do?",
    "options": [
      "Prevents modifications to an object",
      "Creates a new object",
      "Clones an object",
      "Removes properties from an object"
    ],
    "answer": "Prevents modifications to an object",
    "difficulty": "Medium",
    "explanation": "'Object.freeze()' makes an object immutable, preventing property additions or changes."
  },
  {
    "question": "What is the output of this code?\n\n```js\nconst obj = Object.freeze({ x: 1 });\nobj.x = 2;\nconsole.log(obj.x);\n```",
    "options": [
      "1",
      "2",
      "undefined",
      "An error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "'Object.freeze()' prevents changes, so 'x' remains 1."
  },
  {
    "question": "What is a method in JavaScript?",
    "options": [
      "A function that is a property of an object",
      "A function that runs asynchronously",
      "A function that returns another function",
      "A function that cannot take arguments"
    ],
    "answer": "A function that is a property of an object",
    "difficulty": "Easy",
    "explanation": "Methods are functions defined as properties of objects."
  },
  {
    "question": "What does the 'slice' method do when called on an array?",
    "options": [
      "Returns a shallow copy of a portion of an array",
      "Removes elements from an array",
      "Adds elements to an array",
      "Sorts an array"
    ],
    "answer": "Returns a shallow copy of a portion of an array",
    "difficulty": "Easy",
    "explanation": "'slice' returns a new array with elements from the specified start to end indices."
  },
  {
    "question": "What is the output of this code?\n\n```js\nconst arr = [1, 2, 3, 4];\nconsole.log(arr.slice(1, 3));\n```",
    "options": [
      "[2, 3]",
      "[1, 2, 3]",
      "[3, 4]",
      "An error"
    ],
    "answer": "[2, 3]",
    "difficulty": "Easy",
    "explanation": "'slice(1, 3)' returns a new array with elements from index 1 to 2."
  },
  {
    "question": "What does the 'splice' method do in JavaScript?",
    "options": [
      "Modifies an array by adding or removing elements",
      "Creates a shallow copy of an array",
      "Filters elements from an array",
      "Maps elements to a new array"
    ],
    "answer": "Modifies an array by adding or removing elements",
    "difficulty": "Medium",
    "explanation": "'splice' changes the original array by removing or adding elements at a specified index."
  },
  {
    "question": "What is the output of this code?\n\n```js\nconst arr = [1, 2, 3];\narr.splice(1, 1, 5);\nconsole.log(arr);\n```",
    "options": [
      "[1, 5, 3]",
      "[1, 2, 3]",
      "[1, 5]",
      "An error"
    ],
    "answer": "[1, 5, 3]",
    "difficulty": "Medium",
    "explanation": "'splice(1, 1, 5)' removes 1 element at index 1 and inserts 5."
  },
  {
    "question": "What is the purpose of the 'Object.entries()' method?",
    "options": [
      "Returns an array of an object's key-value pairs",
      "Creates a new object",
      "Deletes properties from an object",
      "Returns an array of object values"
    ],
    "answer": "Returns an array of an object's key-value pairs",
    "difficulty": "Medium",
    "explanation": "'Object.entries()' returns an array of arrays, each containing a key-value pair."
  },
  {
    "question": "What is the output of this code?\n\n```js\nconst obj = { a: 1, b: 2 };\nconsole.log(Object.entries(obj));\n```",
    "options": [
      "[['a', 1], ['b', 2]]",
      "{ a: 1, b: 2 }",
      "['a', 'b']",
      "[1, 2]"
    ],
    "answer": "[['a', 1], ['b', 2]]",
   ,en": "'Object.entries()' returns an array of key-value pair arrays."
  },
  {
    "question": "What does the 'find' method do in JavaScript?",
    "options": [
      "Returns the first element in an array that passes a test",
      "Returns all elements that pass a test",
      "Transforms an array",
      "Sorts an array"
    ],
    "answer": "Returns the first element in an array that passes a test",
    "difficulty": "Easy",
    "explanation": "'find' returns the first element that satisfies the provided function or undefined."
  },
  {
    "question": "What is the output of this code?\n\n```js\nconst arr = [1, 2, 3];\nconst found = arr.find(n => n > 1);\nconsole.log(found);\n```",
    "options": [
      "2",
      "[2, 3]",
      "1",
      "undefined"
    ],
    "answer": "2",
    "difficulty": "Easy",
    "explanation": "'find' returns the first element greater than 1, which is 2."
  },
  {
    "question": "What does the 'Object.values()' method do?",
    "options": [
      "Returns an array of an object's values",
      "Returns an array of an object's keys",
      "Creates a new object",
      "Freezes an object"
    ],
    "answer": "Returns an array of an object's values",
    "difficulty": "Easy",
    "explanation": "'Object.values()' returns an array containing the values of an object's enumerable properties."
  },
  {
    "question": "What is the output of this code?\n\n```js\nconst obj = { a: 1, b: 2 };\nconsole.log(Object.values(obj));\n```",
    "options": [
      "[1, 2]",
      "['a', 'b']",
      "{ a: 1, b: 2 }",
      "An error"
    ],
    "answer": "[1, 2]",
    "difficulty": "Easy",
    "explanation": "'Object.values()' returns an array of the object's values."
  },
  {
    "question": "What is a factory function in JavaScript?",
    "options": [
      "A function that returns a new object",
      "A function that creates a new array",
      "A function that modifies the global scope",
      "A function that runs asynchronously"
    ],
    "answer": "A function that returns a new object",
    "difficulty": "Medium",
    "explanation": "Factory functions create and return new objects without using the 'new' keyword."
  },
  {
    "question": "What is the output of this code?\n\n```js\nfunction createPerson(name) {\n  return { name };\n}\nconst person = createPerson('Alice');\nconsole.log(person.name);\n```",
    "options": [
      "Alice",
      "undefined",
      "null",
      "An error"
    ],
    "answer": "Alice",
    "difficulty": "Easy",
    "explanation": "The factory function 'createPerson' returns an object with a 'name' property."
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

