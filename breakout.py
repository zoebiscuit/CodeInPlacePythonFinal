import random

LEXICON_FILE = "Lexicon.txt"
INITIAL_GUESSES = 10

def play_game(secret_word):
    pass

def get_word():
    index = random.randrange(300)

    all_words = []
    

    with open(LEXICON_FILE, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                all_words.append(str(cleaned_line))

    return all_words[index]
    
def main():
    count = 0
    secret_word = get_word().lower()
    announced_word = secret_word
    play_game(secret_word)

    revealed_word = ""
    for i in range(len(secret_word)):
        revealed_word += "-"

    print("Welcome to a simple game of Wordle. All done in Python by Zoe Bisset!")
    print(f"The word has {len(secret_word)} letters.")

    while i < INITIAL_GUESSES:
        print(f"The word looks like this {revealed_word}")
        print(f"You are on guess number {INITIAL_GUESSES-count}")
        guess = input("Type a single letter here, then press enter: ")
        guess = guess.lower()
        count += 1
        x = 0

        print("--------------------------------------------")
        while x<len(revealed_word):
            position = secret_word.find(guess)
            if int(position) == -1:
                x = len(revealed_word) + 1
            else:
                print(f"Letter number {position+1} is {guess}")
                secret_word = secret_word.replace(guess, "-", 1) #im getting an error here
                #print(secret_word) 
                #revealed_word = revealed_word.strip(0, position) + guess + revealed_word.slice(position, len(revealed_word))
                #print(revealed_word)
                new_word = [] #creating a new array!!!!!!!
                #print(new_word)
                for z in range(len(revealed_word)):
                    new_word.append(revealed_word[z])  #trying to find the letter in the revealed word at a certain index and put that letter in the list
                    if z == position:
                        new_word.append(guess)

                revealed_word = "" #resetting string so we can rebuild what i have
                for y in range(len(secret_word)):
                    revealed_word += new_word[y]
                    #print(new_word)
        
            if revealed_word == announced_word:
                print(f"WORDLE! You got it in {INITIAL_GUESSES-count} guesses! The word was {announced_word}!")
                x = len(revealed_word) + 1
                i = INITIAL_GUESSES + 1

        if INITIAL_GUESSES == count:
            i = INITIAL_GUESSES + 1
#######################################################################

    if revealed_word != announced_word:
        print(f"Aww man! You ran out of guesses! The word was {announced_word}!")


if __name__ == '__main__':
    main()