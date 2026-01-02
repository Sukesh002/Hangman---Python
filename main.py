import random
import stages 


word_list=["apple","banana","pineapple","strawberry","cherry"]
chosen_word=random.choice(word_list)
lives=6
display=[]
for i in range(len(chosen_word)):
    display+='_'
print(display)
game_over=False
while not game_over:
    gussed_letter=input("Guess a letter :").lower()
    for position in range(len(chosen_word)) :
        if gussed_letter == chosen_word[position]:
            display[position]=gussed_letter
    print(display)
    if gussed_letter not in chosen_word:
        lives-=1 
        print(stages.hangman_stages[lives])
        if lives==0:
            game_over=True
            print("You Lose")
    if '_' not in display:
        game_over=True
        print("You Win")
        
    