def my_fibonacci(n):
    i = 1
    new_term = 0
    fibonacci = [0 , 1]

    #while fibonacci[-1] < 4000000:
    while i < (n +1) :
        print(fibonacci[-1])
        new_term = 0
        i += 1
        new_term = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(new_term)
    return fibonacci[n]



#print(fibonacci[-1])
assert my_fibonacci(5) == 5
assert my_fibonacci(10) == 55