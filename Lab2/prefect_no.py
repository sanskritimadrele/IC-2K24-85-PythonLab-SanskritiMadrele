num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")

limit = int(input("Enter the limit: "))

print("Perfect numbers up to", limit, "are:")

for num in range(1, limit + 1):

    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum = sum + i

    if sum == num:
        print(num, end=" ")