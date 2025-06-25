N = int(input())
S = input().split()

i = 0
while i < N:
    j = 1
    while j < N and S[j] == S[i]:
        j += 1

    print(S[i], j - i)
    i = j
