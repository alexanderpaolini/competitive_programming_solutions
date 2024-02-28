# Competitive Programming Solutions

This folder contains my solutions to various competitive programming challenges I've participated in, both online and in-person.

## Repository Structure

The solutions are organized in the following manner:

### Online Competitions:

For challenges participated in through online platforms, solutions are stored in directories following the standard format:

```
./COMP/PROBLEM/
├── solution.ext      # Solution file in the appropriate programming language.
├── NAME.in           # Input file for testing the solution. There can be multiple input files.
└── NAME.out          # Output file corresponding to each NAME.in file, containing expected results.
```

**Example**:

```
./codeforces/1000/1a/
├── solution.py
├── 1.in
└── 1.out
```

### In-Person Competitions:

Solutions to challenges from in-person competitions are stored directly within the competition directory, following the format `./COMP/filename.ext`, where:

- `filename.ext` represents the solution file with its appropriate extension.

## Testing Solutions

To test the solutions, I utilize the helper functions in `./helper`. It automatically selects the solution file and test it with the supplied input file.

### Using the Helper Utility

Using the helper scripts is quite easy. Use format: `python main.py --name=PROBLEM_LOCATION --input=NUMBER.in` It then runs the `solution.ext` in the folder with the `NUMBER.in` input, comparing it to the `NUMBER.out` output file.

**Example:**
```sh
python main.py --name=Problem1 --input=1.in
```

This command will run the utility for a problem named `Problem1` using `1.in` as the input file. The utility will look for a solution file within the `./Problem1/` directory, execute it with the contents of `1.in`, and compare its output against the expected output defined in a corresponding `1.out` file.

#### Using the Helper Utility with VSCode

The helper scripts have been implemented as tasks in VSCode. 

So far, there is one task:

- `Test standard solution`
    - Asks for input number.
    - Tests the current file with the provided solution number.

## Contributing

Please don't change my solutions.

However, if better solutions for problems exist, please do make issues explaining how they can be done. I likely won't change them.
