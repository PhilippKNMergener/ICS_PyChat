"""
Author: Rao Daud Ali Khan
File: Encrypt.py
"""

import string
import random


# Class for encrypting and decrypting messages
class Encrypt():
    # Initializers
    def __init__(self):
        pass

    # TODO: write decryption method for each encryption method
    
    # Encryption functions
    def shift_right(d):
        new_word = d[-1] + d[0:len(d)-1]
        return new_word

    # function #3
    # shift all letters to the left
    def shift_left(e):
        newword = e[1:len(e)] + e[0]
        return newword

    # function #4
    # flip the right and left half of the input string
    def flip(f):
        if len(f) % 2 == 0:
            newword = f[int(len(f)/2):] + f[0:int(len(f)/2)]
        else:
            newword = f[(len(f)//2)+1:] + f[len(f)//2] + f[0:(len(f)//2)]
        return newword

    # function #5
    # Add one random letter between each letter of the input
    # Starting after the first letter (this will be important for decoding)
    def add_letters(a,b):
        newword = ''
        for i in a:
            newword += i
            for _ in range(b):
                newword += random.choice(string.ascii_letters)
        # By making this swapcase it will be posible to encode and decode capital and lowercase letters
        # the decode function will just swap the case back
        return newword.swapcase()

    # generate a random key with param length
    def random_key(length = 3):
        letters = ["A", "P", "G", "J", "F"]
        key = ""
        key_length = length
        for i in range(key_length):
            key += random.choice(letters)
        return key

    # Main class methods
    
    def encrypt_message(self, message):
        # TODO: encrypt message and return encrypted (message, key)
        encrypted = ""
        key = ""
        return (encrypted, key)

    def decrypt_message(self, encrypted, key):
        # TODO: decrypt message and return the original string
        pass

    

    

# Commented so that they wont cause extra imports when this file is used as a module in the other files

#
#def ascii_shift(a,b):
#    value = ''
#    for c in a:
#        if c.isupper():
#            if b >= 26:
#                b = b%26
#            elif b <= -26:
#                b = b % -26
#            letter = c
#            value += chr(ord(letter) + b)
#        else:
#            value += c        
#    return value
#
##function #2
#
#def shift_right(d):
#    new_word = d[-1] + d[0:len(d)-1]
#    return new_word
#
#
#
##function #3
#
#def shift_left(e):
#    newword = e[1:len(e)] + e[0]
#    return newword
#
#
#
##function #4
#
#def flip(f):
#    if len(f) % 2 == 0:
#        newword = f[int(len(f)/2):] + f[0:int(len(f)/2)]
#    else:
#        newword = f[(len(f)//2)+1:] + f[len(f)//2] + f[0:(len(f)//2)]
#    return newword
#
#
#
##function #5
#
#def add_letters(a,b):
#    newword = ''
#    for i in a:
#        newword += i
#        for _ in range(b):
#            newword += random.choice(string.ascii_letters)
#    return newword.upper()
#
#
#
##function #6
#
#def delete_characters(a,b):
#    newword = a[0::b+1]
#    return newword

# Test cases
if __name__ == "__main__":
    while True:
        
        pattern = input("Enter an encoding pattern, 'end' to end: ").upper()

        if pattern == "END":
            print("Program ending")
            break
        
        word = input("Enter a word to encode/decode: ").upper()

        for i in pattern:
            if i == ("U"):
                print("* ASCII shift up:", ascii_shift(word,1))
                word = ascii_shift(word,1)
            elif i == ("D"):
                print("* ASCII shift down:", ascii_shift(word,-1))
                word = ascii_shift(word,-1)
            elif i == ("A"):
                print("* Added 1 letter:", add_letters(word,1))
                word = add_letters(word,1)
            elif i == ("X"):
                print("* Deleted 1 character:", delete_characters(word,1))
                word = delete_characters(word,1)
            elif i == ("F"):
                print("* Flipped:", flip(word))
                word = flip(word)
            elif i == ("R"):
                print("* Shifted right:", shift_right(word))
                word = shift_right(word)
            elif i == ("L"):
                print("* Shifted left:", shift_left(word))
                word = shift_left(word)
            else:
                print("* "+i+" is an invalid command, ignoring")
                
        print("Final encoding / decoding:",word)
        print()