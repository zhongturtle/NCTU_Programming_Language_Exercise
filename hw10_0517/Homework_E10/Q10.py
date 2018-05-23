import sys
import subprocess


n = int(sys.argv[1])

results = subprocess.check_output("py primes.py " + str(n))
results = str(results)

results = results.split(" = ")
num_primes = results[1].replace(r"\r\n'", "")

print("There are " + num_primes + " primes smaller than " + str(n) + ".")