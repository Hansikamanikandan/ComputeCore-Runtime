def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number: "))

found = False
for i in range(2, n):
    if isprime(i) and isprime(n - i):
        print(n, "=", i, "+", n - i)
        found = True
        break

if not found:
    print("The number cannot be expressed as sum of two prime numbers")
