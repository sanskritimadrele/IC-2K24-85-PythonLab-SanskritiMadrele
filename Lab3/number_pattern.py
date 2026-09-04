n = 4

for i in range(2 * n - 1):
    for j in range(2 * n - 1):

        distance = max(abs(i - (n - 1)), abs(j - (n - 1)))

        print(distance + 1, end=" ")

    print()