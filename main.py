import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Quiz data - Enhanced with more questions
quiz =[
    {
        "question": "What is Vite used for in a JavaScript project?",
        "options": ["A build tool for fast development", "A linter for code quality", "A testing framework", "A package manager"],
        "answer": "A build tool for fast development",
        "difficulty": "Easy",
        "explanation": "Vite is a modern build tool that provides fast development with hot module replacement and optimized production builds.",
        "category": "CLI Tool: Vite"
    },
    {
        "question": "Which command initializes a new Vite project with React?",
        "options": ["npm create vite@latest my-app --template react", "npm init vite my-app", "vite create my-app --react", "npm vite init my-app"],
        "answer": "npm create vite@latest my-app --template react",
        "difficulty": "Medium",
        "explanation": "The command uses 'create vite' with the '--template react' flag to set up a React project.",
        "category": "CLI Tool: Vite"
    },
    {
        "question": "What is a key advantage of Vite over Create React App?",
        "options": ["Faster dev server startup", "Better TypeScript support", "Built-in testing", "Automatic code splitting"],
        "answer": "Faster dev server startup",
        "difficulty": "Medium",
        "explanation": "Vite uses native ES modules for faster development server startup compared to Create React App.",
        "category": "CLI Tool: Vite"
    },
    {
        "question": "How do you start a Vite development server?",
        "options": ["npm run dev", "npm start", "vite start", "npm run vite"],
        "answer": "npm run dev",
        "difficulty": "Easy",
        "explanation": "The 'dev' script in Vite projects, defined in package.json, starts the development server.",
        "category": "CLI Tool: Vite"
    },
    {
        "question": "What does Vite use for bundling in production?",
        "options": ["Rollup", "Webpack", "Esbuild", "Parcel"],
        "answer": "Rollup",
        "difficulty": "Medium",
        "explanation": "Vite uses Rollup for optimized production builds, while Esbuild powers its dev server.",
        "category": "CLI Tool: Vite"
    },
    {
        "question": "What is the purpose of Create React App (CRA)?",
        "options": ["Set up a React project with zero configuration", "Manage dependencies", "Run unit tests", "Optimize images"],
        "answer": "Set up a React project with zero configuration",
        "difficulty": "Easy",
        "explanation": "CRA provides a pre-configured setup for React projects, including Webpack and Babel.",
        "category": "CLI Tool: Create React App"
    },
    {
        "question": "Which command creates a new CRA project?",
        "options": ["npx create-react-app my-app", "npm init react my-app", "npx cra my-app", "npm create react-app my-app"],
        "answer": "npx create-react-app my-app",
        "difficulty": "Easy",
        "explanation": "'npx create-react-app' initializes a new React project with all necessary configurations.",
        "category": "CLI Tool: Create React App"
    },
    {
        "question": "What is a limitation of Create React App?",
        "options": ["No TypeScript support", "Limited configuration options", "No CSS support", "No hot module replacement"],
        "answer": "Limited configuration options",
        "difficulty": "Medium",
        "explanation": "CRA abstracts Webpack configuration, requiring ejection for custom setups.",
        "category": "CLI Tool: Create React App"
    },
    {
        "question": "How do you start a CRA development server?",
        "options": ["npm start", "npm run dev", "cra start", "npm run cra"],
        "answer": "npm start",
        "difficulty": "Easy",
        "explanation": "The 'start' script in CRA’s package.json runs the development server.",
        "category": "CLI Tool: Create React App"
    },
    {
        "question": "What does 'eject' do in a CRA project?",
        "options": ["Removes dependencies", "Exposes configuration files", "Builds for production", "Clears the build folder"],
        "answer": "Exposes configuration files",
        "difficulty": "Medium",
        "explanation": "'npm run eject' exposes Webpack and other config files for customization.",
        "category": "CLI Tool: Create React App"
    },
    {
        "question": "What is the purpose of the 'src' folder in a React project?",
        "options": ["Stores source code and components", "Holds build output", "Contains configuration files", "Stores dependencies"],
        "answer": "Stores source code and components",
        "difficulty": "Easy",
        "explanation": "The 'src' folder contains the application’s source code, including React components and logic.",
        "category": "Folder Structure"
    },
    {
        "question": "What is typically found in the 'public' folder of a React project?",
        "options": ["index.html and static assets", "React components", "Webpack config", "Test files"],
        "answer": "index.html and static assets",
        "difficulty": "Easy",
        "explanation": "The 'public' folder holds static files like 'index.html' and assets like images or favicon.",
        "category": "Folder Structure"
    },
    {
        "question": "Where are node modules stored in a React project?",
        "options": ["node_modules folder", "src folder", "public folder", "build folder"],
        "answer": "node_modules folder",
        "difficulty": "Easy",
        "explanation": "The 'node_modules' folder stores all project dependencies installed via npm or yarn.",
        "category": "Folder Structure"
    },
    {
        "question": "What is the purpose of the 'package.json' file in a React project?",
        "options": ["Defines dependencies and scripts", "Configures Webpack", "Stores component logic", "Holds test results"],
        "answer": "Defines dependencies and scripts",
        "difficulty": "Easy",
        "explanation": "'package.json' lists project dependencies, scripts, and metadata.",
        "category": "Folder Structure"
    },
    {
        "question": "What is the role of the 'build' folder in a React project?",
        "options": ["Holds production-ready files", "Stores source code", "Contains test scripts", "Manages dependencies"],
        "answer": "Holds production-ready files",
        "difficulty": "Easy",
        "explanation": "The 'build' folder contains optimized files generated by the build process for deployment.",
        "category": "Folder Structure"
    },
    {
        "question": "What is JSX in React?",
        "options": ["A syntax extension for JavaScript", "A CSS preprocessor", "A testing library", "A state management tool"],
        "answer": "A syntax extension for JavaScript",
        "difficulty": "Easy",
        "explanation": "JSX allows writing HTML-like code in JavaScript, which React compiles into JavaScript.",
        "category": "Components: JSX"
    },
    {
        "question": "What does the following JSX return: ```jsx\n<div>Hello, {name}</div>```",
        "options": ["A div with dynamic content", "A JavaScript object", "A string", "An error"],
        "answer": "A div with dynamic content",
        "difficulty": "Easy",
        "explanation": "JSX expressions like {name} render dynamic values within HTML-like elements.",
        "category": "Components: JSX"
    },
    {
        "question": "How do you write a comment in JSX?",
        "options": ["{/* Comment */}", "// Comment", "<!-- Comment -->", "# Comment"],
        "answer": "{/* Comment */}",
        "difficulty": "Medium",
        "explanation": "JSX uses JavaScript-style comments wrapped in curly braces for dynamic content.",
        "category": "Components: JSX"
    },
    {
        "question": "What is the output of: ```jsx\n<div>{2 + 2}</div>```",
        "options": ["4", "2 + 2", "Error", "undefined"],
        "answer": "4",
        "difficulty": "Easy",
        "explanation": "JSX evaluates JavaScript expressions inside curly braces, rendering the result.",
        "category": "Components: JSX"
    },
    {
        "question": "Which of the following is valid JSX?",
        "options": ["<div className='box'>Content</div>", "<div class='box'>Content</div>", "<div id='box'>Content</div>", "<div name='box'>Content</div>"],
        "answer": "<div className='box'>Content</div>",
        "difficulty": "Medium",
        "explanation": "JSX uses 'className' instead of 'class' for CSS classes due to JavaScript reserved words.",
        "category": "Components: JSX"
    },
    {
        "question": "What are props in React?",
        "options": ["Data passed to components", "Component state", "Event handlers", "DOM elements"],
        "answer": "Data passed to components",
        "difficulty": "Easy",
        "explanation": "Props are read-only data passed from a parent to a child component.",
        "category": "Components: Props"
    },
    {
        "question": "How do you pass a prop to a component?",
        "options": ["<Component name='value' />", "<Component prop='value' />", "<Component setProp='value' />", "<Component value='name' />"],
        "answer": "<Component name='value' />",
        "difficulty": "Easy",
        "explanation": "Props are passed as attributes in JSX, like 'name='value''.",
        "category": "Components: Props"
    },
    {
        "question": "What is the output of: ```jsx\nfunction Comp({name}) { return <div>{name}</div>; }\n<Comp name='Alice' />```",
        "options": ["Alice", "name", "undefined", "Error"],
        "answer": "Alice",
        "difficulty": "Medium",
        "explanation": "The 'name' prop is destructured and rendered in the component.",
        "category": "Components: Props"
    },
    {
        "question": "Can props be modified inside a component?",
        "options": ["No, they are read-only", "Yes, using setProps", "Yes, using useState", "Yes, by reassigning"],
        "answer": "No, they are read-only",
        "difficulty": "Medium",
        "explanation": "Props are immutable within a component to ensure predictable data flow.",
        "category": "Components: Props"
    },
    {
        "question": "How do you set default props for a component?",
        "options": ["Component.defaultProps = {}", "Component.props = {}", "Component.setDefaults({})", "useDefaultProps({})"],
        "answer": "Component.defaultProps = {}",
        "difficulty": "Medium",
        "explanation": "'defaultProps' defines fallback values for undefined props.",
        "category": "Components: Props"
    },
    {
        "question": "What is the useState hook used for?",
        "options": ["Managing component state", "Fetching data", "Handling events", "Rendering JSX"],
        "answer": "Managing component state",
        "difficulty": "Easy",
        "explanation": "'useState' allows functional components to manage state with a value and setter.",
        "category": "Components: States (useState)"
    },
    {
        "question": "What does useState return?",
        "options": ["[state, setState]", "[state, updateState]", "[value, setValue]", "[state, dispatch]"],
        "answer": "[state, setState]",
        "difficulty": "Easy",
        "explanation": "'useState' returns an array with the current state and a function to update it.",
        "category": "Components: States (useState)"
    },
    {
        "question": "What is the output of: ```jsx\nconst [count, setCount] = useState(0); setCount(1); console.log(count);```",
        "options": ["0", "1", "undefined", "Error"],
        "answer": "0",
        "difficulty": "Medium",
        "explanation": "'setCount' is asynchronous, so 'count' doesn’t immediately reflect the new value.",
        "category": "Components: States (useState)"
    },
    {
        "question": "How do you update state based on the previous state?",
        "options": ["setState(prev => prev + 1)", "setState(state + 1)", "state = state + 1", "updateState(state + 1)"],
        "answer": "setState(prev => prev + 1)",
        "difficulty": "Medium",
        "explanation": "Using a callback with the previous state ensures correct updates in asynchronous scenarios.",
        "category": "Components: States (useState)"
    },
    {
        "question": "Can useState be used outside a component?",
        "options": ["No, only in functional components", "Yes, in any function", "Yes, in class components", "Yes, in event handlers"],
        "answer": "No, only in functional components",
        "difficulty": "Medium",
        "explanation": "'useState' is a React hook and must be called within a functional component.",
        "category": "Components: States (useState)"
    },
    {
        "question": "What is the data flow model in React?",
        "options": ["Unidirectional from parent to child", "Bidirectional between components", "Random flow", "No data flow"],
        "answer": "Unidirectional from parent to child",
        "difficulty": "Easy",
        "explanation": "React uses a unidirectional data flow, passing data via props from parent to child.",
        "category": "Components: Data Flow"
    },
    {
        "question": "How do child components communicate with parents in React?",
        "options": ["Via callback props", "Via direct state updates", "Via global variables", "Via useState"],
        "answer": "Via callback props",
        "difficulty": "Medium",
        "explanation": "Child components call parent-provided callback functions to send data upward.",
        "category": "Components: Data Flow"
    },
    {
        "question": "What happens if a child component tries to modify a prop directly?",
        "options": ["It causes an error", "It works but is discouraged", "It updates the parent", "It has no effect"],
        "answer": "It has no effect",
        "difficulty": "Medium",
        "explanation": "Props are read-only, so modifying them in a child has no effect and may cause warnings.",
        "category": "Components: Data Flow"
    },
    {
        "question": "How can a parent component update a child’s state?",
        "options": ["By passing new props", "By calling setState directly", "By modifying child state", "By using useEffect"],
        "answer": "By passing new props",
        "difficulty": "Medium",
        "explanation": "Parents update child state indirectly by passing updated props, triggering a re-render.",
        "category": "Components: Data Flow"
    },
    {
        "question": "What is an example of lifting state up in React?",
        "options": ["Moving state to a common parent", "Moving state to a child", "Using global state", "Avoiding state"],
        "answer": "Moving state to a common parent",
        "difficulty": "Medium",
        "explanation": "Lifting state up involves moving shared state to a parent component for coordination.",
        "category": "Components: Data Flow"
    },
    {
        "question": "What are React hooks?",
        "options": ["Functions for state and lifecycle in functional components", "Classes for state management", "Event listeners", "JSX extensions"],
        "answer": "Functions for state and lifecycle in functional components",
        "difficulty": "Easy",
        "explanation": "Hooks like useState and useEffect add state and lifecycle features to functional components.",
        "category": "Hooks"
    },
    {
        "question": "Which hook handles side effects in React?",
        "options": ["useEffect", "useState", "useReducer", "useContext"],
        "answer": "useEffect",
        "difficulty": "Easy",
        "explanation": "'useEffect' runs side effects like data fetching or DOM manipulation after rendering.",
        "category": "Hooks"
    },
    {
        "question": "What is the purpose of the dependency array in useEffect?",
        "options": ["Controls when the effect runs", "Stores state values", "Handles props", "Defines cleanup functions"],
        "answer": "Controls when the effect runs",
        "difficulty": "Medium",
        "explanation": "The dependency array determines when 'useEffect' re-runs based on value changes.",
        "category": "Hooks"
    },
    {
        "question": "What does useEffect(() => {}, []) do?",
        "options": ["Runs once on mount", "Runs on every render", "Runs on unmount", "Never runs"],
        "answer": "Runs once on mount",
        "difficulty": "Medium",
        "explanation": "An empty dependency array means the effect runs only once when the component mounts.",
        "category": "Hooks"
    },
    {
        "question": "What is the useReducer hook used for?",
        "options": ["Managing complex state logic", "Fetching data", "Handling events", "Rendering components"],
        "answer": "Managing complex state logic",
        "difficulty": "Medium",
        "explanation": "'useReducer' is an alternative to useState for complex state transitions.",
        "category": "Hooks"
    },
    {
        "question": "How do you access context in a functional component?",
        "options": ["useContext", "useState", "useEffect", "useReducer"],
        "answer": "useContext",
        "difficulty": "Medium",
        "explanation": "'useContext' accesses the value of a React context in a functional component.",
        "category": "Hooks"
    },
    {
        "question": "What does useMemo do?",
        "options": ["Caches a computed value", "Manages state", "Handles side effects", "Fetches data"],
        "answer": "Caches a computed value",
        "difficulty": "Medium",
        "explanation": "'useMemo' memoizes expensive calculations to prevent unnecessary re-computation.",
        "category": "Hooks"
    },
    {
        "question": "What is the purpose of useCallback?",
        "options": ["Memoizes a function", "Manages state", "Handles events", "Fetches data"],
        "answer": "Memoizes a function",
        "difficulty": "Medium",
        "explanation": "'useCallback' returns a memoized function to prevent re-creation on renders.",
        "category": "Hooks"
    },
    {
        "question": "What does useRef do?",
        "options": ["Holds a mutable reference", "Manages state", "Handles side effects", "Fetches data"],
        "answer": "Holds a mutable reference",
        "difficulty": "Medium",
        "explanation": "'useRef' creates a mutable object that persists across renders, often used for DOM access.",
        "category": "Hooks"
    },
    {
        "question": "How do you create a custom hook?",
        "options": ["Define a function starting with 'use'", "Define a class", "Use a regular function", "Extend useState"],
        "answer": "Define a function starting with 'use'",
        "difficulty": "Medium",
        "explanation": "Custom hooks are functions starting with 'use' that encapsulate reusable logic.",
        "category": "Hooks"
    }
]

