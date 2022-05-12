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
        return newword.swapcase()

    def decrypt_add_letters(x):
        oldword = ''
        for i in x[0:]:
            x.replace(i,"")

        x = oldword
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

    #for philipp: i have been trying to find a way to use the encryption functions inside this encrypt_message() function
    #but somehow thats not the pyhton syntax. What I wanna do is use the return values from encryption functions above in this
    # function so I can generate an encrypted message and same for the key to which I wanna assign the returned value of
    # the random_key() function. My guess is there is something I need to add to the initializing function.
    #  Any suggestions or hints how to tackle this? 

    # RAO: there are a few ways to achive this 
    # First of all if you're already getting a "message" as a parameter for the function you don't need to ask the user for input for a message to encrypt just use the value passed in through the parameter
    # second when you say "random_key" or any method within the encrypt class you need to tell the interpreter that it is a method of that class
    # try using Encrypt.random_key() instead
    # 
    # Second of all (This is a little higher level but bear with me)
    # This class is only used to contain the methods for encrypting and decrypting, this means that you dont actually care about the object itself
    # Because of this you can remove the self parameter from the methods meaning that when you want to call method in this class you will use the same format    
    # ex: method called: "encrypt_message" call: Encrypt.encrypt_message(message)
    # 
    # I added a test case at the bottom of the file which should work once those changes are made

    #for philipp: error solved and checked through your test code. Thanks to you!

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


    # philipp: the decryption function is working now. Had to mess with the test code a bit to check it. Please let me know if there's
    # a problem with that. Secondly, the decryption logic is being a lil-b. The decrypt add letters function is not doing
    #what I want to do. Messed with it a hundred times but still the same response. It;s not deleting the added characters.
    # Please take a look if u have time and let me know if u see somethn sus in there. I will look at it again after waking up,
    #might be able to crack it w a fresh mind. Also, please run this and point out any other errors too u find it and I will correct
    #them asap so I can move on to fitting this into the chat system. Thank you!!

    def decrypt_message(encrypted, key):
        # TODO: decrypt message and return the original string

       # encrypted, key = Encrypt.encrypt_message()

        decrypted = encrypted

        # This should not be necessary
        # Taking the letters out should happen in order as well as this may affect the other decryption methods
        
            # 1. to decrypt the key needs to be read backwards
            # 2. When you call the decryption methods you are giving them "encrypted" not "decrypted" which is the one you are modifying
            #
        for i in key[-1:]:
            if i == "F":
                decrypted = Encrypt.decrypt_flip(encrypted)
            elif i == "L":
                decrypted = Encrypt.decrypt_shift_left(encrypted)
            elif i == "R":
                decrypted = Encrypt.decrypt_shift_right(encrypted)
            elif i == "A":
                decrypted = Encrypt.decrypt_add_letters(encrypted)


        return (decrypted)
    
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
    print("\n\n\n")
    encrypted_msg, key2 = Encrypt.encrypt_message("hello, world")
    print("\n\n\n")
    print(encrypted_msg, key2)
    print("\n\n\n")
    print(Encrypt.decrypt_message(encrypted_msg,key2))
    print("\n\n\n")

"""
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
"""