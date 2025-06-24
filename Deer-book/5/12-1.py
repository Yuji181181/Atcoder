N = int(input())
exist = [0] * 100

for i in range(N):
    d = int(input())
    exist[d] = 1

print(sum(exist))
