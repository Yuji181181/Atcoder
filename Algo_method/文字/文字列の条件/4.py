S = input()


def password(S):
    # 全ての文字が同じか判定
    for i in range(3):
        if S[i] != S[i + 1]:
            return False

    # 連続増加か判定
    for j in range(3):
        if int(S[j + 1]) - int(S[j]) != 1:
            return False

    # 連続減少か判定
    for k in range(3):
        if int(S[k]) - int(S[k + 1]) != 1:
            return False

    return True


if password(S) == True:
    print("safe")
else:
    print("dangerous")
