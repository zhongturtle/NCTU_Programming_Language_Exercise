import os


##### Functions
### 函式：擷取 PDB 檔中所有 residues，回傳格式 Residues[residue id] = residue type
def Pdb_Obtain_Residues(pdb_file):
    Residues = {}

    file = open(pdb_file)
    for line in file:
        if line[0:4] != "ATOM": continue
        residue_id   = line[22:27]
        residue_type = line[17:20]
        Residues[residue_id] = residue_type

    file.close()

    return Residues


### 函式：將 PDB 檔翻譯成氨基酸序列
### 1. 由前自訂函式擷取所有 residues
### 2. 根據全域變數中的 code map 翻譯各 residues
### 3. 注意不同 python 版本對 dic 的 item 排序問題
def Pdb_Obtain_Sequence(pdb_file):
    ThreeLetterCodes = Pdb_Obtain_Residues(pdb_file)
    #print(ThreeLetterCodes)

    sequence = ""
    for res_id in sorted(ThreeLetterCodes.keys()):
        #print(res_id + "\t" + ThreeLetterCodes[res_id])
        sequence += OneLetterCodes[ ThreeLetterCodes[res_id] ]

    return sequence



##### Main Programs
### Make the 3-to-1 letter code map
code_file = open("amino_acid_codes.txt")

OneLetterCodes = {}
for line in code_file:
    if line[0] == "#": continue
    line = line.strip("\n").split("\t")
    OneLetterCodes[ line[0] ] = line[1]

code_file.close()


### 列出目錄中的檔案清單
dir_pdb = "PDB"
Pdb_Files = os.listdir(dir_pdb)


### 解析清單中各檔案
### 1. 以自訂函式將 PDB 檔翻譯成氨基酸序列
### 2. 依題目要求輸出為 fasta 格式
for pdb_file in Pdb_Files:
    pdb_id = pdb_file[0:5]
    sequence = Pdb_Obtain_Sequence(dir_pdb + "\\" + pdb_file)
    print(">" + pdb_id + "\n" + sequence)

