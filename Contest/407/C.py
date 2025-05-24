S = input()
count = 0


for i in len(S):
    if int(S[i]) < int(S[i + 1]):
        count += int(S[i]) - int(S[i + 1]) - 1
    if int(S[i]) > int(S[i + 1]):
        count += 10 + int(S[i]) - int(S[i + 1])

print(count)
