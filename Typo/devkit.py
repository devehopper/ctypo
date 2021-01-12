# devkit.py
#
# Main development kit
# entry point. In the other
# words, front end for Typo
# development kit.

from colored.colored import stylize
import throw
import linker
import config
import compiler
import project_json
from pkgtool import Downloader
from pkgtool import Installer
from pkgtool import Remover
from pkgtool import Cleaner

import os
import sys
import colored
import shutil

file = sys.argv.pop(0)

try:
    option = sys.argv.pop(0)

except IndexError:
    throw.throw("IndexError", "Can't find an option that passed as command line argument.", "Pass a argument as command line parameter.", -1, 1)

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

elif option == "init":
    config.project_name = input(" %s Project Name %s: " % (colored.stylize("?", colored.fg("green")), colored.stylize("?", colored.fg("green")))).lower().replace(" ", "-")
    config.project_authors = input(" %s Project Authors ( Separated with \", \". ) %s: " % (colored.stylize("?", colored.fg("green")), colored.stylize("?", colored.fg("green")))).split(", ")
    config.project_owner = input(" %s Project Owner %s: " % (colored.stylize("?", colored.fg("green")), colored.stylize("?", colored.fg("green"))))

    config.package_channel = "stable"
    config.package_repository = "https://github.com/typolang/tpm-repo"

    config.update()

    os.mkdir(".typo")
    os.mkdir(".typo/lib")
    os.mkdir(".typo/lang")
    os.mkdir(".typo/lang/devkit")
    os.mkdir(".typo/vm")

    project_json_loader = project_json.ProjectJSONGenerator(config.metadata, ".typo/project.json")
    
    project_json_loader.generate()

elif option == "install-runtime":
    print("::Installing runtime elemens...")
    print(" Copying runtime directory from /usr/lib/ctypo/runtime")

    shutil.copytree("/usr/lib/ctypo/runtime.exe", ".typo/lang/runtime.exe")

else:
    throw.throw("OptionNotFound", "There is no option called \"%s\"." % option, "Enter a valid option.", -1, 1)
