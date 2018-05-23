import sys



##### Functions
def is_prime(n):
    if n == 2: return True

    x = 2
    end = pow(n, 0.5)

    while x <= end:
        if n%x == 0: return False

        x += 1

    return True




##### Main Program
num = int(sys.argv[1])

print("Primes smaller than " + str(num))

num_primes = 0
output = ""
for n in range(2, num+1):
    if not is_prime(n): continue

    output += str(n) + "\t"
    num_primes += 1

print(output)

print("\nTotal number of primes = " + str(num_primes))
