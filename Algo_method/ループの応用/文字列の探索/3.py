N = int(input())
S = input()
count = 0

for i in range(N):
    if S[i] == "a":
        count += 1

print(count)


##### pythonのcountメソッドで文字列のカウントができる

N = int(input())
S = input()
print(S.count("a"))
