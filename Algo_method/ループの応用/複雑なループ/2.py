S = input()
T = ""

for i in range(len(S)):
    T += S[i]

print(T)

#####

S = input()
N = len(S) - 1
T = ""
for i in range(N, -1, -1):  # for文の順番を考える
    T += S[i]
print(T)
