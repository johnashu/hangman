import sys
import random

word_file = "words.txt"
word_list = [word.strip() for word in open(word_file).readlines() if len(word) > 6]

def play():

    hangword = random.choice(word_list)
    print(hangword.upper())
    letters_used = []
    progress = ["_"] * len(hangword)
    numwrong = 0    
    while numwrong < 7:
        
        guess = input("Pick a Letter > ")
            
        if guess in hangword and guess not in letters_used:             
            found = [index for index, value in enumerate(hangword) if value == guess]
            letters_used.append(guess.upper())
            for f in found:
                for i in range(len(progress)):                
                    progress[f] = guess.upper()

            print("\nCurrent Progress: ", ''.join(progress))
            print("\nLetters Used: ", letters_used, '\n\n')

        elif guess in letters_used:
            print("\nYou Have Already Picked That Letter!!!")
            print("\nCheck The Letters and Try Again!!", letters_used)
            print("\nCurrent Progress: ", ''.join(progress), '\n\n')

        elif guess not in hangword and guess not in letters_used:
            numwrong += 1
            print("\nThat Letter Is Not In The Word, You Have used %d Guesses Out of 7" % (numwrong))
            letters_used.append(guess.upper())
            print("\nCheck The Letters and Try Again!!", letters_used)
            print("\nCurrent Progress: ", ''.join(progress), '\n\n')

    
    if ''.join(progress) == hangword:
        print("\nCongratulations You have Saved the Hangman!!! :)")
        print("\nYou Had %d Guesses Left" % (numwrong))
        print("\nThe Answer is: ", hangword)        
    else:
        print("\nSorry You Failed, The Hangman Is DeeD!!!")
        print("\nThe Answer is: ", hangword.upper())   
        print("\nGoodbye")
        quit()

play()