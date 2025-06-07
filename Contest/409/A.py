N = int(input())
T = input()
A = input()
result = False

for i in range(N):
    if T[i] == "o" and A[i] == "o":
        result = True

if result == True:
    print("Yes")
else:
    print("No")
