from argparse import ArgumentParser

def parse_arguments():
    parser = ArgumentParser(description="Compile and run code files.")
    parser.add_argument("--name", required=True, help="Problem name")
    parser.add_argument("--input", required=True, help="Input file name")
    return parser.parse_args()
