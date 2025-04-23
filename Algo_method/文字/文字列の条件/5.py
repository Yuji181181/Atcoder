S = input()

result = True  # 大文字なし
for i in S:
    if i.isupper():  # 大文字ありならFalseにしてbreak
        result = False
        break

if result == False:
    print("Yes")
else:
    print("No")
