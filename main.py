# Ceaser cypher thing

import string
# go and load up the strings so we don't have to type out the alphabet
def ceaser(text, shift, alphabets):
# define a function called ceaser that takes 3 arguments
    def shift_alphabet(alphabet):
        #make another function inside the previous function to shift the alphabets
        #should this be a method of a class instead??
        return alphabet[shift_register:] + alphabet[:shift_register]
        # creates a new var that starts the string at the index of shift_register and then appends
        # everything up to the shift register at the end of the string

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    # create a new var shifted alphabets by passing the alphabets argument to
    # the shift_alphabet function above and create a tuple out of that so it is in a fixed order
    final_alphabet = ''.join(alphabets)
    # just stick all thr strings passed as arguments to the cesar function together so
    # that they are now one long string with all the alphabets in it
    final_shifted_alphabets = ''.join(shifted_alphabets)
    # do the same thing but this time with the tuple created above
    table = str.maketrans(final_alphabet, final_shifted_alphabets)
    # create a table that translates the charaters from the alphabet string into
    # the final shifted alphabet tuple
    return text.translate(table)
    # take the text argument input to the function and substitute the
    # shifted characters according to the table created above

againYN = True
#create a var for the while loop so you can cypher several phrases
print(""" wellcome to an implementation of 
___  ____ _ _ _                     _____               _      
|  \/  (_) (_) |                   |  __ \             | |     
| .  . |_| |_| |_ __ _ _ __ _   _  | |  \/_ __ __ _  __| | ___ 
| |\/| | | | | __/ _` | '__| | | | | | __| '__/ _` |/ _` |/ _ \/
| |  | | | | | || (_| | |  | |_| | | |_\ \ | | (_| | (_| |  __/
\_|  |_/_|_|_|\__\__,_|_|   \__, |  \____/_|  \__,_|\__,_|\___|
                             __/ |                             
                            |___/                              
 _____                            _   _                        
|  ___|                          | | (_)                       
| |__ _ __   ___ _ __ _   _ _ __ | |_ _  ___  _ __             
|  __| '_ \ / __| '__| | | | '_ \| __| |/ _ \| '_ \            
| |__| | | | (__| |  | |_| | |_) | |_| | (_) | | | |           
\____/_| |_|\___|_|   \__, | .__/ \__|_|\___/|_| |_|           
                       __/ | |                                 
                      |___/|_|   circa 58-45 BCE     """)
# silly title with ascii art

while againYN:
    again = 'foo'
    # placeholder to trigger the go again loop nested inside the main loop
    plain_text = input('enter your text\n>')
    shift_register = int(input('Enter shift register\n>'))
    if shift_register not in range(-26,26):
        # check to see if a usable number has been ahs been entered
        mod_val = shift_register %26
        #get the modulus vaule to see how many times the shift loops
        shift_register = mod_val
        # change the vaule to the amount of left over after the number is decided by 26

    alphabets_in = string.ascii_letters, string.punctuation
    # create a variable that just calls the stored list of all English ASCII letters, and
    # also punctuation so that gets cypher processed as well, that way it can be quickly changed later

    cypher_text = ceaser(plain_text, shift_register, alphabets_in)
    #asign the output of the ceaser function to the variable cypher_text
    print(f"\n\nYou cypher text is:\n{cypher_text} \n")
    # display the output on the screen as using an f string

    while again not in ['y', 'n']:
    # check to see if y or n has been entered by creating a short list of y n.
        again = input("Do another one?\nY/N >").strip().lower()[0]
        #again holds the value of the charater at the 0th position stripped to lower case
        if again == 'n':
            againYN = False
            # if that character is n, set againYN to false so the main loop will stop
            break
            # break out of this loop
        elif again == 'y':
            againYN = True
            # if the character is a y keep going in the main loop
            break
        else:
            print('Enter Y or N, yah dingus!')
            # prompt the user if they enter some other thing.


# Code Based on a YouTube Tutorial by NeuralNine, with additions and modifications
# https://www.youtube.com/watch?v=JEsUlx0Ps9k