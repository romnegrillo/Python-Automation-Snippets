#!/usr/bin/python3

import os


def count_files_dir_tree(base_dir):
    """
    This function counts all the directory and files
    within the base directory provided and returns a 
    tuple where the first index is number of directory
    and the second index is the number of files.
    """
    print("Input directory: {}".format(base_dir))
    
    if os.path.isdir(base_dir):
        print("Path exists!")
    else:
        return -1, -1

    sum_dir = 0
    sum_files = 0

    for depth, (current_dir, sub_dir_list, file_list) in enumerate(os.walk(base_dir),0):
        print("Depth {}".format(depth))
        print("Current directory: {}".format(current_dir))
        print("Directory list: {}".format(sub_dir_list))
        print("File list: {}".format(file_list))
        print()

        sum_dir += len(sub_dir_list)
        sum_files += len(file_list)


    return sum_dir, sum_files

def main():
    print("Number of directories is {0[0]}. Number of files is {0[1]}.".format(count_files_dir_tree("Sample-Dir")))


if __name__ == "__main__":
    main()


    
