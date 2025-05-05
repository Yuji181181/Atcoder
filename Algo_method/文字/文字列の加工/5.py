S = input()
result = ""

for i in S:  ## ASCIIは10以上がないので変換だと対応できない
    result += str(ord(i) - ord("a") + 1)

print(result)
