"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

question = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if question == 'e':
    message = input("Message: ")
    key = input("Key: ")
    for x in message:
        print(list(x))
        #print(associations.find(x))
    #for y in key:
        #print(associations.find(y))

"""
elif question == 'd':
    message = input("Message: ")
    key = input("Key: ")
elif question == 'q':
    print("Goodbye!")
else:
    print("Did not understand command, try again.")
"""