N = int(input())
S = input()
T = input()

count = 0

for i in range(N):
    if S[i] == T[i]:
        count += 1

print(count)


##### 入力の形式
S, T = input().split()  # SとTを同じ行で空白スペースで入力

S = input()  # SとTを改行して入力
T = input()
