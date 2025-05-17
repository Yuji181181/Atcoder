S = input()
X1 = S[0]
X2 = S[1]
X3 = S[2]
X4 = S[3]


def password(S):
    if X1 == X2 == X3 == X4:
        return False

    if (
        (int(X1) + 1) % 10 == int(X2)
        and (int(X2) + 1) % 10 == int(X3)
        and (int(X3) + 1) % 10 == int(X4)
    ):
        return False

    return True


if password(S) == True:
    print("Strong")
else:
    print("Weak")

"""
4文字ともおなじ
4文字とも次の数が連続している
"""
