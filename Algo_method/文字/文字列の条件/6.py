"""
パス
"""

S = input()
count = 0


if len(S) >= 10:
    count += 1

if S in ():
    count += 1


if not 6 <= len(S) <= 64:
    print("invalid")
elif count == 2:
    print("weak")
elif count == 3:
    print("medium")
elif count >= 4:
    print("strong")


""""
6-64 なし invalid

len10 以上
a-z
A-Z
0-9
!,?,@

2 weak
3 medium
4 strong
"""
