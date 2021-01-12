# project_json.py
#
# The ProjectJSONGenerator.generate()
# method is used for generating JSON file
# that includes configuration and information
# about the Typo project.

import json

class ProjectJSONAlreadyLoaded(Exception):
    pass

class ProjectJSONNotLoaded(Exception):
    pass

class ProjectJSONGenerator:
    config: dict
    json_file: str

    def __init__(self, config: dict, json_file: str):
        self.config = config
        self.json_file = json_file

    def generate(self):
        self.json_file_object = open(self.json_file, "w+")
        self.json_file_object.write(json.dumps(self.config, indent=4))

        self.json_file_object.close()

class ProjectJSONLoader:
    loaded: bool
    json_file: str

    def __init__(self, json_file: str):
        self.loaded = False
        self.json_file = json_file

    def load(self):
        self.json_file_object = open(self.json_file, "r")
        self.project_json = json.loads(self.json_file_object.read())
        self.loaded = True

    def unload(self):
        if self.loaded:
            self.loaded = False
            self.json_file_object.close()

        else:
            raise ProjectJSONAlreadyLoaded("Project JSON is already loaded.");

    def read(self):
        if self.loaded:
            return self.project_json

        else:
            raise ProjectJSONNotLoaded("Load Project JSON before reading it.")
