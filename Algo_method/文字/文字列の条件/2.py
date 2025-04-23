S = input()


def password(S):
    # 隣り合う文字が異なるか判定
    for i in range(3):
        if S[i] != S[i + 1]:
            return False

    # ★関数内でreturnが実行されると、その時点で関数の実行は終了する

    return True


if password(S) == True:
    print("dangerous")
else:
    print("safe")
