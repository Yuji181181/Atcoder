def calc(x):  # Nの桁の総和を計算する関数
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum


N, A, B = map(int, input().split())

result = 0
for i in range(1, N + 1):  # 1からNまでの整数を順に調べる
    if A <= calc(i) <= B:  # もしiの桁の総和がA以上B以下ならば
        result += i  # resultにiを加える
print(result)
