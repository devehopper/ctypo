# config.py
#
# Configuration variables that gets
# imported from $PROJECT_DIR/.typo/project.json.

class Config:
    project_name = ""
    project_authors = []
    project_owner = ""

    package_channel = ""
    package_repository = ""

    metadata = {}

    def update(self):
        self.metadata = {
            "project": {
                "name": self.project_name,
                "authors": self.project_authors,
                "owner": self.project_owner,
            },

            "version": {
                "maximum": "0:0.1",
                "minimum": "0:0.1"
            },

            "packages": {
                "channel": self.package_channel,
                "repository": self.package_repository
            }
        }
