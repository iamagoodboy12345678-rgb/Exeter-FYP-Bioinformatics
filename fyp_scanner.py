sequence = "ATGCGATACTAAGCTATGC_CRZ1_GCTAGCTAGCTAG_DUN1_ATCGATCG_MID1_CYB1_HAK1_TAG"
targets = ["CRZ1", "DUN1", "MID1", "CYB1", "HAK1"]

print("--scan started--")

for gene in targets:
    if gene in sequence: 
        pos= sequence.find(gene)
        length= len(gene)
        count= sequence.count(gene)
        print(f"Gene: {gene}, Position: {pos}, Length: {length}, Count: {count}")

print ("--scan completed--")
