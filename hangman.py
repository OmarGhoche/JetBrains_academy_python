from random import choice
from sys import exit  # so I can close the program when needed

print(*'HANGMAN', sep=' ')

while 1:

    menu = input('Type "play" to play the game, "exit" to quit: ')

    if menu == "play":
    
        word = input("\nHanger! Choose a word to be guessed: ")

        right_basket = set()  # for letters in `word`
        wrong_basket = set()

        def is_ascii(s):
          """ This function checkes if the `char` is btwn 97 and 122 
              in ASCII code, tat is, if `char` is a, b, c .... or z"""
            return all(97 <= ord(c) <= 122 for c in s)

        i = 0
        while i < 8:  # user has 8 lives!
            
            # If basket and set(word) have same length, then user guessed all letters!
            if len(right_basket) != len(set(word)):

                print()
                # '-' is added to `hint` if word's letter is not found
                hint = [c if c in right_basket else '-' for c in word]
                print(''.join(hint))

                ltr = input("Input a letter: ")
                
                # handling user typos
                if len(ltr) != 1:
                    print("You should input a single letter")
                    continue

                if is_ascii(ltr):

                    if ltr in word:
                        if ltr in right_basket:
                            print("You already typed this letter")
                        else:
                            right_basket.add(ltr)
                    else:
                        if ltr in wrong_basket:
                            print("You already typed this letter")
                        else:
                            wrong_basket.add(ltr)
                            print("No such letter in the word")
                            # user only get hanged if letter is not in word!
                            i += 1
                else:
                    print("It is not an ASCII lowercase letter")
            else:
                # if user guesses word:
                print()
                print(word)
                print("You guessed the word!")
                print("You survived!")
                exit(0)
        # this block executes when all chances (8) are used!
        print("You lost!")
        print()

    elif menu == "exit":
        exit(0)

    else:
        continue