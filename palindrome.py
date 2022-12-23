user_word = input("ENTER WORD HERE: ")


# a function to get a word backwards 
def get_backwards_word(word):
    index = len(word) - 1
    output = ""

    while index >= 0: 
        letter = word[index]
        output += letter
        index = index - 1 
    return output

def is_palindrome(word):
    backwards_word = get_backwards_word(word)
    if word == backwards_word:
        return True 
    else:
        return False 


pal = is_palindrome(user_word)
if pal == True:
    print(user_word, " IS A PaLINDROME")
else:
    print(user_word, " IS NOT A PALINDROME")