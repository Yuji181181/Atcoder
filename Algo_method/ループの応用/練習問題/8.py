S = input()

zero_count = 0  # 先頭の 0 をカウントする変数
for i in range(len(S)):
    if S[i] == "0":
        zero_count += 1
    else:
        break

# 初めて 0 でなくなったところからの文字列を出力する
T = ""
for i in range(zero_count, len(S)):
    T += S[i]
print(T)
