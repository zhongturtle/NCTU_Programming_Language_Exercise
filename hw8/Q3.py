seq = "Hello world!"

print("UPPER CASE: ", sum(1 for word in seq if word.isupper()))

print("LOWER CASE: ", sum(1 for word in seq if word.islower()))