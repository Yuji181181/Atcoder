a = [2, 5, 3, 6]
a.sort()  # 小さい順にソート
a.sort(reverse=True)  # 大きい順にソート

b = "abcde"
c = "fghij"
print(b[0])  # 1番目の要素を表示
print(b[-1])  # 最後の要素を表示
print(len(b))  # bの長さを表示
print(b[2:4])  # 3番目から5番目の要素を表示
print(b[1:])  # 2番目から最後までの要素を表示
print(b[:-2])  # 最後の2文字を消し、最初から3番目までの要素を表示
print(b[::2])  # 偶数番目の要素を表示
print(b + c)  # bとcを結合

for i in range(100, 110):
    print(i)  # 100から109までの数字を表示

for i in range(100, 110, 3):
    print(i)  # 100, 103, 106, 109までの数字を表示
