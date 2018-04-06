#AGCNAGQLTVCTGAIAGGARPTAACCSSLRAQQGCFCQFAKDPRYGRYVNSPNARKAVSSCGIALPTCH
protein_file = open("protein.txt")
protein_content = protein_file.read()
protein_file.close()

#print(protein_content)
#protein_content = protein_content.split("")
#print(protein_content)
protein_list = ""
for i in protein_content:
    protein_list = protein_list + i + " "
#print(protein_list)
protein_list = protein_list.split(" ")
#print(protein_list)

odd_list = ""
even_list = ""
for i in range(0,len(protein_content),2):
    odd_list = odd_list + protein_list[i]
print("Odd  residues: " + odd_list)

for i in range(1,len(protein_content),2):
    even_list = even_list + protein_list[i]
print("Even residues: " + even_list)
