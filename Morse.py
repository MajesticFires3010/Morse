import pyperclip                        # pyperclip.copy for copying to Clipboard
from termcolor import cprint, colored   # For Style ;-)
from pyfiglet import figlet_format      # For Style ;-)
import time                             # If Opening in Terminal

#print(ord('A'),ord('Z'))   # Debugging Statement

alphabets = []
for i in range(65,91) :
    alphabets.append(chr(i))                        # alphabets = ['a' , 'b' ,...]
#print(alphabets)   # Debugging Statement

# English Alphabets to Morse Characters
morse_alphabets = [".-" , "-..." , "-.-." , "-.." , '.' , "..-." , "--." , "...." , ".." , ".---" , "-.-" , ".-.." , "--" , "-." , "---" , ".--." , "--.-" , ".-." , "..." , "-" , "..-" , "...-" , ".--" , "-..-" , "-.--" , "--.."]
#for i in morse_alphabets : # Debugging Statement
#    print(i)   # Debugging Statement

Alphabets = {}
for i in range(26) :
    #print(alphabets[i],morse_alphabets[i]) # Debugging Statement
    Alphabets[alphabets[i]] = morse_alphabets[i]    # Alphabets = {'A' = ".-" ,...}
#print(Alphabets)

numbers = []
for i in range(0,10) :
    numbers.append(str(i))                               # numbers = [0,1,2,...]
#print(numbers)

# Numbers to Morse Code
morse_numbers = ["-----" , ".----" , "..---" , "...--" , "....-" , "....." , "-...." , "--..." , "---.." , "----."]
#for i in morse_numbers :   # Debugging Statement
#    print(i)   # Debugging Statement

Numbers = {}
for i in range(10) :
    Numbers[numbers[i]] = morse_numbers[i]          # Numbers = {0 : "-----" ,...}
#print(Numbers) # Debugging Statement

spl_chars = ['.' , ',' , '?' , '\'' , '!' , '/' , '(' , ')' , '&' , ':' , ';' , '=' , '+' , '-' , '_' , '\"' , '$' , '@' , '¿' , '¡']
#for i in spl_chars :   # Debugging Statement
#    print(i)   # Debugging Statement

# Special Characters to Morse Code
morse_spl_chars = [".-.-.-" , "--..--" , "..--.." , ".----." , "-.-.--" , "-..-." , "-.--." , "-.--.-" , ".-..." , "---..." , "-.-.-." , "-...-" , ".-.-." , "-....-" , "..--.-" , ".-..-." , "...-..-" , ".--.-." , "..-.-" , "--...-"]
#for i in morse_spl_chars :  # Debugging Statement
#    print(i)    # Debugging Statement

Spl_Chars = {}
for i in range(20) :
    Spl_Chars[spl_chars[i]] = morse_spl_chars[i]    # Spl_chars = {'.' = ".-.-.-" , ...}
#print(Spl_Chars) # Debugging Statement

morse = {}
morse.update(Alphabets)
morse.update(Numbers)
morse.update(Spl_Chars)
#print(morse) # Debugging Statement

# Encrypting English Word to Morse Code
def encrypt(word) :
    morse_word = ''
    word = word.upper()
    #print(word)    # Debugging Statement
    for i in word :
        #print(i)   # Debugging Statement
        if i in morse.keys() :
            morse_word += str(morse[i])
            morse_word += ' '   # Letter Change
            #print(morse.keys())    # Debugging Statement
            #print(i,morse_word)    # Debugging Statement
        elif i == ' ' :
            morse_word += '/'   # Word Change
    print(morse_word)
    pyperclip.copy(morse_word)  # To Copy Encrypted Morse Code to Clipboard

# Decrypting from Morse Code to English
def decrypt(morse_code) :
    morse_word = ''
    morse_letter = ''
    for i in morse_code :
        if i == '.' or i == '-' :   # Conversion
            morse_letter += i
        elif i == ' ' :             # Letter Change
            if morse_letter in morse.values() :
                for m in morse.items() :
                    if morse_letter == m[1] :
                        morse_word += m[0]
            morse_letter = ''
        elif i == '/' :                 # Word Change
            morse_word += ' '
        #print(morse_letter)    # Debugging Statement
        #print(morse_word)  # Debugging Statement
    print(morse_word)
    pyperclip.copy(morse_word)  # To Copy Decrypted Word to Clipboard simultaneously


f3 = figlet_format("Morse", font="doh", width = 200)
print(colored(f3, "green"))
a = input("Enter What Do You Wanna Do (1 for Encrypt/ 2 for Decrypt) ? ")
if a == "1" :
    z = input("Enter String to be Encrypted in Morse Code : ")
    encrypt(z)
elif a == "2" :
    z = input("Enter String to be Decrypted : ")
    decrypt(z)
else :
    print("Please Recheck Options")
time.sleep(100)  # So that terminal doesn't crash if opened by double clicking before the User has Read the Output