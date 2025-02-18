from pathlib import Path
from .src.project_builder import BuildProject
from .src.package_generator import PackageGenerator

class SnapToCode:
    def __init__(self, input_path: str, output_path: str):
        self.project_path = Path(input_path)
        self.output_path = Path(output_path)

    async def run(self):
        try:
            self._validate_path()
            async for update in BuildProject(self.project_path, self.output_path).build_project():
                yield update  # Stream each progress update
            # yield "All files processed successfully!"

            self.ProjectGenerator = PackageGenerator(self.output_path)
            self.ProjectGenerator.create_init_files()
            yield "Project created successfully!"

        except Exception as e:
            yield f"Error: {str(e)}"


    def _validate_path(self):
        if not self.project_path.exists():
            raise ValueError(f"Input path {self.project_path} does not exist.")
        if not self.output_path.exists():
            raise ValueError(f"Output path {self.output_path} does not exist.")
        if not self.project_path.is_dir():
            raise ValueError(f"Input path {self.project_path} is not a directory.")
        if not self.output_path.is_dir():
            raise ValueError(f"Output path {self.output_path} is not a directory.")
