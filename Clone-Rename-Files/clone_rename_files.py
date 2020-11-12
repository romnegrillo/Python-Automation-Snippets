"""
This programs creates multiple copies of
one file and rename it with the chosen 
naming convention.
"""

import os
import shutil

original_file_name = "original_file.txt"
new_base_name = "Sample"

# Get the file name and extension.
f_name, f_extension = os.path.splitext(original_file_name)

# Loop through chosen file name convention with numbers
# as new file name and add the file name extension.
for i in range(1,11):
    new_file_name = new_base_name + " - " + str(i).zfill(2) + f_extension
    shutil.copy(original_file_name, new_file_name)