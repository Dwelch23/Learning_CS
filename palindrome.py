user_word = input("ENTER WORD HERE: ")


# a function to get a word backwards 
def get_backwards_word(word):
    index = len(word) - 1
    output = ""
    while index >= 0: 
        letter = word[index]
        output += letter
        index -= 1
    return output


# checks to see if it is a palindrome
# using backwards word helper function 
def is_palindrome(word):
    word = word.lower()
    backwards_word = get_backwards_word(word)
    return word == backwards_word


# function to check if it is a palendrome
# using recursion to compare first and last letters
def is_pal(word):
    word = word.lower()
    if len(word) == 1 or len(word) == 0:
        return True
    elif word[0] != word[len(word) - 1]:
        return False
    else:
        return is_pal(word[1 : len(word) - 2])


pal = is_pal(user_word)
if pal == True:
    print(user_word, " IS A PaLINDROME")
else:
    print(user_word, " IS NOT A PALINDROME")
