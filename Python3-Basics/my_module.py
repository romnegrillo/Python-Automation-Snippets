print("Imported my_module")

test_string = "Test string."

def find_item_index(source, target):

    for index,item in enumerate(source):
        if item==target:
           return index

    return -1