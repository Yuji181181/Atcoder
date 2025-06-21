N = int(input())
D = list(map(int, input().split()))

stations = [0] * N
for i in range(N - 1):
    stations[i + 1] = stations[i] + D[i]

for i in range(N):
    for j in range(i + 1, N):
        print(stations[j] - stations[i])
