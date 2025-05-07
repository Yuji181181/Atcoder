N, M = map(int, input().split())
for i in range(N):
    A, B = map(int, input().split())
    ans = 0

for i in range(N):
    if M >= B:  ## BがM以下の場合
        if ans < A:  ## 最大値を更新する
            ans = A

print(ans)
