#check the palindrome
def ispalindrome(a):
    reverse_word=(a[::-1])
    if a==reverse_word:
        return True
    else:
        return  False



x=input("enter any word: ")
y=ispalindrome(x)
print(f"palindrome of word you enter: {y}")
