N, A = map(int, input().split())
B = N % A

if B == 0:
    print(N // A)
else:
    print((N // A) + 1)
