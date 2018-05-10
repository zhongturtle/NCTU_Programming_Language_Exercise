dna_1 = "ACGTATTATGTTGCTATCAGATCGATTATGCGTTATCATCATATATACGT"
dna_2 = "TATTAGTGTCGGCCGCACATACTAT"
dna_3 = "CCGGGGTAGGATGATTGGACCCATCGGGTATGCCATACGT"
dna_list = [dna_1 , dna_2 , dna_3]

def my_cg_content(dna):
    
    length = len(dna)
    c_count = dna.upper().count('C')
    g_count = dna.upper().count('G')
    cg_content = (c_count + g_count) / length
    
    return cg_content


assert my_cg_content(dna_1) == 0.32
assert my_cg_content(dna_2) == 0.44
assert my_cg_content(dna_3) == 0.575

count = 1
for i in dna_list:
    print("dna" + str(count) + " : " + i)
    print("my_cg_content" + "(" + "dna" + str(count) + ")"  + " = " + str(my_cg_content(i)))
    print()
    count = count + 1

