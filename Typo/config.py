# config.py
#
# Configuration variables that gets
# imported from $PROJECT_DIR/.typo/project.json.

class config:
    project_name: str
    project_authors: list
    project_owner: str

    package_channel: str
    package_repository: str

    metadata: dict

    @staticmethod
    def update():
        metadata = {
            "project": {
                "name": config.project_name,
                "authors": config.project_authors,
                "owner": config.project_owner,
            },

            "version": {
                "maximum": "0:0.1",
                "minimum": "0:0.1"
            },

            "packages": {
                "channel": config.package_channel,
                "repository": config.package_repository
            }
        }
