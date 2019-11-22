from random import choice

# Checks input from a player
def check_letter(letter, word, show_word):
    if letter in word:
        position_lst = list()
        index = 0
        while index < len(word):
            index = word.find(letter, index)
            if index == -1:
                break
            position_lst.append(index)
            index += 1
        for pos in position_lst:
            show_word[pos] = letter
        print()
    else:
        print("No such letter in the word\n")


# Start of a program
print("H A N G M A N\n")

words_list = ["python", "java", "kotlin", "javascript"]
rigth_answer = choice(words_list)
answer_to_show = ["-"] * len(rigth_answer)

for i in range(8):
    print("".join(answer_to_show))
    letter = input("Input a letter: ")
    check_letter(letter, rigth_answer, answer_to_show)

print("Thanks for playing!")
print("We'll see how well you did in the next stage")