N = int(input())
A = list(map(int, input().split()))
ans = 0


for i in range(N):
    if ans < A[i]:
        ans = A[i]  ## ここで最大値が確定しansに入る

for i in range(N):
    if ans == A[i]:  ## Aの中から最大値のものの番号を全てprintする
        print(i)
