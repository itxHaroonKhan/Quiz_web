import streamlit as st
import random
from datetime import datetime
import uuid

# === 100 QUESTÕES TYPESCRIPT ===
quiz = [
    # 1-10: TS Compiler
    {"question": "What does `tsc` do?", "options": ["Compiles TS to JS", "Runs TS", "Bundles code", "Deletes files"], "answer": "Compiles TS to JS", "difficulty": "Easy", "explanation": "`tsc file.ts` → file.js", "category": "Compiler"},
    {"question": "What is the purpose of `tsconfig.json`?", "options": ["Compiler settings", "Package list", "HTML file", "CSS file"], "answer": "Compiler settings", "difficulty": "Easy", "explanation": "Controls target, module, strict mode, etc.", "category": "Compiler"},
    {"question": "What does `strict: true` enable?", "options": ["All strict checks", "Only null checks", "No checks", "Faster compile"], "answer": "All strict checks", "difficulty": "Medium", "explanation": "noImplicitAny, strictNullChecks, etc.", "category": "Compiler"},
    {"question": "Which flag enables fast compile without type checking?", "options": ["--transpileOnly", "--noEmit", "--watch", "--build"], "answer": "--transpileOnly", "difficulty": "Medium", "explanation": "Uses esbuild/swc for speed", "category": "Compiler"},
    {"question": "How to generate `.d.ts` declaration files?", "options": ["declaration: true", "emit: true", "types: true", "export: true"], "answer": "declaration: true", "difficulty": "Medium", "explanation": "For publishing libraries", "category": "Compiler"},
    {"question": "Command for auto-recompile on save?", "options": ["tsc -w", "tsc --watch", "Both", "tsc --live"], "answer": "Both", "difficulty": "Easy", "explanation": "Watch mode", "category": "Compiler"},
    {"question": "What does `target: 'ES2020'` mean?", "options": ["Output ES2020 JS", "Module system", "Output folder", "File name"], "answer": "Output ES2020 JS", "difficulty": "Easy", "explanation": "Allows modern JS features", "category": "Compiler"},
    {"question": "What does `noEmitOnError` do?", "options": ["No JS if error", "Ignores errors", "Always emits JS", "Deletes files"], "answer": "No JS if error", "difficulty": "Medium", "explanation": "Safer builds", "category": "Compiler"},
    {"question": "What does `module: 'CommonJS'` output?", "options": ["require()", "import/export", "global variables", "AMD"], "answer": "require()", "difficulty": "Medium", "explanation": "Node.js style modules", "category": "Compiler"},
    {"question": "Which package enables decorator metadata?", "options": ["reflect-metadata", "tslib", "core-js", "zone.js"], "answer": "reflect-metadata", "difficulty": "Hard", "explanation": "Stores metadata at runtime", "category": "Compiler"},
    # 11-25: Type Annotations
    {"question": "How to annotate a number?", "options": [": number", ": num", ":: number", "<number>"], "answer": ": number", "difficulty": "Easy", "explanation": "let age: number = 25;", "category": "Annotations"},
    {"question": "How to type an array of strings?", "options": ["string[]", "Array<string>", "Both", "Str[]"], "answer": "Both", "difficulty": "Easy", "explanation": "Both syntaxes are valid", "category": "Annotations"},
    {"question": "How to specify function return type?", "options": ["(): string", "=> string", "-> string", ": string"], "answer": "(): string", "difficulty": "Easy", "explanation": "function greet(): string", "category": "Annotations"},
    {"question": "How to type a Promise<string>?", "options": ["Promise<string>", "Future<string>", "async string", "Thenable<string>"], "answer": "Promise<string>", "difficulty": "Medium", "explanation": "async function fetch(): Promise<string>", "category": "Annotations"},
    {"question": "How to define a tuple?", "options": ["[string, number]", "(string, number)", "string | number", "string & number"], "answer": "[string, number]", "difficulty": "Medium", "explanation": "let user: [string, number] = ['Ram', 25]", "category": "Annotations"},
    {"question": "When should you use `any`?", "options": ["When type is unknown", "Never", "Only for numbers", "Only for strings"], "answer": "When type is unknown", "difficulty": "Easy", "explanation": "For dynamic or legacy code", "category": "Annotations"},
    {"question": "`never` type is used for?", "options": ["Functions that never return", "All functions", "Error functions only", "Both A & C"], "answer": "Both A & C", "difficulty": "Hard", "explanation": "throw error or infinite loop", "category": "Annotations"},
    {"question": "Why is `unknown` safer than `any`?", "options": ["Requires type checking", "Allows anything", "Faster", "Smaller"], "answer": "Requires type checking", "difficulty": "Medium", "explanation": "You must narrow before use", "category": "Annotations"},
    {"question": "What does `void` return type mean?", "options": ["Returns nothing", "Returns null", "Returns undefined", "Empty object"], "answer": "Returns nothing", "difficulty": "Easy", "explanation": "function log(): void", "category": "Annotations"},
    {"question": "What is a literal type?", "options": ["'left' | 'right'", "string", "any", "boolean"], "answer": "'left' | 'right'", "difficulty": "Medium", "explanation": "Exact string/number values", "category": "Annotations"},
    # 26-45: Interfaces
    {"question": "What does an interface define?", "options": ["Object shape", "Class behavior", "Function signature", "Variable type"], "answer": "Object shape", "difficulty": "Easy", "explanation": "Structure of an object", "category": "Interfaces"},
    {"question": "How to make a property optional?", "options": ["age?: number", "age!: number", "age*: number", "age~: number"], "answer": "age?: number", "difficulty": "Easy", "explanation": "May or may not exist", "category": "Interfaces"},
    {"question": "How to extend an interface?", "options": ["extends", "implements", "inherits", "uses"], "answer": "extends", "difficulty": "Easy", "explanation": "interface Admin extends User", "category": "Interfaces"},
    {"question": "How to make a property readonly?", "options": ["readonly id: number", "const id: number", "fixed id", "immutable id"], "answer": "readonly id: number", "difficulty": "Easy", "explanation": "Cannot be reassigned", "category": "Interfaces"},
    {"question": "What is an index signature?", "options": ["[key: string]: string", "[key]: string", "keyof string", "{key: string}"], "answer": "[key: string]: string", "difficulty": "Hard", "explanation": "For dynamic property names", "category": "Interfaces"},
    {"question": "Can an interface have a function?", "options": ["greet(): void", "greet: () => void", "Both", "None"], "answer": "Both", "difficulty": "Medium", "explanation": "Call signature allowed", "category": "Interfaces"},
    {"question": "What is a hybrid type?", "options": ["Function + Object", "Only function", "Only object", "Array"], "answer": "Function + Object", "difficulty": "Hard", "explanation": "Like jQuery: callable + properties", "category": "Interfaces"},
    {"question": "Do interfaces merge?", "options": ["Yes, same name", "No", "Only classes", "Only types"], "answer": "Yes, same name", "difficulty": "Medium", "explanation": "Declaration merging", "category": "Interfaces"},
    {"question": "Interface vs Type alias?", "options": ["Both similar", "Interface better", "Type more powerful", "Interface faster"], "answer": "Both similar", "difficulty": "Medium", "explanation": "Use case dependent", "category": "Interfaces"},
    {"question": "How does a class use an interface?", "options": ["implements", "extends", "uses", "follows"], "answer": "implements", "difficulty": "Easy", "explanation": "class User implements Person", "category": "Interfaces"},
    # 46-65: Classes
    {"question": "How does a class inherit?", "options": ["extends", "implements", "inherits", "uses"], "answer": "extends", "difficulty": "Easy", "explanation": "class Dog extends Animal", "category": "Classes"},
    {"question": "Modern private field syntax?", "options": ["#name", "private name", "Both", "_name"], "answer": "Both", "difficulty": "Medium", "explanation": "ES2022 (#) + TS (private)", "category": "Classes"},
    {"question": "Are class members public by default?", "options": ["Yes", "No", "Only in constructor", "Only methods"], "answer": "Yes", "difficulty": "Easy", "explanation": "No keyword needed", "category": "Classes"},
    {"question": "What does `protected` allow?", "options": ["Child class access", "Same class only", "No access", "All access"], "answer": "Child class access", "difficulty": "Medium", "explanation": "Inheritance safe", "category": "Classes"},
    {"question": "How to define a static property?", "options": ["static count: number", "count: number", "const count", "#count"], "answer": "static count: number", "difficulty": "Easy", "explanation": "Accessed via Class.count", "category": "Classes"},
    {"question": "What is an abstract class?", "options": ["abstract class Shape", "virtual class Shape", "interface Shape", "type Shape"], "answer": "abstract class Shape", "difficulty": "Medium", "explanation": "Must be extended", "category": "Classes"},
    {"question": "Getter and setter?", "options": ["get/set methods", "Both", "Only get", "None"], "answer": "Both", "difficulty": "Easy", "explanation": "For encapsulation", "category": "Classes"},
    {"question": "What are parameter properties?", "options": ["constructor(public name)", "constructor(name)", "Both", "None"], "answer": "constructor(public name)", "difficulty": "Hard", "explanation": "Shorthand for field + param", "category": "Classes"},
    {"question": "When must you call `super()`?", "options": ["In child constructor", "Anywhere", "Never", "Optional"], "answer": "In child constructor", "difficulty": "Medium", "explanation": "Calls parent constructor", "category": "Classes"},
    {"question": "Which are class decorators?", "options": ["@sealed", "@log", "@Component", "All"], "answer": "All", "difficulty": "Hard", "explanation": "Modify class behavior", "category": "Classes"},
    # 66-85: Generics
    {"question": "Generic function syntax?", "options": ["<T>(x: T): T", "<T> x: T", "T => T", "[T] x"], "answer": "<T>(x: T): T", "difficulty": "Medium", "explanation": "Type-safe reuse", "category": "Generics"},
    {"question": "How to constrain a generic?", "options": ["T extends string", "T implements string", "T: string", "T < string"], "answer": "T extends string", "difficulty": "Medium", "explanation": "Limits possible types", "category": "Generics"},
    {"question": "Default generic type?", "options": ["T = string", "T: string", "T ? string", "T | string"], "answer": "T = string", "difficulty": "Hard", "explanation": "Fallback if not provided", "category": "Generics"},
    {"question": "What is a conditional type?", "options": ["T extends U ? X : Y", "T | U ? X : Y", "T & U => X", "T = U ? X : Y"], "answer": "T extends U ? X : Y", "difficulty": "Hard", "explanation": "Type-level if statement", "category": "Generics"},
    {"question": "What does `infer` do?", "options": ["Extracts a type", "Creates a type", "Deletes a type", "Copies a type"], "answer": "Extracts a type", "difficulty": "Hard", "explanation": "From return or param", "category": "Generics"},
    {"question": "What is a mapped type?", "options": ["{ [K in keyof T]: U }", "{ K in T: U }", "[K in keyof T] => U", "keyof T[U]"], "answer": "{ [K in keyof T]: U }", "difficulty": "Hard", "explanation": "Transforms object keys", "category": "Generics"},
    {"question": "What does `keyof` return?", "options": ["Union of keys", "Values", "Both", "None"], "answer": "Union of keys", "difficulty": "Medium", "explanation": "type Keys = keyof User", "category": "Generics"},
    {"question": "What does `Partial<T>` do?", "options": ["Makes all optional", "Makes all required", "Makes all readonly", "Makes all string"], "answer": "Makes all optional", "difficulty": "Medium", "explanation": "Built-in utility", "category": "Generics"},
    {"question": "What does `Pick<T, K>` do?", "options": ["Selects properties", "Removes all", "Renames", "Copies"], "answer": "Selects properties", "difficulty": "Medium", "explanation": "Pick<User, 'name' | 'age'>", "category": "Generics"},
    {"question": "What does `Omit<T, K>` do?", "options": ["Removes properties", "Removes all", "Renames", "Copies"], "answer": "Removes properties", "difficulty": "Medium", "explanation": "Omit<User, 'password'>", "category": "Generics"},
    # 86-95: Enums
    {"question": "Numeric enum starts from?", "options": ["0", "1", "A", "null"], "answer": "0", "difficulty": "Easy", "explanation": "Auto-incrementing", "category": "Enums"},
    {"question": "How to define a string enum?", "options": ["Up = 'UP'", "Up: 'UP'", "Up => 'UP'", "Up == 'UP'"], "answer": "Up = 'UP'", "difficulty": "Easy", "explanation": "Explicit string values", "category": "Enums"},
    {"question": "What is a `const enum`?", "options": ["Inlined at compile time", "Runtime object", "Both", "None"], "answer": "Inlined at compile time", "difficulty": "Hard", "explanation": "No JS object emitted", "category": "Enums"},
    {"question": "Can enum members be computed?", "options": ["Yes, with expressions", "No", "String only", "Number only"], "answer": "Yes, with expressions", "difficulty": "Hard", "explanation": "Size = 'abc'.length", "category": "Enums"},
    {"question": "Reverse mapping works for?", "options": ["Numeric enums", "String enums", "Both", "None"], "answer": "Numeric enums", "difficulty": "Medium", "explanation": "Color[0] === 'Red'", "category": "Enums"},
    # 96-100: Advanced Topics
    {"question": "What type is inferred for `let x = 'hi'`?", "options": ["string", "any", "unknown", "let"], "answer": "string", "difficulty": "Easy", "explanation": "Type inference", "category": "Inference"},
    {"question": "Where does contextual typing help?", "options": ["Event handlers", "let variables", "function params", "interfaces"], "answer": "Event handlers", "difficulty": "Medium", "explanation": "e: MouseEvent inferred", "category": "Inference"},
    {"question": "What makes a discriminated union?", "options": ["A common 'kind' property", "id property", "name property", "type property"], "answer": "A common 'kind' property", "difficulty": "Hard", "explanation": "Enables narrowing", "category": "Union"},
    {"question": "How to create a user-defined type guard?", "options": ["x is string", "x: string", "x == string", "x === string"], "answer": "x is string", "difficulty": "Hard", "explanation": "Narrows type in if block", "category": "Guards"},
    {"question": "What is a decorator factory?", "options": ["@log('msg')", "@log", "@log()", "@log[]"], "answer": "@log('msg')", "difficulty": "Hard", "explanation": "Returns a decorator function", "category": "Decorators"},
]

