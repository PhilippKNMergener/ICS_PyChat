"""
Author: Rao Daud Ali Khan
File: Encrypt.py
"""

import string
import random


# Class for encrypting and decrypting messages
class Encrypt():
    # Initializers
    # you dont actually need an initializer because every instance of the class will be the same
    def __init__(self):
        pass


    # TODO: write decryption method for each encryption method
    # Done and checked
    
    # Encryption functions
    def shift_right(d):
        new_word = d[-1] + d[0:len(d)-1]
        return new_word
    
    def decrypt_shift_right(x):
        oldword = x[1:len(x)] + x[0]
        return oldword
        

    # function #3
    # shift all letters to the left
    def shift_left(e):
        newword = e[1:len(e)] + e[0]
        return newword

    def decrypt_shift_left(x):
        oldword = x[-1] + x[0:len(x)-1]
        return oldword


    # function #4
    # flip the right and left half of the input string
    def flip(f):
        if len(f) % 2 == 0:
            newword = f[int(len(f)/2):] + f[0:int(len(f)/2)]
        else:
            newword = f[(len(f)//2)+1:] + f[len(f)//2] + f[0:(len(f)//2)]
        return newword

    def decrypt_flip(x):
        if len(x) % 2 == 0:
            oldword = x[int(len(x)/2):] + x[0:int(len(x)/2)]
        else:
            oldword = x[(len(x)//2)+1:] + x[len(x)//2] + x[0:(len(x)//2)]
        return oldword

    # function #5
    # Add one random letter between each letter of the input
    # Starting after the first letter (this will be important for decoding)
    def add_letters(a, b):
        newword = ''
        for i in a:
            newword += i
            for _ in range(b):
                newword += random.choice(string.ascii_letters)
        # By making this swapcase it will be posible to encode and decode capital and lowercase letters
        # the decode function will just swap the case back
        return newword

    def decrypt_add_letters(x):
        #return "".join([letter for i, letter in enumerate(x) if i%2 == 0])
        oldword = ''
        for i, letter in enumerate(x):
            if i%2 == 0:
                oldword += letter
        return oldword

    # generate a random key with param length
    def random_key(length = 3):
        letters = ["A", "F", "R", "L"]
        key = ""
        key_length = length
        for i in range(key_length):
            key += random.choice(letters)
        return key


    # Main class methods


    def encrypt_message(message):
        # TODO: encrypt message and return encrypted (message, key)
        encrypted = message
        key = Encrypt.random_key()

        for i in key:
            
            if i == ("A"):
                print("* Added 1 letter:", Encrypt.add_letters(encrypted,1))
                encrypted = Encrypt.add_letters(encrypted,1)
            elif i == ("F"):
                print("* Flipped:", Encrypt.flip(encrypted))
                encrypted = Encrypt.flip(encrypted)
            elif i == ("R"):
                print("* Shifted right:", Encrypt.shift_right(encrypted))
                encrypted = Encrypt.shift_right(encrypted)
            elif i == ("L"):
                print("* Shifted left:", Encrypt.shift_left(encrypted))
                encrypted = Encrypt.shift_left(encrypted)

        return (encrypted, key)


    def decrypt_message(encrypted, key):
        # TODO: decrypt message and return the original string

       # encrypted, key = Encrypt.encrypt_message()

        #decrypted = encrypted
        decrypted = encrypted

        for i in list(reversed(key)):
            if i == "F":
                decrypted = Encrypt.decrypt_flip(decrypted) 
                print("*  decrypt flip", decrypted)
            if i == "L":
                decrypted = Encrypt.decrypt_shift_left(decrypted)
                print("* decrypt left shift", decrypted)
            if i == "R":
                decrypted = Encrypt.decrypt_shift_right(decrypted)
                print("* decrypt right shift", decrypted)
            if i == "A":
                decrypted = Encrypt.decrypt_add_letters(decrypted)
                print("* decrypt add", decrypted)

        
        return (decrypted)
    

if __name__ == "__main__":
    print("\n\n\n")
    encrypted_msg, key2 = Encrypt.encrypt_message("hello, world")
    print("\n\n\n")
    print(encrypted_msg, key2)
    print("\n\n\n")
    print(Encrypt.decrypt_message(encrypted_msg, key2))
    print("\n\n\n")

