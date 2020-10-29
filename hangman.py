from getpass import getpass  # to input user text without writing it to the console
from sys import exit  # so I can close the program when needed
from time import sleep  # to control program execution


print("\n\t\t-----------------")
print('\t\t  H A N G M A N', end="    ")
print("by Omar")
print("\t\t-----------------\n")


while 1:
    # adapted from Hangman ascii art by chrishorton (GitHub)
    hangmanpics = ['''
                                          +---+
                                              |
                                              |
                                              |
                                              |
                                              |
                                        =========''', ''' 
                                          +---+
                                          |   |
                                              |
                                              |
                                              |
                                              |
                                        =========''', '''
                                          +---+
                                          |   |
                                          O   |
                                              |
                                              |
                                              |
                                        =========''', '''
                                          +---+
                                          |   |
                                          O   |
                                          |   |
                                              |
                                              |
                                        =========''', '''
                                          +---+
                                          |   |
                                          O   |
                                         /|   |
                                              |
                                              |
                                        =========''', '''
                                          +---+
                                          |   |
                                          O   |
                                         /|\  |
                                              |
                                              |
                                        =========''', '''
                                          +---+
                                          |   |
                                          O   |
                                         /|\  |
                                         /    |
                                              |
                                        =========''', '''
                                          +---+
                                          |   |
                                          O   |
                                         /|\  |
                                         / \  |
                                              |
                                        =========''']

    menu = input('Type "play" to play the game, "exit" to quit: ')

    if menu == "play":        
    
        word = ""
        while word == "":
            word = getpass("\nHanger! Choose a word to be guessed (lower case | no spaces): ")
        
        print("\n\n\nNow pass the device to the poor hanged man/woman", flush=True)
        sleep(2)
        print("\nLet's see if he/she can guess your word!", flush=True)
        sleep(2)
        
        right_basket = set()  # for letters in `word`
        wrong_basket = set()
        
        # function adapted from Alexander Kojevnikov (Stack Overflow)
        def is_ascii(s):
            """ This function checkes if the `char` is btwn 97 and 122 
                in ASCII code, tat is, if `char` is a, b, c .... or z"""
            return all(97 <= ord(c) <= 122 for c in s)
        print("\nYou got 8 chances to guess wrong!")
        
        i = 0
        while i < 8:  # user has 8 lives!
            
            sleep(2)
            # If basket and set(word) have same length, then user guessed all letters!
            if len(right_basket) != len(set(word)):

                print()
                # '-' is added to `hint` if word's letter is not found
                hint = [c if c in right_basket else '-' for c in word]
                print(hangmanpics[i])
                print(f"\t\t\t\t{''.join(hint)}\n")

                ltr = input("\t\t\t\tInput a letter: ")
                
                # handling user typos
                if len(ltr) != 1:
                    print("\n\t\t\t\tYou should input a single letter")
                    continue

                if is_ascii(ltr):

                    if ltr in word:
                        if ltr in right_basket:
                            print("\n\t\t\t\tYou already typed this letter...")
                        else:
                            right_basket.add(ltr)
                            print(f"\n\t\t\t\tYes! The word has the letter '{ltr}'!")
                    else:
                        if ltr in wrong_basket:
                            print("\n\t\t\t\tYou already typed this letter...")
                        else:
                            wrong_basket.add(ltr)
                            print("\n\t\t\t\tNo such letter in the word")
                            # user only get hanged if letter is not in word!
                            i += 1
                else:
                    print("\n\t\t\t\tThat's not an English lowercase letter!")
            else:
                # if user guesses word:
                print()
                print('\t\t\t\t' + word)
                print("\n\t\t\t\tYou guessed the word!")
                print("\t\t\t\tYou survived!\n")
                exit(0)
        # this block executes when all chances (8) are used!
        sleep(1)
        print("\n\t\t\t\tYOU DIED!", flush=True)
        print("\n\t\t\t\tAt least you had no chance to find out that you are a LOSER!!", flush=True)
        sleep(2)
        print()

    elif menu == "exit":
        exit(0)

    else:
        continue
    
