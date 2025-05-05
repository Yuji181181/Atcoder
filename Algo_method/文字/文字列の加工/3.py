N = input()
result = ""

for i in range(5):
    a = int(N[i])
    if a >= 7:
        result += str(a - 7)
    else:
        result += str(a + 3)

print(result)
