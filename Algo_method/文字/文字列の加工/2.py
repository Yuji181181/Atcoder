M = int(input())
count = 0

for i in range(9):
    if i % 2 == 0:
        count += int(N[i])
    if i % 2 == 1:
        count += int(N[i]) * 2


plus = count % 10
answer = int(N + str(plus))

if M == answer:
    print("Yes")
else:
    print("No")
