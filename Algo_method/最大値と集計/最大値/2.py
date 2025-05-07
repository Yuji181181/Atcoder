N = int(input())
A = list(map(int, input().split()))
ans = 10000

for i in A:
    if i < ans:
        ans = i

print(ans)
