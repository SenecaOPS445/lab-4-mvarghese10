#!/usr/bin/env python3
# Author ID: mvarghese10/118830223
# Author Name: Megodwin Varghese
    

def is_digits(sobj):
    for char in sobj:
        if not char.isdigit():
            return False
    return True 
"this will loop through each character in sobj"


# Main block

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')