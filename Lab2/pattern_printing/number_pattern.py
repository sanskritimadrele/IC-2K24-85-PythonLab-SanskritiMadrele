n = int(input("Enter number of rows: "))
print("\n Number Pattern")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()