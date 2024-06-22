#! ==== Final code ====
#! ==== Optimizing the UI Experience ====

import os
from art import logo

clear = lambda: os.system('cls')

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text, shift, direction):
    result=""

    if direction=="decode":
        shift *= -1
        
    for char in text:
        
        if char not in alphabet:
            result+=char
        else:
            position=alphabet.index(char)
            new_position=position+shift
            
            index=new_position%len(alphabet) #! handles the error: List index out of range.
            new_letter=alphabet[index]
        
            result+=new_letter
    
    print(f"The {direction}d text is: {result}")


print(logo, "\n")


def restart():
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'encode' or direction == 'decode':    
        message=input("Type your message. \n").lower()
        shift_number=int(input("Type the shift number. \n"))
            
        caeser(text=message, shift=shift_number, direction=direction)
    
    else:
        print("Invalid direction.\n")
    
    question=input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()
    
    if question=="yes":
        clear()
        restart()
    
restart()
print("GoodBYE!!!")