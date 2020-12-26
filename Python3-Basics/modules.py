import my_module 
import my_module as mm
from my_module import find_item_index
from my_module import *
import sys
import os

courses = ["Math", "Science", "History", "Computer Science"]

print(my_module.find_item_index(courses, "History"))
print(mm.find_item_index(courses, "History"))
print(find_item_index(courses, "History"))

print(my_module.test_string)
print(mm.test_string)
print(test_string)

print(sys.path)
print(os.getcwd())