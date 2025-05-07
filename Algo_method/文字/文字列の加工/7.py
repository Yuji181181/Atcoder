## 難

S = input()
result = ""
i = 0  ## 初期値

while i < len(S):  ## 長さの数だけループ
    x = S[i]  ## 今見てる文字
    j = i + 1  ## 次の文字の位置(今+1)
    while j < len(S) and x == S[j]:  ## i+1 < len(S) かつ S[i] == S[i+1] の間ループ
        j += 1  ## 次のループに行くのに+1して次の文字の位置へ
    result += x + str(j - i)  ## resultに追加
    i = j  ## 次に見る位置(1つ目のwhile文)をiからjに更新

print(result)


##### 正解


S = input()
ans = ""

N = len(S)
i = 0
while i < N:
    c = S[i]
    j = i + 1
    while j < N and c == S[j]:
        j += 1
    ans += c + str(j - i)
    i = j

print(ans)
