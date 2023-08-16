import random
import asset.logo as logo


stages = logo.stages


lives = len(stages)
words = ['swarnava','kihbe','kjane']

chosen_word = random.choice(words)



display=[ "_" for i in chosen_word ]
end_of_game=False
while not end_of_game:
    guess_word = input("Guess a letter").lower()
    for pos in range(0,len(chosen_word)):
        if guess_word == chosen_word[pos]:
            display[pos]=guess_word
    if guess_word not in chosen_word:
        lives-=1
        print(stages[lives])
        if lives == 0:
            end_of_game=True
            print(f"the word is {chosen_word}")
    else:
        print(" ".join(display))
    if '_' not in display:
        end_of_game = True
        print("You won")




