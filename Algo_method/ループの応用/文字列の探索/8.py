S = input()
T = input()

N = len(S)
M = len(T)

result = False

for i in range(N - M + 1):  ##
    if S[i : i + M] == T:
        result = True

if result == True:
    print("Yes")
else:
    print("No")


## N-M+1の理由 T = 3の時、i+2まで探索するため
"""
例 S="algorism"(N=8) , T="ris"(M=3) の時 → range(6)

i=0: S[0:3] -> "alg"
i=1: S[1:4] -> "lgo"
.
.
.
i=4: S[4:7] -> "rim" (一致！)
i=5: S[5:8] -> "ism" (最後)
"""
