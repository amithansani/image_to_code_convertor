class FileGenerator:
    def create_file(self, file_path: str, content: str) -> None:
        try:
            with open(file_path, "w") as file:
                file.write(content)
        except Exception as e:
            print(f"Error creating file: {e}")
            return

        print(f"File created at: {file_path}")
