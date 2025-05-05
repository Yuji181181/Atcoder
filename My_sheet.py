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

# for i in range()
for i in range(100, 110):
    print(i)  # 100から109までの数字を表示

for i in range(100, 110, 3):
    print(i)  # 100, 103, 106, 109までの数字を表示

for i in range(10, 0, -1):
    print(i)  # 10から1までの数字を表示

for i in range(60, 10, -10):
    print(i)  # 60, 50, 40, 30, 20までの数字を表示

# その他のfor文(リスト、文字列)
S = "abcd"
for i in S:
    print(i)  # 実行結果 a,b,c,d(縦)

L = [4, 2, 5, 3]
for i in L:
    print(i)  # 実行結果 4,2,5,3(縦)


print("こんにちは", end=" ")
print("世界")
# こんにちは  世界 を出力

print("ABC", end="")
print("DEF")
# こんにちは世界 を出力

print("一列目", end=" ")
print("終わり", end=" ")
print()
print("二列目")
# 一列目 終わり
# 二列目         を出力

## for,while 文中の else,continue,break
# continue :以降を無視してfor,while文の先頭に戻る
# break : 以降を無視してfor,while文の処理自体を終了する

for x in range(5):
    if x == 3:  # i=3のときprint(x)を無視してi=4にいく
        continue
    print(x)  # 実行結果 0,1,2,4(縦)

for x in range(5):
    if x == 3:  # i=3になったらfor文を抜ける
        break
    print(x)  # 実行結果 0,1,2(縦)


### 演算子

# a ** b  aのb乗
# a / b   割り算
# a % b   aをbで割った余り
# a // b  切り捨ての割り算

# a in b  aがbに含まれている
# a not in b  aがbに含まれていない


print(ord("A"))  # 65を出力
print(chr(65))  # Aを出力

# 大文字小文字を判定する関数
print("abc".islower())  # Trueを返す
print('"DEF'.islower())  # Falseを返す
print("ABC".isupper())  # Trueを返す

print("appleいく 1　9".islower())  # Trueを返す
# 数、日本語、空白などは無視される

print("11 514".isdigit())  # Trueを返す
# 数の判定だが""は必要

print(int("001"))  # 1を出力
