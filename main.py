# The def is used to create a function named caesar. The user will input the text, shift, and 
# encrypt value. The default encrypt value is set to true 

from matplotlib import text


def caesar(text, shift, encrypt=True): 
# We must start by handling edge cases, such as if users input a string instead of 
# an integer for the shift value 
     if not isinstance(shift, int): 
          return 'Shift must be an integer value.' 
     if shift < 1 or shift > 25: 
          return 'Shift must be an integer between 1 and 25.' 
     
# We must also define the alphabet 
     alphabet = 'abcdefghijklmnopqrstuvwxyz' 

#If encrypt is not true, we want to set the shift backward to return the original message 
     if not encrypt: shift = - shift 

# Our shifted alphabet will be equal to the alphabet beginning at the shift point, concatenating 
# with the alphabet ending at the shift point. This uses slicing to account for the alphabet at the 
# shift point 
     shifted_alphabet = alphabet[shift:] + alphabet[:shift] 

# str.maketrans creates a mapping dictionary between the alphabet and alphabet in uppercase 
# and the shifted alphabet in upper and lowercase 
     translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()) 

# Now that we have a mapping dictionary, we can use translate on the text to move it into the mapping 
# table/translation table. We will assign the output to encrypted text 

     encrypted_text = text.translate(translation_table) 

# Once encryption is complete, return the encrypted text 
     return encrypted_text 
# We will create an encryption function where the user can input the text and shift and the function 
# will encrypt the data for the user. 
def encrypt(text, shift): 
     return caesar(text, shift) 

# We will also create a decryption function to decrypt the text by inputting the shift 
def decrypt(text, shift): 
     return caesar(text, shift, encrypt=False) 

# Ask the user whether they would like to encrypt or decrypt the message 
print("Would you like to encrypt or decrypt the message?") 

# Save the user's input as the variable user_choice 
user_choice = input() 

# If the user selects encrypt, ask them to enter the message and shift 
if user_choice.lower() == 'encrypt': 
     print("Please enter the message to encrypt:") 
     message = input() 
     print("Please enter the shift:") 
     shift = int(input()) 
     print("Encrypted message:" + encrypt(message, shift)) 
     
# If the user selects decrypt, ask them to enter the encrypted message and shift 
if user_choice.lower() == 'decrypt': 
     print("Please enter the message to decrypt:") 
     message = input() 
     print("Please enter the shift:") 
     shift = int(input()) 
     print("Decrypted message:" + decrypt(message, shift)) 
     
# If the user does not enter either option, tell them to only enter encrypt or decrypt 
if user_choice.lower() != 'encrypt' and user_choice.lower() !="decrypt": 
     print("Please enter encrypt or decrypt. I will not accept other options")