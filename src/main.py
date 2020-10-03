print("Welcome to MY PROGRAM")
print("Python is awesome!")

def f(x):
    return 2**x

# def f2(x):
#     sum = 0
#     with open("data\\num.txt") as input:
#         numbers = input.readlines()
#         for n in numbers:
#             sum += int(n) ** x
#     return sum

x = int(input("enter a number: "))
print("f(x) = " + str(f(x)))
