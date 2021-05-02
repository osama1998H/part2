import random
litters = ['a', 'e', 'i', 'o', 'u']

char_list = ['a', 'e', 'i', 'o', 'u']

for i in range(len(char_list)**3):

    random.shuffle(char_list)
    print(''.join(char_list))
