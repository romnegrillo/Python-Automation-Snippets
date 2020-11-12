import csv

def read_csv(path):
    with open(path, "r") as f:
        csv_reader = csv.reader(f)

        for line in csv_reader:
            print(line)

def write_csv(path, list_to_write):
    with open(path, "a", newline="") as f:  # We add newline="" because writer adds additional newl ine.
        csv_writer = csv.writer(f)

        csv_writer.writerow(list_to_write)  # writerow writes contents of one iterable as values in each column.

def read_csv_dict(path):
    with open(path, "r") as f:
        csv_reader = csv.DictReader(f)
        
        for line in csv_reader:
            for key,value in line.items():
                print("Key: {}\tValue: {}".format(key,value))

def write_csv_dict(path, dict_to_write):
    with open(path, "a", newline="") as f:  # We add newline="" because writer adds additional newl ine.
        csv_writer = csv.DictWriter(f, fieldnames = ["firstname", "lastname", "age", "department"])

        csv_writer.writerows(dict_to_write) # writerows writes a list of dictionary where each values in the dictionary will be the values to be written.

read_csv("sample_csv.csv")

sample_list = ["IP", "Man", 22, "Wing Chun"]
write_csv("sample_csv.csv", sample_list)
read_csv("sample_csv.csv")

read_csv_dict("sample_csv.csv")

sample_dict = [
    {"firstname": "General",
    "lastname": "Miura",
    "age": 22,
    "department": "Karate"},

    {"firstname": "The",
    "lastname": "Twister",
    "age": 22,
    "department": "Boxing"},
]

write_csv_dict("sample_csv.csv", sample_dict)

read_csv_dict("sample_csv.csv")


