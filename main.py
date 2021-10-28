# importing libraries
import random
import string

print('Useless game \'key\' generator. 1.0') # first thing
print('Game = Half Life 2 Episode 3')

# making the 'key'
letters = string.ascii_letters
print ( ''.join(random.choice(letters) for i in range(16)) )
