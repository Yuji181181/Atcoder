N = int(input())
A = list(map(int, input().split()))

## 初期値を準備
count = [0, 0, 0, 0, 0, 0, 0, 0, 0]

## Aの中身を数えてcountに反映させる
for i in A:
    count[i - 1] += 1


for i in count:
    print(i)
