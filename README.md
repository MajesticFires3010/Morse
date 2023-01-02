# Morse Coder Decoder

**Morse Code Encryption and Decryption in Python3**

**Use this Easy to Use GitHub Repository to Converse in a Morse Code Format**

## Special Instruction for Shared Copying of Morse/Normal Text
> If Terminal or Python IDE or any special Environment is being used for Morse Enryption/Decryption, Copying of Output is not necessary because the code pushes the Output into the Clipboard Automatically.

**Self-Explanatory Code with Ample amount of Comments**

## Installation
Code can be simply executed by downloading the "morse.exe" and running it on the system.

You can install the all requirements for running the code properly from **requirements.txt** by using pip.

    pip install -r requirements.txt


### Morse Encryption-Decryption Algorithm : 

> Alphabets, Numbers and Special Characters with their Morse Code are stored in a dictionary "morse".

> If the User selects to Encrypt Normal Text into Morse Code:  
User inputted string is firstly converted into Uppercase.   
Each character is compared to the keys in the dictionary "morse" and hence replaced by it's value in the dictionary or '/' is added in place of space.   
This is then added into the void array "morse_word".   
This process continues for the entire string and is hence printed.

> If the User selects to Decrypt Morse Code to Normal Text:  
Two void arrays are taken as "morse_word" and "morse_letter".   
The whole array of dots and dashes is calculated and entered inside the "morse_letter". On encountering a space, the letter is changed and hence using the key-value pair from the dictionary and hence the english alphabet is added to the "morse_word" and the "morse_letter" is reset to void array for the next alphabet. On the other hand, if '/' is encountered, a space is added into the "morse_word".   
This process continues for the entire string and is hence printed.

> At the end, the output is automatically copied on the clipboard.


### Morse Code Conversion :

> Letters   
A	. _  
B	_ . . .	
C	_ . _ .	
D	_ . .	 	
E	.	 	
F	. . _ .	
G	_ _ .	 	
H	. . . .	
I	. .	 	
J	. _ _ _	
K	_ . _	 	
L	. _ . .	
M	_ _	 	
N	_ .	 
O	_ _ _	 
P	. _ _ .	
Q	_ _ . _	
R	. _ .	   
S	. . .	 
T	_	 
U	. . _	 
V	. . . _	
W	. _ _	  
X	_ . . _	 
Y	_ . _ _	
Z	_ _ . .	  

 	 	 	 			 
> Numbers
1	. _ _ _ _	 	
2	. . _ _ _	 	
3	. . . _ _	 	
4	. . . . _	 	
5	. . . . .	 	
6	_ . . . .	 
7	_ _ . . .	 
8	_ _ _ . .	 
9	_ _ _ _ .	 
0	_ _ _ _ _

> Special Characters
.	.-.-.-   
,	--..--   	
?	..--..   	
'	.----.  	
!	-.-.--  	
/	-..-.	  	
(	-.--.	  	
)	-.--.-  	
&	.-...	  	
:	---...     
;	-.-.-.  
=	-...-  
+	.-.-.  
-	-....-  
_	..--.-  
"	.-..-.  
$	...-..-  
@	.--.-.  
¿	..-.-	  	
¡	--...-  
