N = int(input())
A = list(map(int, input().split()))

counter = 0

while True:

    ############################ 操作ができるかの判定
    can_do = True
    for i in range(N):
        if A[i] % 2 == 0:
            can_do = False
        if can_do == False:  # 操作ができない場合はwhile文を抜ける
            break
    #############################  ↓ 操作ができる場合の処理

    for i in range(N):
        A[i] //= 2

    counter += 1


print(counter)
