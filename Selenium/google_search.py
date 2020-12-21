#!/usr/bin/python3

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

 
"""
First time trying Selenium with Python.
Install Selenium via pip:
- pip3 install selenium

Install a webdriver, I used Firefox.
- Download Selenium geckodriver
- Place it in /home/username/.local/bin/geckodriver or
- add in in the path temporary like I did below.
"""

# Adding geckodriver to path temporarily.
# Works in Linux 64 bit only for now.
import set_geckodriver_path
set_geckodriver_path.add_geckodriver_to_PATH()

  
def search(text, driver):
    """
    This function accepts a text to be searched in Google and
    a selenium driver object then it opens a browser, go to
    Google and search the text that the user entered.
    """

    # Wait at least 10 seconds until the element with attribute name q appears.
    # Example: <input name="q">
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "q")))

    # Find the element by name with letter q.
    # Set value attribute for that element to be the 
    # the that text catiable hold. 
    driver.find_element_by_name("q").send_keys(text)

    # Delay by one second.
    time.sleep(1)

    # Find the element with name btnkK and perform submit operation.
    # In Google home page, it is the "Search" button
    # with input with type submit in its html code.
    # We can emulate a button click with submit.
    driver.find_element_by_name("btnK").submit()
                                        

def main():
    # Creates an option for how the browser behaves. 
    opts = Options()
    #opts.set_headless()    # Headless browser.
    #assert opts.headless   

    # Creates firefox webdriver.
    driver = Firefox(options=opts)

    # Navigate to the link provided.
    driver.get("https://www.google.com")

    try:
        search_query = input("What do you want to search? ")
        search(search_query, driver)

    except Exception as exp:
        print("An error has occured!")
        print(str(exp))

    finally:
        input("Program ended.")
        driver.close()


if __name__ == "__main__":
    main()