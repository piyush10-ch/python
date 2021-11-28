def check_palindrome(word):
    reverse_word=word[::-1]
    if word==reverse_word:
        return True
    else:
        return False
a= input("enter any word: ")
b=check_palindrome(a)
print(f"the word you enter is palindrome: {b}")