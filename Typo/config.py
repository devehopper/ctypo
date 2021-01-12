# config.py
#
# Configuration variables that gets
# imported from $PROJECT_DIR/.typo/project.json.

project_name: str
project_authors: list
project_owner: str

package_channel: str
package_repository: str

metadata: dict

def update():
    metadata = {
        "project": {
            "name": project_name,
            "authors": project_authors,
            "owner": project_owner,
        },

        "version": {
            "maximum": "0:0.1",
            "minimum": "0:0.1"
        },

        "packages": {
            "channel": package_channel,
            "repository": package_repository
        }
    }