# === CSS STYLING ===
st.markdown("""
<style>
:root {
    --primary: #6b21a8;
    --primary-hover: #8b5cf6;
    --success: #34c759;
    --danger: #ff3b30;
    --warning: #ff9500;
    --info: #007aff;
    --dark: #1a1a3b;
    --light: #f3e8ff;
}
body {
    background: linear-gradient(135deg, var(--dark) 0%, #2c2c54 100%);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}
.main-container {
    background: #2c2c54;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    margin: 1rem auto;
    max-width: 900px;
    color: white;
}
.title {
    text-align: center;
    font-size: 2.5rem;
    background: linear-gradient(90deg, var(--primary), var(--info));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
    font-weight: bold;
}
.stButton>button {
    background: var(--primary);
    color: white;
    border: none;
    border-radius: 0.75rem;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    width: 100%;
    margin: 0.5rem 0;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background: var(--primary-hover);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(139, 92, 246, 0.4);
}
.option-button {
    background: rgba(107, 33, 168, 0.1) !important;
    border: 2px solid var(--primary) !important;
    text-align: left;
}
.selected-correct {
    background: var(--success) !important;
    color: white !important;
    border-color: var(--success) !important;
}
.selected-wrong {
    background: var(--danger) !important;
    color: white !important;
    border-color: var(--danger) !important;
}
.difficulty-badge {
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.8rem;
    font-weight: bold;
    display: inline-block;
    margin-right: 0.5rem;
}
.easy { background: var(--success); color: white; }
.medium { background: var(--warning); color: white; }
.hard { background: var(--danger); color: white; }
.category-badge {
    background: var(--info);
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.8rem;
    display: inline-block;
}
.progress-container {
    background: rgba(255,255,255,0.1);
    border-radius: 0.5rem;
    height: 10px;
    margin: 1rem 0;
    overflow: hidden;
}
.progress-fill {
    background: linear-gradient(90deg, var(--primary), var(--info));
    height: 100%;
    border-radius: 0.5rem;
    transition: width 0.3s ease;
}
.timer-display {
    font-size: 1.5rem;
    text-align: center;
    background: rgba(255,255,255,0.1);
    padding: 0.5rem;
    border-radius: 0.5rem;
    margin: 1rem 0;
    font-weight: bold;
}
.feedback-box {
    padding: 1rem;
    border-radius: 0.5rem;
    margin: 1rem 0;
    font-weight: bold;
    border-left: 4px solid;
}
.correct-feedback {
    background: rgba(52, 199, 89, 0.2);
    border-color: var(--success);
    color: var(--success);
}
.wrong-feedback {
    background: rgba(255, 59, 48, 0.2);
    border-color: var(--danger);
    color: var(--danger);
}
.stats-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin: 1rem 0;
}
.stat-card {
    background: rgba(255,255,255,0.1);
    padding: 1rem;
    border-radius: 0.5rem;
    text-align: center;
}
.achievement-badge {
    background: linear-gradient(135deg, var(--primary), var(--info));
    color: white;
    padding: 1rem;
    border-radius: 1rem;
    text-align: center;
    margin: 1rem 0;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# === FUNCTIONS ===
def initialize_session_state():
    if "quiz_data" not in st.session_state:
        st.session_state.update({
            "quiz_data": shuffle_quiz(quiz),
            "score": 0,
            "current_q": 0,
            "start_time": None,
            "answers": [None] * len(quiz),
            "show_results": False,
            "selected_option": None,
            "feedback": None,
            "time_left": 600,
            "streak": 0,
            "max_streak": 0,
            "started": False,
            "quiz_duration": 600
        })

def shuffle_quiz(_quiz):
    shuffled = random.sample(_quiz, len(_quiz))
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = q["options"].copy()
        random.shuffle(q["display_options"])
    return shuffled

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
        "time_left": 600,
        "streak": 0,
        "max_streak": 0,
        "started": False
    })

def update_timer():
    if st.session_state.started and not st.session_state.show_results and st.session_state.start_time:
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        st.session_state.time_left = max(600 - elapsed, 0)
        if st.session_state.time_left <= 0:
            st.session_state.show_results = True

def get_achievement(score, max_streak, total):
    percentage = (score / (total * 2)) * 100
    if percentage >= 90: return "TypeScript Master"
    elif percentage >= 80: return "TypeScript Expert"
    elif percentage >= 70: return "TypeScript Pro"
    elif percentage >= 60: return "Good Job"
    else: return "Keep Practicing"

# === MAIN APP ===
def main():
    initialize_session_state()
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">TypeScript Mastery Quiz</h1>', unsafe_allow_html=True)

    if not st.session_state.started:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h2>Bem-vindo ao Quiz TypeScript!</h2>
            <p>Teste seus conhecimentos com <strong>100 questões</strong> sobre TypeScript</p>
            <p><strong>Tempo:</strong> 10 minutos</p>
            <p><strong>Tópicos:</strong> Compilador, Tipos, Interfaces, Classes, Generics, Enums e mais!</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Iniciar Quiz", use_container_width=True, type="primary"):
            st.session_state.started = True
            st.session_state.start_time = datetime.now()
            st.rerun()

    else:
        update_timer()

        if not st.session_state.show_results:
            minutes, seconds = divmod(int(st.session_state.time_left), 60)
            st.markdown(f'<div class="timer-display">Tempo: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

            progress = (st.session_state.current_q + 1) / len(st.session_state.quiz_data)
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; margin: 0.5rem 0; font-size: 0.9rem;">
                <span>Questão: {st.session_state.current_q + 1}/{len(quiz)}</span>
                <span>Pontos: {st.session_state.score}</span>
                <span>Sequência: {st.session_state.streak}</span>
            </div>
            <div class="progress-container">
                <div class="progress-fill" style="width: {progress * 100}%"></div>
            </div>
            """, unsafe_allow_html=True)

            q = st.session_state.quiz_data[st.session_state.current_q]

            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 0.75rem; margin: 1rem 0;">
                <div style="margin-bottom: 1rem;">
                    <span class="difficulty-badge {q['difficulty'].lower()}">{q['difficulty']}</span>
                    <span class="category-badge">{q['category']}</span>
                </div>
                <p style="font-size: 1.2rem; line-height: 1.6; font-weight: 500;">{q['question']}</p>
            </div>
            """, unsafe_allow_html=True)

            for opt in q["display_options"]:
                key = f"opt_{q['id']}_{opt}"
                is_selected = st.session_state.selected_option == opt
                is_correct = opt == q["answer"]

                if st.button(
                    opt,
                    key=key,
                    use_container_width=True,
                    disabled=st.session_state.selected_option is not None,
                    type="primary" if is_selected and is_correct else "secondary"
                ):
                    if st.session_state.selected_option is None:
                        st.session_state.selected_option = opt
                        correct = opt == q["answer"]
                        st.session_state.feedback = f"{'Correto!' if correct else 'Incorreto'} {q['explanation']}"
                        
                        if correct:
                            st.session_state.score += 2
                            st.session_state.streak += 1
                            st.session_state.max_streak = max(st.session_state.streak, st.session_state.max_streak)
                        else:
                            st.session_state.streak = 0
                        
                        st.session_state.answers[st.session_state.current_q] = opt
                        st.rerun()

            if st.session_state.feedback:
                color = "correct-feedback" if "Correto" in st.session_state.feedback else "wrong-feedback"
                st.markdown(f'<div class="feedback-box {color}">{st.session_state.feedback}</div>', unsafe_allow_html=True)

            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                if st.session_state.current_q > 0 and st.button("Anterior", use_container_width=True):
                    st.session_state.current_q -= 1
                    st.session_state.selected_option = st.session_state.answers[st.session_state.current_q]
                    st.session_state.feedback = None
                    st.rerun()

            with col2:
                if st.button("Reiniciar Quiz", use_container_width=True, type="secondary"):
                    reset_quiz()
                    st.rerun()

            with col3:
                if st.button("Próxima", use_container_width=True):
                    st.session_state.current_q += 1
                    if st.session_state.current_q >= len(st.session_state.quiz_data):
                        st.session_state.show_results = True
                    else:
                        st.session_state.selected_option = st.session_state.answers[st.session_state.current_q]
                        st.session_state.feedback = None
                    st.rerun()

        else:
            total = len(quiz) * 2
            percentage = (st.session_state.score / total) * 100

            st.markdown(f"""
            <div style="text-align: center; padding: 2rem;">
                <h2>Quiz Concluído!</h2>
                <div class="achievement-badge">
                    <h1 style="font-size: 3.5rem; margin: 0;">{st.session_state.score}/{total}</h1>
                    <p style="font-size: 1.5rem; margin: 0.5rem 0;">{percentage:.1f}% de acertos</p>
                </div>

                <div class="stats-container">
                    <div class="stat-card">
                        <h3>Maior Sequência</h3>
                        <p style="font-size: 2rem; color: #ff9500; margin: 0.5rem 0;">{st.session_state.max_streak}</p>
                    </div>
                    <div class="stat-card">
                        <h3>Tempo Total</h3>
                        <p style="font-size: 1.2rem; margin: 0.5rem 0;">10:00</p>
                    </div>
                </div>

                <h2 style="margin: 2rem 0; color: #8b5cf6;">{get_achievement(st.session_state.score, st.session_state.max_streak, len(quiz))}</h2>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Fazer Novamente", use_container_width=True, type="primary"):
                reset_quiz()
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(page_title="TypeScript Quiz", layout="centered")
    main()
