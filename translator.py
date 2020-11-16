# ------------------------------------------- STAGE 7/7 ---------------------------------- #
from sys import argv, exit
import requests
from bs4 import BeautifulSoup


# dict of numbers to languages
langs = {"1": "arabic", "2": "german", "3": "english", "4": "spanish",
         "5": "french", "6": "hebrew", "7": "japanese", "8": "dutch",
         "9": "polish", "10": "portuguese", "11": "romanian",
         "12": "russian", "13": "turkish"}

# User inputs - if done throw CLI arguments
if len(argv) > 1:

    # Handling LanguagesNotSupportedError
    a = argv[1]
    b = argv[2]
    for p in a, b:
        if p in langs.values() or p == "all":
            pass
        else:
            print(f"Sorry, the program doesn't support {p}")
            exit(1)

    # Function to get `langs` key from argv!
    # Credits to GeeksForGeeks for this one!
    def get_key(val):
        for key, value in langs.items():
            if val == value:
                return key

    lang1 = get_key(a)
    lang2 = "all" if b == "all" else get_key(b)
    word = argv[3]
else:
    print("Hello, you're welcome to the translator. Translator supports:")
    for k, v in langs.items():
        print(f"{k}. {v}")
    lang1 = input("Type the number of your language:\n")
    lang2 = input("Type the number of language you want to translate to"
                  "or '0' to translate to all languages:\n")
    word = input('Type the word you want to translate:\n').lower()

if lang2 == '0' or lang2 == "all":
    # saves the mother language to a variable
    # and then deletes it from the dict `langs`
    # not to translate a word to same language!!
    w = langs[lang1]
    del langs[lang1]
    # I goes throw all remaining idioms in dict `langs` and
    # makes a request for each language translation then
    # prints to the console the result and writes it to file
    with open(f"{word}.txt", "w", encoding="utf-8") as file:
        global s
        s = requests.Session()
        for z in langs.values():
            url = f"https://context.reverso.net/translation/{f'{w}-{z}'}/{word}"

            # Handling InternetConnectionError
            try:
                r = s.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            except requests.exceptions.ConnectionError:
                print('Something wrong with your internet connection...')
                exit(1)

            # Handling JabberwockyWordError
            if not r:
                print(f'Sorry, unable to find "{word}"')
                exit(1)

            soup = BeautifulSoup(r.content, 'html.parser')
            # Since only one word is translated, there is only need for `soup.find`
            try:
                translation = soup.find('a', class_='dict').text.strip()
                
                # To save some time, gets nly the first 2 elements of examples
                # Because only a pair of examples is needed!
                e = soup.find_all('div', {'class': ['src', 'trg']})
                examples = [j.text.strip() for j in e[:2]]
                # Saving to `word`.txt
                file.write(f"\n{z.title()} Translation:\n{translation}")
                file.write(f"\n{z.title()} Examples:\n{examples[0]}:\n{examples[1]}\n")
                # Printing to Console
                print(f"\n{z.title()} Translation:\n{translation}")
                print(f"\n{z.title()} Examples:\n{examples[0]}:\n{examples[1]}\n")
                
            except AttributeError:
                # Saving to `word`.txt
                file.write(f"\nNo translation available in {z.title()}\n")
                # Printing to Console
                print(f"\nNo translation available in {z.title()}\n")
            
            # Just to ensure the last `trail` is not printed
            if z != list(langs.values())[-1]:
                print("-------------------------------------------------")
                file.write("\n-------------------------------------------------\n")
else:
    # Algorithm logic and URL parser
    x = f"{langs[lang1]}-{langs[lang2]}"
    url = f"https://context.reverso.net/translation/{x}/{word}"

    # Handling InternetConnectionError
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    except requests.exceptions.ConnectionError:
        print('Something wrong with your internet connection')
        exit(1)

    # Handling JabberwockyWordError
    if not r:
        print(f'Sorry, unable to find "{word}"')
        exit(1)

    # Organizing html data
    soup = BeautifulSoup(r.content, 'html.parser')
    # Keeping only translations
    c = soup.find_all('a', class_='dict')

    # Converting html tags to `string` and stripping white spaces
    translations = [i.text.strip() for i in c]
    
    y = langs[lang2]
    
    # Alternative Handling JabberwockyWordError
    if not translations:
        print(f"\nNo translation available in {y.title()}\n")
        exit(1)
        
    # Getting the examples
    e = soup.find_all('div', {'class': ['src', 'trg']})
    # removing empty text from examples, adapted from Łukasz Nawrot
    examples = list(filter(None, [j.text.strip() for j in e]))

    # Printing to Console
    print(f"\n{y.title()} Translations:")
    for i in translations[:5]:
        print(i)

    print(f"\n{y.title()} Examples:")
    j = 0
    while j < 9:
        print(f"{examples[j]}:")
        j += 1
        print(f"{examples[j]}\n")
        j += 1
