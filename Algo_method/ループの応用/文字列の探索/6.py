N = int(input())
S = input()
count = 0

for i in range(N):
    if S[i] == "a" and S[i + 1] == "b" and S[i + 2] == "c":
        count += 1

print(count)
