n = int(input("Enter the number of rows: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()