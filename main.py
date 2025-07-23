
import streamlit as st
import random
from datetime import datetime
import uuid

# Quiz data with 67 questions covering specified JavaScript topics
quiz = [
    {
        "question": "What is the primary purpose of the `async` keyword in JavaScript?",
        "options": [
            "To define a function that returns a Promise",
            "To execute a function synchronously",
            "To create a loop that runs asynchronously",
            "To handle errors in synchronous code"
        ],
        "answer": "To define a function that returns a Promise",
        "difficulty": "Easy",
        "explanation": "The `async` keyword before a function ensures it returns a Promise, allowing the use of `await` inside it to handle asynchronous operations."
    },
    {
        "question": "What does the `await` keyword do in an async function?",
        "options": [
            "Pauses execution until a Promise resolves",
            "Executes a callback function immediately",
            "Skips the Promise and continues execution",
            "Converts a Promise to a synchronous function"
        ],
        "answer": "Pauses execution until a Promise resolves",
        "difficulty": "Easy",
        "explanation": "`await` pauses the execution of an async function until the Promise it is waiting for resolves or rejects, then resumes with the resolved value."
    },
    {
        "question": "What happens if you use `await` outside of an async function?",
        "options": [
            "It works normally",
            "It throws a SyntaxError",
            "It converts the function to async",
            "It ignores the await keyword"
        ],
        "answer": "It throws a SyntaxError",
        "difficulty": "Medium",
        "explanation": "`await` can only be used inside an `async` function. Using it outside results in a SyntaxError because it requires an async context."
    },
    {
        "question": "What does the following code output?\n```javascript\nasync function test() {\n  return 'Hello';\n}\ntest().then(result => console.log(result));\n```",
        "options": [
            "undefined",
            "Hello",
            "Promise { 'Hello' }",
            "Error"
        ],
        "answer": "Hello",
        "difficulty": "Easy",
        "explanation": "The `async` function `test` returns a Promise that resolves to 'Hello'. The `.then` method logs the resolved value, which is 'Hello'."
    },
    {
        "question": "What is a Promise in JavaScript?",
        "options": [
            "A function that runs synchronously",
            "An object representing the eventual completion or failure of an asynchronous operation",
            "A method to handle synchronous callbacks",
            "A loop that executes asynchronously"
        ],
        "answer": "An object representing the eventual completion or failure of an asynchronous operation",
        "difficulty": "Easy",
        "explanation": "A Promise is an object that represents the result of an asynchronous operation, which can either resolve (success) or reject (failure)."
    },
    {
        "question": "What does the `.then()` method do on a Promise?",
        "options": [
            "Executes a callback when the Promise is rejected",
            "Executes a callback when the Promise is resolved",
            "Pauses execution until the Promise resolves",
            "Converts the Promise to a synchronous function"
        ],
        "answer": "Executes a callback when the Promise is resolved",
        "difficulty": "Easy",
        "explanation": "The `.then()` method is called when a Promise resolves, passing the resolved value to the callback function."
    },
    {
        "question": "What does the `.catch()` method do on a Promise?",
        "options": [
            "Handles resolved values",
            "Handles rejected Promises",
            "Executes a synchronous callback",
            "Pauses the Promise execution"
        ],
        "answer": "Handles rejected Promises",
        "difficulty": "Easy",
        "explanation": "The `.catch()` method is used to handle errors when a Promise is rejected, allowing error handling in asynchronous code."
    },
    {
        "question": "What is the output of this code?\n```javascript\nsetTimeout(() => console.log('A'), 0);\nconsole.log('B');\n```",
        "options": [
            "A, B",
            "B, A",
            "A",
            "B"
        ],
        "answer": "B, A",
        "difficulty": "Medium",
        "explanation": "`setTimeout` schedules 'A' to be logged after a delay (even if 0), so it runs after synchronous code. 'B' is logged first, then 'A'."
    },
    {
        "question": "What is an asynchronous callback in JavaScript?",
        "options": [
            "A function that executes immediately",
            "A function passed to another function to be executed later",
            "A function that returns a Promise",
            "A function that runs synchronously"
        ],
        "answer": "A function passed to another function to be executed later",
        "difficulty": "Easy",
        "explanation": "An asynchronous callback is a function passed as an argument to another function, executed later when an asynchronous operation completes."
    },
    {
        "question": "What does `Promise.all()` do?",
        "options": [
            "Executes Promises one by one",
            "Waits for all Promises to resolve or one to reject",
            "Converts callbacks to Promises",
            "Runs Promises synchronously"
        ],
        "answer": "Waits for all Promises to resolve or one to reject",
        "difficulty": "Medium",
        "explanation": "`Promise.all()` takes an array of Promises and returns a new Promise that resolves when all input Promises resolve or rejects if any Promise rejects."
    },
    {
        "question": "What is the output of this code?\n```javascript\nasync function test() {\n  await Promise.resolve('Hello');\n  console.log('World');\n}\ntest();\n```",
        "options": [
            "Hello",
            "World",
            "Hello, World",
            "Nothing"
        ],
        "answer": "World",
        "difficulty": "Medium",
        "explanation": "The `await` resolves the Promise, and then 'World' is logged. 'Hello' is not logged because it is the resolved value, not printed."
    },
    {
        "question": "What happens if a Promise rejects inside an async function without a try-catch block?",
        "options": [
            "The error is silently ignored",
            "The async function throws an error",
            "The Promise resolves with undefined",
            "The function continues execution"
        ],
        "answer": "The async function throws an error",
        "difficulty": "Medium",
        "explanation": "If a Promise rejects in an async function and is not caught with try-catch, the async function rejects with that error."
    },
    {
        "question": "What does the following code output?\n```javascript\nconsole.log('Start');\nsetTimeout(() => console.log('Timeout'), 0);\nPromise.resolve().then(() => console.log('Promise'));\nconsole.log('End');\n```",
        "options": [
            "Start, End, Promise, Timeout",
            "Start, Promise, End, Timeout",
            "Start, End, Timeout, Promise",
            "Start, Timeout, Promise, End"
        ],
        "answer": "Start, End, Promise, Timeout",
        "difficulty": "Hard",
        "explanation": "Synchronous code ('Start', 'End') runs first. Microtasks (Promise) run before macrotasks (setTimeout), so the order is Start, End, Promise, Timeout."
    },
    {
        "question": "What is the purpose of `Promise.resolve()`?",
        "options": [
            "To create a rejected Promise",
            "To create a resolved Promise with a given value",
            "To pause a Promise",
            "To convert a callback to a Promise"
        ],
        "answer": "To create a resolved Promise with a given value",
        "difficulty": "Easy",
        "explanation": "`Promise.resolve(value)` creates a Promise that is already resolved with the specified value."
    },
    {
        "question": "What does `Promise.reject()` do?",
        "options": [
            "Creates a resolved Promise",
            "Creates a rejected Promise with a given reason",
            "Converts a Promise to a callback",
            "Pauses a Promise"
        ],
        "answer": "Creates a rejected Promise with a given reason",
        "difficulty": "Easy",
        "explanation": "`Promise.reject(reason)` creates a Promise that is already rejected with the specified reason."
    },
    {
        "question": "What is the output of this code?\n```javascript\nasync function test() {\n  try {\n    await Promise.reject('Error');\n  } catch (e) {\n    console.log(e);\n  }\n}\ntest();\n```",
        "options": [
            "Error",
            "undefined",
            "Nothing",
            "SyntaxError"
        ],
        "answer": "Error",
        "difficulty": "Medium",
        "explanation": "The `await Promise.reject('Error')` throws an error, which is caught by the try-catch block and logged as 'Error'."
    },
    {
        "question": "What is a key difference between callbacks and Promises?",
        "options": [
            "Callbacks are always synchronous, Promises are always asynchronous",
            "Promises can handle errors more easily with `.catch()`",
            "Callbacks return Promises",
            "Promises are executed immediately"
        ],
        "answer": "Promises can handle errors more easily with `.catch()`",
        "difficulty": "Medium",
        "explanation": "Promises provide a cleaner way to handle errors using `.catch()`, while callbacks often require explicit error handling logic."
    },
    {
        "question": "What does the following code output?\n```javascript\nsetTimeout(() => console.log('A'), 100);\nsetTimeout(() => console.log('B'), 0);\nconsole.log('C');\n```",
        "options": [
            "C, B, A",
            "A, B, C",
            "C, A, B",
            "B, C, A"
        ],
        "answer": "C, B, A",
        "difficulty": "Medium",
        "explanation": "Synchronous code ('C') runs first. `setTimeout` with 0ms ('B') runs before `setTimeout` with 100ms ('A') due to the shorter delay."
    },
    {
        "question": "What is the purpose of `async/await` compared to raw Promises?",
        "options": [
            "To make asynchronous code look synchronous",
            "To replace synchronous code",
            "To execute code faster",
            "To avoid using Promises"
        ],
        "answer": "To make asynchronous code look synchronous",
        "difficulty": "Easy",
        "explanation": "`async/await` is syntactic sugar over Promises, making asynchronous code easier to read by resembling synchronous code."
    },
    {
        "question": "What does `Promise.race()` do?",
        "options": [
            "Resolves when all Promises resolve",
            "Resolves or rejects as soon as one Promise resolves or rejects",
            "Rejects all Promises",
            "Runs Promises sequentially"
        ],
        "answer": "Resolves or rejects as soon as one Promise resolves or rejects",
        "difficulty": "Medium",
        "explanation": "`Promise.race()` takes an array of Promises and resolves or rejects as soon as any one of the Promises settles."
    },
    {
        "question": "What is the output of this code?\n```javascript\nasync function test() {\n  console.log('Start');\n  await new Promise(resolve => setTimeout(resolve, 1000));\n  console.log('End');\n}\ntest();\nconsole.log('Outside');\n```",
        "options": [
            "Start, End, Outside",
            "Start, Outside, End",
            "Outside, Start, End",
            "End, Start, Outside"
        ],
        "answer": "Start, Outside, End",
        "difficulty": "Hard",
        "explanation": "'Start' logs first, then `await` pauses `test`. 'Outside' logs next (synchronous). After 1 second, 'End' logs when the Promise resolves."
    },
    {
        "question": "What happens if you forget to return a Promise in an async function?",
        "options": [
            "The function returns undefined",
            "The function automatically returns a resolved Promise",
            "The function throws an error",
            "The function waits indefinitely"
        ],
        "answer": "The function automatically returns a resolved Promise",
        "difficulty": "Medium",
        "explanation": "An async function always returns a Promise. If no value is returned, it returns a Promise that resolves to `undefined`."
    },
    {
        "question": "What is callback hell?",
        "options": [
            "A Promise chain that fails",
            "Nested callbacks causing unreadable code",
            "A rejected Promise",
            "An async function with too many awaits"
        ],
        "answer": "Nested callbacks causing unreadable code",
        "difficulty": "Easy",
        "explanation": "Callback hell refers to deeply nested callbacks in asynchronous code, making it hard to read and maintain."
    },
    {
        "question": "What does the following code output?\n```javascript\nfunction delay(ms) {\n  return new Promise(resolve => setTimeout(() => resolve('Done'), ms));\n}\nasync function test() {\n  console.log(await delay(100));\n}\ntest();\n```",
        "options": [
            "Done",
            "undefined",
            "Promise { 'Done' }",
            "Error"
        ],
        "answer": "Done",
        "difficulty": "Medium",
        "explanation": "The `delay` function returns a Promise that resolves to 'Done' after 100ms. `await` gets the resolved value, so 'Done' is logged."
    },
    {
        "question": "What is the main advantage of using Promises over callbacks?",
        "options": [
            "Promises are faster",
            "Promises avoid nested code with chaining",
            "Promises are synchronous",
            "Promises eliminate errors"
        ],
        "answer": "Promises avoid nested code with chaining",
        "difficulty": "Medium",
        "explanation": "Promises allow chaining with `.then()`, reducing the nesting seen in callback-based code, improving readability."
    },
    {
        "question": "What does `Promise.allSettled()` do?",
        "options": [
            "Resolves when all Promises resolve",
            "Resolves when any Promise resolves",
            "Returns the status and result of all Promises, regardless of whether they resolve or reject",
            "Rejects if any Promise rejects"
        ],
        "answer": "Returns the status and result of all Promises, regardless of whether they resolve or reject",
        "difficulty": "Medium",
        "explanation": "`Promise.allSettled()` waits for all Promises to settle (resolve or reject) and returns an array of their statuses and results."
    },
    {
        "question": "What is the output of this code?\n```javascript\nconsole.log('A');\nPromise.resolve().then(() => console.log('B'));\nsetTimeout(() => console.log('C'), 0);\nPromise.resolve().then(() => console.log('D'));\nconsole.log('E');\n```",
        "options": [
            "A, E, B, D, C",
            "A, B, D, E, C",
            "A, E, C, B, D",
            "A, B, E, D, C"
        ],
        "answer": "A, E, B, D, C",
        "difficulty": "Hard",
        "explanation": "Synchronous code ('A', 'E') runs first. Microtasks ('B', 'D') run next in order. `setTimeout` ('C') runs last as a macrotask."
    },
    {
        "question": "What does the `finally()` method do on a Promise?",
        "options": [
            "Executes a callback whether the Promise resolves or rejects",
            "Resolves the Promise",
            "Rejects the Promise",
            "Pauses the Promise"
        ],
        "answer": "Executes a callback whether the Promise resolves or rejects",
        "difficulty": "Medium",
        "explanation": "The `.finally()` method runs a callback after a Promise settles, regardless of whether it resolved or rejected."
    },
    {
        "question": "What is the output of this code?\n```javascript\nasync function test() {\n  return await Promise.resolve('Test');\n}\ntest().then(console.log);\n```",
        "options": [
            "Test",
            "undefined",
            "Promise { 'Test' }",
            "Error"
        ],
        "answer": "Test",
        "difficulty": "Medium",
        "explanation": "The `await` resolves the Promise to 'Test', which is returned by the async function and logged by `.then(console.log)`."
    },
    {
        "question": "What is the purpose of wrapping a callback-based function in a Promise?",
        "options": [
            "To make it synchronous",
            "To allow it to be used with async/await",
            "To make it run faster",
            "To avoid errors"
        ],
        "answer": "To allow it to be used with async/await",
        "difficulty": "Medium",
        "explanation": "Wrapping a callback-based function in a Promise allows it to be used with `async/await`, making asynchronous code easier to manage."
    },
    {
        "question": "What does the following code output?\n```javascript\nsetTimeout(() => console.log('A'), 0);\nnew Promise(resolve => {\n  console.log('B');\n  resolve();\n}).then(() => console.log('C'));\nconsole.log('D');\n```",
        "options": [
            "B, D, C, A",
            "A, B, C, D",
            "B, C, D, A",
            "D, B, C, A"
        ],
        "answer": "B, D, C, A",
        "difficulty": "Hard",
        "explanation": "Synchronous code ('B', 'D') runs first. The Promise's `.then` ('C') runs as a microtask. `setTimeout` ('A') runs last as a macrotask."
    },
    {
        "question": "What happens if you call `await` on a non-Promise value?",
        "options": [
            "It throws an error",
            "It wraps the value in a resolved Promise",
            "It skips the await",
            "It pauses execution indefinitely"
        ],
        "answer": "It wraps the value in a resolved Promise",
        "difficulty": "Medium",
        "explanation": "`await` on a non-Promise value automatically wraps it in a resolved Promise, so the value is returned immediately."
    },
    {
        "question": "What is the output of this code?\n```javascript\nasync function test() {\n  console.log('A');\n  await Promise.resolve();\n  console.log('B');\n}\ntest();\nconsole.log('C');\n```",
        "options": [
            "A, B, C",
            "A, C, B",
            "C, A, B",
            "B, A, C"
        ],
        "answer": "A, C, B",
        "difficulty": "Hard",
        "explanation": "'A' logs first, then `await` pauses `test`. 'C' logs next (synchronous). After the Promise resolves, 'B' logs."
    },
    {
        "question": "What is the difference between `Promise.all()` and `Promise.race()`?",
        "options": [
            "Promise.all waits for all to resolve, Promise.race waits for any to settle",
            "Promise.race waits for all to resolve, Promise.all waits for any to settle",
            "Promise.all is synchronous, Promise.race is asynchronous",
            "Promise.race handles errors, Promise.all does not"
        ],
        "answer": "Promise.all waits for all to resolve, Promise.race waits for any to settle",
        "difficulty": "Medium",
        "explanation": "`Promise.all` resolves when all Promises resolve or one rejects. `Promise.race` settles as soon as any Promise settles."
    },
    {
        "question": "What does this code output?\n```javascript\nfunction callback(cb) {\n  setTimeout(() => cb('Done'), 100);\n}\ncallback(result => console.log(result));\n```",
        "options": [
            "Done",
            "undefined",
            "Error",
            "Nothing"
        ],
        "answer": "Done",
        "difficulty": "Easy",
        "explanation": "The `callback` function calls the provided callback with 'Done' after 100ms, so 'Done' is logged."
    },
    {
        "question": "What is the output of this code?\n```javascript\nasync function test() {\n  await Promise.reject('Error').catch(e => console.log(e));\n  console.log('Continue');\n}\ntest();\n```",
        "options": [
            "Error, Continue",
            "Continue, Error",
            "Error",
            "Continue"
        ],
        "answer": "Error, Continue",
        "difficulty": "Medium",
        "explanation": "The rejected Promise is caught by `.catch`, logging 'Error'. The async function continues, logging 'Continue'."
    },
    {
        "question": "What is the purpose of the `async` keyword when used with an arrow function?",
        "options": [
            "To make the arrow function synchronous",
            "To return a Promise from the arrow function",
            "To execute the arrow function immediately",
            "To prevent errors in the arrow function"
        ],
        "answer": "To return a Promise from the arrow function",
        "difficulty": "Easy",
        "explanation": "The `async` keyword with an arrow function ensures it returns a Promise, just like with regular functions."
    },
    {
        "question": "What does this code output?\n```javascript\nPromise.resolve('A').then(v => console.log(v));\nPromise.resolve('B').then(v => console.log(v));\nconsole.log('C');\n```",
        "options": [
            "C, A, B",
            "A, B, C",
            "C, B, A",
            "A, C, B"
        ],
        "answer": "C, A, B",
        "difficulty": "Hard",
        "explanation": "Synchronous code ('C') runs first. The `.then` callbacks ('A', 'B') run as microtasks in the order they were queued."
    },
    {
        "question": "What happens if you chain multiple `.then()` calls on a Promise?",
        "options": [
            "Only the first `.then` executes",
            "Each `.then` executes in sequence, passing the result to the next",
            "All `.then` calls execute simultaneously",
            "The Promise rejects"
        ],
        "answer": "Each `.then` executes in sequence, passing the result to the next",
        "difficulty": "Medium",
        "explanation": "Chaining `.then()` calls allows sequential processing of a Promise's result, with each `.then` receiving the previous one's return value."
    },
    {
        "question": "What is the output of this code?\n```javascript\nasync function test() {\n  console.log('A');\n  await new Promise(resolve => setTimeout(() => resolve('B'), 0));\n  console.log(await Promise.resolve('C'));\n}\ntest();\nconsole.log('D');\n```",
        "options": [
            "A, D, C",
            "A, C, D",
            "D, A, C",
            "A, D, B"
        ],
        "answer": "A, D, C",
        "difficulty": "Hard",
        "explanation": "'A' logs first, then `await` pauses `test`. 'D' logs next (synchronous). After the Promise resolves, 'C' is logged."
    },
    {
        "question": "What is the benefit of using `async/await` over Promise chains?",
        "options": [
            "It runs code faster",
            "It makes asynchronous code easier to read and write",
            "It eliminates the need for Promises",
            "It handles synchronous code better"
        ],
        "answer": "It makes asynchronous code easier to read and write",
        "difficulty": "Easy",
        "explanation": "`async/await` simplifies asynchronous code by making it look synchronous, improving readability over nested `.then()` chains."
    },
    {
        "question": "What does this code output?\n```javascript\nfunction asyncTask(cb) {\n  setTimeout(() => cb('Done'), 100);\n}\nasyncTask(result => console.log(result));\n```",
        "options": [
            "Done",
            "undefined",
            "Error",
            "Nothing"
        ],
        "answer": "Done",
        "difficulty": "Easy",
        "explanation": "The `asyncTask` function calls the callback with 'Done' after 100ms, so 'Done' is logged."
    },
    {
        "question": "What is the output of this code?\n```javascript\nasync function test() {\n  return Promise.resolve('Success');\n}\ntest().then(v => console.log(v));\n```",
        "options": [
            "Success",
            "undefined",
            "Promise { 'Success' }",
            "Error"
        ],
        "answer": "Success",
        "difficulty": "Medium",
        "explanation": "The async function returns a Promise resolving to 'Success', which is logged by the `.then` callback."
    },
    {
        "question": "What is the purpose of the `setTimeout` function in asynchronous code?",
        "options": [
            "To execute code synchronously",
            "To delay execution of a callback",
            "To resolve a Promise",
            "To pause the event loop"
        ],
        "answer": "To delay execution of a callback",
        "difficulty": "Easy",
        "explanation": "`setTimeout` schedules a callback to run after a specified delay, making it useful for asynchronous operations."
    },
    {
        "question": "What does this code output?\n```javascript\nasync function test() {\n  console.log('A');\n  await Promise.resolve('B');\n  console.log('C');\n  await Promise.resolve('D');\n  console.log('E');\n}\ntest();\nconsole.log('F');\n```",
        "options": [
            "A, F, C, E",
            "A, C, E, F",
            "F, A, C, E",
            "A, C, F, E"
        ],
        "answer": "A, F, C, E",
        "difficulty": "Hard",
        "explanation": "'A' logs first, then `await` pauses `test`. 'F' logs next (synchronous). After the first Promise resolves, 'C' logs, then 'E' after the second."
    },
    {
        "question": "What is the output of this code?\n```javascript\nPromise.reject('Error').catch(e => console.log(e));\nconsole.log('Done');\n```",
        "options": [
            "Error, Done",
            "Done, Error",
            "Error",
            "Done"
        ],
        "answer": "Done, Error",
        "difficulty": "Hard",
        "explanation": "'Done' logs first (synchronous). The rejected Promise is caught by `.catch`, logging 'Error' as a microtask."
    },
    {
        "question": "What is the purpose of converting a callback-based function to a Promise?",
        "options": [
            "To make it run faster",
            "To allow chaining and better error handling",
            "To make it synchronous",
            "To avoid using callbacks entirely"
        ],
        "answer": "To allow chaining and better error handling",
        "difficulty": "Medium",
        "explanation": "Converting callbacks to Promises allows chaining with `.then()` and centralized error handling with `.catch()`."
    },
    {
        "question": "What does this code output?\n```javascript\nasync function test() {\n  console.log(await Promise.resolve('A'));\n  console.log('B');\n}\ntest();\nconsole.log('C');\n```",
        "options": [
            "A, B, C",
            "A, C, B",
            "C, A, B",
            "B, A, C"
        ],
        "answer": "C, A, B",
        "difficulty": "Hard",
        "explanation": "'C' logs first (synchronous). The async function logs 'A' after the Promise resolves, then 'B'."
    },
    {
        "question": "What is the output of this code?\n```javascript\nsetTimeout(() => console.log('A'), 0);\nnew Promise(resolve => resolve('B')).then(v => console.log(v));\nconsole.log('C');\n```",
        "options": [
            "C, B, A",
            "A, B, C",
            "C, A, B",
            "B, C, A"
        ],
        "answer": "C, B, A",
        "difficulty": "Hard",
        "explanation": "Synchronous code ('C') runs first. The Promise's `.then` ('B') runs as a microtask. `setTimeout` ('A') runs last as a macrotask."
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
