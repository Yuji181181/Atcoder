N = int(input())
A = list(map(int, input().split()))
S = list(input().split())
ans = 0
name = ""

for i in range(N):
    if ans < A[i]:
        ans = A[i]
        name = S[i]

print(name)
