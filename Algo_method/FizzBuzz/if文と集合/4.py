N = int(input())

for i in range(1, N + 1):
    if N % 15 == 0:
        print("FizzBuzz")
    elif N % 5 == 0:
        print("Buzz")
    elif N % 3 == 0:
        print("Fizz")
    else:
        print(N)
