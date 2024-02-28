# Helper Utility

A basic helper utiity create to aide in competitive programmong problem solving.

## Components

The utility is comprised of four main components:

1. **arg_parser.py**: Parses command-line arguments.
2. **comparator.py**: Compares actual program output with expected output.
3. **file_executor.py**: Compiles and runs code files.
4. **main.py**: Integrates the above components, orchestrating the process of running a solution file and comparing its output.
5. **create_problem_set.py**: Create boilerplate code for each language to bootstrap solution creation.

### 1. arg_parser.py

Parses command-line arguments provided to the utility.

- `parse_arguments()`: Parses command-line arguments and returns an object containing the values associated with each argument.

#### Command-Line Arguments

- `--name`: The name of the problem. This argument is required.
- `--input`: The name of the input file to be used. This argument is required.

### 2. comparator.py

Compares the actual output of a code file against an expected output, highlighting any differences.

- `compare_outputs(actual_output: str, expected_output: str)`: Compares `actual_output` against `expected_output` and prints the differences, if any.

### 3. file_executor.py

Compiles and runs code files in various programming languages.

- `FileExecutor`: A class that contains methods for compiling and running code files.
- `_run_LANGUAGE(file_path: Path, input_data: str)`: Compiles and runs the specified code.
- `compile_and_run(file_path: Path, input_data: str)`: Determines the file type and invokes the appropriate method to compile and run the file.

### 4. main.py

Serves as the entry point for the utility, integrating all components to compile and run the code file, and then compare its output.

- Parses command-line arguments to determine the problem name and input file.
- Identifies the correct solution file based on supported file extensions.
- Reads the input and expected output files.
- Executes the solution file with the provided input.
- Compares the actual output against the expected output.

### 5. create_problem_set.py

Interactive python script to copy boilerplate code to the specified problem directory. Allows for `n` solutions consisting of `[1-n].in` and `[1-n].out`.

- Creates the directory for the corresponding problem name.
- Asks how many sample input files are provided
- Creates inputs and corresponding output files for each given input
- Automaticallly copies the specified language's boilerplate solution code to `PROBLEM_PATH/soluton.ext`
- Example: `python create_problem_set.py`

## Usage Example

```sh
python main.py --name=Problem1 --input=1.in
```

This command will run the utility for a problem named `Problem1` using `1.in` as the input file. The utility will look for a solution file within the `./Problem1/` directory, execute it with the contents of `1.in`, and compare its output against the expected output defined in a corresponding `1.out` file.

## Error Handling

- If no file is found for the given problem name, an error message is printed.
- Unsupported file extensions will result in an exception being raised.

## Extensibility

The utility can be extended to support more programming languages by adding additional methods to the `FileExecutor` class.
