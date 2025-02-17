from .text_extractor import TextExtractor
from .file_generator import FileGenerator
from .code_formatter import CodeFormatter
from .utils import has_directories, list_folders, list_jpg_files_glob, has_files,create_folder
from pathlib import Path

class BuildProject:

    def __init__(self, project_path:Path,output_path:Path):
        self.project_path = project_path
        self.output_path = output_path
        self.text_extractor = TextExtractor()
        self.file_generator = FileGenerator()
        self.code_formatter = CodeFormatter()


    def build_project(self):
        self._build_path(self.project_path,self.output_path)

    @staticmethod
    def _build_path(project_path,output_path):
        if has_directories(project_path):
            for folder in list_folders(project_path):
                new_project_path = project_path  / folder
                new_output_path = output_path / folder
                # print(project_path[6:])

                if has_directories(new_project_path):
                    create_folder(folder, output_path)
                    BuildProject._build_path(new_project_path,new_output_path)
                if has_files(new_project_path):
                    # create_py_file(path[6:]+".py")
                    code_text = ""
                    for file in list_jpg_files_glob(new_project_path):
                        file_path = new_project_path / file
                        code_text = code_text + TextExtractor().extract_text(file_path) + "\n"
                    formatted_code = CodeFormatter().format_code(code=code_text)
                    py_file_path = new_output_path.with_suffix(".py")
                    FileGenerator().create_file(py_file_path, formatted_code)




        else:
            return



