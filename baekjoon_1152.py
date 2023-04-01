word = input().split(' ')

length = len(word)

if word[0] == '':

    length = len(word) - 1

if word[-1] == '':

    length = len(word) - 1

if word[0] == '' and word[-1] == '':

    length = len(word) - 2

print(length)