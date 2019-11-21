from random import choice

print("H A N G M A N")

words_list = ["python", "java", "kotlin", "javascript"]
rigth_answer = choice(words_list)
word = input("Guess the world: ")
if word == rigth_answer:
    print("You survived!")
else:
    print("You are hanged!")