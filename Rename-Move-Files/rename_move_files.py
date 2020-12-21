#!/usr/bin/python3

"""
This program copy all the files in the chosen directory,
and moves it to a new directory with a new customized file name.
"""

import os
import shutil 

def rename_move_files(file_path):
    # Change directory to the original files to be copied.
    os.chdir(file_path)

    # Get all the contents as a list and remove non .txt files
    files = os.listdir()
    files = [file for file in files if ".txt" in file]

    # Loop through the files and customize a new file name.
    # Sample:
    # Mecury - 01.txt should be renamed to
    # 01 - Mercury.txt
    # So that number orders will be sorted rather than the name.
    for file in files:
        file_name, file_extesion = os.path.splitext(file)
    
        file_title, file_number = file_name.split("-")

        file_title = file_title.strip()
        file_number = file_number.strip()

        new_file_name = "{} - {}{}".format(file_number, file_title, file_extesion)

        print("Copied and renamed '{}' to '{}'".format(file_name, new_file_name))

        shutil.copy(file, os.path.join("new_files", new_file_name))


def main():
    target_path = "original_files"
    rename_move_files(target_path)


if __name__ == "__main__":
    main()