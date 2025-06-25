from collections import defaultdict

a = ["cat", "dog", "tac", "god", "act", "cat"]

num = defaultdict(int)

for i in a:
    num[i] += 1

for key in num:
    print(key, num[key])
