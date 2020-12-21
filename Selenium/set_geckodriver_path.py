import os
import sys

def add_geckodriver_to_PATH():
    current_path = os.getcwd()
    geckodriver_path = os.path.join(current_path, "geckodriver-v0.28.0-linux64")


    print("PATH before:")
    print(os.environ["PATH"])


    if geckodriver_path in os.environ["PATH"]:
        print("Geckodriver already in PATH.")
    else:
        os.environ["PATH"] += os.pathsep + geckodriver_path
        print("Geckodriver added in PATH.")

    print("PATH after:")
    print(os.environ["PATH"])