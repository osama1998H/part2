
word = input("Enter The Name: ")


def new_func(word):
    new_word = word[::-1]
    result = int(word) + int(new_word)
    invered_result = str(result)[::-1]
    
    if str(result) == invered_result:
        return(True, result, invered_result)
    else:
        return(False, result, invered_result)
    


print(new_func(word))
