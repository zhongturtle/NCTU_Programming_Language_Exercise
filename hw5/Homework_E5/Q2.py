dna_file = open("genomic_dna.txt")
dna_content = dna_file.read()
dna_file.close()

#Exon1
stop_num = dna_content.find("GTA")
Exon_1 = dna_content[0 : stop_num + 3]

print("Exon 1 : " + Exon_1)

#Exon2
start_num = 90 - 1
stop_num = len(dna_content)
Exon_2 = dna_content[start_num : stop_num]

print("Exon 2 : " + Exon_2)