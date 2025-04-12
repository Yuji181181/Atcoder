S = input()
a = len(S)

flag = True
for i in range(a):
    if S[i] != S[(a - 1) - i]:  # i=0のとき、(a-1)  # i=1のとき、(a-2)
        flag = False

if flag == True:
    print("Yes")
else:
    print("No")
