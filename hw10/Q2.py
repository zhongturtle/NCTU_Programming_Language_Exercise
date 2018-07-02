import os
pdb_dict = "Homework_E10/PDB/"

for i in os.listdir(pdb_dict):
    file = open(pdb_dict + i)
    file_content = file.read()
    file.close()
	
    #print(int(file_content[23:27]))
    #print(int(file_content[-58:-53]))
    print(i, ":\t", int(file_content[-58 : -53]) - int(file_content[23 : 27]) + 1, "residues")
	

#file = open(pdb_dict + "1mp1A.pdb")
#file_content = file.read()
#file.close()

#print(file_content)
#print(file_content.count("\n"))
#print(file_content.find("\n"))