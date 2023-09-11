f = open("myfile.txt", "w") # a, x

"""
Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist
"""

import sys

script_name = sys.argv[0]
arguments = sys.argv[1:]
print('script:',script_name)
print('arg:',arguments)

python_version = sys.version
print('version:',python_version)

platform = sys.platform
print('platform',platform)

user_input = sys.stdin.readline()
sys.stdout.write("Hello, World!\n")
sys.stderr.write("Error: Something went wrong\n")
print('user:',user_input)
