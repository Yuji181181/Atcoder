N = int(input())

for i in range(1, N + 1):
    if "4" in str(i) or "9" in str(i):
        continue  # 4,9が入ってるとき、print(x)を無視してfor文冒頭に戻る
    print(i)
