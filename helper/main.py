from pathlib import Path
from file_executor import FileExecutor
from arg_parser import parse_arguments
from comparator import compare_outputs

def main():
    args = parse_arguments()
    
    file_path = None
    for ext in FileExecutor.methods:
        path = Path(f"./{args.name}/solution.{ext}")
        if path.exists():
            file_path = path
            break

    if not file_path:
        print("Error: No file found for the given problem name")
        return

    print(f"Running problem: ./{file_path}")

    input_data = Path(f"./{args.name}/{args.input}").read_text()
    expected_output_path = Path(f"./{args.name}/{args.input}").with_suffix('.out')
    expected_output = expected_output_path.read_text()

    actual_output = FileExecutor.compile_and_run(file_path, input_data)

    compare_outputs(actual_output, expected_output)

if __name__ == "__main__":
    main()