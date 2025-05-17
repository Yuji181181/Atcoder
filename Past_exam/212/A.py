A, B = map(int, input().split())

if 0 < A and B == 0:
    print("純金")
elif A == 0 and 0 < B:
    print("純銀")
elif 0 < A and 0 < B:
    print("合金")
