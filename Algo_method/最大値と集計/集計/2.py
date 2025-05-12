N = int(input())
A = list(map(int, input().split()))

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(N):
    count[A[i] // 10] += 1

for i in range(10):
    print(count[i])
