N = int(input())
count = 0

for i in range(1, N + 1):
    if N % 3 == 0 and N % 5 != 0:
        count += 1

print(count)
