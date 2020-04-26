import sys

def process_user_input():
    return([int(arg)*2 for arg in sys.argv[1:]])

print(process_user_input())
