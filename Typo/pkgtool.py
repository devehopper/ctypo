# pkgtool.py
#
# Common functions
# that used by package
# manager.

import linker
import config
import compiler
from config_class import configuration

from urllib import request
import zipfile
import shutil
import os

package_channel = "stable"
package_repository = "https://github.com/typolang/pkgrepo"

class PackageTool:
    package: str

    def __init__(self, package: str):
        self.package = package

class Downloader(PackageTool):
    def download(self):
        print(" Retrieving %s..." % self.package)

        request.urlretrieve("%s/raw/%s/%s.zip" % (package_repository, package_channel, self.package), "%s.zip" % self.package)

class Installer(PackageTool):
    def install(self):
        print(" Extracting %s..." % self.package)

        with zipfile.ZipFile("%s.zip" % self.package, "r") as zipped_package_file:
            zipped_package_file.extractall(".typo/lib")

class Remover(PackageTool):
    def remove(self):
        print(" Removing %s directory..." % self.package)

        shutil.rmtree(".typo/lib/%s" % self.package)

class Cleaner(PackageTool):
    def clean(self):
        print(" Removing %s.zip..." % self.package)

        os.remove("%s.zip" % self.package)
