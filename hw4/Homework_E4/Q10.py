dna_fragment_1_file = open("dna_fragments/dna_fragment_1.txt")
dna_fragment_1_content = dna_fragment_1_file.read()
dna_fragment_1_file.close()

dna_fragment_2_file = open("dna_fragments/dna_fragment_2.txt")
dna_fragment_2_content = dna_fragment_2_file.read()
dna_fragment_2_file.close()

dna_fragment_3_file = open("dna_fragments/dna_fragment_3.txt")
dna_fragment_3_content = dna_fragment_3_file.read()
dna_fragment_3_file.close()

dna_fragment_4_file = open("dna_fragments/dna_fragment_4.txt")
dna_fragment_4_content = dna_fragment_4_file.read()
dna_fragment_4_file.close()

dna_fragment_5_file = open("dna_fragments/dna_fragment_5.txt")
dna_fragment_5_content = dna_fragment_5_file.read()
dna_fragment_5_file.close()

dna_fragment_merge_file = open("dna_fragments/dna_fragment_merge_file.txt","w")
dna_fragment_merge_file.write(dna_fragment_1_content)
dna_fragment_merge_file.write(dna_fragment_2_content)
dna_fragment_merge_file.write(dna_fragment_3_content)
dna_fragment_merge_file.write(dna_fragment_4_content)
dna_fragment_merge_file.write(dna_fragment_5_content)
dna_fragment_merge_file.close()
