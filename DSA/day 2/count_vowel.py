text = input('enter your word: ')
count = 0
for i in text.lower():
    if i == 'a':
        count += 1
    elif i == 'e':
        count += 1
    elif i == 'i':
        count += 1
    elif i == 'o':
        count += 1
    elif i == 'u':
        count += 1

print(f'no of vowels: {count}')