import sys
import random
import time


word_file = "words.txt"
word_list = [word.strip() for word in open(word_file).readlines() if len(word) > 3]

def play():
    start_time = time.time()
    hangword = random.choice(word_list).upper()
    #print(hangword)
    letters_used = []
    progress = [" _ "] * len(hangword)
    incorrect = 0    
    while incorrect < 7:
        if ''.join(progress) == hangword:
            break                   
        guess = input("Pick a Letter > ").upper()      
       
        if guess in hangword and guess not in letters_used:             
            found = [index for index, value in enumerate(hangword) if value == guess]
            letters_used.append(guess)
            for f in found:
                for i in range(len(progress)):                
                    progress[f] = guess
            print("\n\nNice One, '%s' Is A Correct Letter!!.." % (guess))
            print("\nCurrent Progress: ", ''.join(progress))
            print("\nLetters Used: ", ' | '.join(letters_used), '\n\n')
        elif guess in letters_used:
            print("\n\nYou Have Already Picked That Letter!!!")
            print("\nCheck The Letters and Try Again!!", ' | '.join(letters_used))
            print("\nCurrent Progress: ", ''.join(progress), '\n\n')
        elif guess not in hangword and guess not in letters_used:
            incorrect += 1
            print("\n\nThat Letter Is Not In The Word, You Have used %d Guesses Out of 7" % (incorrect))
            letters_used.append(guess)
            print("\nCheck The Letters and Try Again!!", ' | '.join(letters_used))
            print("\nCurrent Progress: ", ''.join(progress), '\n\n')    
    if ''.join(progress) == hangword:
        print("\nCongratulations You have Saved the Hangman!!! :)")
        print("\nYou used %d Guesses" % (incorrect))
        print("\nThe Answer is: ", hangword)
        print("You Saved THe Hangman THis GAme In %f seconds" % (time.time() - start_time))  
        new_game = input("Would You Like To Play Again? y/n?: ")   
        if new_game == 'y':
            play()
        else:
            quit()
    else:
        print("\nSorry You Failed, The Hangman Is DeeD!!!")
        print("\nThe Answer is: ", hangword, '\n')   
        print("It Took You In %f Seconds To Send The Man To his Death!" % (time.time() - start_time), '\n\n')
        new_game = input("Would You Like To Play Again? y/n?: ")   
        if new_game == 'y':
            play()
        else:
            quit()       
play()

