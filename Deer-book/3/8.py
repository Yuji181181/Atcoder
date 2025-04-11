def AC(i):
    if i[0] != "A":
        return False
    if i[2:-1].count("C") != 1:
        return False
    if sum(map(str.isupper, S)) != 2:
        return False
    return True


S = input()

if AC(S) == True:
    print("AC")
else:
    print("WA")
