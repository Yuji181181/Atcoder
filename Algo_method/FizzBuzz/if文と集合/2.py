N = int(input())

if N % 5 == 0 or N % 3 == 0:  # この場合は15の倍数の判定は不要
    print("Yes")
else:
    print(N)
