import sys

# print(sys.argv)
if len(sys.argv) == 1:
    print("USAGE: python3 filename.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)

# run the command in terminal to run this program
# python3 command_line_arguments.py
# and
# python3 command_line_arguments.py 1234
