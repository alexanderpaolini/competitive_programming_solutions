import subprocess
import os
from pathlib import Path

class FileExecutor:
    @staticmethod
    def _run_cpp(file_path: Path, input_data: str) -> str:
        parent_dir = file_path.parent
        executable = file_path.parent / file_path.stem
        subprocess.run(["g++", file_path, "-o", executable], check=True)
        process = subprocess.Popen(executable, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        output, _ = process.communicate(input=input_data)
        os.remove(executable)
        return output

    @staticmethod
    def _run_java(file_path: Path, input_data: str) -> str:
        parent_dir = file_path.parent
        subprocess.run(["javac", file_path], check=True)
        class_name = file_path.parent / file_path.stem
        process = subprocess.Popen(["java", "-cp", parent_dir, class_name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        output, _ = process.communicate(input=input_data)
        os.remove(str(class_name) + ".class")
        return output

    @staticmethod
    def _run_python(file_path: Path, input_data: str) -> str:
        process = subprocess.Popen(["python3", file_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        output, _ = process.communicate(input=input_data)
        return output

    methods = {
        'cpp': _run_cpp,
        'java': _run_java,
        'py': _run_python
    }

    @staticmethod
    def compile_and_run(file_path: Path, input_data: str) -> str:
        extension = file_path.suffix[1:]
        if extension in FileExecutor.methods:
            return FileExecutor.methods[extension](file_path, input_data)
        else:
            raise Exception("Unsupported file extension")