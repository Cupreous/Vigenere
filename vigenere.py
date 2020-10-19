import sys # for args - recommended to use by the group that I was in during class (I asked for some help with python)

# User inputs that will be used in the function
action = sys.argv[1] # The thing I imported is using the python file itself as the first argument
text = sys.argv[2]
key = sys.argv[3]

#Vigenere Function
def vigenere(text, key, encode):

    #sets up main variables for use in the encoding/decoding
    text = text.lower() #takes the text in lower case
    key = key.lower() #takes the key in lower case
    alphabet = 'abcdefghijklmnopqrstuvwxyz' #alphabet, which is compatible because of previous two lines

    #more variables
    output = ''
    index = 0 # counter for index in key (I forgot and couldn't find on google how to do a for loop with this built in in python)

    #checks if the key length is less than the length of the text (if it is then it is modified so that they are equal)
    if len(text) > len(key):
        times = (len(text) // len(key)) + 1 # the number of repeats needed
        auxkey = key * times #multiplies the key so that it's length is >= text
        key = auxkey[:len(text)] # Truncates the key so that it's length is = text if the multiplication sent it over

    #processing - encoding/decoding
    for letter in text:
        kindex = alphabet.index(key[index]) #the letter at the specified index of the key translated to the alphabet (for displacement)
        if encode != True: #As Mr.K recommended for the previous assignment, this robustifies the function such that the displacement for encoding/decoding doesn't need separate functions
            kindex *= -1 
        new = alphabet.index(letter) + kindex
        output += alphabet[new % 26] # This wraps it around the alphabet, so you won't get any weirdness
        index += 1 #increases counter
        

    #output
    return output

#printing
if sys.argv[1] == 'encode':
    print(vigenere(text, key, True))
else:
    print(vigenere(text, key, False))
