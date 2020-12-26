import sys
import os
import datetime

print("Parameters:")
print(sys.argv)

file_name = sys.argv[1]

if os.path.isfile(file_name):
    print("File already exists!")
else:
    with open(file_name, "w") as f:
        datetime_now = datetime.datetime.now()
        f.write("Hello! File created at {}".format(datetime_now.strftime("%Y/%m/%d, %H:%M:%S")))

    print("{} file created".format(file_name))