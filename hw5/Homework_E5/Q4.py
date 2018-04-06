protein_file = open("protein.txt")
protein_content = protein_file.read()
protein_file.close()

odd_residules = ""
for i in range(0 , len(protein_content) , 2):
    odd_residules = odd_residules + protein_content[i]

print("Odd residues  : " + odd_residules)

even_residules = ""
for i in range(1 , len(protein_content) , 2):
    even_residules = even_residules + protein_content[i]

print("Even residues : " + even_residules)
