H, A = map(int, input().split())
x = H // A  # 商
if H % A == 0:  # HとAが割り切れる場合
    print(x)
else:  # HとAが割り切れない場合
    print(x + 1)

# 12,4 → 3
# 20,6 → 4
