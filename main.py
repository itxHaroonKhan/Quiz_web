import streamlit as st
import random
from datetime import datetime
import uuid

quiz = [
    # 13. Testing sets of conditions (if...else and else if)
    {
        "question": "What is logged?\n```javascript\nlet temp = 25;\nif (temp > 30) {\n  console.log('Hot');\n} else if (temp > 20) {\n  console.log('Warm');\n} else {\n  console.log('Cool');\n}\n```",
        "options": ["Hot", "Warm", "Cool", "Nothing"],
        "answer": "Warm",
        "difficulty": "Medium",
        "explanation": "Since `temp = 25` satisfies `temp > 20` but not `temp > 30`, 'Warm' is logged.",
        "hint": "Check which condition is evaluated first in an if...else if chain."
    },
    {
        "question": "What is logged?\n```javascript\nlet score = 85;\nif (score >= 90) {\n  console.log('A');\n} else if (score >= 80) {\n  console.log('B');\n} else {\n  console.log('C');\n}\n```",
        "options": ["A", "B", "C", "Nothing"],
        "answer": "B",
        "difficulty": "Medium",
        "explanation": "Since `score = 85` satisfies `score >= 80` but not `score >= 90`, 'B' is logged.",
        "hint": "Evaluate the conditions in order."
    },

    # 14. if statements nested
    {
        "question": "What is logged?\n```javascript\nlet num = 6;\nif (num > 5) {\n  if (num % 2 === 0) {\n    console.log('Even and large');\n  }\n}\n```",
        "options": ["Even and large", "Nothing", "Error", "6"],
        "answer": "Even and large",
        "difficulty": "Medium",
        "explanation": "Since `num > 5` and `num % 2 === 0` are true for `num = 6`, 'Even and large' is logged.",
        "hint": "Check both conditions in the nested if structure."
    },
    {
        "question": "What is logged?\n```javascript\nlet x = 10;\nif (x > 5) {\n  if (x < 15) {\n    console.log('In range');\n  }\n}\n```",
        "options": ["In range", "Nothing", "Error", "10"],
        "answer": "In range",
        "difficulty": "Medium",
        "explanation": "Since `x > 5` and `x < 15` are true for `x = 10`, 'In range' is logged.",
        "hint": "Both nested conditions must be true."
    },

    # 15. Arrays
    {
        "question": "What is logged?\n```javascript\nlet arr = [10, 20, 30];\nconsole.log(arr[2]);\n```",
        "options": ["30", "20", "10", "undefined"],
        "answer": "30",
        "difficulty": "Easy",
        "explanation": "Arrays are zero-indexed, so `arr[2]` accesses the third element, 30.",
        "hint": "Array indices start at 0."
    },
    {
        "question": "What is logged?\n```javascript\nlet arr = [1, 2, 3];\nconsole.log(arr[0]);\n```",
        "options": ["1", "2", "3", "undefined"],
        "answer": "1",
        "difficulty": "Easy",
        "explanation": "The first element of the array is at index 0, so `arr[0]` is 1.",
        "hint": "Check the first index of an array."
    },

    # 16. Arrays: adding and removing elements
    {
        "question": "What is logged?\n```javascript\nlet arr = [1, 2];\narr.push(3);\nconsole.log(arr.length);\n```",
        "options": ["3", "2", "1", "4"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "The `push(3)` method adds 3 to the array, making it `[1, 2, 3]`, so `arr.length` is 3.",
        "hint": "What does `push()` do to an array’s length?"
    },
    {
        "question": "What is logged?\n```javascript\nlet arr = [1, 2, 3];\narr.pop();\nconsole.log(arr.length);\n```",
        "options": ["2", "3", "1", "0"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "The `pop()` method removes the last element, leaving `[1, 2]`, so `arr.length` is 2.",
        "hint": "What happens when you remove the last element?"
    },

    # 17. Arrays: removing, inserting, and extracting elements
    {
        "question": "What is logged?\n```javascript\nlet arr = [1, 2, 3, 4];\nlet removed = arr.splice(1, 2);\nconsole.log(arr);\n```",
        "options": ["[1, 4]", "[1, 2, 3, 4]", "[2, 3]", "[1]"],
        "answer": "[1, 4]",
        "difficulty": "Hard",
        "explanation": "`splice(1, 2)` removes 2 elements starting at index 1, leaving `arr` as `[1, 4]`.",
        "hint": "Check how `splice()` modifies the array."
    },
    {
        "question": "What is logged?\n```javascript\nlet arr = [1, 2, 3];\narr.splice(1, 0, 4);\nconsole.log(arr);\n```",
        "options": ["[1, 4, 2, 3]", "[1, 2, 3, 4]", "[1, 2, 4]", "[4, 1, 2, 3]"],
        "answer": "[1, 4, 2, 3]",
        "difficulty": "Hard",
        "explanation": "`splice(1, 0, 4)` inserts 4 at index 1 without removing elements, resulting in `[1, 4, 2, 3]`.",
        "hint": "What does `splice()` do when the second argument is 0?"
    },

    # 18. for loops
    {
        "question": "What is logged?\n```javascript\nfor (let i = 0; i < 3; i++) {\n  console.log(i * 2);\n}\n```",
        "options": ["0, 2, 4", "0, 1, 2", "2, 4, 6", "Nothing"],
        "answer": "0, 2, 4",
        "difficulty": "Medium",
        "explanation": "The loop runs for `i = 0, 1, 2`, logging `i * 2` each time: `0, 2, 4`.",
        "hint": "Trace the loop iterations and multiply by 2."
    },
    {
        "question": "What is logged?\n```javascript\nfor (let i = 1; i <= 3; i++) {\n  console.log(i);\n}\n```",
        "options": ["1, 2, 3", "0, 1, 2", "1, 2", "Nothing"],
        "answer": "1, 2, 3",
        "difficulty": "Easy",
        "explanation": "The loop runs for `i = 1, 2, 3`, logging each value.",
        "hint": "Check the loop’s start and end conditions."
    },

    # 19. for loops: flags, Booleans, array length, and breaks
    {
        "question": "What is logged?\n```javascript\nlet arr = [5, 10, 15];\nlet found = false;\nfor (let i = 0; i < arr.length; i++) {\n  if (arr[i] > 12) {\n    found = true;\n    break;\n  }\n}\nconsole.log(found);\n```",
        "options": ["true", "false", "15", "Nothing"],
        "answer": "true",
        "difficulty": "Hard",
        "explanation": "The loop breaks when `arr[i] = 15` (`> 12`), setting `found = true`, which is logged.",
        "hint": "When does the loop stop, and what does `break` do?"
    },
    {
        "question": "What is logged?\n```javascript\nlet arr = [1, 2, 3];\nlet found = false;\nfor (let i = 0; i < arr.length; i++) {\n  if (arr[i] > 5) {\n    found = true;\n    break;\n  }\n}\nconsole.log(found);\n```",
        "options": ["true", "false", "3", "Nothing"],
        "answer": "false",
        "difficulty": "Medium",
        "explanation": "No element in `[1, 2, 3]` is `> 5`, so `found` remains `false`.",
        "hint": "Check if any array element meets the condition."
    },

    # 20. for loops nested
    {
        "question": "What is logged?\n```javascript\nlet sum = 0;\nfor (let i = 1; i <= 2; i++) {\n  for (let j = 1; j <= 2; j++) {\n    sum += i + j;\n  }\n}\nconsole.log(sum);\n```",
        "options": ["10", "6", "8", "12"],
        "answer": "10",
        "difficulty": "Hard",
        "explanation": "The nested loops compute `sum += i + j` for `(i,j) = (1,1), (1,2), (2,1), (2,2)`, giving `2 + 3 + 3 + 4 = 10`.",
        "hint": "Calculate the sum for each pair of `i` and `j`."
    },
    {
        "question": "What is logged?\n```javascript\nlet count = 0;\nfor (let i = 1; i <= 2; i++) {\n  for (let j = 1; j <= 2; j++) {\n    count++;\n  }\n}\nconsole.log(count);\n```",
        "options": ["4", "2", "6", "0"],
        "answer": "4",
        "difficulty": "Medium",
        "explanation": "The nested loops run for `(i,j) = (1,1), (1,2), (2,1), (2,2)`, incrementing `count` 4 times.",
        "hint": "Count how many times the inner loop runs."
    },

    # 21. Changing case
    {
        "question": "What is logged?\n```javascript\nlet str = 'JavaScript';\nconsole.log(str.toLowerCase());\n```",
        "options": ["javascript", "JavaScript", "JAVASCRIPT", "js"],
        "answer": "javascript",
        "difficulty": "Easy",
        "explanation": "The `toLowerCase()` method converts all characters to lowercase, resulting in 'javascript'.",
        "hint": "What does `toLowerCase()` do to a string?"
    },
    {
        "question": "What is logged?\n```javascript\nlet str = 'JavaScript';\nconsole.log(str.toUpperCase());\n```",
        "options": ["JAVASCRIPT", "javascript", "JavaScript", "JS"],
        "answer": "JAVASCRIPT",
        "difficulty": "Easy",
        "explanation": "The `toUpperCase()` method converts all characters to uppercase, resulting in 'JAVASCRIPT'.",
        "hint": "What does `toUpperCase()` do to a string?"
    },

    # 22. Strings: measuring length and extracting parts
    {
        "question": "What is logged?\n```javascript\nlet str = 'Hello World';\nconsole.log(str.slice(6, 11));\n```",
        "options": ["World", "Hello", "Worl", "ld"],
        "answer": "World",
        "difficulty": "Medium",
        "explanation": "The `slice(6, 11)` method extracts characters from index 6 to 10, giving 'World'.",
        "hint": "Check the start and end indices for `slice()`."
    },
    {
        "question": "What is logged?\n```javascript\nlet str = 'JavaScript';\nconsole.log(str.length);\n```",
        "options": ["10", "9", "11", "8"],
        "answer": "10",
        "difficulty": "Easy",
        "explanation": "The `length` property returns the number of characters in 'JavaScript', which is 10.",
        "hint": "Count the characters in the string."
    },

    # 23. Strings: finding segments
    {
        "question": "What is logged?\n```javascript\nlet str = 'Hello World';\nconsole.log(str.includes('World'));\n```",
        "options": ["true", "false", "World", "5"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The `includes()` method checks if 'World' is a substring, returning `true`.",
        "hint": "Does the string contain the substring 'World'?"
    },
    {
        "question": "What is logged?\n```javascript\nlet str = 'Hello World';\nconsole.log(str.indexOf('World'));\n```",
        "options": ["6", "-1", "0", "5"],
        "answer": "6",
        "difficulty": "Medium",
        "explanation": "`indexOf('World')` returns the starting index of 'World', which is 6.",
        "hint": "Where does the substring 'World' start?"
    },

    # 24. Strings: finding a character at a location
    {
        "question": "What is logged?\n```javascript\nlet str = 'JavaScript';\nconsole.log(str[4]);\n```",
        "options": ["S", "a", "J", "c"],
        "answer": "S",
        "difficulty": "Medium",
        "explanation": "Bracket notation `str[4]` accesses the character at index 4, which is 'S'.",
        "hint": "Strings can be indexed like arrays."
    },
    {
        "question": "What is logged?\n```javascript\nlet str = 'Hello';\nconsole.log(str.charAt(1));\n```",
        "options": ["e", "H", "l", "o"],
        "answer": "e",
        "difficulty": "Medium",
        "explanation": "`charAt(1)` returns the character at index 1, which is 'e'.",
        "hint": "What character is at the second position?"
    },

    # 25. Strings: replacing characters
    {
        "question": "What is logged?\n```javascript\nlet str = 'Hello World';\nconsole.log(str.replace('World', 'Universe'));\n```",
        "options": ["Hello Universe", "Hello World", "Universe", "Nothing"],
        "answer": "Hello Universe",
        "difficulty": "Medium",
        "explanation": "The `replace()` method replaces the first occurrence of 'World' with 'Universe'.",
        "hint": "What does `replace()` do with the first match?"
    },
    {
        "question": "What is logged?\n```javascript\nlet str = 'Hello Hello';\nconsole.log(str.replace('Hello', 'Hi'));\n```",
        "options": ["Hi Hello", "Hi Hi", "Hello Hi", "Nothing"],
        "answer": "Hi Hello",
        "difficulty": "Medium",
        "explanation": "`replace()` replaces only the first occurrence of 'Hello' with 'Hi'.",
        "hint": "Does `replace()` affect all occurrences?"
    },

    # 26. Rounding numbers
    {
        "question": "What is logged?\n```javascript\nlet num = 3.14159;\nconsole.log(Math.floor(num));\n```",
        "options": ["3", "4", "3.14", "3.1"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "`Math.floor()` rounds down to the nearest integer, so 3.14159 becomes 3.",
        "hint": "What does `Math.floor()` do to decimals?"
    },
    {
        "question": "What is logged?\n```javascript\nlet num = 3.14159;\nconsole.log(Math.ceil(num));\n```",
        "options": ["4", "3", "3.14", "3.1"],
        "answer": "4",
        "difficulty": "Medium",
        "explanation": "`Math.ceil()` rounds up to the nearest integer, so 3.14159 becomes 4.",
        "hint": "What does `Math.ceil()` do to decimals?"
    },

    # 27. Generating random numbers
    {
        "question": "What is a possible value of `num`?\n```javascript\nlet num = Math.floor(Math.random() * 10) + 1;\n```",
        "options": ["5", "10", "0", "11"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "`Math.random() * 10` gives 0 to <10, `Math.floor()` rounds down, and `+ 1` shifts the range to 1–10, so 5 is possible.",
        "hint": "What range does this expression produce?"
    },

    # 28. Converting strings to integers and decimals
    {
        "question": "What is logged?\n```javascript\nlet str = '123.45';\nconsole.log(parseFloat(str));\n```",
        "options": ["123.45", "123", "NaN", "123.5"],
        "answer": "123.45",
        "difficulty": "Medium",
        "explanation": "`parseFloat()` converts the string '123.45' to the number 123.45.",
        "hint": "Does `parseFloat()` keep decimals?"
    },
    {
        "question": "What is logged?\n```javascript\nlet str = '123';\nconsole.log(parseInt(str));\n```",
        "options": ["123", "123.0", "NaN", "12"],
        "answer": "123",
        "difficulty": "Medium",
        "explanation": "`parseInt()` converts the string '123' to the integer 123.",
        "hint": "Does `parseInt()` include decimals?"
    },

    # 29. Converting strings to numbers, numbers to strings
    {
        "question": "What is logged?\n```javascript\nlet num = 100;\nconsole.log(typeof num.toString());\n```",
        "options": ["string", "number", "object", "undefined"],
        "answer": "string",
        "difficulty": "Medium",
        "explanation": "The `toString()` method converts the number 100 to a string, so `typeof` returns 'string'.",
        "hint": "What does `toString()` do to a number?"
    },

    # 30. Controlling the length of decimals
    {
        "question": "What is logged?\n```javascript\nlet num = 9.8765;\nconsole.log(num.toFixed(3));\n```",
        "options": ["9.877", "9.876", "9.88", "9.8765"],
        "answer": "9.877",
        "difficulty": "Medium",
        "explanation": "`toFixed(3)` rounds to 3 decimal places, so 9.8765 becomes '9.877' (as a string).",
        "hint": "How many decimal places does `toFixed(3)` keep?"
    },

    # 31. Getting the current date and time
    {
        "question": "What is logged?\n```javascript\nlet date = new Date();\nconsole.log(typeof date);\n```",
        "options": ["object", "string", "number", "undefined"],
        "answer": "object",
        "difficulty": "Medium",
        "explanation": "The `Date` constructor creates a Date object, so `typeof` returns 'object'.",
        "hint": "What type is a `Date` instance?"
    },

    # 32. Extracting parts of the date and time
    {
        "question": "What does `date.getHours()` return for 09:39 AM?\n```javascript\nlet date = new Date('2025-06-09T09:39:00');\n```",
        "options": ["9", "21", "39", "12"],
        "answer": "9",
        "difficulty": "Medium",
        "explanation": "`getHours()` returns the hour in 24-hour format, so 09:39 AM is 9.",
        "hint": "Is the time in 24-hour format?"
    },
    {
        "question": "What is logged?\n```javascript\nlet date = new Date('2025-06-09');\nconsole.log(date.getDay());\n```",
        "options": ["1", "0", "6", "9"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "`getDay()` returns the day of the week (0=Sunday, 6=Saturday). June 9, 2025, is a Monday, so it returns 1.",
        "hint": "What day of the week is June 9, 2025?"
    },

    # 33. Specifying a date and time
    {
        "question": "What is logged?\n```javascript\nlet date = new Date('2025-12-25T14:30:00');\nconsole.log(date.getHours());\n```",
        "options": ["14", "2", "12", "30"],
        "answer": "14",
        "difficulty": "Medium",
        "explanation": "`getHours()` returns the hour in 24-hour format, so 14:30 (2:30 PM) returns 14.",
        "hint": "Check the hour in 24-hour format."
    },

    # 34. Changing elements of a date and time
    {
        "question": "What is logged?\n```javascript\nlet date = new Date('2025-06-09');\ndate.setFullYear(2026);\nconsole.log(date.getFullYear());\n```",
        "options": ["2026", "2025", "2027", "6"],
        "answer": "2026",
        "difficulty": "Medium",
        "explanation": "`setFullYear(2026)` changes the year to 2026, so `getFullYear()` returns 2026.",
        "hint": "What does `setFullYear()` modify?"
    },

    # 35. Functions
    {
        "question": "What is logged?\n```javascript\nfunction multiply(x, y) {\n  return x * y;\n}\nconsole.log(multiply(4, 5));\n```",
        "options": ["20", "9", "45", "undefined"],
        "answer": "20",
        "difficulty": "Easy",
        "explanation": "The `multiply` function returns `x * y`, so `4 * 5 = 20`.",
        "hint": "What does the function return?"
    },

    # 36. Functions: passing them data
    {
        "question": "What is logged?\n```javascript\nfunction formatName(first, last) {\n  return `${first} ${last}`;\n}\nconsole.log(formatName('John', 'Doe'));\n```",
        "options": ["John Doe", "John", "Doe", "undefined"],
        "answer": "John Doe",
        "difficulty": "Medium",
        "explanation": "The function uses a template literal to combine `first` and `last`, returning 'John Doe'.",
        "hint": "How are the arguments combined?"
    },

    # 37. Functions: passing data back from them
    {
        "question": "What is logged?\n```javascript\nfunction isEven(num) {\n  return num % 2 === 0;\n}\nconsole.log(isEven(10));\n```",
        "options": ["true", "false", "10", "0"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The `isEven` function returns `true` if `num` is divisible by 2, which 10 is.",
        "hint": "What does the function check?"
    }
]

# Cache shuffled quiz (unchanged)
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

# Initialize session state (unchanged)
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
        "time_left": 1800,
        "theme": "dark",
        "streak": 0,
        "show_hint": False,
        "started": False
    })

# Theme toggle (unchanged)
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# Timer logic (unchanged)
def update_timer():
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.session_state.time_left = max(1800 - elapsed, 0)
    if st.session_state.time_left <= 0:
        st.session_state.show_results = True
        st.rerun()

# Reset quiz (unchanged)
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

# NEW: Progress snapshot function
def show_progress_snapshot():
    answered = sum(1 for ans in st.session_state.answers if ans is not None)
    st.markdown("""
        <div style='background: var(--bg-container); padding: 15px; border-radius: 10px; box-shadow: 0 4px 12px var(--shadow); margin: 10px 0;'>
            <h4 style='color: var(--text-color);'>📊 Progress Snapshot</h4>
            <div style='color: var(--text-color); font-size: 14px;'>
                - 🏆 Current Score: {score}<br>
                - 🔥 Streak: {streak}<br>
                - ✅ Questions Answered: {answered}/{total}
            </div>
        </div>
    """.format(
        score=st.session_state.score,
        streak=st.session_state.streak,
        answered=answered,
        total=len(st.session_state.quiz_data)
    ), unsafe_allow_html=True)

# CSS (unchanged)
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

# Main UI (unchanged)
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 JavaScript Quiz Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript Skills!</p>', unsafe_allow_html=True)

# Theme toggle button (unchanged)
if st.button("🌙 Toggle Theme", key="theme_toggle"):
    toggle_theme()
    st.rerun()

# Welcome screen (unchanged)
if not st.session_state.started:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: var(--text-color); font-size: 18px;">Test your JavaScript knowledge with 50 exciting questions!</p>
        <p style="color: #b0b0d0;">30 minutes, 2 points per correct answer. Ready?</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Quiz", key="start_quiz"):
        st.session_state.started = True
        st.session_state.start_time = datetime.now()
        st.rerun()
else:
    # Timer (unchanged)
    if not st.session_state.show_results:
        update_timer()
        minutes = int(st.session_state.time_left // 60)
        seconds = int(st.session_state.time_left % 60)
        st.markdown(f'<div class="timer">⏰ Time Left: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

    if not st.session_state.quiz_data:
        st.error("No quiz questions available.")
    else:
        # Progress bar (unchanged)
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

                # Display difficulty and streak (unchanged)
                st.markdown(f'<div class="difficulty">Difficulty: {q["difficulty"]} | Streak: 🔥 {st.session_state.streak}</div>', unsafe_allow_html=True)

                # Split question into text and code (unchanged)
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

                # Option buttons (unchanged)
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
                                st.session_state.score += 1
                        else:
                            st.session_state.streak = 0
                        st.rerun()

                # Feedback (unchanged)
                if st.session_state.feedback:
                    if st.session_state.feedback["is_correct"]:
                        st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="color: var(--text-color); font-size: 14px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                # Hint button (unchanged)
                if st.button("💡 Show Hint", key="hint", disabled=st.session_state.show_hint or st.session_state.selected_option is not None):
                    st.session_state.show_hint = True
                    st.session_state.score = max(0, st.session_state.score - 0.5)
                    st.rerun()
                if st.session_state.show_hint:
                    st.markdown(f'<div style="color: #facc15; font-size: 14px;">Hint: {q["hint"]}</div>', unsafe_allow_html=True)

                # CHANGED: Updated navigation (removed Previous and Skip, added Progress Snapshot)
                col1, col2 = st.columns(2)  # Now only two columns
                with col1:
                    if st.button("📊 Progress Snapshot", key="progress"):
                        show_progress_snapshot()
                with col2:
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

                # Reset quiz button (unchanged)
                if st.button("🔄 Reset Quiz", key="reset"):
                    reset_quiz()

                st.markdown("</div>", unsafe_allow_html=True)
