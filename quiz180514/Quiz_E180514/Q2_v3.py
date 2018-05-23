import os


##### Functions
### 擷取 PDB 檔中所有 residues，回傳格式 Residues[residue id] = residue type
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



##### Main Program
### 列出目錄中的檔案清單
dir_pdb = "PDB"
Pdb_Files = os.listdir(dir_pdb)


### 解析清單中各檔案
### 1. 以自訂函式擷取 PDB 檔中所有 residues，回傳格式 Residues[residue id] = residue type
### 2. 計算有幾個 residues
for pdb_file in Pdb_Files:
    Residues = Pdb_Obtain_Residues(dir_pdb + "\\" + pdb_file)
    num_residues = str( len(Residues) )
    print(pdb_file + ":\t" + num_residues + " residues")

