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
            if show_word[pos] == letter:
                print("No improvements")
                return False
            show_word[pos] = letter 
        return True
    else:
        print("No such letter in the word")
        return False


# Start of a program
print("H A N G M A N")

words_list = ["python", "java", "kotlin", "javascript"]
rigth_answer = choice(words_list)
answer_to_show = ["-"] * len(rigth_answer)

i = 0
while i < 8:
    print()
    print("".join(answer_to_show))
    if "-" not in answer_to_show:
        print("You guessed the word!\nYou survived!")
        break
    letter = input("Input a letter: ")
    if check_letter(letter, rigth_answer, answer_to_show):
        continue
    else:
        i += 1
        if i == 8:
            print("You are hanged!")