N = int(input())
S = input()

for i in S:
    if i.islower == True:
        print("lowercase")
    elif i.isupper == True:
        print("uppercase")
    elif i.isdigit():
        print("Digit")
    else:
        print(i)
