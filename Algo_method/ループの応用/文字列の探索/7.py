N, L, R = map(int, input().split())
S = input()

for i in range(L, R + 1):
    print(S[i])


##### ↑ 出力が1行ずつ改行されてしまう


N, L, R = map(int, input().split())
S = input()
result = ""

for i in range(L, R + 1):
    result += S[i]

print(result)


##### ↓ スライスを使った場合


N, L, R = map(int, input().split())
S = input()

print(S[L : R + 1])
