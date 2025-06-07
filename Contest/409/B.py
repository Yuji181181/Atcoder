N = int(input())
A = list(map(int, input().split()))
result = 0

for i in range(N + 1):
    count = 0
    for j in range(N):
        if i <= A[j]:
            count += 1
    if i <= count:
        result = i

print(result)
