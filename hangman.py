import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#1
words=["abhi","venky","vamshi"]
lives=6
choose_words = random.choice(words)
print(choose_words)

#3
placeholder=""
lenght =len(choose_words)
for i in range(lenght):
    placeholder+="_"
print(placeholder)

#4
game_over=False
correct_letters=[]
while not game_over:
    guess=input("Guess a word:").lower()

#2
    display=""
    for letters in choose_words:
        if letters==guess:
            display+=letters
            correct_letters.append(letters)
        elif letters in correct_letters:
            display+=letters
        else:
            display+="_"
    print(display)
#6
    if guess not in choose_words:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives==0:
            game_over=True
            print("You lose")  

#5
    if "_" not in display:
        game_over=True
        print("You Win")    
#7
    print(stages[lives])


    