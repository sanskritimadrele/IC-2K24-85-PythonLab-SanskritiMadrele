num = int(input("Enter a number: "))

original = num
digits = len(str(num))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if sum == original:
    print(original, "is an Armstrong number")

else:
    print(original, "is not an Armstrong number")

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
print("Armstrong numbers are:")

for num in range(start, end + 1):
    original = num
    digits = len(str(num))
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit ** digits
        num = num // 10

    if sum == original:
        print(original)