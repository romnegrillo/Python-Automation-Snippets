import re

test_string = """Hello, my name is Rom.
 
Email: romnegrillo@romnegrillo@gmail.com or romnegrillo@protonmail.com
Celphone No.:  09171234567
Telephone No.: 123-123-1234
Address: 123 Zoldyck Residence, Kukuroo Mountain

key1=value1
key2 = value2
key3 = value with space
"""

# name = re.search(r"Rom", test_string)
name = re.search(r"R.m", test_string)
print(name)
print(name.group())
print(name.span())

greeting = re.search(r"^H.+.", test_string)
print(greeting.group())

cellphone_number = re.search(r"\d+", test_string)
print(cellphone_number)

email_address = re.findall(r"\S+@\S+.com", test_string)
print(email_address)

value1 = re.search(r"key1\s*=\s*(.+)", test_string)
print(value1.group(1))

value2 = re.search(r"key2\s*=\s*(.+)", test_string)
print(value2.group(1))

value3 = re.search(r"key3\s*=\s*(.+)", test_string)
print(value3.group(1))