import csv

with open("written_csv.csv", "w") as f:
    csv_writer = csv.writer(f)
    fieldnames = ["Error", "Count"]
    csv_writer.writerow(fieldnames)
    csv_writer.writerow(["Test", 1])
    csv_writer.writerow({"Error": "Test2", "Count": 23})
    csv_writer.writerow(("Test3", 64))

with open("written_csv.csv", "r") as f:
    csv_reader = csv.reader(f, delimiter = ",")
    
    for line in csv_reader:
        print(line)

print("==============================")

with open("written_dict_csv.csv", "w") as f:
    csv_writer = csv.DictWriter(f, fieldnames = ["Error", "Count"])
    csv_writer.writeheader()
    data = {"Error": "Test1", "Count":34}
    data_list = [{"Error": "Test2", "Count":34}, {"Error": "Test3", "Count":34}]
    csv_writer.writerow(data)
    csv_writer.writerows(data_list)

 

with open("written_dict_csv.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    for line in csv_reader:
        print(line)


print("==============================")


