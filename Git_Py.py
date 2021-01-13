word = input("Enter a string, please: ")
word_copy = word
count = 0


def counting(word, word_copy,count):
    if len(word_copy) < 1:
        return
    for i in range(len(word_copy)):
        if word_copy[i] == word[i]:
            count += 1
    counting(word_copy[1:])

