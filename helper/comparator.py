import difflib

def compare_outputs(actual_output: str, expected_output: str):
    # actual_lines = actual_output.strip().splitlines()
    # expected_lines = expected_output.strip().splitlines()
    # diff = difflib.unified_diff(expected_lines, actual_lines, fromfile='Expected Output', tofile='Actual Output', lineterm='')

    # differences = '\n'.join(diff)
    # if differences:
    #     print("Differences detected:")
    #     print(differences)
    # else:
    #     print("Outputs are the same.")
    actual_output = actual_output.strip()
    expected_output = expected_output.strip()
    if actual_output != expected_output:
        print("Differences detected:")
        print("Actual Output:")
        print(actual_output)
        print("Expected Output:")
        print(expected_output)
    else:
        print("Outputs are the same.")