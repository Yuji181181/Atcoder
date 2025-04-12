N = int(input())
A = []

front = 0
back = 2*N-1

for i in range(N):
    A.append(front)
    A.append(back)
    front += 1
    back -= 1

for i in A:
    print(i)


#########

[0,1,2,,,,,2*N-2,2*N-1]