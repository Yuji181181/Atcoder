T = input()
a = len(T) // 2
## int(T)だと0102などの場合4にならない
## /ではrangeの中身が整数ではない可能性がでてエラーになる

result = ""

for i in range(a):
    x = T[2 * i] + T[2 * i + 1]  ## Tの0番目と1番目、２番目と３番目の文字列を結合
    y = int(x)  ## int型に変換
    result += chr(97 + y - 1)  ## ord("a") - 変換した数 + 1で調整

print(result)
