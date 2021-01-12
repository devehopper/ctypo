# devkit.py
#
# Main development kit
# entry point. In the other
# words, front end for Typo
# development kit.

import throw
import linker
import config
import compiler
import project_json
from pkgtool import Downloader
from pkgtool import Installer
from pkgtool import Remover
from pkgtool import Cleaner

import sys

option = sys.argv.pop(0)

if option == "install":
    packages = sys.argv

    for package in packages:
        print("::Loading classes...")
        downloader = Downloader(package)
        installer = Installer(package)
        cleaner = Cleaner(package)

        print("::Installing %s..." % package)
        downloader.download()
        installer.install()
        cleaner.clean()

elif option == "download":
    packages = sys.argv

    for package in packages:
        print("::Loading classes...")
        downloader = Downloader(package)

        print("::Downloading %s..." % package)
        downloader.download()

elif option == "package":
    pass

elif option == "build":
    pass

elif option == "run":
    pass

elif option == "remove":
    packages = sys.argv

else:
    pass

