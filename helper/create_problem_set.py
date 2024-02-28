import os
from pathlib import Path

def get_input() -> str:
    output = ""
    while True:
        line = input()
        if line == "DONE":
            break
        output += line + "\n"
    return output.strip()

def read_file(relative_path) -> str:
    current_dir = Path(os.path.dirname(__file__))
    file_path = current_dir / relative_path
    
    with open(file_path, 'r') as file:
        return file.read()

def create_problem_set():
    problem_name = input("Enter the name of the problem: ")

    problem_dir = f"./{problem_name}"
    os.makedirs(problem_dir, exist_ok=True)

    num_inputs = int(input("Enter the number of inputs: "))
    
    for i in range(1, num_inputs + 1):
        print(f"Enter input {i} (say DONE when complete):")
        input_text = get_input()
        print(f"Enter expected output for input {i} (say DONE when complete:")
        output_text = get_input()
        
        with open(f"{problem_dir}/{i}.in", "w") as input_file:
            input_file.write(input_text)
        with open(f"{problem_dir}/{i}.out", "w") as output_file:
            output_file.write(output_text)
    
    lang = input("Which language (cpp, py, java): ")

    solution_file = "solution.py"
    solution_content = read_file("solution_template/py.txt")
    if lang == "cpp":
        solution_file = "solution.cpp"
        solution_content = read_file("solution_template/cpp.txt")
    elif lang == "java":
        solution_file = "solution.java"
        solution_content = read_file("solution_template/java.txt")
    with open(f"{problem_dir}/{solution_file}", "w") as solution_file:
        solution_file.write(solution_content)

    print(f"Problem set '{problem_name}' created with {num_inputs} inputs.")

if __name__ == "__main__":
    create_problem_set()
