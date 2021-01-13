#!/usr/bin/python3

import re

def check_valid_email(email):
    pattern = r"^[\w\.\-]+@[\w\.\-]+\.com$"
    result = re.search(pattern, email)

    if result is None:
        return False

    return True
