N = int(input())
P = list(map(int, input().split()))
count = 0


def child(P):
    if len(P) < 4:
        return False

    elif P[0] > P[1]:
        return False

    for i in range(1, N + 1):
        if P[i] < P[i + 1] and P[i + 1] < P[i + 2]:
            return False

        if P[i] > P[i + 1] and P[i + 1] < P[i + 2]:
            return False

    return True


### 無理
