import streamlit as st
import random
from datetime import datetime
import streamlit.components.v1 as components

# Corrected Quiz Data (fixed the block-scoping question)
quiz = [

    {
        "question": "Which function displays a message in a popup?",
        "options": ["alert()", "prompt()", "confirm()", "message()"],
        "answer": "alert()"
    },
    {
        "question": "What does alert('Error!') do?",
        "options": ["Logs to console", "Shows a popup", "Creates a variable", "Nothing"],
        "answer": "Shows a popup"
    },
    {
        "question": "What is the return value of alert()?",
        "options": ["string", "undefined", "null", "boolean"],
        "answer": "undefined"
    },
    {
        "question": "What happens if alert() is called with no argument?",
        "options": ["Empty popup", "Throws error", "Shows 'undefined'", "Does nothing"],
        "answer": "Shows 'undefined'"
    },
    {
        "question": "How do you add a line break in an alert message?",
        "options": ["<br>", "\\n", "/n", ";"],
        "answer": "\\n"
    },
    {
        "question": "What does alert('Hello\\nWorld') show?",
        "options": ["HelloWorld", "Hello World", "Hello\\nWorld", "Error"],
        "answer": "Hello World"
    },
    {
        "question": "Can alert() accept multiple arguments?",
        "options": ["Yes", "No", "Only strings", "Only numbers"],
        "answer": "No"
    },
    {
        "question": "What does alert(5 + 5) display?",
        "options": ["'5 + 5'", "10", "'10'", "Error"],
        "answer": "'10'"
    },

    // Variables for Strings (8 questions)
    {
        "question": "How do you declare a string variable?",
        "options": ["let str = 'text';", "let str = text;", "string str = 'text';", "var str = (text);"],
        "answer": "let str = 'text';"
    },
    {
        "question": "What is typeof 'hello'?",
        "options": ["'string'", "'text'", "'object'", "'char'"],
        "answer": "'string'"
    },
    {
        "question": "What does 'test'.length return?",
        "options": ["3", "4", "5", "undefined"],
        "answer": "4"
    },
    {
        "question": "How do you declare a string with double quotes?",
        "options": ["let str = 'text';", "let str = \"text\";", "let str = (text);", "let str = text;"],
        "answer": "let str = \"text\";"
    },
    {
        "question": "What is 'hello'[0]?",
        "options": ["'h'", "'e'", "0", "undefined"],
        "answer": "'h'"
    },
    {
        "question": "What does 'abc'.toUpperCase() return?",
        "options": ["'ABC'", "'abc'", "'Abc'", "undefined"],
        "answer": "'ABC'"
    },
    {
        "question": "What is the value of let str = 'code'; str = 'test';?",
        "options": ["'code'", "'test'", "undefined", "Error"],
        "answer": "'test'"
    },
    {
        "question": "What does 'hi'.charAt(1) return?",
        "options": ["'h'", "'i'", "undefined", "Error"],
        "answer": "'i'"
    },

    // Variables for Numbers (8 questions)
    {
        "question": "Which is a valid number declaration?",
        "options": ["let num = '10';", "let num = 10;", "let num = ten;", "let num = [10];"],
        "answer": "let num = 10;"
    },
    {
        "question": "What is typeof 42?",
        "options": ["'number'", "'int'", "'float'", "'integer'"],
        "answer": "'number'"
    },
    {
        "question": "What does let num = 5; num = 10; return?",
        "options": ["5", "10", "undefined", "Error"],
        "answer": "10"
    },
    {
        "question": "What is parseInt('15')?",
        "options": ["15", "'15'", "NaN", "undefined"],
        "answer": "15"
    },
    {
        "question": "What is parseFloat('3.14')?",
        "options": ["3", "3.14", "'3.14'", "NaN"],
        "answer": "3.14"
    },
    {
        "question": "What does Number('123') return?",
        "options": ["123", "'123'", "NaN", "undefined"],
        "answer": "123"
    },
    {
        "question": "What is typeof 10.5?",
        "options": ["'number'", "'float'", "'double'", "'decimal'"],
        "answer": "'number'"
    },
    {
        "question": "What does isNaN(5) return?",
        "options": ["true", "false", "NaN", "undefined"],
        "answer": "false"
    },

    // Variable Names (Legal and Illegal) (8 questions)
    {
        "question": "Which is a legal variable name?",
        "options": ["myVar", "1var", "my-var", "let"],
        "answer": "myVar"
    },
    {
        "question": "Which character can start a variable name?",
        "options": ["number", "letter", "$", "Both B and C"],
        "answer": "Both B and C"
    },
    {
        "question": "Which is NOT a reserved keyword?",
        "options": ["if", "else", "data", "for"],
        "answer": "data"
    },
    {
        "question": "Is '2name' a legal variable name?",
        "options": ["Yes", "No", "Only in strict mode", "Only with var"],
        "answer": "No"
    },
    {
        "question": "Which is a valid variable name?",
        "options": ["_count", "count!", "count#", "count space"],
        "answer": "_count"
    },
    {
        "question": "What happens if you use 'function' as a variable name?",
        "options": ["Works fine", "SyntaxError", "ReferenceError", "undefined"],
        "answer": "SyntaxError"
    },
    {
        "question": "Is 'my_name' a legal variable name?",
        "options": ["Yes", "No", "Only in strict mode", "Only with let"],
        "answer": "Yes"
    },
    {
        "question": "Which naming convention is used for constants?",
        "options": ["camelCase", "UPPER_CASE", "PascalCase", "kebab-case"],
        "answer": "UPPER_CASE"
    },

    // Math Expressions: Familiar Operators (6 questions)
    {
        "question": "What is 5 + 3 * 2?",
        "options": ["16", "11", "8", "10"],
        "answer": "11"
    },
    {
        "question": "What is 10 - 4 / 2?",
        "options": ["3", "8", "6", "2"],
        "answer": "8"
    },
    {
        "question": "What is 15 % 4?",
        "options": ["3", "4", "2", "0"],
        "answer": "3"
    },
    {
        "question": "What is 6 * 2 + 3?",
        "options": ["15", "18", "9", "12"],
        "answer": "15"
    },
    {
        "question": "What is 20 / 5 - 1?",
        "options": ["3", "4", "5", "2"],
        "answer": "3"
    },
    {
        "question": "What is 2 + 3 - 1?",
        "options": ["4", "5", "6", "3"],
        "answer": "4"
    },

    // Math Expressions: Unfamiliar Operators (6 questions)
    {
        "question": "What does 2 ** 3 return?",
        "options": ["6", "8", "9", "Error"],
        "answer": "8"
    },
    {
        "question": "What is the ++ operator in x++?",
        "options": ["Adds 1", "Subtracts 1", "Multiplies by 1", "Divides by 1"],
        "answer": "Adds 1"
    },
    {
        "question": "What does x-- do if x is 5?",
        "options": ["4", "5", "6", "Error"],
        "answer": "4"
    },
    {
        "question": "What is 10 ** 2?",
        "options": ["20", "100", "12", "Error"],
        "answer": "100"
    },
    {
        "question": "What does += do in x += 5?",
        "options": ["Assigns 5", "Adds 5 to x", "Subtracts 5", "Multiplies by 5"],
        "answer": "Adds 5 to x"
    },
    {
        "question": "What is x *= 2 if x is 3?",
        "options": ["6", "5", "9", "Error"],
        "answer": "6"
    },

    // Math Expressions: Eliminating Ambiguity (6 questions)
    {
        "question": "What is (2 + 3) * 4?",
        "options": ["20", "14", "24", "10"],
        "answer": "20"
    },
    {
        "question": "How do parentheses affect 2 + 3 * 4?",
        "options": ["No effect", "Changes result to 20", "Causes error", "Changes result to 14"],
        "answer": "Changes result to 20"
    },
    {
        "question": "What is 10 / (2 + 3)?",
        "options": ["2", "5", "1", "Error"],
        "answer": "2"
    },
    {
        "question": "What is 4 * (2 + 1)?",
        "options": ["12", "9", "10", "8"],
        "answer": "12"
    },
    {
        "question": "What does (5 - 2) * 3 return?",
        "options": ["9", "6", "15", "3"],
        "answer": "9"
    },
    {
        "question": "How do you ensure 2 + 3 * 4 evaluates to 20?",
        "options": ["Use spaces", "Use parentheses", "Use comments", "Use variables"],
        "answer": "Use parentheses"
    },

    // Concatenating Text Strings (8 questions)
    {
        "question": "What is 'Hello' + ' ' + 'World'?",
        "options": ["'HelloWorld'", "'Hello World'", "'Hello + World'", "Error"],
        "answer": "'Hello World'"
    },
    {
        "question": "What is '5' + 2?",
        "options": ["7", "'7'", "'52'", "Error"],
        "answer": "'52'"
    },
    {
        "question": "What is `Hi ${'there'}`?",
        "options": ["'Hi there'", "'Hi ${there}'", "'there'", "Error"],
        "answer": "'Hi there'"
    },
    {
        "question": "What is 3 + '3'?",
        "options": ["6", "'6'", "'33'", "Error"],
        "answer": "'33'"
    },
    {
        "question": "How do you convert a number to string for concatenation?",
        "options": ["num.toString()", "String(num)", "num + ''", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "What is 'test' + null?",
        "options": ["'testnull'", "'test'", "null", "Error"],
        "answer": "'testnull'"
    },
    {
        "question": "What is `Sum: ${4 + 2}`?",
        "options": ["'Sum: 6'", "'Sum: 4+2'", "'Sum: 42'", "Error"],
        "answer": "'Sum: 6'"
    },
    {
        "question": "What is 'a' + 'b' + 'c'?",
        "options": ["'abc'", "'a b c'", "'a+b+c'", "Error"],
        "answer": "'abc'"
    },

    // Prompts (8 questions)
    {
        "question": "What does prompt('Enter name') return if the user clicks Cancel?",
        "options": ["null", "empty string", "undefined", "Error"],
        "answer": "null"
    },
    {
        "question": "What does prompt('Age', '18') return if the user enters '20'?",
        "options": ["18", "20", "'20'", "null"],
        "answer": "'20'"
    },
    {
        "question": "What does confirm('Save?') return on OK?",
        "options": ["true", "false", "'OK'", "null"],
        "answer": "true"
    },
    {
        "question": "How do you convert prompt input to a number?",
        "options": ["parseInt(prompt())", "prompt().toNumber()", "prompt().parse()", "Not possible"],
        "answer": "parseInt(prompt())"
    },
    {
        "question": "What does prompt('Enter') return if the user clicks OK with no input?",
        "options": ["null", "empty string", "undefined", "Error"],
        "answer": "empty string"
    },
    {
        "question": "What does confirm('Delete?') return on Cancel?",
        "options": ["true", "false", "'Cancel'", "null"],
        "answer": "false"
    },
    {
        "question": "What is Number(prompt('Enter number', '10')) if the user enters '5'?",
        "options": ["5", "'5'", "10", "null"],
        "answer": "5"
    },
    {
        "question": "Can prompt() accept multiple default values?",
        "options": ["Yes", "No", "Only strings", "Only numbers"],
        "answer": "No"
    },

    // If Statements (6 questions)
    {
        "question": "What is the correct if statement syntax?",
        "options": ["if (x == 5) {}", "if x = 5 {}", "if (x = 5) {}", "if x == 5 then"],
        "answer": "if (x == 5) {}"
    },
    {
        "question": "When does an if statement execute its block?",
        "options": ["Always", "When condition is true", "When condition is false", "At runtime"],
        "answer": "When condition is true"
    },
    {
        "question": "What does if (x) {} evaluate?",
        "options": ["A number", "A boolean", "A string", "Any value"],
        "answer": "Any value"
    },
    {
        "question": "What happens if the condition in if (x == 5) {} is false?",
        "options": ["Executes block", "Skips block", "Throws error", "Returns null"],
        "answer": "Skips block"
    },
    {
        "question": "What is the output of if (5 > 3) { console.log('Yes'); }?",
        "options": ["'Yes'", "undefined", "true", "Error"],
        "answer": "'Yes'"
    },
    {
        "question": "Can an if statement have no curly braces for a single statement?",
        "options": ["Yes", "No", "Only in strict mode", "Only with var"],
        "answer": "Yes"
    },

    // Comparison Operators (6 questions)
    {
        "question": "What does x === 5 check?",
        "options": ["Value only", "Type only", "Value and type", "Reference"],
        "answer": "Value and type"
    },
    {
        "question": "What is 5 == '5'?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true"
    },
    {
        "question": "What does x !== 5 check?",
        "options": ["Value not equal", "Type not equal", "Value and type not equal", "Value or type not equal"],
        "answer": "Value and type not equal"
    },
    {
        "question": "What is 10 > 5?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true"
    },
    {
        "question": "What does 3 <= 3 return?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true"
    },
    {
        "question": "What is '10' != 10?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "false"
    },

    // If...Else and Else If Statements (6 questions)
    {
        "question": "What does the else statement do?",
        "options": ["Runs if true", "Runs if false", "Always runs", "Skips condition"],
        "answer": "Runs if false"
    },
    {
        "question": "What is the purpose of else if?",
        "options": ["Multiple conditions", "Error handling", "Looping", "Variable declaration"],
        "answer": "Multiple conditions"
    },
    {
        "question": "What is the output of: let x = 5; if (x > 10) { console.log('big'); } else { console.log('small'); }?",
        "options": ["'big'", "'small'", "undefined", "Error"],
        "answer": "'small'"
    },
    {
        "question": "How many else if statements can you have?",
        "options": ["1", "2", "As many as needed", "None"],
        "answer": "As many as needed"
    },
    {
        "question": "What does else require?",
        "options": ["An if statement", "A loop", "A function", "A variable"],
        "answer": "An if statement"
    },
    {
        "question": "What is the output of: let x = 0; if (x > 0) { console.log('positive'); } else if (x < 0) { console.log('negative'); } else { console.log('zero'); }?",
        "options": ["'positive'", "'negative'", "'zero'", "Error"],
        "answer": "'zero'"
    },

    // Testing Sets of Conditions (6 questions)
    {
        "question": "What does x > 5 && x < 10 test?",
        "options": ["x is between 5 and 10", "x is less than 5 or greater than 10", "x equals 5 or 10", "x is not a number"],
        "answer": "x is between 5 and 10"
    },
    {
        "question": "What is true && false?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "false"
    },
    {
        "question": "What does x === 5 || x === 10 return if x is 5?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true"
    },
    {
        "question": "What is !false?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true"
    },
    {
        "question": "What does 5 < 3 || 3 < 5 return?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true"
    },
    {
        "question": "What is the result of x >= 10 && x <= 20 if x is 15?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true"
    },

    // If Statements Nested (6 questions)
    {
        "question": "What is a nested if statement?",
        "options": ["An if inside another if", "An if after else", "Multiple else ifs", "An if with many conditions"],
        "answer": "An if inside another if"
    },
    {
        "question": "What is the output of: let x = 5; if (x > 0) { if (x < 10) { console.log('valid'); } }?",
        "options": ["'valid'", "undefined", "Error", "Nothing"],
        "answer": "'valid'"
    },
    {
        "question": "When are nested if statements used?",
        "options": ["For multiple related conditions", "To loop code", "To declare variables", "To reduce code"],
        "answer": "For multiple related conditions"
    },
    {
        "question": "What is the output of: let x = 15; if (x > 10) { if (x < 20) { console.log('range'); } } else { console.log('out'); }?",
        "options": ["'range'", "'out'", "undefined", "Error"],
        "answer": "'range'"
    },
    {
        "question": "Can a nested if have its own else?",
        "options": ["Yes", "No", "Only in strict mode", "Only with let"],
        "answer": "Yes"
    },
    {
        "question": "What is the output of: let x = 5; if (x > 0) { if (x > 10) { console.log('big'); } else { console.log('small'); } }?",
        "options": ["'big'", "'small'", "undefined", "Error"],
        "answer": "'small'"
    },

    // Arrays (6 questions)
    {
        "question": "How do you create an array?",
        "options": ["let arr = [1, 2, 3];", "let arr = (1, 2, 3);", "let arr = {1, 2, 3};", "let arr = 1, 2, 3;"],
        "answer": "let arr = [1, 2, 3];"
    },
    {
        "question": "What is [1, 2, 3].length?",
        "options": ["2", "3", "4", "undefined"],
        "answer": "3"
    },
    {
        "question": "What is [1, 2, 3][1]?",
        "options": ["1", "2", "3", "undefined"],
        "answer": "2"
    },
    {
        "question": "What does [1, 2, 3].includes(2) return?",
        "options": ["true", "false", "undefined", "Error"],
        "answer": "true"
    },
    {
        "question": "What is typeof [1, 2, 3]?",
        "options": ["'array'", "'object'", "'list'", "'collection'"],
        "answer": "'object'"
    },
    {
        "question": "What does [1, 2, 3].join('-') return?",
        "options": ["'1-2-3'", "'123'", "'1,2,3'", "Error"],
        "answer": "'1-2-3'"
    },

    // Arrays: Adding/Removing and Removing/Inserting/Extracting Elements (8 questions)
    {
        "question": "What does [1, 2, 3].push(4) do?",
        "options": ["Adds 4 to start", "Adds 4 to end", "Removes 4", "Replaces 3"],
        "answer": "Adds 4 to end"
    },
    {
        "question": "What does [1, 2, 3].pop() return?",
        "options": ["1", "2", "3", "undefined"],
        "answer": "3"
    },
    {
        "question": "What does [1, 2, 3].shift() return?",
        "options": ["1", "2", "3", "undefined"],
        "answer": "1"
    },
    {
        "question": "What does [1, 2, 3].unshift(0) do?",
        "options": ["Adds 0 to end", "Adds 0 to start", "Removes 0", "Replaces 1"],
        "answer": "Adds 0 to start"
    },
    {
        "question": "What does [1, 2, 3].slice(1, 2) return?",
        "options": ["[1]", "[2]", "[1, 2]", "[2, 3]"],
        "answer": "[2]"
    },
    {
        "question": "What does [1, 2, 3].splice(1, 1) return?",
        "options": ["[1]", "[2]", "[1, 2]", "[2, 3]"],
        "answer": "[2]"
    },
    {
        "question": "What does [1, 2, 3].splice(1, 0, 4) do?",
        "options": ["Removes 4", "Inserts 4 at index 1", "Replaces 2 with 4", "Adds 4 to end"],
        "answer": "Inserts 4 at index 1"
    },
    {
        "question": "What is [1, 2, 3].concat([4])?",
        "options": ["[1, 2, 3, 4]", "[1, 2, 3, [4]]", "[4, 1, 2, 3]", "Error"],
        "answer": "[1, 2, 3, 4]"
    },

    // For Loops (6 questions)
    {
        "question": "What is the syntax of a for loop?",
        "options": ["for (i = 0; i < 5; i++) {}", "for (i = 0, i < 5, i++) {}", "for i = 0 to 5 {}", "for (i < 5) {}"],
        "answer": "for (i = 0; i < 5; i++) {}"
    },
    {
        "question": "What does for (let i = 0; i < 3; i++) { console.log(i); } output?",
        "options": ["0, 1, 2", "1, 2, 3", "0, 1", "Error"],
        "answer": "0, 1, 2"
    },
    {
        "question": "What is the purpose of i++ in a for loop?",
        "options": ["Initializes i", "Checks condition", "Increments i", "Logs i"],
        "answer": "Increments i"
    },
    {
        "question": "What does for (let i = 1; i <= 3; i++) { console.log(i); } output?",
        "options": ["1, 2, 3", "0, 1, 2", "1, 2", "Error"],
        "answer": "1, 2, 3"
    },
    {
        "question": "How do you loop through [1, 2, 3]?",
        "options": ["for (let i = 0; i < arr.length; i++) {}", "for (let i = 1; i <= arr.length; i++) {}", "for (let i = 0; i <= arr.length; i++) {}", "for i in arr {}"],
        "answer": "for (let i = 0; i < arr.length; i++) {}"
    },
    {
        "question": "What is the output of: let sum = 0; for (let i = 1; i <= 3; i++) { sum += i; } console.log(sum);?",
        "options": ["6", "3", "9", "Error"],
        "answer": "6"
    }
]



# Set page configuration
st.set_page_config(page_title="JS Quiz Pro", page_icon="🚀", layout="wide")

def shuffle_quiz():
    """Shuffle questions and options randomly, mapping options to A, B, C, D"""
    if not quiz:
        st.error("No quiz data available. Please add questions.")
        return []
    shuffled = random.sample(quiz, len(quiz))
    for q in shuffled:
        labeled_options = list(zip(q['options'], ['A', 'B', 'C', 'D'][:len(q['options'])]))
        random.shuffle(labeled_options)
        q['display_options'] = [f"{label}: {option}" for option, label in labeled_options]
        for option, label in labeled_options:
            if option == q['answer']:
                q['labeled_answer'] = f"{label}: {option}"
                break
    return shuffled

# Custom CSS for premium UI
st.markdown("""
    <style>
    body {
        background: linear-gradient(180deg, #1a1a3b, #2c2c54);
        color: #ffffff;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    .main-container {
        background: #2c2c54;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4), inset 0 2px 5px rgba(255,255,255,0.1);
        max-width: 900px;
        margin: 30px auto;
        animation: fadeIn 0.8s ease;
    }
    .stButton>button {
        background: linear-gradient(45deg, #6b21a8, #a855f7);
        color: #ffffff;
        border: none;
        border-radius: 12px;
        padding: 15px;
        width: 100%;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
        margin: 8px 0;
        cursor: pointer;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #8b5cf6, #c084fc);
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.4);
    }
    .stButton>button:active {
        transform: translateY(0);
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .stButton>button:disabled {
        background: #4b4b6b;
        cursor: not-allowed;
        opacity: 0.7;
    }
    .question-container {
        background: #373760;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3), inset 0 2px 3px rgba(255,255,255,0.05);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .question-container:hover {
        transform: translateY(-5px);
    }
    .feedback-correct {
        color: #34c759;
        font-weight: 700;
        font-size: 20px;
        margin: 20px 0;
        animation: bounce 0.5s;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .feedback-wrong {
        color: #ff3b30;
        font-weight: 700;
        font-size: 20px;
        margin: 20px 0;
        animation: shake 0.5s;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .progress-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .title {
        font-size: 42px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 0 2px 5px rgba(0,0,0,0.3);
    }
    .caption {
        text-align: center;
        color: #b0b0d0;
        font-size: 18px;
        margin-bottom: 30px;
    }
    .sidebar .sidebar-content {
        background: #2c2c54;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .timer {
        font-size: 20px;
        color: #ff6b6b;
        font-weight: 700;
        text-align: center;
        margin-top: 15px;
        text-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-12px); }
        60% { transform: translateY(-6px); }
    }
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-6px); }
        20%, 40%, 60%, 80% { transform: translateX(6px); }
    }
    @media (max-width: 600px) {
        .main-container {
            padding: 20px;
            margin: 15px;
        }
        .stButton>button {
            font-size: 14px;
            padding: 12px;
        }
        .question-container {
            padding: 20px;
        }
        .title {
            font-size: 32px;
        }
        .caption {
            font-size: 16px;
        }
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Initialize session state
if 'quiz_data' not in st.session_state:
    st.session_state.update({
        'quiz_data': shuffle_quiz(),
        'score': 0,
        'current_q': 0,
        'start_time': datetime.now(),
        'answers': [None] * len(quiz),
        'show_results': False,
        'selected_option': None,
        'feedback': None,
        'time_left': 1800  # 30 minutes in seconds
    })

# JavaScript timer
timer_html = """
<div id="timer" class="timer">⏰ Time Left: 30:00</div>
<script>
    let timeLeft = """ + str(st.session_state.time_left) + """;
    const timerElement = document.getElementById('timer');
    function updateTimer() {
        if (timeLeft <= 0) {
            timerElement.innerHTML = '⏰ Time Up!';
            window.Streamlit.setComponentValue({time_up: true});
            return;
        }
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        timerElement.innerHTML = `⏰ Time Left: ${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        timeLeft--;
        setTimeout(updateTimer, 1000);
    }
    updateTimer();
</script>
"""
timer_component = components.html(timer_html, height=50)

# Check if time is up
timer_value = st.session_state.get('timer_value', {})
if timer_value.get('time_up', False):
    st.session_state.show_results = True

# Main UI
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1 class="title">😈 JavaScript Mastery Quiz 👿</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption"> by Haroon Rasheed 😎 Master JavaScript with Style</p>', unsafe_allow_html=True)

# Check if quiz data is valid
if not st.session_state.quiz_data:
    st.error("Quiz data is empty or invalid. Please check the quiz list.")
else:
    # Progress circle
    progress = st.session_state.current_q / len(st.session_state.quiz_data)
    progress_percentage = int(progress * 100)
    progress_svg = f"""
    <div class="progress-container">
        <svg width="100" height="100" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="45" stroke="#4b4b6b" stroke-width="10" fill="none"/>
            <circle cx="50" cy="50" r="45" stroke="#6b21a8" stroke-width="10" fill="none"
                stroke-dasharray="283" stroke-dashoffset="{283 * (1 - progress)}"
                style="transition: stroke-dashoffset 0.5s ease;"/>
            <text x="50" y="55" fill="#ffffff" font-size="20" text-anchor="middle">{progress_percentage}%</text>
        </svg>
        <div style="color: #b0b0d0; font-size: 14px; margin-top: 10px;">
            Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
        </div>
    </div>
    """
    st.markdown(progress_svg, unsafe_allow_html=True)

    # Quiz interface
    if not st.session_state.show_results:
        with st.container():
            st.markdown('<div class="question-container">', unsafe_allow_html=True)
            q = st.session_state.quiz_data[st.session_state.current_q]

            st.markdown(f"### Question {st.session_state.current_q + 1}")
            st.markdown(f"**{q['question']}**")

            # Display options as buttons
            for i, display_option in enumerate(q['display_options']):
                if st.button(display_option, key=f"q{st.session_state.current_q}opt{i}",
                            use_container_width=True, disabled=st.session_state.selected_option is not None):
                    original_option = display_option[3:]
                    is_correct = (display_option == q['labeled_answer'])
                    st.session_state.selected_option = display_option
                    st.session_state.feedback = {
                        'is_correct': is_correct,
                        'correct_answer': q['labeled_answer']
                    }
                    st.session_state.answers[st.session_state.current_q] = {
                        'question': q['question'],
                        'user_answer': display_option,
                        'correct_answer': q['labeled_answer'],
                        'is_correct': is_correct
                    }
                    if is_correct:
                        st.session_state.score += 1
                        try:
                            confetti_script = """
                            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                            <script>
                            confetti({
                                particleCount: 150,
                                spread: 80,
                                origin: { y: 0.6 },
                                colors: ['#6b21a8', '#a855f7', '#ffffff']
                            });
                            </script>
                            """
                            st.markdown(confetti_script, unsafe_allow_html=True)
                        except:
                            pass
                    st.rerun()

            # Display feedback
            if st.session_state.feedback:
                if st.session_state.feedback['is_correct']:
                    st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="feedback-wrong">❌ Wrong! Correct answer: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)

            # Navigation buttons
            col_prev, col_next = st.columns([1, 1])
            with col_prev:
                if st.button("⬅️ Previous", disabled=st.session_state.current_q == 0):
                    if st.session_state.answers[st.session_state.current_q] and st.session_state.answers[st.session_state.current_q]['is_correct']:
                        st.session_state.score -= 1
                    st.session_state.current_q -= 1
                    st.session_state.selected_option = None
                    st.session_state.feedback = None
                    st.rerun()
            with col_next:
                if st.session_state.current_q < len(quiz) - 1:
                    if st.button("➡️ Next", disabled=st.session_state.selected_option is None):
                        st.session_state.current_q += 1
                        st.session_state.selected_option = None
                        st.session_state.feedback = None
                        st.rerun()
                else:
                    if st.button("🏁 Finish", disabled=st.session_state.selected_option is None):
                        st.session_state.show_results = True
                        st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

    # Results page
    else:
        time_taken = datetime.now() - st.session_state.start_time
        accuracy = (st.session_state.score / len(quiz)) * 100

        st.markdown('<div class="question-container">', unsafe_allow_html=True)
        st.markdown(f'<h2 style="color: #34c759; text-align: center;">🏆 Final Score: {st.session_state.score}/{len(quiz)}</h2>', unsafe_allow_html=True)
        st.markdown(f"""
        <h3 style="color: #ffffff;">📊 Performance Analysis</h3>
        <div style="color: #b0b0d0; font-size: 16px;">
            - ⏱️ Time Taken: {time_taken.seconds // 60}m {time_taken.seconds % 60}s<br>
            - 🎯 Accuracy: {accuracy:.1f}%<br>
            - ✅ Correct Answers: {st.session_state.score}<br>
            - ❌ Wrong Answers: {len(quiz) - st.session_state.score}
        </div>
        """, unsafe_allow_html=True)

        # Leaderboard
        leaderboard = [
            {"name": "Alex", "score": 8, "time": 180},
            {"name": "Sam", "score": 7, "time": 200},
            {"name": "You", "score": st.session_state.score, "time": time_taken.seconds}
        ]
        leaderboard = sorted(leaderboard, key=lambda x: (-x['score'], x['time']))

        st.markdown('<h3 style="color: #ffffff;">🏅 Leaderboard</h3>', unsafe_allow_html=True)
        for i, entry in enumerate(leaderboard[:5], 1):
            st.markdown(f'<div style="color: #b0b0d0; font-size: 16px;">{i}. <b>{entry["name"]}</b>: {entry["score"]}/{len(quiz)} (Time: {entry["time"]//60}m {entry["time"]%60}s)</div>', unsafe_allow_html=True)

        # Detailed review
        with st.expander("📝 Detailed Review", expanded=True):
            for i, answer in enumerate(st.session_state.answers):
                if answer:
                    st.markdown(f'<b style="color: #ffffff;">Q{i+1}:</b> {answer["question"]}', unsafe_allow_html=True)
                    col1, col2 = st.columns(2)
                    with col1:
                        status = "✅" if answer['is_correct'] else "❌"
                        st.markdown(f'<span style="color: #b0b0d0;">{status} Your answer: {answer["user_answer"]}</span>', unsafe_allow_html=True)
                    with col2:
                        if not answer['is_correct']:
                            st.markdown(f'<span style="color: #b0b0d0;">💡 Correct answer: {answer["correct_answer"]}</span>', unsafe_allow_html=True)
                    st.markdown('<hr style="border-color: #4b4b6b;">', unsafe_allow_html=True)

        # Restart or share results
        col_restart, col_share = st.columns(2)
        with col_restart:
            if st.button("🔄 Try Again", type="primary"):
                st.session_state.clear()
                st.rerun()
        with col_share:
            if st.button("📤 Share Score"):
                share_text = f"I scored {st.session_state.score}/{len(quiz)} ({accuracy:.1f}%) on the JS Quiz Pro! 🚀 Test your JavaScript skills at [your-app-link]!"
                st.code(share_text, language="text")
                st.markdown('<div style="color: #b0b0d0; font-size: 14px;">Copy and share your achievement!</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div style="color: #ffffff; font-size: 24px; font-weight: 700;">📚 Quiz Info</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color: #b0b0d0;">Total Questions: {len(quiz)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color: #b0b0d0;">Current Score: {st.session_state.score}/{len(quiz)}</div>', unsafe_allow_html=True)
    if not st.session_state.show_results:
        st.markdown(f'<div style="color: #b0b0d0;">Timer updates above ⬆️</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="color: #b0b0d0;">Time Taken: {time_taken.seconds // 60}m {time_taken.seconds % 60}s</div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-color: #4b4b6b;">', unsafe_allow_html=True)
    st.markdown('<div style="color: #ffffff; font-size: 18px; font-weight: 600;">💡 Tips</div>', unsafe_allow_html=True)
    st.markdown('<div style="color: #b0b0d0; font-size: 14px;">- Click an option for instant feedback.<br>- Use Previous/Next to navigate.<br>- Finish to see results!</div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-color: #4b4b6b;">', unsafe_allow_html=True)
    st.markdown('<div style="color: #ffffff; font-size: 18px; font-weight: 600;">ℹ️ About</div>', unsafe_allow_html=True)
    st.markdown('<div style="color: #b0b0d0; font-size: 14px;">JS Quiz Pro is built with Streamlit to master JavaScript. Feedback: [your-contact-link]</div>', unsafe_allow_html=True)

