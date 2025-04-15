N = int(input())
S = input()
T = input()
count = 0

for i in range(N):
    if S[i] == T[i]:
        count += 1
    if S[i] or T[i] == "?":
        count += 1

print(count)

# 間違い箇所
# 1,NとS両方"?"だった場合重複になる
# 2,orの解釈  この場合S[i]になにかしら入っていた場合Trueを返し+=1されてしまう
