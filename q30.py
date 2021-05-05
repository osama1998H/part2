word = input("Enter The Name: ")


def new_func(word):
    new_word = word[::-1]
    if new_word == word:
        return(True)
    else:
        return(False)


print(new_func(word))
