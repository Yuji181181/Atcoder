S = input()


def password(S):
    # 四文字の判定
    if len(S) != 4:
        return False

    # 数字か判定
    for i in S:
        if not (ord("0") <= ord(i) <= ord("9")):
            return False

    return True


if password(S) == True:
    print("valid")
else:
    print("invalid")
