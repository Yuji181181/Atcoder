N = input()
count = 0

for i in range(9):
    if i % 2 == 0:  ## ここはint(N[i])ではなく i でいい
        count += int(N[i])
    if i % 2 == 1:
        count += int(N[i]) * 2


plus = count % 10

print(N + str(plus))
