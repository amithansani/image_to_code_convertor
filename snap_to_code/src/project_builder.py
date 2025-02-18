from .text_extractor import TextExtractor
from .file_generator import FileGenerator
from .code_formatter import CodeFormatter
from .utils import has_directories, list_folders, list_jpg_files_glob, has_files, create_folder
from pathlib import Path
import asyncio

class BuildProject:

    def __init__(self, project_path: Path, output_path: Path):
        self.project_path = project_path
        self.output_path = output_path
        self.text_extractor = TextExtractor()
        self.file_generator = FileGenerator()
        self.code_formatter = CodeFormatter()

    async def build_project(self):
        async for update in self._build_path(self.project_path, self.output_path):
            yield update

    async def _build_path(self, project_path, output_path):
        if has_directories(project_path):
            for folder in list_folders(project_path):
                new_project_path = project_path / folder
                new_output_path = output_path / folder

                if has_directories(new_project_path):
                    create_folder(folder, output_path)
                    async for update in self._build_path(new_project_path, new_output_path):
                        yield update

                if has_files(new_project_path):
                    code_text=""
                    for file in list_jpg_files_glob(new_project_path):
                        file_path = new_project_path / file
                        code_text = code_text + self.text_extractor.extract_text(file_path)

                    formatted_code = self.code_formatter.format_code(code_text)
                    formatted_code = formatted_code[9:-3]

                    py_file_path = new_output_path.with_suffix(".py")
                    self.file_generator.create_file(py_file_path, formatted_code)

                    yield f"Processing {py_file_path}..."
                    await asyncio.sleep(0.5)  # Simulate delay for UI update
        else:
            return
