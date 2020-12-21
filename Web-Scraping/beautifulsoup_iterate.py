"""
In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Asia.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: D
Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.
"""


import urllib.request
from bs4 import BeautifulSoup
import ssl

# To ignore https cert.
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Get inputs
url_input = input("Enter url: ")
count = int(input("Enter count: "))  # Based on example, count of 4 means loop 5 times since it starts with 0.
link_pos = int(input("Enter position: "))-1   # Based on example, position 3 means index 2 so we subtract 1.

for i in range(count+1):
    
    # Open link with the input url.
    with urllib.request.urlopen(url_input, context = context) as f:
        
        print("Retrieving: {}".format(url_input))

        # Get the first contents of the link and
        # find the anchor tags then retrive href values.

        html_elements = f.read().decode()
        soup = BeautifulSoup(html_elements, "html.parser")
        tag_target = soup("a")
        href_values = [i.get("href", None) for i in tag_target]

        # Now you have new link list, fetch new link using target index.
        # Then start the loop again.
        url_input = href_values[link_pos]

        




    
    
    
