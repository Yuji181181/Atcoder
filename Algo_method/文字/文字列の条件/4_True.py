S = input()

# True : 危険
# False: 安全

# 最初は危険(True)を前提にしている


def is_dangerous(S):
    # 全ての文字が同じか判定
    all_same = True
    for i in range(3):
        if S[i] != S[i + 1]:
            all_same = False  # 違う文字が見つかったら False(安全) を返す
            break  # False(安全)のままこのfor文を抜けてif文へ

    if all_same == True:  # ループ後も all_same が True なら本当に全て同じ(危険)
        return True

    # 連続増加か判定
    increasing = True
    for j in range(3):
        if int(S[j + 1]) != int(S[j]) + 1:
            increasing = False  # 連続増加でない箇所が見つかったらFalse(安全)を返す
            break  # False(安全)のままこのfor文を抜けて次のif文へ

    if increasing == True:  # ループ後も increasing が True なら本当に連続増加(危険)
        return True

    # 連続減少か判定
    decreasing = True
    for k in range(3):
        if int(S[k]) != int(S[k + 1]) + 1:
            decreasing = False  # 連続減少でない箇所が見つかったらFalse(安全)を返す
            break  # False(安全)のままこのfor文を抜けてif文へ

    if decreasing == True:  # ループ後も decreasing が True なら本当に連続減少(危険)
        return True

    # 危険なpasswordの条件に一つもあてはまらなかったらFalse(安全)を返す
    return False


if is_dangerous(S) == True:
    print("dangerous")
else:
    print("safe")
