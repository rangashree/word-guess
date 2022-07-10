words = ['cat', 'dog', 'why', 'what', 'this', 'stupid', 'idiot', 'man',
         'women', 'ink', 'blue', 'green', 'yellow', 'black', 'yes', 'no',
         'when', 'will']
hard_words = ['elephant', 'google', 'missing',
              'statement', 'white', 'greeter']


import random


def did_user_win(answer, guessed_letter):
    won = True
    for letter in answer:
        if letter not in guessed_letter:
            won = False
            break
    return won


assert(did_user_win('hi', ['h','i','s']) == True)
assert(did_user_win('hi', ['i','s']) == False)

def word_game():
    answer = random.choice(words)
    num_wrong_guess_left = 6
    guessed_letter = []

    while num_wrong_guess_left > 0:
        display_word = ""
        for letter in answer:
            if letter in guessed_letter:
                display_word += letter
            else:
                display_word += '_'
            display_word += ' '
        print(display_word.strip())
        print(f'{num_wrong_guess_left} wrong guess left')
        print(f'guesses: {guessed_letter}')

        guess = input("guessed letter")
        guessed_letter.append(guess)

        if guess in answer:
            print("correct")
        else:
            print("nope")
            num_wrong_guess_left -= 1

        if did_user_win(answer, guessed_letter):
            print("you win !")
            return
    print("sorry you lose")
    print(f'the answer was {answer}')


word_game()
