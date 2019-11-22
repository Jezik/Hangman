from random import choice

print("H A N G M A N")

words_list = ["python", "java", "kotlin", "javascript"]
rigth_answer = choice(words_list)
answer_to_show = rigth_answer[:3] + "-" * (len(rigth_answer) - 3)
word = input("Guess the world {}: ".format(answer_to_show))
if word == rigth_answer:
    print("You survived!")
else:
    print("You are hanged!")