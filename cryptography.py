"""
cryptography.py
Author: Esther Hacker
Credit: n/A

Assignment: Cryptography

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

question = input("Enter e to encrypt, d to decrypt, or q to quit: ")

messagenmbrs = []
keynmbrs = []
bothnmbrs = []
ecommand = []
bothdifference = []
dcommand = []


if question == 'e':
    
    message = input("Message: ")
    key = input("Key: ")
    message = list(message)
    key = list(key)
    
    for x in message:
        messagenmbrs.append(associations.find(x))
    for y in key:
        keynmbrs.append(associations.find(y))
    for z in range(0, len(messagenmbrs)):
        bothnmbrs.append(messagenmbrs[z] + keynmbrs[z%len(keynmbrs)])
    for a in bothnmbrs:
        ecommand.append(associations[a%85])
    
    print(''.join(ecommand))
    
    messagenmbrs = []
    keynmbrs = []
    bothnmbrs = []
    ecommand = []

elif question == 'd':
    
    emessage = input("Message: ")
    key = input("Key: ")
    
    for x in emessage:
        messagenmbrs.append(associations.find(x))
    for y in key:
        keynmbrs.append(associations.find(y))
    for z in range(0, len(messagenmbrs)):
        bothnmbrs.append(messagenmbrs[z]-keynmbrs[z%len(keynmbrs)])
    for a in bothnmbrs:
        dcommand.append(associations[a%85])
    
    print(''.join(dcommand))
    
    messagenmbrs = []
    keynmbrs = []
    bothnmbrs = []
    dcommand = []

elif question == 'q':
    print("Goodbye!")
else:
    print("Did not understand command, try again.")