N = int(input())
S = input()
result = ""

for i in S:
    if i == "A":
        result += "T"
    elif i == "T":
        result += "A"
    elif i == "G":
        result += "C"
    elif i == "C":
        result += "G"

print(result)
