N = int(input())
A = list(map(int, input().split()))
score = []

for i in range(N):
    score.append((A[i], i + 1))

score.sort()

print(score[N - 2][1])
