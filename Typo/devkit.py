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

elif option == "remove":
    packages = sys.argv

    for package in packages:
        print("::Loading classes...")
        remover = Remover(package)

        print("::Removing %s..." % package)
        remover.remove()

elif option == "load":
    packages = sys.argv

    for package in packages:
        print("::Loading classes...")
        installer = Installer(package)

        print("::Installing %s..." % package)
        installer.install()

        ask_for_garbage = input("\n? Want to clean garbage ? [Y/n]: ")
        print()

        if ask_for_garbage in "Yy":
            print("::Loading cleaner class...")
            cleaner = Cleaner(package)

            print(" Cleaning %s.zip..." % package)
            cleaner.clean()

        elif ask_for_garbage in "Nn":
            print("\n ! Not cleaning garbage !\n")

            exit(0)

        elif ask_for_garbage == "":
            print("\n ! Not cleaning garbage !\n")

            exit(0)

        else:
            print("\n ! Not cleaning garbage !\n")

            exit(0)

elif option == "package":
    pass

elif option == "build":
    pass

elif option == "run":
    pass

else:
    pass
