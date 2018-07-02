import sys
import subprocess


n = int(sys.argv[1])

results = subprocess.check_output("python primes.py " + str(n))
results = str(results)

num_primes = results

print("There are " + num_primes + " primes smaller than " + str(n) + ".")