N, L, R = map(int, input().split())
A = []

for i in range(L, R + 1):  # L~Rをまず入れる
    A.append(i)

for i in range(0, L):
    A.append(i)

for i in range(R + 1, N):
    A.append(i)

for x in A:
    print(x)
