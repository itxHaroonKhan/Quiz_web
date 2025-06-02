import streamlit as st
import random
from datetime import datetime
import streamlit.components.v1 as components

quiz = [
    // For Loops (30 questions: Flags, Booleans, Array Length, Loop Interruption, Nested Loops)
    {"question": "What does this code output: let flag = false; for (let i = 0; i < 5; i++) { if (i > 3) flag = true; } console.log(flag);?", "options": ["true", "false", "undefined", "Error"], "answer": "true"},
    {"question": "What is the output of: for (let i = 0; i < 4; i++) { if (i === 2) break; console.log(i); }?", "options": ["0 1", "0 1 2", "0 1 2 3", "Error"], "answer": "0 1"},
    {"question": "What does this nested loop output: let str = ''; for (let i = 1; i <= 2; i++) { for (let j = 1; j <= 2; j++) { str += i + j + ' '; } } console.log(str);?", "options": ["'2 3 3 4 '", "'1 2 3 4 '", "'2 4 '", "Error"], "answer": "'2 3 3 4 '"},
    {"question": "What is the value of arr.length after: let arr = [1, 2]; for (let i = 0; i < arr.length; i++) { arr.push(i); }?", "options": ["2", "4", "Infinite loop", "Error"], "answer": "Infinite loop"},
    {"question": "What does this loop output: let count = 0; for (let i = 1; i <= 5; i++) { if (i % 2 === 0) continue; count += i; } console.log(count);?", "options": ["6", "9", "12", "15"], "answer": "9"},
    {"question": "What does this code output: let x = 0; for (let i = 0; i < 3; i++) { x += i; } console.log(x);?", "options": ["0", "3", "6", "Error"], "answer": "3"},
    {"question": "What is the output of: let arr = [1, 2, 3]; for (let i = 0; i < arr.length; i++) { arr[i] *= 2; } console.log(arr);?", "options": ["[2, 4, 6]", "[1, 2, 3]", "[1, 4, 9]", "Error"], "answer": "[2, 4, 6]"},
    {"question": "What does this loop do: let flag = true; for (let i = 0; i < 5; i++) { if (i === 4) flag = false; } console.log(flag);?", "options": ["true", "false", "undefined", "Error"], "answer": "false"},
    {"question": "What is the output of: for (let i = 5; i > 0; i--) { console.log(i); }?", "options": ["5 4 3 2 1", "1 2 3 4 5", "0 1 2 3 4", "Error"], "answer": "5 4 3 2 1"},
    {"question": "What does this nested loop output: let sum = 0; for (let i = 1; i <= 2; i++) { for (let j = 1; j <= 3; j++) { sum += j; } } console.log(sum);?", "options": ["6", "12", "9", "Error"], "answer": "12"},
    {"question": "What happens in: let arr = [1, 2, 3]; for (let i = 0; i < arr.length; i++) { arr.push(4); }?", "options": ["arr becomes [1, 2, 3, 4]", "Infinite loop", "arr becomes [1, 2, 3, 4, 4, 4]", "Error"], "answer": "Infinite loop"},
    {"question": "What does this code output: let x = 0; for (let i = 0; i <= 4; i++) { if (i % 2 === 0) x += i; } console.log(x);?", "options": ["6", "4", "8", "Error"], "answer": "6"},
    {"question": "What is the output of: let flag = false; for (let i = 1; i < 6; i++) { if (i === 3) { flag = true; break; } } console.log(flag);?", "options": ["true", "false", "undefined", "Error"], "answer": "true"},
    {"question": "What does this loop output: let str = ''; for (let i = 0; i < 3; i++) { str += i + ' '; } console.log(str);?", "options": ["'0 1 2 '", "'1 2 3 '", "'0 1 '", "Error"], "answer": "'0 1 2 '"},
    {"question": "What is the output of: let arr = [1, 2, 3]; for (let i = arr.length - 1; i >= 0; i--) { console.log(arr[i]); }?", "options": ["3 2 1", "1 2 3", "2 3 1", "Error"], "answer": "3 2 1"},
    {"question": "What does this nested loop output: let arr = []; for (let i = 1; i <= 2; i++) { for (let j = 1; j <= 2; j++) { arr.push(i * j); } } console.log(arr);?", "options": ["[1, 2, 2, 4]", "[1, 2, 3, 4]", "[1, 4]", "Error"], "answer": "[1, 2, 2, 4]"},
    {"question": "What is the output of: let count = 0; for (let i = 0; i < 5; i++) { if (i === 3) continue; count++; } console.log(count);?", "options": ["4", "5", "3", "Error"], "answer": "4"},
    {"question": "What does this code output: let flag = true; for (let i = 0; i < 4; i++) { if (i === 2) flag = false; } console.log(flag);?", "options": ["true", "false", "undefined", "Error"], "answer": "false"},
    {"question": "What is the output of: let arr = [1, 2, 3]; for (let i = 0; i < arr.length; i++) { arr[i] += i; } console.log(arr);?", "options": ["[1, 3, 5]", "[1, 2, 3]", "[0, 2, 4]", "Error"], "answer": "[1, 3, 5]"},
    {"question": "What does this loop output: for (let i = 0; i < 5; i++) { if (i === 4) console.log('end'); }?", "options": ["'end'", "undefined", "Nothing", "Error"], "answer": "'end'"},
    {"question": "What is the output of: let x = 0; for (let i = 1; i <= 3; i++) { x += i * 2; } console.log(x);?", "options": ["6", "12", "9", "Error"], "answer": "12"},
    {"question": "What does this nested loop output: let str = ''; for (let i = 1; i <= 2; i++) { for (let j = 1; j <= 2; j++) { str += j; } } console.log(str);?", "options": ["'1122'", "'1234'", "'11'", "Error"], "answer": "'1122'"},
    {"question": "What is arr.length after: let arr = [1, 2]; for (let i = 0; i < 3; i++) { arr.push(i); } console.log(arr.length);?", "options": ["2", "5", "3", "Error"], "answer": "5"},
    {"question": "What does this loop output: let flag = false; for (let i = 0; i < 5; i++) { if (i > 2) flag = true; } console.log(flag);?", "options": ["true", "false", "undefined", "Error"], "answer": "true"},
    {"question": "What is the output of: for (let i = 0; i < 3; i++) { console.log(i * 2); }?", "options": ["0 2 4", "0 1 2", "2 4 6", "Error"], "answer": "0 2 4"},
    {"question": "What does this code output: let arr = [1, 2, 3]; for (let i = 0; i < arr.length; i++) { arr[i] = arr[i] ** 2; } console.log(arr);?", "options": ["[1, 4, 9]", "[1, 2, 3]", "[2, 4, 6]", "Error"], "answer": "[1, 4, 9]"},
    {"question": "What is the output of: let count = 0; for (let i = 0; i < 5; i++) { if (i % 2 !== 0) count++; } console.log(count);?", "options": ["2", "3", "4", "Error"], "answer": "3"},
    {"question": "What does this nested loop output: let sum = 0; for (let i = 1; i <= 3; i++) { for (let j = 1; j <= i; j++) { sum += j; } } console.log(sum);?", "options": ["6", "9", "12", "Error"], "answer": "9"},
    {"question": "What is the output of: let flag = true; for (let i = 0; i < 3; i++) { if (i === 1) { flag = false; break; } } console.log(flag);?", "options": ["true", "false", "undefined", "Error"], "answer": "false"},
    {"question": "What does this loop output: let str = ''; for (let i = 1; i <= 3; i++) { str += i + ' '; } console.log(str);?", "options": ["'1 2 3 '", "'1 2 '", "'2 3 4 '", "Error"], "answer": "'1 2 3 '"},

    // Strings (30 questions: Changing Case, Measuring Length, Extracting Parts, Finding Segments, Finding Character, Replacing Characters)
    {"question": "What does 'JavaScript'.toUpperCase() return?", "options": ["'JAVASCRIPT'", "'javascript'", "'JavaScript'", "Error"], "answer": "'JAVASCRIPT'"},
    {"question": "What is 'Hello World'.length?", "options": ["10", "11", "12", "Error"], "answer": "11"},
    {"question": "What does 'Programming'.slice(0, 4) return?", "options": ["'Prog'", "'gram'", "'Progr'", "Error"], "answer": "'Prog'"},
    {"question": "What is 'Test Case'.indexOf('Case')?", "options": ["4", "5", "6", "Error"], "answer": "5"},
    {"question": "What does 'hello'.charAt(1) return?", "options": ["'h'", "'e'", "'l'", "Error"], "answer": "'e'"},
    {"question": "What does 'abcde'.replace('cd', 'xy') return?", "options": ["'abxye'", "'abcxy'", "'axyde'", "Error"], "answer": "'abxye'"},
    {"question": "What is 'TeSt'.toLowerCase()?", "options": ["'test'", "'TeSt'", "'TEST'", "Error"], "answer": "'test'"},
    {"question": "What does 'JavaScript'.substring(4, 7) return?", "options": ["'Scr'", "'ipt'", "'Scri'", "Error"], "answer": "'Scr'"},
    {"question": "What is 'Hello World'.indexOf('o')?", "options": ["4", "5", "6", "Error"], "answer": "4"},
    {"question": "What does 'test'[2] return?", "options": ["'s'", "'t'", "'e'", "Error"], "answer": "'s'"},
    {"question": "What does 'abc'.replace('b', 'x') return?", "options": ["'axc'", "'abc'", "'bxc'", "Error"], "answer": "'axc'"},
    {"question": "What is 'CODE'.toLowerCase().length?", "options": ["4", "5", "6", "Error"], "answer": "4"},
    {"question": "What does 'JavaScript'.slice(-3) return?", "options": ["'ipt'", "'rip'", "'ava'", "Error"], "answer": "'ipt'"},
    {"question": "What is 'Hello World'.indexOf('z')?", "options": ["-1", "0", "10", "Error"], "answer": "-1"},
    {"question": "What does 'xyz'.charAt(5) return?", "options": ["'z'", "''", "undefined", "Error"], "answer": "''"},
    {"question": "What does 'hello'.replace('l', 'x') return?", "options": ["'hexlo'", "'hxllo'", "'hello'", "Error"], "answer": "'hexlo'"},
    {"question": "What is 'JavaScript'.toUpperCase().slice(0, 4)?", "options": ["'JAVA'", "'java'", "'JAVAS'", "Error"], "answer": "'JAVA'"},
    {"question": "What is 'Test Case'.length?", "options": ["8", "9", "10", "Error"], "answer": "9"},
    {"question": "What does 'Programming'.substring(2, 5) return?", "options": ["'ogr'", "'gra'", "'rog'", "Error"], "answer": "'ogr'"},
    {"question": "What is 'JavaScript'.indexOf('Script')?", "options": ["4", "5", "6", "Error"], "answer": "4"},
    {"question": "What does 'test'[0] return?", "options": ["'t'", "'e'", "'s'", "Error"], "answer": "'t'"},
    {"question": "What does 'abcde'.replace('e', 'z') return?", "options": ["'abcdz'", "'abcde'", "'zbcde'", "Error"], "answer": "'abcdz'"},
    {"question": "What is 'HELLO'.toLowerCase()?", "options": ["'hello'", "'HELLO'", "'Hello'", "Error"], "answer": "'hello'"},
    {"question": "What does 'JavaScript'.slice(2, -2) return?", "options": ["'vaScri'", "'vaSc'", "'Java'", "Error"], "answer": "'vaScri'"},
    {"question": "What is 'Hello World'.indexOf('World', 7)?", "options": ["6", "7", "-1", "Error"], "answer": "-1"},
    {"question": "What does 'code'.charAt(2) return?", "options": ["'d'", "'e'", "'o'", "Error"], "answer": "'d'"},
    {"question": "What does 'test case'.replace('case', 'example') return?", "options": ["'test example'", "'example case'", "'testcase'", "Error"], "answer": "'test example'"},
    {"question": "What is 'JavaScript'.toLowerCase().length?", "options": ["9", "10", "11", "Error"], "answer": "10"},
    {"question": "What does 'Hello'.slice(1, 4) return?", "options": ["'ell'", "'Hel'", "'llo'", "Error"], "answer": "'ell'"},
    {"question": "What is 'Programming'.indexOf('m')?", "options": ["3", "4", "5", "Error"], "answer": "3"},

    // Numbers (30 questions: Rounding, Random Numbers, Converting Strings to Numbers, Controlling Decimal Length)
    {"question": "What does Math.round(4.7) return?", "options": ["4", "5", "4.7", "Error"], "answer": "5"},
    {"question": "What is the range of Math.random()?", "options": ["0 to 1 (inclusive)", "0 to 1 (exclusive)", "0 to 100", "1 to 100"], "answer": "0 to 1 (exclusive)"},
    {"question": "What does parseInt('15.9') return?", "options": ["15", "16", "15.9", "Error"], "answer": "15"},
    {"question": "What does Number('12.345').toFixed(2) return?", "options": ["'12.34'", "'12.35'", "12.34", "Error"], "answer": "'12.34'"},
    {"question": "What does Math.floor(Math.random() * 10) return?", "options": ["0 to 9", "0 to 10", "1 to 9", "1 to 10"], "answer": "0 to 9"},
    {"question": "What does Math.ceil(3.1) return?", "options": ["3", "4", "3.1", "Error"], "answer": "4"},
    {"question": "What is parseFloat('7.89')?", "options": ["7", "7.89", "'7.89'", "Error"], "answer": "7.89"},
    {"question": "What does Number('123abc') return?", "options": ["123", "NaN", "'123abc'", "Error"], "answer": "NaN"},
    {"question": "What does (5.6789).toFixed(1) return?", "options": ["'5.6'", "'5.7'", "5.7", "Error"], "answer": "'5.7'"},
    {"question": "What does Math.floor(9.9) return?", "options": ["9", "10", "9.9", "Error"], "answer": "9"},
    {"question": "What is Math.random() * 5 likely to produce?", "options": ["0 to 4.999...", "0 to 5", "1 to 5", "Error"], "answer": "0 to 4.999..."},
    {"question": "What does parseInt('10px') return?", "options": ["10", "NaN", "'10px'", "Error"], "answer": "10"},
    {"question": "What does (3.14159).toFixed(3) return?", "options": ["'3.141'", "'3.142'", "3.141", "Error"], "answer": "'3.142'"},
    {"question": "What does Math.round(2.5) return?", "options": ["2", "3", "2.5", "Error"], "answer": "3"},
    {"question": "What does Math.floor(Math.random() * 3 + 1) return?", "options": ["0 to 2", "1 to 3", "0 to 3", "1 to 4"], "answer": "1 to 3"},
    {"question": "What is parseFloat('12.34.56')?", "options": ["12.34", "12.3456", "NaN", "Error"], "answer": "12.34"},
    {"question": "What does Number('') return?", "options": ["0", "NaN", "''", "Error"], "answer": "0"},
    {"question": "What does (10.555).toFixed(0) return?", "options": ["'10'", "'11'", "10", "Error"], "answer": "'11'"},
    {"question": "What does Math.ceil(7.01) return?", "options": ["7", "8", "7.01", "Error"], "answer": "8"},
    {"question": "What is parseInt('abc')?", "options": ["0", "NaN", "'abc'", "Error"], "answer": "NaN"},
    {"question": "What does Math.random() * 100 return?", "options": ["0 to 99.999...", "0 to 100", "1 to 100", "Error"], "answer": "0 to 99.999..."},
    {"question": "What does (8.7654).toFixed(2) return?", "options": ["'8.76'", "'8.77'", "8.76", "Error"], "answer": "'8.77'"},
    {"question": "What does Math.round(1.4) return?", "options": ["1", "2", "1.4", "Error"], "answer": "1"},
    {"question": "What does Math.floor(Math.random() * 4) return?", "options": ["0 to 3", "0 to 4", "1 to 3", "1 to 4"], "answer": "0 to 3"},
    {"question": "What is parseFloat('0.009')?", "options": ["0.009", "0.01", "'0.009'", "Error"], "answer": "0.009"},
    {"question": "What does Number('42') return?", "options": ["42", "'42'", "NaN", "Error"], "answer": "42"},
    {"question": "What does (6.789).toFixed(1) return?", "options": ["'6.7'", "'6.8'", "6.8", "Error"], "answer": "'6.8'"},
    {"question": "What does Math.ceil(0.1) return?", "options": ["0", "1", "0.1", "Error"], "answer": "1"},
    {"question": "What is parseInt('-5.7')?", "options": ["-5", "-6", "NaN", "Error"], "answer": "-5"},
    {"question": "What does Math.random() * 2 + 1 return?", "options": ["0 to 2", "1 to 2.999...", "1 to 3", "Error"], "answer": "1 to 2.999..."},

    // Array Methods (15 questions: Map, Filter, Reduce)
    {"question": "What does [1, 2, 3].map(x => x + 1) return?", "options": ["[2, 3, 4]", "[1, 2, 3]", "[1, 2, 4]", "Error"], "answer": "[2, 3, 4]"},
    {"question": "What does [2, 4, 6].filter(x => x > 3) return?", "options": ["[2, 4]", "[4, 6]", "[6]", "Error"], "answer": "[4, 6]"},
    {"question": "What does [1, 2, 3].reduce((a, b) => a * b, 1) return?", "options": ["6", "12", "1", "Error"], "answer": "6"},
    {"question": "What does ['a', 'b', 'c'].map(x => x.toUpperCase()) return?", "options": ["['A', 'B', 'C']", "['a', 'b', 'c']", "['A', 'b', 'c']", "Error"], "answer": "['A', 'B', 'C']"},
    {"question": "What does [1, 3, 5].filter(x => x % 2 === 0) return?", "options": ["[1, 3, 5]", "[]", "[3, 5]", "Error"], "answer": "[]"},
    {"question": "What does [2, 4, 6].reduce((a, b) => a + b) return?", "options": ["12", "24", "6", "Error"], "answer": "12"},
    {"question": "What does [0, 1, 2].map(x => x * x) return?", "options": ["[0, 1, 4]", "[0, 1, 2]", "[0, 2, 4]", "Error"], "answer": "[0, 1, 4]"},
    {"question": "What does [10, 20, 30].filter(x => x >= 20) return?", "options": ["[10, 20]", "[20, 30]", "[30]", "Error"], "answer": "[20, 30]"},
    {"question": "What does [1, 2, 3].reduce((a, b) => a - b, 0) return?", "options": ["-6", "6", "0", "Error"], "answer": "-6"},
    {"question": "What does ['x', 'y'].map(x => x + 'z') return?", "options": ["['xz', 'yz']", "['x', 'y']", "['xyz']", "Error"], "answer": "['xz', 'yz']"},
    {"question": "What does [1, 2, 3, 4].filter(x => x > 2) return?", "options": ["[1, 2]", "[3, 4]", "[2, 3, 4]", "Error"], "answer": "[3, 4]"},
    {"question": "What does [5, 5, 5].reduce((a, b) => a + b, 0) return?", "options": ["15", "25", "5", "Error"], "answer": "15"},
    {"question": "What does [1, 2, 3].map(x => x ** 2) return?", "options": ["[1, 4, 9]", "[1, 2, 3]", "[2, 4, 6]", "Error"], "answer": "[1, 4, 9]"},
    {"question": "What does [0, 1, 2, 3].filter(x => x % 2 === 1) return?", "options": ["[0, 2]", "[1, 3]", "[0, 1, 2, 3]", "Error"], "answer": "[1, 3]"},
    {"question": "What does [1, 2].reduce((a, b) => a * b) return?", "options": ["2", "3", "1", "Error"], "answer": "2"},

    // Basic Error Handling (15 questions)
    {"question": "What does this code output: try { let x = y; } catch (e) { console.log(e.name); }?", "options": ["'ReferenceError'", "'TypeError'", "'SyntaxError'", "Error"], "answer": "'ReferenceError'"},
    {"question": "What does try { throw new Error('Test'); } catch (e) { console.log(e.message); } output?", "options": ["'Test'", "'Error'", "undefined", "Error"], "answer": "'Test'"},
    {"question": "What happens in: try { console.log(undefinedVar); } catch (e) { console.log('Caught'); }?", "options": ["'Caught'", "undefined", "Error", "Nothing"], "answer": "'Caught'"},
    {"question": "What does try { parseInt('abc'); } catch (e) { console.log(e.name); } output?", "options": ["'TypeError'", "'ReferenceError'", "'SyntaxError'", "Nothing"], "answer": "Nothing"},
    {"question": "What does try { throw 'Error'; } catch (e) { console.log(typeof e); } output?", "options": ["'string'", "'object'", "'error'", "Error"], "answer": "'string'"},
    {"question": "What happens in: try { let x = 1 / 0; } catch (e) { console.log('Error'); }?", "options": ["'Error'", "Infinity", "Nothing", "Error"], "answer": "Nothing"},
    {"question": "What does try { JSON.parse('invalid'); } catch (e) { console.log(e.name); } output?", "options": ["'SyntaxError'", "'TypeError'", "'ReferenceError'", "Error"], "answer": "'SyntaxError'"},
    {"question": "What does try { throw new Error('Fail'); } catch (e) { console.log(e.message); } output?", "options": ["'Fail'", "'Error'", "undefined", "Error"], "answer": "'Fail'"},
    {"question": "What happens in: try { null.toString(); } catch (e) { console.log(e.name); }?", "options": ["'TypeError'", "'ReferenceError'", "'SyntaxError'", "Nothing"], "answer": "'TypeError'"},
    {"question": "What does try { let x = 1; x(); } catch (e) { console.log(e.name); } output?", "options": ["'TypeError'", "'ReferenceError'", "'SyntaxError'", "Error"], "answer": "'TypeError'"},
    {"question": "What does try { throw new Error('Stop'); } catch (e) { console.log(e.message); } output?", "options": ["'Stop'", "'Error'", "undefined", "Error"], "answer": "'Stop'"},
    {"question": "What happens in: try { let arr = []; arr[0](); } catch (e) { console.log(e.name); }?", "options": ["'TypeError'", "'ReferenceError'", "'SyntaxError'", "Nothing"], "answer": "'TypeError'"},
    {"question": "What does try { eval('let 1x = 1;'); } catch (e) { console.log(e.name); } output?", "options": ["'SyntaxError'", "'TypeError'", "'ReferenceError'", "Error"], "answer": "'SyntaxError'"},
    {"question": "What does try { throw 'Custom'; } catch (e) { console.log(e); } output?", "options": ["'Custom'", "'Error'", "undefined", "Error"], "answer": "'Custom'"},
    {"question": "What happens in: try { let x; x.a; } catch (e) { console.log(e.name); }?", "options": ["'TypeError'", "'ReferenceError'", "'SyntaxError'", "Nothing"], "answer": "'TypeError'"}
]
st.set_page_config(page_title="JS Quiz Pro", page_icon="🚀", layout="wide")

