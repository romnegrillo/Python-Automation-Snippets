# Context manage to mange resources
# properly by closing the resources
# such as file afterwards.

# r - read
# w - write
# r+ - read/write
# a - append
# binary


with open("my_file.txt", "r") as f:
    # Read whole contents of the file.
    #f_contents = f.read()

    # Read line by line.
    #f_contents = f.readline()

    # Read whole contents and place each line in a list.
    f_contents = f.readlines()

    print(f_contents)

with open("my_file.txt", "a") as f:
    f.write("Hello" + "\n")

with open("my_file.txt", "r") as f:
    # You can loop through a file descriptor
    for line in f:
        print(line)

with open("my_file.txt", "r") as f:
    # It is more efficient to read file with specified number of bytes.
    byte_per_read = 512

    f_contents = f.read(byte_per_read)

    while len(f_contents) > 0:
        print(f_contents)
        f_contents = f.read(byte_per_read)