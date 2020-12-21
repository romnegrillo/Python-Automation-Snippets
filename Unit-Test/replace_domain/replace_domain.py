import re
import os
import csv

def is_email_domain_exists(email, target_domain):
    pattern = r"[\w\-\.]+@([\w\-\.]+)\.com$"
    result = re.search(pattern, email)

    if result is None:
        return False

    if result.group(1) == target_domain:
        return True
    else:
        return False

def replace_email_domain(email, new_domain):
    pattern = r"([\w\-\.]+@)([\w\-\.]+)(\.com$)"
    result = re.sub(pattern, r"\1" + new_domain + r"\3", email)

    if result is None:
        return email
    else:
        return result


if __name__ == "__main__":
    
    # This is an example of manual testing.
    # You put values and check if the function returns
    #  what you expect it to.

    with open("info.csv", "r") as f:
        csv_reader = csv.DictReader(f)
        
        new_list = []
        for line in csv_reader:

            email = line["email"]

            if is_email_domain_exists(email, "gmail"):
                new_email = replace_email_domain(email, "hunter")
                line["email"] = new_email

            new_list.append(line)
  
        print("Updated email of info.csv")

        for info in new_list:
            print(info)

        with open("info_new.csv", "w", newline = "") as f:
            fieldnames = ["first_name", "last_name", "email"]
            csv_writer = csv.DictWriter(f, fieldnames = fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(new_list)
            


