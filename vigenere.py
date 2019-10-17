'''
This program gets a key and plain text from the user and converts it into cipher
text by the Vigenere Cipher 

Hina Sekine 
'''

# Initialization 
ALPHABET_LOWER = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Greeting
print('This program will conduct a Vigenere Cipher for a key of your choice')
print('for text you enter.\n')

# User input key + error check
key = input('Key: ')
while key.isalpha() == False:
    key = input('Key: ')

key = key.lower()

# User input plain text 
plaintext = input('Plaintext: ')

# Converts key into a list of numbers corresponding to alphabet order 
numKey = []
for i in key:
    numKey.append(ALPHABET_LOWER.find(i))

# Converts each letter by the index of the key
ciphertext = ''
keyUse = 0
for j in range(0, len(plaintext)):
    letter = plaintext[j]
    shift = (ALPHABET_LOWER.find(letter.lower()) + numKey[keyUse % len(key)]) \
            % len(ALPHABET_LOWER)
    if letter in ALPHABET_LOWER:
        ciphertext = ciphertext + ALPHABET_LOWER[shift]
        keyUse = keyUse + 1
    elif letter in ALPHABET_UPPER:
        ciphertext = ciphertext + ALPHABET_UPPER[shift]
        keyUse = keyUse + 1
    else:
        ciphertext = ciphertext + letter

# Display cipher text
print('Ciphertext: ' + ciphertext)
