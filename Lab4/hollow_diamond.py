n = int(input("Enter an odd number: "))

if n % 2 == 0:
    print("Please enter an odd number.")
else:
    mid = n // 2
    for i in range(n):
        lev = i if i <= mid else n - 1 - i

        for j in range(2 * n - 1):
            if j == mid - lev or j == mid + lev:
                print("*", end="")
            else:
                print(" ", end="")

        print()