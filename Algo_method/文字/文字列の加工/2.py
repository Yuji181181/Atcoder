M = input()
count = 0

for i in range(9):
    if i % 2 == 0:
        count += int(M[i])
    if i % 2 == 1:
        count += int(M[i]) * 2


plus = count % 10

if int(M[9]) == plus:
    print("Yes")
else:
    print("No")
