n = int(input("Enter number of rows: "))
print("\n1. Star Pattern")

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
