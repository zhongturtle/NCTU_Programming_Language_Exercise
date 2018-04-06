dna = "ATGCTGGTACCTAGTTGATCGTTACCCAGATTTAGTCAAGCTCAC"

rna = dna.replace("A", "u")
#print(rna)
rna = rna.replace("T", "a")
#print(rna)
rna = rna.replace("G", "c")
#print(rna)
rna = rna.replace("C", "g")

#print(rna)
print("messenger RNA = " + rna.upper())