def shuffle_quiz():
    shuffled = random.sample(quiz, len(quiz))
    for q in shuffled:
        labeled_options = list(zip(q['options'], ['A', 'B', 'C', 'D']))
        random.shuffle(labeled_options)
        q['display_options'] = [f"{label}: {option}" for option, label in labeled_options]
        for option, label in labeled_options:
            if option == q['answer']:
                q['labeled_answer'] = f"{label}: {option}"
                break
    return shuffled

st.markdown("""
    <style>
    body {
        background: linear-gradient(180deg, #1a1a3b, #2c2c54);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    .main-container {
        background: #2c2c54;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        max-width: 900px;
        margin: 30px auto;
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
        margin: 8px 0;
        cursor: pointer;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #8b5cf6, #c084fc);
        transform: translateY(-3px);
    }
    .question-container {
        background: #373760;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    .feedback-correct {
        color: #34c759;
        font-weight: 700;
        font-size: 20px;
        margin: 20px 0;
    }
    .feedback-wrong {
        color: #ff3b30;
        font-weight: 700;
        font-size: 20px;
        margin: 20px 0;
    }
    .progress-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .title {
        font-size: 42px;
        text-align: center;
        margin-bottom: 10px;
    }
    .caption {
        text-align: center;
        color: #b0b0d0;
        font-size: 18px;
        margin-bottom: 30px;
    }
    .timer {
        font-size: 15px;
        color: #ff6b6b;
        font-weight: 700;
        text-align: center;
        margin-top: 15px;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

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
        'time_left': 300
    })

timer_html = f"""
<div id="timer" class="timer">⏰ Time Left: {st.session_state.time_left//60:02d}:{st.session_state.time_left%60:02d}</div>
<script>
    let timeLeft = {st.session_state.time_left};
    const timerElement = document.getElementById('timer');
    function updateTimer() {{
        if (timeLeft <= 0) {{
            timerElement.innerHTML = '⏰ Time Up!';
            window.Streamlit.setComponentValue({{time_up: true}});
            return;
        }}
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        timerElement.innerHTML = `⏰ Time Left: ${{'${{minutes}}'.padStart(2, '0')}}:${{'${{seconds}}'.padStart(2, '0')}}`;
        timeLeft--;
        setTimeout(updateTimer, 1000);
    }}
    updateTimer();
</script>
"""
components.html(timer_html, height=50)

if st.session_state.get('timer_value', {}).get('time_up', False):
    st.session_state.show_results = True

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1 class="title">😈 JavaScript Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Test Your JavaScript Knowledge</p>', unsafe_allow_html=True)

if not st.session_state.quiz_data:
    st.error("Quiz data is empty")
else:
    progress = st.session_state.current_q / len(st.session_state.quiz_data)
    progress_percentage = int(progress * 100)
    progress_svg = f"""
    <div class="progress-container">
        <svg width="100" height="100" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="45" stroke="#4b4b6b" stroke-width="10" fill="none"/>
            <circle cx="50" cy="50" r="45" stroke="#6b21a8" stroke-width="10" fill="none"
                stroke-dasharray="283" stroke-dashoffset="{283 * (1 - progress)}"/>
            <text x="50" y="55" fill="#ffffff" font-size="20" text-anchor="middle">{progress_percentage}%</text>
        </svg>
        <div style="color: #b0b0d0; font-size: 14px; margin-top: 10px;">
            Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
        </div>
    </div>
    """
    st.markdown(progress_svg, unsafe_allow_html=True)

    if not st.session_state.show_results:
        with st.container():
            st.markdown('<div class="question-container">', unsafe_allow_html=True)
            q = st.session_state.quiz_data[st.session_state.current_q]
            st.markdown(f"### Question {st.session_state.current_q + 1}")
            st.markdown(f"**{q['question']}")

            for i, option in enumerate(q['display_options']):
                if st.button(option, key=f"q{i}", use_container_width=True, disabled=st.session_state.selected_option is not None):
                    original_option = option[3:]
                    is_correct = option == q['labeled_answer']
                    st.session_state.selected_option = option
                    st.session_state.feedback = {'is_correct': is_correct, 'correct_answer': q['labeled_answer']}
                    st.session_state.answers[st.session_state.current_q] = {
                        'question': q['question'], 'user_answer': option, 'correct_answer': q['labeled_answer'], 'is_correct': is_correct
                    }
                    if is_correct:
                        st.session_state.score += 1
                    st.rerun()

            if st.session_state.feedback:
                if st.session_state.feedback['is_correct']:
                    st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)

            col_prev, col_next = st.columns([1, 1])
            with col_prev:
                if st.button("⬅ Previous", disabled=st.session_state.current_q == 0):
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

    else:
        time_taken = datetime.now() - st.session_state.start_time
        accuracy = (st.session_state.score / len(quiz)) * 100
        st.markdown('<div class="question-container">', unsafe_allow_html=True)
        st.markdown(f'<h2 style="color: #34c759; text-align: center;">🏆 Score: {st.session_state.score}/{len(quiz)}</h2>', unsafe_allow_html=True)
        st.markdown(f"""
        <h3>📊 Results</h3>
        <div style="color: #b0b0d0; font-size: 16px;">
            - ⏱️ Time: {time_taken.seconds // 60}m {time_taken.seconds % 60}s<br>
            - 🎯 Accuracy: {accuracy:.1f}%<br>
            - ✅ Correct: {st.session_state.score}<br>
            - ❌ Wrong: {len(quiz) - st.session_state.score}
        </div>
        """, unsafe_allow_html=True)

        leaderboard = [
            {"name": "Alex", "score": 8, "time": 180},
            {"name": "Sam", "score": 7, "time": 200},
            {"name": "You", "score": st.session_state.score, "time": time_taken.seconds}
        ]
        leaderboard.sort(key=lambda x: (-x['score'], x['time']))
        st.markdown('<h3>🏅 Leaderboard</h3>', unsafe_allow_html=True)
        for i, entry in enumerate(leaderboard[:5], 1):
            st.markdown(f'<div style="color: #b0b0d0;">{i}. <b>{entry["name"]}</b>: {entry["score"]}/{len(quiz)} (Time: {entry["time"]//60}m {entry["time"]%60}s)</div>', unsafe_allow_html=True)

        with st.expander("📝 Review", expanded=True):
            for i, answer in enumerate(st.session_state.answers):
                if answer:
                    st.markdown(f'<b style="color: #ffffff;">Q{i+1}:</b> {answer["question"]}', unsafe_allow_html=True)
                    col1, col2 = st.columns(2)
                    with col1:
                        status = "✅" if answer['is_correct'] else "❌"
                        st.markdown(f'<span style="color: #b0b0d0;">{status} Your: {answer["user_answer"]}</span>', unsafe_allow_html=True)
                    with col2:
                        if not answer['is_correct']:
                            st.markdown(f'<span style="color: #b0b0d0;">Correct: {answer["correct_answer"]}</span>', unsafe_allow_html=True)
                    st.markdown('<hr style="border-color: #4b4b6b;">', unsafe_allow_html=True)

        col_restart, col_share = st.columns(2)
        with col_restart:
            if st.button("🔄 Try Again", type="primary"):
                st.session_state.clear()
                st.rerun()
        with col_share:
            if st.button("📤 Share Score"):
                share_text = f"Scored {st.session_state.score}/{len(quiz)} ({accuracy:.1f}%) on JS Quiz Pro!"
                st.code(share_text, language="text")

        st.markdown('</div>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div style="color: #ffffff; font-size: 24px;">📚 Quiz Info</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color: #b0b0d0;">Questions: {len(quiz)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color: #b0b0d0;">Score: {st.session_state.score}/{len(quiz)}</div>', unsafe_allow_html=True)
    if not st.session_state.show_results:
        st.markdown(f'<div style="color: #b0b0d0;">Timer above ⬆️</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="color: #b0b0d0;">Time: {time_taken.seconds // 60}m {time_taken.seconds % 60}s</div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-color: #4b4b6b;">', unsafe_allow_html=True)
    st.markdown('<div style="color: #ffffff; font-size: 18px;">ℹ️ About</div>', unsafe_allow_html=True)
    st.markdown('<div style="color: #b0b0d0; font-size: 14px;">JS Quiz Pro tests JavaScript skills.</div>', unsafe_allow_html=True)
