import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Quiz data - Enhanced with more questions
quiz =[
    {
        "question": "What is the output of: ```typescript\nlet x: number = 5; console.log(x);```",
        "options": ["5", "undefined", "Error", "null"],
        "answer": "5",
        "difficulty": "Easy",
        "explanation": "TypeScript's type annotation ensures 'x' is a number, and it logs 5 as expected.",
        "category": "TypeScript"
    },
    {
        "question": "What does the TypeScript compiler (tsc) do?",
        "options": ["Compiles TypeScript to JavaScript", "Runs TypeScript code directly", "Minifies JavaScript", "Bundles modules"],
        "answer": "Compiles TypeScript to JavaScript",
        "difficulty": "Easy",
        "explanation": "The 'tsc' compiler transpiles TypeScript code to JavaScript for browser or Node.js execution.",
        "category": "TS Compiler"
    },
    {
        "question": "Which command compiles a TypeScript file?",
        "options": ["tsc file.ts", "ts file.ts", "typescript file.ts", "compile file.ts"],
        "answer": "tsc file.ts",
        "difficulty": "Easy",
        "explanation": "'tsc file.ts' compiles a TypeScript file to JavaScript based on tsconfig.json settings.",
        "category": "TS Compiler"
    },
    {
        "question": "What is the purpose of 'noEmitOnError' in tsconfig.json?",
        "options": ["Prevents output if errors occur", "Disables type checking", "Enables strict mode", "Minifies output"],
        "answer": "Prevents output if errors occur",
        "difficulty": "Medium",
        "explanation": "'noEmitOnError: true' stops the compiler from generating JavaScript if type errors are found.",
        "category": "TS Compiler"
    },
    {
        "question": "What happens if you run: ```typescript\ntsc --strict app.ts``` and app.ts has type errors?",
        "options": ["Compiles with warnings", "Fails to compile", "Ignores errors", "Generates minified JS"],
        "answer": "Fails to compile",
        "difficulty": "Medium",
        "explanation": "The '--strict' flag enables strict type-checking, and compilation fails if errors are detected.",
        "category": "TS Compiler"
    },
    {
        "question": "What is the correct type annotation for a string variable?",
        "options": ["let x: string", "let x: String", "let x: text", "let x = string"],
        "answer": "let x: string",
        "difficulty": "Easy",
        "explanation": "TypeScript uses lowercase 'string' for primitive string types, not the 'String' object.",
        "category": "Type Annotations"
    },
    {
        "question": "What is the output of: ```typescript\nlet x: number | string = 10; x = 'hello'; console.log(x);```",
        "options": ["10", "hello", "Error", "undefined"],
        "answer": "hello",
        "difficulty": "Medium",
        "explanation": "The union type 'number | string' allows 'x' to be reassigned to a string, logging 'hello'.",
        "category": "Type Annotations"
    },
    {
        "question": "How do you annotate a function that returns nothing?",
        "options": ["function fn(): void", "function fn(): null", "function fn(): undefined", "function fn(): any"],
        "answer": "function fn(): void",
        "difficulty": "Easy",
        "explanation": "'void' is used to indicate a function returns nothing.",
        "category": "Type Annotations"
    },
    {
        "question": "What is wrong with: ```typescript\nlet x: number = 'text';```",
        "options": ["Type mismatch", "Syntax error", "No error", "Missing declaration"],
        "answer": "Type mismatch",
        "difficulty": "Easy",
        "explanation": "Assigning a string to a number-typed variable causes a type error.",
        "category": "Type Annotations"
    },
    {
        "question": "How do you annotate an array of numbers?",
        "options": ["let arr: number[]", "let arr: Array<number>", "let arr: [number]", "Both A and B"],
        "answer": "Both A and B",
        "difficulty": "Medium",
        "explanation": "TypeScript supports both 'number[]' and 'Array<number>' for number arrays.",
        "category": "Type Annotations"
    },
    {
        "question": "What is the purpose of an interface in TypeScript?",
        "options": ["Defines object shape", "Creates a class", "Declares variables", "Compiles code"],
        "answer": "Defines object shape",
        "difficulty": "Easy",
        "explanation": "Interfaces define the structure of objects, specifying properties and their types.",
        "category": "Interfaces"
    },
    {
        "question": "What is the output of: ```typescript\ninterface User { name: string; } let user: User = { name: 'Alice' }; console.log(user.name);```",
        "options": ["Alice", "undefined", "Error", "null"],
        "answer": "Alice",
        "difficulty": "Easy",
        "explanation": "The interface ensures 'user' has a 'name' property, logging 'Alice'.",
        "category": "Interfaces"
    },
    {
        "question": "Can an interface include optional properties?",
        "options": ["Yes, using ?", "No", "Only with !", "Only with readonly"],
        "answer": "Yes, using ?",
        "difficulty": "Medium",
        "explanation": "Optional properties are marked with '?' in an interface, e.g., 'age?: number'.",
        "category": "Interfaces"
    },
    {
        "question": "What is wrong with: ```typescript\ninterface Point { x: number; } let p: Point = { x: 1, y: 2 };```",
        "options": ["Extra property 'y'", "Missing property 'x'", "Type mismatch", "No error"],
        "answer": "Extra property 'y'",
        "difficulty": "Medium",
        "explanation": "TypeScript flags extra properties not defined in the interface as errors in strict mode.",
        "category": "Interfaces"
    },
    {
        "question": "How do you extend an interface?",
        "options": ["interface B extends A {}", "interface B : A {}", "interface B implements A {}", "interface B = A {}"],
        "answer": "interface B extends A {}",
        "difficulty": "Medium",
        "explanation": "The 'extends' keyword allows an interface to inherit properties from another.",
        "category": "Interfaces"
    },
    {
        "question": "What is the output of: ```typescript\nclass Person { name: string = 'John'; } let p = new Person(); console.log(p.name);```",
        "options": ["John", "undefined", "Error", "null"],
        "answer": "John",
        "difficulty": "Easy",
        "explanation": "The class initializes 'name' to 'John', which is logged.",
        "category": "Classes"
    },
    {
        "question": "How do you define a private property in a class?",
        "options": ["private x: number", "#x: number", "protected x: number", "Both A and B"],
        "answer": "Both A and B",
        "difficulty": "Medium",
        "explanation": "TypeScript supports 'private' keyword and '#x' for private fields (ES private fields).",
        "category": "Classes"
    },
    {
        "question": "What does 'extends' do in a class declaration?",
        "options": ["Inherits from another class", "Implements an interface", "Declares a method", "Creates an instance"],
        "answer": "Inherits from another class",
        "difficulty": "Easy",
        "explanation": "'extends' allows a class to inherit properties and methods from a parent class.",
        "category": "Classes"
    },
    {
        "question": "What is the output of: ```typescript\nclass A { x = 1; } class B extends A { x = 2; } let b = new B(); console.log(b.x);```",
        "options": ["1", "2", "Error", "undefined"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "The subclass 'B' overrides the 'x' property, so 'b.x' is 2.",
        "category": "Classes"
    },
    {
        "question": "What does 'implements' do in a class?",
        "options": ["Ensures interface compliance", "Inherits a class", "Declares a method", "Creates a constructor"],
        "answer": "Ensures interface compliance",
        "difficulty": "Medium",
        "explanation": "'implements' ensures a class adheres to an interface’s structure.",
        "category": "Classes"
    },
    {
        "question": "What is a generic in TypeScript?",
        "options": ["A type that works with any data type", "A fixed type", "A class method", "An interface property"],
        "answer": "A type that works with any data type",
        "difficulty": "Easy",
        "explanation": "Generics allow reusable code that works with different types while maintaining type safety.",
        "category": "Generics"
    },
    {
        "question": "What is the output of: ```typescript\nfunction identity<T>(arg: T): T { return arg; }\nconsole.log(identity<number>(42));```",
        "options": ["42", "undefined", "Error", "null"],
        "answer": "42",
        "difficulty": "Medium",
        "explanation": "The generic function 'identity' returns the input value, typed as 'number', so it logs 42.",
        "category": "Generics"
    },
    {
        "question": "How do you constrain a generic type?",
        "options": ["extends", "implements", "restrict", "typeof"],
        "answer": "extends",
        "difficulty": "Medium",
        "explanation": "'extends' constrains a generic type to a specific type or interface, e.g., 'T extends string'.",
        "category": "Generics"
    },
    {
        "question": "What is wrong with: ```typescript\nfunction fn<T>(x: T): T { return x.length; }```",
        "options": ["'length' is not guaranteed on T", "Syntax error", "No error", "Missing return type"],
        "answer": "'length' is not guaranteed on T",
        "difficulty": "Hard",
        "explanation": "Without a constraint like 'T extends { length: number }', 'length' is not guaranteed.",
        "category": "Generics"
    },
    {
        "question": "What is the output of: ```typescript\nfunction merge<T, U>(a: T, b: U) { return { ...a, ...b }; }\nconsole.log(merge({ x: 1 }, { y: 2 }).y);```",
        "options": ["2", "undefined", "Error", "1"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "The generic function merges two objects, and the resulting object has property 'y' with value 2.",
        "category": "Generics"
    },
    {
        "question": "What is an enum in TypeScript?",
        "options": ["A set of named constants", "A class", "A function", "A variable"],
        "answer": "A set of named constants",
        "difficulty": "Easy",
        "explanation": "Enums define a set of named constants, often used for fixed values like states or categories.",
        "category": "Enums"
    },
    {
        "question": "What is the output of: ```typescript\nenum Color { Red, Green, Blue }\nconsole.log(Color.Green);```",
        "options": ["1", "Green", "Error", "undefined"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "By default, enum values are numeric, starting at 0, so 'Green' is 1.",
        "category": "Enums"
    },
    {
        "question": "How do you create a string enum?",
        "options": ["enum E { A = 'a' }", "enum E { A: 'a' }", "enum E { A = string }", "enum E = 'a'"],
        "answer": "enum E { A = 'a' }",
        "difficulty": "Medium",
        "explanation": "String enums assign string values to enum members, e.g., 'A = 'a''. ",
        "category": "Enums"
    },
    {
        "question": "What is the output of: ```typescript\nenum Status { Active = 1, Inactive }\nconsole.log(Status.Inactive);```",
        "options": ["2", "1", "Inactive", "Error"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "Enums increment numeric values, so 'Inactive' is 2 after 'Active = 1'.",
        "category": "Enums"
    },
    {
        "question": "How do you access an enum’s value by its name?",
        "options": ["Enum['name']", "Enum.get('name')", "Enum.name", "Enum.value('name')"],
        "answer": "Enum['name']",
        "difficulty": "Medium",
        "explanation": "Enums are objects at runtime, so 'Enum['name']' accesses the value by name.",
        "category": "Enums"
    },
    {
        "question": "What does TypeScript’s type inference do?",
        "options": ["Automatically assigns types", "Compiles code", "Removes types", "Generates classes"],
        "answer": "Automatically assigns types",
        "difficulty": "Easy",
        "explanation": "Type inference assigns types to variables based on their initial values when no type is specified.",
        "category": "Type Inference"
    },
    {
        "question": "What type is inferred for: ```typescript\nlet x = 42;```",
        "options": ["number", "any", "string", "undefined"],
        "answer": "number",
        "difficulty": "Easy",
        "explanation": "TypeScript infers 'number' based on the value 42.",
        "category": "Type Inference"
    },
    {
        "question": "What is inferred for: ```typescript\nconst x = [1, 2, 3];```",
        "options": ["number[]", "any[]", "Array<number>", "Both A and C"],
        "answer": "Both A and C",
        "difficulty": "Medium",
        "explanation": "TypeScript infers 'number[]' or 'Array<number>' for an array of numbers.",
        "category": "Type Inference"
    },
    {
        "question": "What happens if you assign a string to: ```typescript\nlet x = 42; x = 'text';```",
        "options": ["Type error", "No error", "Converts to string", "undefined"],
        "answer": "Type error",
        "difficulty": "Medium",
        "explanation": "TypeScript infers 'x' as 'number', so assigning a string causes a type error.",
        "category": "Type Inference"
    },
    {
        "question": "What is inferred for: ```typescript\nfunction fn(x) { return x; }```",
        "options": ["any", "void", "unknown", "number"],
        "answer": "any",
        "difficulty": "Medium",
        "explanation": "Without type annotations, TypeScript infers 'any' for untyped parameters and return types.",
        "category": "Type Inference"
    },
    {
        "question": "What is a union type in TypeScript?",
        "options": ["A type that can be one of multiple types", "A type combining all properties", "A fixed type", "A class type"],
        "answer": "A type that can be one of multiple types",
        "difficulty": "Easy",
        "explanation": "Union types, e.g., 'string | number', allow a value to be one of several types.",
        "category": "Union and Intersection Types"
    },
    {
        "question": "What is the output of: ```typescript\nlet x: string | number = 10; x = 'test'; console.log(x);```",
        "options": ["test", "10", "Error", "undefined"],
        "answer": "test",
        "difficulty": "Medium",
        "explanation": "The union type allows 'x' to be a string or number, so it logs 'test'.",
        "category": "Union and Intersection Types"
    },
    {
        "question": "What is an intersection type?",
        "options": ["Combines multiple types into one", "Selects one type", "Excludes types", "Creates a union"],
        "answer": "Combines multiple types into one",
        "difficulty": "Medium",
        "explanation": "Intersection types, e.g., 'A & B', combine properties of multiple types.",
        "category": "Union and Intersection Types"
    },
    {
        "question": "What is wrong with: ```typescript\ntype A = { x: number }; type B = { y: string }; let obj: A & B = { x: 1 };```",
        "options": ["Missing 'y' property", "Type mismatch", "No error", "Invalid syntax"],
        "answer": "Missing 'y' property",
        "difficulty": "Medium",
        "explanation": "An intersection type 'A & B' requires all properties from both types.",
        "category": "Union and Intersection Types"
    },
    {
        "question": "What does this log: ```typescript\ntype A = { x: number }; type B = { y: string }; let obj: A | B = { x: 1 }; console.log(obj.x);```",
        "options": ["1", "undefined", "Error", "null"],
        "answer": "Error",
        "difficulty": "Hard",
        "explanation": "With a union type 'A | B', 'x' is not guaranteed, requiring a type guard to access it safely.",
        "category": "Union and Intersection Types"
    },
    {
        "question": "What is a type guard in TypeScript?",
        "options": ["Narrows a type within a scope", "Declares a type", "Compiles code", "Creates an interface"],
        "answer": "Narrows a type within a scope",
        "difficulty": "Easy",
        "explanation": "Type guards, like 'typeof' or 'instanceof', narrow types for safe access.",
        "category": "Type Guards"
    },
    {
        "question": "What does this log: ```typescript\nfunction fn(x: string | number) { if (typeof x === 'string') { console.log(x.length); } } fn('test');```",
        "options": ["4", "undefined", "Error", "null"],
        "answer": "4",
        "difficulty": "Medium",
        "explanation": "The 'typeof' type guard narrows 'x' to 'string', allowing safe access to 'length'.",
        "category": "Type Guards"
    },
    {
        "question": "What is a user-defined type guard?",
        "options": ["A function returning 'x is Type'", "A type annotation", "A class method", "An enum"],
        "answer": "A function returning 'x is Type'",
        "difficulty": "Medium",
        "explanation": "User-defined type guards use a return type like 'x is Type' to narrow types.",
        "category": "Type Guards"
    },
    {
        "question": "What is wrong with: ```typescript\nfunction isString(x: any): x is string { return x.length !== undefined; }```",
        "options": ["Incorrect type check", "No error", "Syntax error", "Missing return type"],
        "answer": "Incorrect type check",
        "difficulty": "Hard",
        "explanation": "Checking 'length' is not a reliable way to confirm a string, as other types have 'length'.",
        "category": "Type Guards"
    },
    {
        "question": "What does this log: ```typescript\nclass A { x = 1; } function isA(obj: any): obj is A { return obj instanceof A; } let a = new A(); console.log(isA(a));```",
        "options": ["true", "false", "Error", "undefined"],
        "answer": "true",
        "difficulty": "Medium",
        "explanation": "The 'instanceof' type guard confirms 'a' is an instance of 'A', logging 'true'.",
        "category": "Type Guards"
    },
    {
        "question": "What is a decorator in TypeScript?",
        "options": ["A function that modifies class behavior", "A type annotation", "A variable", "An interface"],
        "answer": "A function that modifies class behavior",
        "difficulty": "Easy",
        "explanation": "Decorators are functions that can modify classes, methods, or properties at declaration time.",
        "category": "Decorators"
    },
    {
        "question": "What is required to use decorators in TypeScript?",
        "options": ["'experimentalDecorators' in tsconfig.json", "'useDecorators' in tsconfig.json", "'strict' mode", "No special configuration"],
        "answer": "'experimentalDecorators' in tsconfig.json",
        "difficulty": "Medium",
        "explanation": "Decorators require 'experimentalDecorators: true' in tsconfig.json to be enabled.",
        "category": "Decorators"
    },
    {
        "question": "What does this log: ```typescript\nfunction log(target: any, key: string) { console.log(key); } class C { @log x = 1; } new C();```",
        "options": ["x", "undefined", "Error", "null"],
        "answer": "x",
        "difficulty": "Medium",
        "explanation": "The decorator 'log' is applied to the 'x' property, logging its key 'x' during class initialization.",
        "category": "Decorators"
    },
    {
        "question": "What is a method decorator used for?",
        "options": ["Modifies method behavior", "Declares a type", "Creates a class", "Defines a variable"],
        "answer": "Modifies method behavior",
        "difficulty": "Medium",
        "explanation": "Method decorators can wrap or modify the behavior of class methods.",
        "category": "Decorators"
    },
    {
        "question": "What is wrong with: ```typescript\n@decorator class C {}``` without 'experimentalDecorators'?",
        "options": ["Compilation error", "No error", "Runtime error", "Syntax error"],
        "answer": "Compilation error",
        "difficulty": "Medium",
        "explanation": "Decorators require 'experimentalDecorators: true' in tsconfig.json, or the compiler fails.",
        "category": "Decorators"
    },
    {
        "question": "What is the output of: ```typescript\nlet x: any = 42; console.log(x);```",
        "options": ["42", "undefined", "Error", "null"],
        "answer": "42",
        "difficulty": "Easy",
        "explanation": "The 'any' type allows any value, so 'x' logs 42 without type errors.",
        "category": "TypeScript"
    },
    {
        "question": "What is the 'target' in tsconfig.json?",
        "options": ["Output JavaScript version", "Input file path", "Module type", "Compiler mode"],
        "answer": "Output JavaScript version",
        "difficulty": "Medium",
        "explanation": "'target' specifies the JavaScript version (e.g., 'ES2020') for compiled output.",
        "category": "TS Compiler"
    },
    {
        "question": "How do you annotate a function parameter as optional?",
        "options": ["param?: type", "param: type?", "param: ?type", "param = type"],
        "answer": "param?: type",
        "difficulty": "Medium",
        "explanation": "Optional parameters are marked with '?' in function declarations.",
        "category": "Type Annotations"
    },
    {
        "question": "What does this log: ```typescript\ninterface A { x: number; } let a: A = { x: 1 }; console.log(a.x);```",
        "options": ["1", "undefined", "Error", "null"],
        "answer": "1",
        "difficulty": "Easy",
        "explanation": "The interface ensures 'x' is a number, so 'a.x' logs 1.",
        "category": "Interfaces"
    },
    {
        "question": "What is the output of: ```typescript\nclass A { constructor(public x: number) {} } let a = new A(5); console.log(a.x);```",
        "options": ["5", "undefined", "Error", "null"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The 'public' parameter property automatically assigns 'x' to the instance, logging 5.",
        "category": "Classes"
    },
    {
        "question": "What does this log: ```typescript\nfunction fn<T extends { length: number }>(x: T) { console.log(x.length); } fn('test');```",
        "options": ["4", "undefined", "Error", "null"],
        "answer": "4",
        "difficulty": "Medium",
        "explanation": "The generic constraint ensures 'x' has a 'length' property, so 'test' logs 4.",
        "category": "Generics"
    },
    {
        "question": "What is the output of: ```typescript\nenum E { A = 'a' } console.log(E.A);```",
        "options": ["a", "0", "Error", "undefined"],
        "answer": "a",
        "difficulty": "Medium",
        "explanation": "String enums assign string values, so 'E.A' is 'a'.",
        "category": "Enums"
    },
    {
        "question": "What is inferred for: ```typescript\nlet x = 'hello';```",
        "options": ["string", "any", "text", "undefined"],
        "answer": "string",
        "difficulty": "Easy",
        "explanation": "TypeScript infers 'string' based on the value 'hello'.",
        "category": "Type Inference"
    },
    {
        "question": "What does this log: ```typescript\nfunction fn(x: string | number) { if (typeof x === 'number') { console.log(x + 1); } } fn(10);```",
        "options": ["11", "undefined", "Error", "null"],
        "answer": "11",
        "difficulty": "Medium",
        "explanation": "The type guard narrows 'x' to 'number', so 'x + 1' logs 11.",
        "category": "Type Guards"
    },
    {
        "question": "What does this log: ```typescript\nfunction log(target: any, key: string, descriptor: PropertyDescriptor) { console.log(key); } class C { @log method() {} } new C();```",
        "options": ["method", "undefined", "Error", "null"],
        "answer": "method",
        "difficulty": "Medium",
        "explanation": "The method decorator logs the method name 'method' during class initialization.",
        "category": "Decorators"
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


