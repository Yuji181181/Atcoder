S = input()


def password(S):
    # 連続するか判定
    for i in range(3):
        if int(S[i + 1]) - int(S[i]) != 1:  # 後-前=1
            return False
    return True


if password(S) == True:
    print("dangerous")
else:
    print("safe")
