import sys

def is_prime(n):
    if n == 2: 
        return 1
    for i in range(2 , pow(n, 0.5)):
        if n % i == 0 :
            return 0
    return 1

number = int(sys.argv[1])

num_primes = 0
for n in range(2, number+1):
    if is_prime(n) == 0: 
        continue

    num_primes += 1

print(str(num_primes))
