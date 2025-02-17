import os

class PackageGenerator:
    def __init__(self,path):
        self.path = path
    def create_init_files(self):
        path=self.path
        print(path)
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                init_file_path = os.path.join(dir_path, '__init__.py')
                if not os.path.exists(init_file_path):
                    with open(init_file_path, 'w') as f:
                        pass

        return True

