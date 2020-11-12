"""
This program scans the html document of logged in Shopee account in
their purchased item page then scans through the puchased items
and sum all the items the user has spent.
"""

import re

# Open and read the copied file as string of the whole body tag in Shopee 
# purchased page and save it as some_filename.html.

with open("shopee_account_source.html", "r", encoding="utf-8") as f:
    data = f.read()

# Regular expression was used: 
# Example: r"somestring01mytargetsomestring02"
# "somestring01(.+?*)somestring2" will return "mytarget"
# Using findall will find all those substring repeatedly and returns a list.

target_opening_string = r'<span class="purchase-card-buttons__total-price">'
target_closing_string = r"</span>"
result = re.findall(target_opening_string + r'(.+?)' + target_closing_string , data)

# If the list contains one or mor than one item, we
# add it together. The list will return string with "₱" and ","
# We remove that by using string replacement with an empty character
# and convert it to foat
if result:

    for items in result:
        print(items)
        
    total_spent = sum([float(i.replace("₱","").replace(",","")) for i in result])
    print("Total Spent in Shopee: ", total_spent)
