import time

words = input("Enter some words ")

for latter in words:
    if latter.isdigit():
        '''
        Check later for even or odd
        '''
        if int(latter) % 2 == 0:
            print(f"A difit {latter} is even")
        elif int(latter) % 2 != 0:
            print(f"A difit {latter} is odd")
    elif latter.isalnum():
        '''
        Check later for capital or not
        '''
        if latter.isupper():
            print(f"A latter {latter} is а capital")
        else:
            print(f"A latter {latter} is а not capital")
    else:
        '''
        Other values are symbols
        '''
        print(f"A latter {latter} is а symbol")

print()

while True:
    '''
    Eternal cycle, with a timer for the print function
    '''
    time.sleep(4.2)
    print("I love Python")