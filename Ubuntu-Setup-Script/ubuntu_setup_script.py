#!/usr/bin/python3

import subprocess


def install():
    """
    This functions executes the command in the commands list.
    It just runs sudo install for all the commonly software
    I always install when settings up my Ubuntu machine.
    """

    message = """This script is used to update and
    install packages that I normally used 

    Tested in Ubuntu 20.04.1"""

    print(message)


    input("Press enter to cotinue.")


    commands = [
    "sudo apt update -y",
    "sudo apt upgrade -y",
    "sudo apt install git -y",
    "sudo apt install qtcreator -y",
    "sudo apt install qt5-default -y",
    "sudo add-apt-repository ppa:rock-core/qt4",
    "sudo apt install qt4-default -y",
    "sudo apt install python3-pip -y",
    "sudo apt install gnome-tweak-tool -y",
    "sudo apt install preload",
    "sudo apt install tlp tlp-rdw",
    "sudo apt install ubuntu-restricted-extras -y",
    "sudo apt install timeshift",
    "sudo snap install --classic code"
    ]

    failed_commands = []

    for command in commands:
        result = subprocess.run([command], shell = True)

        if result.returncode != 0:
            failed_commands.append(command)
    
    if len(failed_commands):
        print("The following commands failed.")
        
        for command in failed_commands:
            print(command)
    else:
        print("All commands successfully executed")

def main():
    install()

if __name__ == "__main__":
    main()

