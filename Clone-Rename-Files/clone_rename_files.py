#!/usr/bin/python3

import os
import shutil

def clone_rename_files(orig_filename, new_filename, num_copies):
    """
    This function creates multiple copies of
    orig_filename  in the current directory and renames it 
    with the a specific naming convention pattern based
    on new_filename.
    """

    # Get the file name and extension.
    f_name, f_extension = os.path.splitext(orig_filename)

    # Loop through number of copies and create a new file name
    # with the number as a pattern at the end. 
    # Ex: sample_copy_01

    # Start the loop at 1 and add zfill to have 2 digits as the format.

    for i in range(1,num_copies+1):
        new_file_name = new_filename + "_" + str(i).zfill(2) + f_extension
        print("Creating {}...".format(new_file_name))
        shutil.copy(orig_filename, new_file_name)

def main():
    orig_filename = "original_file.txt"
    new_filename = "sample_copy"
    num_copies = 10
    clone_rename_files(orig_filename, new_filename, num_copies)

if __name__ == "__main__":
    main()

