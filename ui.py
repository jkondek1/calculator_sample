from counting import get_count

def ask_user():
    print('Hello. This is an awesome calculator. Input a number:')
    number = int(input())
    print('divisor')
    is_correct = False
    while not is_correct:
        try:
            divisor = int(input())
            is_correct = True
        except ValueError:
            print('zadaj korektne cislo') 
    print(get_count(number,divisor))
