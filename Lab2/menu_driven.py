while True:

    print("\n========== MENU ==========")
    print("1. Armstrong Number")
    print("2. Prime Number")
    print("3. Perfect Number")
    print("4. Palindrome")
    print("5. Fibonacci Series")
    print("6. Pattern Printing")
    print("7. Exit")
    print("====================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        original = num
        digits = len(str(num))
        total = 0

        while num > 0:
            digit = num % 10
            total = total + digit ** digits
            num = num // 10

        if total == original:
            print(original, "is an Armstrong number")
        else:
            print(original, "is not an Armstrong number")

    elif choice == 2:
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

    elif choice == 3:
        num = int(input("Enter a number: "))
        total = 0

        for i in range(1, num):
            if num % i == 0:
                total = total + i

        if total == num:
            print(num, "is a perfect number")
        else:
            print(num, "is not a perfect number")

    elif choice == 4:
        num = int(input("Enter a number: "))
        original = num
        reverse = 0

        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10

        if original == reverse:
            print(original, "is a palindrome")
        else:
            print(original, "is not a palindrome")

    elif choice == 5:
        n = int(input("Enter number of terms: "))
        a = 0
        b = 1
        print("Fibonacci Series:")

        for i in range(n):
            print(a, end=" ")

            c = a + b
            a = b
            b = c
        print()

    elif choice == 6:
        n = int(input("Enter number of rows: "))
        print("\nStar Pattern:")
        for i in range(1, n + 1):
            for j in range(i):
                print("*", end=" ")
            print()

        print("\nNumber Pattern:")
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

        print("\nPyramid Pattern:")
        for i in range(1, n + 1):
            for j in range(n - i):
                print(" ", end=" ")
            for j in range(2 * i - 1):
                print("*", end=" ")
            print()
    elif choice == 7:
        print("Program exited successfully.")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 7.")