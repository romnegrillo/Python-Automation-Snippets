"""
Welcome Romulo Negrillo Jr. from Using Python to Access Web Data

Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1022135.html (Sum ends with 42)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
"""

import urllib.request
from bs4 import BeautifulSoup
import ssl

# To ignore https cert.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_input = input("Enter url: ")

with urllib.request.urlopen(url_input, context = ctx) as f:
    html_elements = f.read().decode()
   
    soup = BeautifulSoup(html_elements, "html.parser")
    tag_target = soup("span")
    
    span_tag_list = [int(i.contents[0]) for i in tag_target]
    
    print("Count {}".format(len(span_tag_list)))
    print("Sum {}".format(sum(span_tag_list)))
    
