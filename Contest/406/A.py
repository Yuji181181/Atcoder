A, B, C, D = map(int, input().split())

if A < C:
    print("No")
    exit()
elif A > C:
    print("Yes")
    exit()
elif A == C:
    if B < D:
        print("No")
        exit()
    elif B > D:
        print("Yes")
        exit()
