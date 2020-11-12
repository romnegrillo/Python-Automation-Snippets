import os
import subprocess

# Print the PATH in enviroment variables.
print(os.environ.get("PATH"))

# Copy environment variable
env_var_copy = os.environ.copy()

print(env_var_copy["PATH"])

# When you execute a command from the shell in Unix,
# it has a returncode indicating if the command
# is successful or not. When it has a return code of 0
# it is successful.

# You can run os commands in Python and get its output
# and return code using subproceess module. 

# Example for Unix.

# Success  command.
result = subprocess.run(["ls"], capture_output = True)
print(result.returncode)
print(result.stdout)
print(result.stderr)

# Fail command, file does not exists
result = subprocess.run(["rm", "test_file"], capture_output = True)
print(result.returncode)
print(result.stdout)
print(result.stderr)