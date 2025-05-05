M = input()
result = ""

for i in range(5):
    a = int(M[i])
    if a <= 2:
        result += str(a + 7)
    else:
        result += str(a - 3)

print(result)
