N, Q = map(int, input().split())
X = list(map(int, input().split()))

result = []
box_count = [0] * (N + 1)


for i in range(Q):
    if X[i] == 0:
        min_ball = box_count[1]  ## 最小のボールの初期値
        best_box = 1  ## 最適な箱の初期値
        for j in range(2, N + 1):
            if box_count[j] < min_ball:
                min_ball = box_count[j]
                best_box = j

        result.append(best_box)
        box_count[best_box] += 1

    if X[i] >= 1:
        result.append(X[i])
        box_count[X[i]] += 1

for k in result:
    print(k, end=" ")
