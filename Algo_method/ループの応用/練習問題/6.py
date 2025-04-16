N = input()
result = ""

for i in range(1, len(N) + 1):  # 1~len(N)まで回す
    result = N[-i] + result  # 1文字ずつ逆順にresultに追加していく

    if i % 3 == 0 and i != len(N):  # 3の倍数の時にカンマを追加
        result = "," + result


print(result)