# Enhanced CSS with better styling
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
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

[data-theme="light"] {
    --bg-gradient: linear-gradient(135deg, #e0e7ff 0%, #f3e8ff 100%);
    --text-color: #1f2937;
    --card-bg: #ffffff;
}

[data-theme="dark"] {
    --bg-gradient: linear-gradient(135deg, #1a1a3b 0%, #2c2c54 100%);
    --text-color: #ffffff;
    --card-bg: #2c2c54;
}

.main-container {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    margin: 1rem auto;
    max-width: 900px;
    color: var(--text-color);
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

.subtitle {
    text-align: center;
    color: var(--text-color);
    opacity: 0.8;
    margin-bottom: 2rem;
}

.stButton>button {
    background: var(--primary);
    color: white;
    border: none;
    border-radius: 0.75rem;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s ease;
    margin: 0.5rem 0;
    width: 100%;
}

.stButton>button:hover {
    background: var(--primary-hover);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.option-button {
    background: rgba(107, 33, 168, 0.1) !important;
    border: 2px solid var(--primary) !important;
    color: var(--text-color) !important;
}

.option-button:hover {
    background: var(--primary) !important;
    color: white !important;
}

.selected-correct {
    background: var(--success) !important;
    color: white !important;
    border: 2px solid var(--success) !important;
}

.selected-wrong {
    background: var(--danger) !important;
    color: white !important;
    border: 2px solid var(--danger) !important;
}

.difficulty-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.8rem;
    font-weight: bold;
    margin: 0.5rem 0;
}

.easy { background: var(--success); color: white; }
.medium { background: var(--warning); color: white; }
.hard { background: var(--danger); color: white; }

.category-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.8rem;
    background: var(--info);
    color: white;
    margin-left: 0.5rem;
}

.progress-container {
    background: rgba(255,255,255,0.1);
    border-radius: 1rem;
    padding: 1rem;
    margin: 1rem 0;
}

.progress-bar {
    background: rgba(255,255,255,0.2);
    border-radius: 0.5rem;
    height: 0.75rem;
    margin: 0.5rem 0;
    overflow: hidden;
}

.progress-fill {
    background: linear-gradient(90deg, var(--primary), var(--info));
    height: 100%;
    border-radius: 0.5rem;
    transition: width 0.3s ease;
}

.streak-counter {
    background: linear-gradient(135deg, #ff6b6b, #ffa726);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    font-weight: bold;
    text-align: center;
    margin: 0.5rem 0;
}

.timer-display {
    font-size: 1.5rem;
    font-weight: bold;
    text-align: center;
    background: rgba(255,255,255,0.1);
    padding: 0.5rem;
    border-radius: 0.5rem;
    margin: 0.5rem 0;
}

.feedback-box {
    padding: 1rem;
    border-radius: 0.5rem;
    margin: 1rem 0;
    font-weight: bold;
}

.correct-feedback {
    background: rgba(52, 199, 89, 0.2);
    border: 2px solid var(--success);
    color: var(--success);
}

.wrong-feedback {
    background: rgba(255, 59, 48, 0.2);
    border: 2px solid var(--danger);
    color: var(--danger);
}

.results-container {
    text-align: center;
    padding: 2rem;
}

.score-display {
    font-size: 3rem;
    font-weight: bold;
    background: linear-gradient(90deg, var(--primary), var(--info));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 1rem 0;
}

.achievement-badge {
    background: linear-gradient(135deg, #ffd700, #ffa726);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    font-weight: bold;
    margin: 0.5rem;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
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
            "time_left": 3600,
            "theme": "dark",
            "streak": 0,
            "max_streak": 0,
            "started": False,
            "paused": False,
            "pause_time": None,
            "quiz_duration": 3600
        })

def shuffle_quiz(_quiz):
    shuffled = random.sample(_quiz, len(_quiz))
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = q["options"].copy()
        random.shuffle(q["display_options"])
        q["labeled_answer"] = q["answer"]
    return shuffled

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

def update_timer():
    if not st.session_state.paused and st.session_state.start_time:
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        st.session_state.time_left = max(st.session_state.quiz_duration - elapsed, 0)
        if st.session_state.time_left <= 0:
            st.session_state.show_results = True

def toggle_pause():
    if st.session_state.paused:
        pause_duration = (datetime.now() - st.session_state.pause_time).total_seconds()
        st.session_state.start_time += timedelta(seconds=pause_duration)
        st.session_state.paused = False
    else:
        st.session_state.paused = True
        st.session_state.pause_time = datetime.now()

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
        "time_left": st.session_state.quiz_duration,
        "streak": 0,
        "max_streak": 0,
        "started": False,
        "paused": False,
        "pause_time": None
    })

def get_achievement(score, max_streak, total_questions):
    percentage = (score / (total_questions * 2)) * 100
    if percentage >= 90 and max_streak >= total_questions:
        return "JavaScript Master 🏆"
    elif percentage >= 80:
        return "Expert Developer 💻"
    elif percentage >= 70:
        return "Skilled Programmer ⚡"
    elif percentage >= 60:
        return "Good Learner 📚"
    else:
        return "Keep Practicing 🌱"

# Main application
def main():
    initialize_session_state()
    
    st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="title">🚀 JavaScript Mastery Quiz</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Test your JavaScript skills with interactive coding challenges!</p>', unsafe_allow_html=True)
    
    # Theme toggle
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🌓 Toggle Theme"):
            toggle_theme()
            st.rerun()
    
    # Welcome screen
    if not st.session_state.started:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h2>📋 Quiz Overview</h2>
            <p><strong>10 Questions</strong> • <strong>60 Minutes</strong> • <strong>2 Points per Question</strong></p>
            <p>Categories: Variables, DOM, Error Handling, Browser API, and more!</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎯 Start Quiz", use_container_width=True):
            st.session_state.started = True
            st.session_state.start_time = datetime.now()
            st.rerun()
    else:
        # Timer and controls
        if not st.session_state.show_results:
            update_timer()
            
            # Timer display
            minutes = int(st.session_state.time_left // 60)
            seconds = int(st.session_state.time_left % 60)
            timer_color = "🔴" if st.session_state.time_left < 300 else "🟡" if st.session_state.time_left < 900 else "🟢"
            st.markdown(f'<div class="timer-display">{timer_color} {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)
            
            # Control buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                pause_label = "⏸️ Pause" if not st.session_state.paused else "▶️ Resume"
                if st.button(pause_label, use_container_width=True):
                    toggle_pause()
                    st.rerun()
            with col2:
                if st.button("🔄 Restart", use_container_width=True):
                    reset_quiz()
                    st.rerun()
            with col3:
                if st.button("🏁 Submit", use_container_width=True):
                    st.session_state.show_results = True
                    st.rerun()
        
        # Progress section
        total_questions = len(st.session_state.quiz_data)
        current_q = min(st.session_state.current_q, total_questions - 1)
        progress = ((current_q + 1) / total_questions) * 100
        
        st.markdown(f"""
        <div class="progress-container">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span>Question {current_q + 1} of {total_questions}</span>
                <span>Score: {st.session_state.score}/{total_questions * 2}</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress}%"></div>
            </div>
            <div style="display: flex; justify-content: space-between; margin-top: 0.5rem;">
                <span>Progress: {progress:.1f}%</span>
                <div class="streak-counter">🔥 Streak: {st.session_state.streak}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.show_results:
            # Question display
            q = st.session_state.quiz_data[current_q]
            
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 0.75rem; margin: 1rem 0;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="difficulty-badge {q['difficulty'].lower()}">{q['difficulty']}</span>
                    <span class="category-badge">{q['category']}</span>
                </div>
                {q['question']}
            </div>
            """, unsafe_allow_html=True)
            
            # Options
            for option in q["display_options"]:
                button_class = "option-button"
                if st.session_state.selected_option == option:
                    button_class = "selected-correct" if option == q["answer"] else "selected-wrong"
                
                if st.button(option, key=f"option_{q['id']}_{option}", use_container_width=True):
                    st.session_state.selected_option = option
                    is_correct = option == q["answer"]
                    st.session_state.feedback = {
                        "message": f"{'✅ Correct!' if is_correct else '❌ Incorrect'} {q['explanation']}",
                        "type": "correct" if is_correct else "wrong"
                    }
                    
                    if is_correct:
                        st.session_state.score += 2
                        st.session_state.streak += 1
                        st.session_state.max_streak = max(st.session_state.streak, st.session_state.max_streak)
                    else:
                        st.session_state.streak = 0
                    
                    st.session_state.answers[current_q] = option
                    st.rerun()
            
            # Feedback
            if st.session_state.feedback:
                feedback_class = "correct-feedback" if st.session_state.feedback["type"] == "correct" else "wrong-feedback"
                st.markdown(f'<div class="feedback-box {feedback_class}">{st.session_state.feedback["message"]}</div>', unsafe_allow_html=True)
            
            # Navigation buttons
            col1, col2 = st.columns(2)
            with col1:
                if current_q > 0 and st.button("⬅️ Previous", use_container_width=True):
                    st.session_state.current_q -= 1
                    st.session_state.selected_option = st.session_state.answers[st.session_state.current_q]
                    st.session_state.feedback = None
                    st.rerun()
            with col2:
                if st.session_state.selected_option and st.button("Next ➡️", use_container_width=True):
                    st.session_state.current_q += 1
                    if st.session_state.current_q >= total_questions:
                        st.session_state.show_results = True
                    else:
                        st.session_state.selected_option = st.session_state.answers[st.session_state.current_q]
                        st.session_state.feedback = None
                    st.rerun()
        else:
            # Results screen
            achievement = get_achievement(st.session_state.score, st.session_state.max_streak, total_questions)
            
            st.markdown(f"""
            <div class="results-container">
                <h2>🎉 Quiz Completed!</h2>
                <div class="score-display">{st.session_state.score}/{total_questions * 2}</div>
                <div class="achievement-badge">{achievement}</div>
                <p>Maximum Streak: 🔥 {st.session_state.max_streak}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Detailed results
            st.markdown("### 📊 Detailed Results")
            for i, (q, ans) in enumerate(zip(st.session_state.quiz_data, st.session_state.answers)):
                is_correct = ans == q["answer"]
                result_icon = "✅" if is_correct else "❌"
                
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 0.5rem; margin: 0.5rem 0;">
                    <div style="display: flex; justify-content: space-between;">
                        <strong>Question {i + 1} {result_icon}</strong>
                        <span class="difficulty-badge {q['difficulty'].lower()}">{q['difficulty']}</span>
                    </div>
                    {q['question']}
                    <p><strong>Your Answer:</strong> <span style="color: {'var(--success)' if is_correct else 'var(--danger)'}">{ans or "Not answered"}</span></p>
                    <p><strong>Correct Answer:</strong> {q['answer']}</p>
                    <p><em>{q['explanation']}</em></p>
                </div>
                """, unsafe_allow_html=True)
            
            if st.button("🔄 Take Quiz Again", use_container_width=True):
                reset_quiz()
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

