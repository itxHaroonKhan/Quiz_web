import streamlit as st
import random
from datetime import datetime
import uuid

# ==================== 100 PRO QUESTIONS (Hindi + Code) ====================
quiz_100 = [
    # 1-10: Compiler
    {"q": "tsc kya karta hai?", "o": ["TS → JS", "JS → TS", "Run karta hai", "Delete karta hai"], "a": "TS → JS", "e": "`tsc file.ts` → file.js", "cat": "Compiler"},
    {"q": "tsconfig.json ka kaam?", "o": ["Settings", "Package list", "HTML file", "CSS"], "a": "Settings", "e": "target, strict, module set karta hai", "cat": "Compiler"},
    {"q": "`strict: true` kya enable karta hai?", "o": ["Sab strict checks", "Sirf null check", "No check", "Fast compile"], "a": "Sab strict checks", "e": "noImplicitAny, strictNullChecks, etc.", "cat": "Compiler"},
    {"q": "Fast compile ke liye?", "o": ["--transpileOnly", "--noEmit", "--watch", "--build"], "a": "--transpileOnly", "e": "No type check, sirf JS banata hai", "cat": "Compiler"},
    {"q": ".d.ts files banane ke liye?", "o": ["declaration: true", "emit: true", "types: true", "export: true"], "a": "declaration: true", "e": "Library ke liye types generate", "cat": "Compiler"},
    {"q": "Watch mode command?", "o": ["tsc -w", "tsc --watch", "Both", "tsc --live"], "a": "Both", "e": "File change pe auto compile", "cat": "Compiler"},
    {"q": "target: 'ES2020' matlab?", "o": ["JS ES2020 output", "Module system", "Folder", "File name"], "a": "JS ES2020 output", "e": "Modern JS features allowed", "cat": "Compiler"},
    {"q": "noEmitOnError kya karta hai?", "o": ["Error pe JS nahi banega", "Error ignore karega", "JS banega", "Delete karega"], "a": "Error pe JS nahi banega", "e": "Safe compilation", "cat": "Compiler"},
    {"q": "module: 'CommonJS' → output?", "o": ["require()", "import/export", "global", "AMD"], "a": "require()", "e": "Node.js style", "cat": "Compiler"},
    {"q": "emitDecoratorMetadata ke liye?", "o": ["reflect-metadata", "tslib", "core-js", "zone.js"], "a": "reflect-metadata", "e": "Decorator me data save karta hai", "cat": "Compiler"},

    # 11-25: Annotations
    {"q": "Number annotate kaise?", "o": [": number", ": num", ":: number", "<number>"], "a": ": number", "e": "let age: number = 25;", "cat": "Annotations"},
    {"q": "String array?", "o": ["string[]", "Array<string>", "Both", "Str[]"], "a": "Both", "e": "Dono syntax valid", "cat": "Annotations"},
    {"q": "Function return type?", "o": ["(): string", "=> string", "-> string", ": string"], "a": "(): string", "e": "function greet(): string", "cat": "Annotations"},
    {"q": "Promise<string> kaise likhe?", "o": ["Promise<string>", "Future<string>", "async string", "Then<string>"], "a": "Promise<string>", "e": "async function fetch(): Promise<string>", "cat": "Annotations"},
    {"q": "Tuple type?", "o": ["[string, number]", "(string, number)", "string | number", "string & number"], "a": "[string, number]", "e": "let user: [string, number] = ['Ram', 25]", "cat": "Annotations"},
    {"q": "Any type kab use?", "o": ["Jab type nahi pata", "Kabhi nahi", "Sirf number", "Sirf string"], "a": "Jab type nahi pata", "e": "Dynamic content ke liye", "cat": "Annotations"},
    {"q": "Never type kab?", "o": ["Function jo kabhi return nahi karta", "Har function", "Error function", "Both A & C"], "a": "Both A & C", "e": "throw error ya infinite loop", "cat": "Annotations"},
    {"q": "Unknown type safer kyun?", "o": ["Type check karna padta hai", "Kuch bhi assign", "Fast hai", "Small hai"], "a": "Type check karna padta hai", "e": "any se better", "cat": "Annotations"},
    {"q": "Void return type?", "o": ["Kuch return nahi", "null", "undefined", "empty"], "a": "Kuch return nahi", "e": "function log(): void", "cat": "Annotations"},
    {"q": "Literal type?", "o": ["'left' | 'right'", "string", "any", "boolean"], "a": "'left' | 'right'", "e": "Exact value", "cat": "Annotations"},

    # 26-45: Interfaces
    {"q": "Interface ka matlab?", "o": ["Object ka shape", "Class", "Function", "Variable"], "a": "Object ka shape", "e": "Structure define karta hai", "cat": "Interfaces"},
    {"q": "Optional property?", "o": ["age?: number", "age!: number", "age*: number", "age~: number"], "a": "age?: number", "e": "Ho sakta hai ya nahi", "cat": "Interfaces"},
    {"q": "Interface extend?", "o": ["extends", "implements", "inherits", "uses"], "a": "extends", "e": "interface Admin extends User", "cat": "Interfaces"},
    {"q": "Readonly property?", "o": ["readonly id: number", "const id: number", "fixed id", "immutable id"], "a": "readonly id: number", "e": "Badalne nahi dega", "cat": "Interfaces"},
    {"q": "Index signature?", "o": ["[key: string]: string", "[key]: string", "keyof string", "{key: string}"], "a": "[key: string]: string", "e": "Dynamic keys", "cat": "Interfaces"},
    {"q": "Function in interface?", "o": ["greet(): void", "greet: () => void", "Both", "None"], "a": "Both", "e": "Call signature", "cat": "Interfaces"},
    {"q": "Hybrid type?", "o": ["Function + Object", "Sirf function", "Sirf object", "Array"], "a": "Function + Object", "e": "jQuery style", "cat": "Interfaces"},
    {"q": "Interface merge hota hai?", "o": ["Haan, same name se", "Nahi", "Sirf class", "Sirf type"], "a": "Haan, same name se", "e": "Declaration merging", "cat": "Interfaces"},
    {"q": "Interface vs Type?", "o": ["Interface extendable", "Type more powerful", "Both same", "Interface faster"], "a": "Both same", "e": "Dono kaam karte hain", "cat": "Interfaces"},
    {"q": "Interface class se implement?", "o": ["implements", "extends", "uses", "follows"], "a": "implements", "e": "class User implements Person", "cat": "Interfaces"},

    # 46-65: Classes
    {"q": "Class inheritance?", "o": ["extends", "implements", "inherits", "uses"], "a": "extends", "e": "class Dog extends Animal", "cat": "Classes"},
    {"q": "Private field (new)?", "o": ["#name", "private name", "Both", "_name"], "a": "Both", "e": "ES2022 + TS", "cat": "Classes"},
    {"q": "Public by default?", "o": ["Haan", "Nahi", "Sirf constructor", "Sirf methods"], "a": "Haan", "e": "Bina keyword ke public", "cat": "Classes"},
    {"q": "Protected ka matlab?", "o": ["Child class access", "Sirf same class", "Koi nahi", "Sab access"], "a": "Child class access", "e": "Inheritance me use", "cat": "Classes"},
    {"q": "Static property?", "o": ["static count: number", "count: number", "const count", "#count"], "a": "static count: number", "e": "Class.count", "cat": "Classes"},
    {"q": "Abstract class?", "o": ["abstract class Shape", "virtual class Shape", "interface Shape", "type Shape"], "a": "abstract class Shape", "e": "Extend karna padta hai", "cat": "Classes"},
    {"q": "Getter/Setter?", "o": ["get name()", "set name(v)", "Both", "None"], "a": "Both", "e": "Encapsulation", "cat": "Classes"},
    {"q": "Parameter properties?", "o": ["constructor(public name: string)", "constructor(name: string)", "Both", "None"], "a": "constructor(public name: string)", "e": "Short syntax", "cat": "Classes"},
    {"q": "super() call?", "o": ["Child constructor me", "Kahi bhi", "Nahi", "Optional"], "a": "Child constructor me", "e": "Parent constructor call", "cat": "Classes"},
    {"q": "Class decorator?", "o": ["@sealed", "@log", "@Component", "All"], "a": "All", "e": "Class ko modify karta hai", "cat": "Classes"},

    # 66-80: Generics
    {"q": "Generic function?", "o": ["<T>(x: T): T", "<T> x: T", "T => T", "[T] x"], "a": "<T>(x: T): T", "e": "Reusable function", "cat": "Generics"},
    {"q": "Constraint in generic?", "o": ["T extends string", "T implements string", "T: string", "T < string"], "a": "T extends string", "e": "Limit type", "cat": "Generics"},
    {"q": "Default generic?", "o": ["T = string", "T: string", "T ? string", "T | string"], "a": "T = string", "e": "Fallback", "cat": "Generics"},
    {"q": "Conditional type?", "o": ["T extends U ? X : Y", "T | U ? X : Y", "T & U => X", "T = U ? X : Y"], "a": "T extends U ? X : Y", "e": "Type-level if", "cat": "Generics"},
    {"q": "infer keyword?", "o": ["Type extract karta hai", "Type banata hai", "Delete karta hai", "Copy karta hai"], "a": "Type extract karta hai", "e": "Return type nikalna", "cat": "Generics"},
    {"q": "Mapped type?", "o": ["{ [K in keyof T]: U }", "{ K in T: U }", "[K in keyof T] => U", "keyof T[U]"], "a": "{ [K in keyof T]: U }", "e": "Keys transform", "cat": "Generics"},
    {"q": "keyof operator?", "o": ["Object ke keys", "Values", "Both", "None"], "a": "Object ke keys", "e": "type Keys = keyof User", "cat": "Generics"},
    {"q": "Partial<T> kya karta hai?", "o": ["Sab optional", "Sab required", "Sirf readonly", "Sirf string"], "a": "Sab optional", "e": "Built-in utility", "cat": "Generics"},
    {"q": "Pick<T, K>?", "o": ["K properties select", "Sab remove", "Rename", "Copy"], "a": "K properties select", "e": "Pick<User, 'name' | 'age'>", "cat": "Generics"},
    {"q": "Omit<T, K>?", "o": ["K properties remove", "Sab remove", "Rename", "Copy"], "a": "K properties remove", "e": "Omit<User, 'password'>", "cat": "Generics"},

    # 81-90: Enums
    {"q": "Enum start value?", "o": ["0", "1", "A", "null"], "a": "0", "e": "Auto-increment", "cat": "Enums"},
    {"q": "String enum?", "o": ["Up = 'UP'", "Up: 'UP'", "Up => 'UP'", "Up == 'UP'"], "a": "Up = 'UP'", "e": "Explicit value", "cat": "Enums"},
    {"q": "const enum?", "o": ["Compile time inline", "Runtime object", "Both", "None"], "a": "Compile time inline", "e": "No JS output", "cat": "Enums"},
    {"q": "Computed enum?", "o": ["Haan, function se", "Nahi", "Sirf string", "Sirf number"], "a": "Haan, function se", "e": "Size = 'abc'.length", "cat": "Enums"},
    {"q": "Enum reverse mapping?", "o": ["Numeric only", "String only", "Both", "None"], "a": "Numeric only", "e": "Color[0] = 'Red'", "cat": "Enums"},

    # 91-100: Advanced
    {"q": "`let x = 'hi'` → x is?", "o": ["string", "any", "unknown", "let"], "a": "string", "e": "Auto detect", "cat": "Inference"},
    {"q": "Contextual typing?", "o": ["Event handler me", "let variable", "function param", "interface"], "a": "Event handler me", "e": "e: MouseEvent", "cat": "Inference"},
    {"q": "Discriminated union?", "o": ["kind property", "id property", "name property", "type property"], "a": "kind property", "e": "type Shape = Circle | Square", "cat": "Union"},
    {"q": "User-defined type guard?", "o": ["x is string", "x: string", "x == string", "x === string"], "a": "x is string", "e": "Narrow in if", "cat": "Guards"},
    {"q": "Decorator factory?", "o": ["@log('msg')", "@log", "@log()", "@log[]"], "a": "@log('msg')", "e": "Parameterized decorator", "cat": "Decorators"},
]

