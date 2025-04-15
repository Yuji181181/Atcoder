for i in range(-2, 32):
    if i < 1:
        print(".", end=" ")
    else:
        print(i, end=" ")
    if i % 7 == 4:
        print()
