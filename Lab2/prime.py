num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

limit = int(input("Enter the limit: "))

print("Prime numbers up to", limit, "are:")

for num in range(2, limit + 1):

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")