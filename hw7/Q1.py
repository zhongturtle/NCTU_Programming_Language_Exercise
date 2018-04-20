def my_round(number , num_digits):
    round_num  = round(number , num_digits)
    number_string = str(number)
    number_length = len(number_string)
    
    dot_position = number_string.find('.')
    #print(dot_position)
    float_or_not = number_string.count('.')

    if(float_or_not):
        #print("Is float num")
        num_of_digit_after_dot = number_length - dot_position -1
        #print(num_of_digit_after_dot)
        
        if(num_of_digit_after_dot < num_digits):
            #print("Add O's")
            round_num = number_string + "0" * (num_digits - num_of_digit_after_dot)
        else:
            round_num = number_string[0 : dot_position + 1] + number_string[dot_position + 1 : dot_position + 1 + num_digits]

    else:
        round_num = number_string + "." + "0" * (num_digits)
    return round_num 
    #return number_length

#print(my_round(12.14444 , 8))
assert my_round(10, 3) == "10.000"
assert my_round(0.2345, 3) == "0.234"
assert my_round(12.32, 5) == "12.32000"

print("my_round(10, 3) == " + "\"" + my_round(10, 3) + "\"")
print("my_round(0.2345, 3) == " + "\"" + my_round(0.2345, 3) + "\"")
print("my_round(12.32, 5) == " + "\"" + my_round(12.32, 5) + "\"")
