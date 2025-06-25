N = int(input())
S = set()  ## 空の集合を作成
for i in range(N):
    S.add(input())  ## 1行ず入力を受け取り集合に追加
print(len(S))

## set(集合)は重複を許さないので、同じ値が追加されても内容は変わらない。
