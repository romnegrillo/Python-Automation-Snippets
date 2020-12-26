import os

print(os.getcwd())

os.chdir("dir1")

print(os.getcwd())

print(os.listdir())


#os.mkdir("files")
#os.makedirs("files1\\files2")

#os.rmdir("files")

print(os.stat("test.txt"))

current_path = os.getcwd()
#new_file_path = current_path + "\\" + "sample.txt"
new_file_path = os.path.join(current_path, "sample.txt")

print(new_file_path)

print(os.path.isdir(new_file_path))
print(os.path.isfile(new_file_path))

print(os.path.basename(new_file_path))
print(os.path.dirname(new_file_path))