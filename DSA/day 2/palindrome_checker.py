text = input('enter your word: ')
reverse = text[::-1]
if text.lower() == reverse.lower() :
    print("this is a palindrome")
else :
    print('this is not a palindrome')
