import random

def hang_man():
    personages = [
        "   ------------------- \n   |                 |\n   0                 |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n   |                 |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n  /|                 |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n  /|\                |\n                     |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n  /|\                |\n  /                  |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________",
        "   ------------------- \n   |                 |\n   0                 |\n  /|\                |\n  / \                |\n                     |\n                     |\n                     |\n                     |\n                     |\n______________________________"
    ]

    words = ["Mercedes", "BMW", "Tesla", "Lada", "McLaren", "Opel", "Ferrari", "Lamborghini", "Bugatti"]

    word = random.choice(words).lower()
    #print(word)
    guessed_letters = []
    progress = ["_" for _ in range(len(word))]
    print(" ".join(progress))

    count = 6
    true_count = 0
    j = 0

    while count > 0:
        if true_count == len(word):
            break

        letter = input("Enter a letter: ").lower()

        if letter in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(letter)

        if letter in word:
            for i in range(len(word)):
                if letter == word[i]:
                    progress[i] = letter
                    true_count += 1

            print(" ".join(progress))
        else:
            print(personages[j])
            j += 1
            count -= 1

    print("----------------------------------------")
    if count == 0:
        print("You lost!")
        print("The word was:", word)
    else:
        print("Congratulations! You won!")
        print("The word was:", word)


print("Hangman Game")
print("The computer has selected a word, and you have to guess it by entering letters.")
print("If you guess a letter correctly, it will be revealed in the word.")
print("If you guess a letter incorrectly, the hangman will be drawn step by step.")
print("You have 6 attempts to guess the word or the hangman will be complete.")
print()
print("Let's start the game!")
print()

hang_man()
