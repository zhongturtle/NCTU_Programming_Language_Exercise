def my_fibonacci(n):
    if (n == 0):
        fibonacci_ans = 0
    elif (n == 1):
        fibonacci_ans = 1
    else:
        fibonacci_ans = my_fibonacci(n - 1) + my_fibonacci(n - 2)

    return fibonacci_ans


assert my_fibonacci(5) == 5
assert my_fibonacci(10) == 55

print("n = 5 " + " : " + "my_fibonacci(5) == " + str(my_fibonacci(5)))
print("n = 10" + " : " + "my_fibonacci(10) == " + str(my_fibonacci(10)))