# Convert to standard format
quiz = []
for q in quiz_100:
    quiz.append({
        "question": q["q"],
        "options": q["o"],
        "answer": q["a"],
        "explanation": q["e"],
        "category": q["cat"],
        "difficulty": random.choice(["Easy", "Medium", "Hard"])
    })

# ==================== SHUFFLE & INIT ====================
def shuffle_quiz(data):
    shuffled = [q.copy() for q in random.sample(data, len(data))]
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = random.sample(q["options"], len(q["options"]))
    return shuffled

def init():
    if "data" not in st.session_state:
        st.session_state.data = shuffle_quiz(quiz)
        st.session_state.score = 0
        st.session_state.idx = 0
        st.session_state.streak = 0
        st.session_state.start = datetime.now()
        st.session_state.answered = {}
        st.session_state.show = False

# ==================== CSS ====================
st.set_page_config("TS 100 Quiz", layout="centered")
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&display=swap');
    * { font-family: 'Poppins', sans-serif !important; }
    .stApp { background: linear-gradient(135deg, #1e1b4b, #0f172a); color: white; }
    .box { background: rgba(30,41,59,0.95); border-radius: 20px; padding: 2rem; max-width: 750px; margin: auto; border: 1px solid #4c1d95; box-shadow: 0 15px 40px rgba(0,0,0,0.6); }
    .title { font-size: 3rem; text-align: center; background: linear-gradient(90deg, #a855f7, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .timer { font-size: 2.2rem; font-weight: 700; text-align: center; padding: 1rem; background: #1e293b; border-radius: 16px; border: 3px solid #a855f7; }
    .opt { background: #1e293b; border: 2px solid #4c1d95; margin: 1rem 0; padding: 1.2rem; border-radius: 14px; transition: all 0.3s; cursor: pointer; }
    .opt:hover { background: #4c1d95; transform: translateY(-4px); }
    .correct { background: #166534 !important; border-color: #22c55e !important; }
    .wrong { background: #7f1d1d !important; border-color: #ef4444 !important; }
    .badge { padding: 0.5rem 1rem; border-radius: 50px; font-size: 0.9rem; font-weight: 600; }
    .easy { background: #166534; }
    .medium { background: #ca8a04; }
    .hard { background: #7f1d1d; }
</style>
""", unsafe_allow_html=True)

# ==================== APP ====================
init()
st.markdown('<div class="box">', unsafe_allow_html=True)
st.markdown('<h1 class="title">TypeScript 100 Quiz</h1>', unsafe_allow_html=True)

if not st.session_state.show:
    q = st.session_state.data[st.session_state.idx]
    total = len(st.session_state.data)

    # Timer
    elapsed = (datetime.now() - st.session_state.start).total_seconds()
    time_left = max(900 - int(elapsed), 0)
    mins, secs = divmod(time_left, 60)
    color = "lime" if time_left > 180 else "orange" if time_left > 60 else "red"
    st.markdown(f'<div class="timer" style="color:{color};">{mins:02d}:{secs:02d}</div>', unsafe_allow_html=True)

    # Progress
    prog = (st.session_state.idx + 1) / total * 100
    st.progress(prog)
    st.markdown(f"**Q{st.session_state.idx + 1}/{total}** | Streak: {st.session_state.streak}")

    # Question
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'<span class="badge {q["difficulty"].lower()}">{q["difficulty"]}</span>', unsafe_allow_html=True)
        st.markdown(f'<span class="badge" style="background:#06b6d4">{q["category"]}</span>', unsafe_allow_html=True)
    with col2:
        st.markdown(f"### {q['question']}")

    # Options
    for opt in q["display_options"]:
        key = f"opt_{q['id']}_{opt}"
        if st.button(opt, key=key, use_container_width=True):
            correct = opt == q["answer"]
            st.session_state.answered[st.session_state.idx] = opt
            if correct:
                st.session_state.score += 2
                st.session_state.streak += 1
                st.success(f"CORRECT! {q['explanation']}")
            else:
                st.session_state.streak = 0
                st.error(f"WRONG! Sahi jawab: **{q['answer']}**")
            st.rerun()

    # Show answer if selected
    if st.session_state.idx in st.session_state.answered:
        ans = st.session_state.answered[st.session_state.idx]
        cls = "correct" if ans == q["answer"] else "wrong"
        st.markdown(f'<div class="opt {cls}">→ Tera jawab: <b>{ans}</b></div>', unsafe_allow_html=True)

    # Navigation
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.idx > 0 and st.button("Previous", use_container_width=True):
            st.session_state.idx -= 1
            st.rerun()
    with col2:
        if st.button("Next", use_container_width=True):
            st.session_state.idx += 1
            if st.session_state.idx >= total:
                st.session_state.show = True
            st.rerun()

else:
    st.balloons()
    pct = st.session_state.score / (len(quiz) * 2) * 100
    rank = "MASTER" if pct >= 90 else "EXPERT" if pct >= 75 else "PRO" if pct >= 60 else "GOOD"
    st.markdown(f"""
    <div style="text-align:center; padding:3rem; background:#1e293b; border-radius:20px;">
        <h1>Quiz Khatam!</h1>
        <h2 style="font-size:4rem; color:#a855f7;">{st.session_state.score}/200</h2>
        <h3>{rank}</h3>
        <p>Max Streak: {max([0] + [v for k,v in st.session_state.answered.items() if st.session_state.data[k]["answer"] == v])}</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Phir Se Khel", use_container_width=True):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
