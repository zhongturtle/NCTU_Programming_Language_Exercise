atom_file = open("atomic_weight.txt")
atom_data = atom_file.read()
atom_file.close
#print(atom_data)

atom_data = atom_data.split("\n")
#atom_data = atom_data.split("\t")
#for i in atom_data:
#    i = i.split("\t")
#print(atom_data)
dict = {}
#print(atom_data[2].split("\t"))
for i in atom_data:
    atom = i.split("\t")
    dict[atom[0]] = atom[1]
#atom_table = 
keys = dict.keys()
keys.sort()
print(dict)

