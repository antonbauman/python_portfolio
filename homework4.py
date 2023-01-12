# Program for entering a number or word and checking its parameters: Lengths for words or evens or odd for numbers

var = input("Input anything: ")

if var.isdigit():
    var = int(var)

    def is_even(x):
        """
        Check for evenness or oddness of a number
        """
        return x % 2 == 0

    if is_even(var):
        print(f"You input a number {var} is even")
    else:
        print(f"You input a number {var} is odd")
else:
    len_var = len(var)
    print(f"You input a Word, length {len_var}")

print(" ")
print("Thanks for checking")
