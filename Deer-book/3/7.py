N = int(input())
a = list(map(int, input().split()))


a.sort(reverse=True) 大きい順にソート
result = 0

for i in range(N):
    if i % 2 == 0: # Nが偶数の時
        result += a[i]
    else: # Nが奇数の時
        result -= a[i] 

print(result)
