N = int(input())
exist = [0] * 100

for i in range(N):
    d = int(input())  ## 1行ず入力を受け取る
    exist[d] = 1  ## 存在する番号を1にする(今回はcountするだけ)

print(sum(exist))
