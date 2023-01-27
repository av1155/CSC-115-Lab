''' 3.1: String Basics'''

# String = sequence of characters.
# String Literal = Text, spaces, or numbers surrounded by single or double quotes.

''' Sequence type = specifies a collection of objects ordered from left to right. A characters position in a string is called the characters index. Ex: in the string 'Andrea' the character A is at index 0, n is at 1, d is at 2, r is at 3, e is at 4, and a is at 5. '''

# String lenght and indexing.

''' The len() function can be used to output how many characters were used in X sentence. 
Ex: '''

george_v = 'hihihihihihihihihihihihihihihihihihihi'

print(len(george_v))

''' Accessing individual charcaters of a string can be done by using [] and inputting an index inside the brackets. 
Ex: '''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabet[3]

print(alphabet[0], alphabet[1], alphabet[2], alphabet[3])

# You can also use a negative index to input a charcater from the right instead of the left.

print(alphabet[-0], 'negative 0 does not exist though',
      alphabet[-1], alphabet[-2], alphabet[-3])

print()
''' ----------------------------------------------------------------'''

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

user_number = int(input('Enter a number to use as index: '))

print('\nThe letter at index', user_number,
      'of the alphabet is', alphabet[user_number])

# Changing string variables and concatenarting strings
