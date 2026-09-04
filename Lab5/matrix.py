matrix = []

# Input the 3x3 matrix
print("Enter 9 elements of the matrix:")

for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

# 1. Display the matrix
print("\nMatrix:")
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()

# 2. Sum of all elements
total_sum = 0

for i in range(3):
    for j in range(3):
        total_sum += matrix[i][j]

print("\nSum of all elements:", total_sum)

# 3. Sum of main diagonal elements
diagonal_sum = 0

for i in range(3):
    diagonal_sum += matrix[i][i]

print("Sum of main diagonal elements:", diagonal_sum)

# 4. Largest and smallest element
largest = matrix[0][0]
smallest = matrix[0][0]

for i in range(3):
    for j in range(3):
        if matrix[i][j] > largest:
            largest = matrix[i][j]

        if matrix[i][j] < smallest:
            smallest = matrix[i][j]

print("Largest element:", largest)
print("Smallest element:", smallest)

# 5. Transpose of the matrix
print("\nTranspose of the matrix:")

for i in range(3):
    for j in range(3):
        print(matrix[j][i], end=" ")
    print()