#!/usr/bin/python3

import subprocess

message = """This script is used to update and
install packages that I normally used 

Tested in Ubuntu 20.04.1"""

print("===================================")
print(message)
print("===================================")

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
    print("===================================")
    print("All commands successfully executed!")
    print("===================================")
