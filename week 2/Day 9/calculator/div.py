#division module
def div(a,b):
    try:
        division = a / b
        print(f'division: {division: }')
    except ZeroDivisionError:
        print('Division by 0 not possible')

if __name__ == '__main__' :
    div(1,2)