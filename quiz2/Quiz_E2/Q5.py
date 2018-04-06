n = 4
string = ""
my_file = open("output/Q5_result.txt", "w")
print("n = " + str(n))
my_file.write("n = " + str(n) + "\n")
for i in range(1, n+1):
	string = ""
	#print(string)
	for j in range(0 , i):
		string = string + "*"
	for j in range(0 , (n-i)):
		string = string + "--"
	for j in range(0 , i):
		string = string + "*"
	print(string)
	my_file.write(string + "\n")
