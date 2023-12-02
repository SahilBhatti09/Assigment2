class FileProcessor:
    def __init__(self, input_file, output_file_task1, output_file_task2):
        self.input_file = input_file
        self.output_file_task1 = output_file_task1
        self.output_file_task2 = output_file_task2

    def file_exists(self, file_path):
        with open(file_path, 'r'):
            pass
        return True

    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def write_file(self, file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)

    def task_1(self):
        if not self.file_exists(self.input_file):
            print(f"Error: File '{self.input_file}' not found.")
            return

        code = self.read_file(self.input_file)        
        with open(self.input_file, 'r') as file:
            code = file.read()

        code_lines = [line for line in code.split('\n') if not line.strip().startswith('import') and not line.strip().startswith('from')]

        # Remove docstring
        inside_docstring = False
        new_code_lines = []
        for line in code_lines:
            if '"""' in line:
                inside_docstring = not inside_docstring
            elif not inside_docstring:
                new_code_lines.append(line)

        code_lines = [line for line in new_code_lines if not line.strip().startswith('#')]

        code_lines = [line for line in code_lines if 'input(' not in line]

        # Remove blank lines and empty spaces
        code = '\n'.join(line.strip() for line in code_lines if line.strip())

        # Save modified code to Output.01
        with open(self.output_file_task1, 'w') as file:
            file.write(code)

        # Print modified code
        print("Task 1 Output:")
        print(code)
        print("----------------------------")

    def task_2(self):
        if not self.file_exists(self.output_file_task1):
            print(f"Error: File '{self.output_file_task1}' not found.")
            return

        modified_code = self.read_file(self.output_file_task1)

        with open(self.output_file_task1, 'r') as file:
            modified_code = file.read()
        
        # Put all code into one line with semicolons
        modified_code = modified_code.replace('\n', ';')

        # Add "$" at the end of the code
        modified_code += '$'

        # Save modified code to Output.02
        with open(self.output_file_task2, 'w') as file:
            file.write(modified_code)

        print("\nTask 2 Output:")
        print(modified_code)
        print("----------------------------")

    def task_3(self):
        if not self.file_exists(self.output_file_task2):
            print(f"Error: File '{self.output_file_task2}' not found.")
            return

        modified_code = self.read_file(self.output_file_task2)
        with open(self.output_file_task2, 'r') as file:
            modified_code = file.read()

                # Find all tokens
        tokens = self.extract_tokens(modified_code)

        # Print tokens
        print("\nTask 3 Output:")
        print(tokens)
        print("----------------------------")

        # Print total number of tokens
        print(f"Total number of tokens: {len(tokens)}")

class CodeProcessor(FileProcessor):
    def __init__(self, input_file="Code.txt", output_file_task1="Output.01", output_file_task2="Output.02"):
        super().__init__(input_file, output_file_task1, output_file_task2)

    def extract_tokens(self, code):
        # Extract tokens without using regular expressions
        tokens = []
        current_token = ''
        for char in code:
            if char.isalnum() or char == '_':
                current_token += char
            else:
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
                if char.isspace():
                    continue
                tokens.append(char)
        if current_token:
            tokens.append(current_token)
        return tokens

# Example Usage
processor = CodeProcessor()
processor.task_1()
processor.task_2()
processor.task_3()

print("Coded by: Sahil Bhatti")