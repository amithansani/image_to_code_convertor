from pathlib import Path
from .src.project_builder import BuildProject
from .src.package_generator import PackageGenerator
class SnapToCode:
    def __init__(self, input_path:Path,output_path:Path):
        self.project_path=Path(input_path) if input_path else input_path
        self.output_path=Path(output_path)



    def run(self):
        try:
            self._validate_path()
            BuildProject(self.project_path, self.output_path).build_project()
            PackageGenerator(self.output_path).create_init_files()
        except Exception as e:
            return {"error": str(e)}



    def _validate_path(self):
        if not self.project_path.exists():
            raise ValueError(f"Input path {self.project_path} does not exist.")
        if not self.output_path.exists():
            raise ValueError(f"Output path {self.output_path} does not exist.")
        if not self.project_path.is_dir():
            raise ValueError(f"Input path {self.project_path} is not a directory.")
        if not self.output_path.is_dir():
            raise ValueError(f"Output path {self.output_path} is not a directory.")




