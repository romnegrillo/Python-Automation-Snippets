import os
from datetime import datetime

# Get current working diretory
print("Current directory:", os.getcwd())

# Get info about file in the current worknig directory.
file_name = "test.txt"
file_info = os.stat(file_name)

# Get modification time.
# It is in timestamp format so we use datetime module to
# convert it to human readable date and time
mod_time = file_info.st_mtime
print("Modification Time:", datetime.fromtimestamp(mod_time))

# Get the absolute path of the file in the current working directory
abs_path = os.path.abspath(file_name)

# From the absolute path, we can get the:
# Base path
# File name
# Path without the extension of the file
# Extension of the file.
file_base_path, file_name = os.path.split(abs_path)
file_path_noext, file_ext = os.path.splitext(abs_path)

print(file_base_path)
print(file_name)
print(file_path_noext)
print(file_ext)

# Check if directory or file exists.
print(os.path.isdir(abs_path))
print(os.path.isdir(file_base_path))

print(os.path.isfile(abs_path))
print(os.path.isfile(file_base_path))

# Check if path exists. Remove and renaming.
if os.path.exists("to_delete.txt"):
    os.remove("to_delete.txt")
else:
    print("to_delete.txt does not exists.")

if os.path.exists("to_rename.txt"):
    os.rename("to_rename.txt", "renamed.txt")
else:
    print("to_rename.txt does not exists.")

if os.path.exists("sample_path"):
    print("sample_path directory exists.")
else:
    print("sample_path directory exists.")


# Get size and modification time (another way)
print("Size of test.txt: {} bytes".format(os.path.getsize("test.txt")))

print(os.path.getsize("test.txt"))
time_stamp = os.path.getmtime("test.txt")   # Modification time
dt = datetime.fromtimestamp(time_stamp)
print(dt)

print(os.path.abspath("sample_path"))

# Change directory.
os.chdir("sample_path")
print(os.getcwd())

# List of directory contents.
print(os.listdir())