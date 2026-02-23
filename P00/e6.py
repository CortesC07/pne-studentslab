from P00.Seq0 import seq_reverse, seq_read_fasta
from pathlib import Path

U5 = "../sequences/U5.txt"
ADA = "../sequences/ADA.txt"
FRAT1 = "../sequences/FRAT1.txt"
FXN = "../sequences/FXN.txt"

cleanU5 = seq_read_fasta(U5)
cleanADA = seq_read_fasta(ADA)
cleanFRAT1 = seq_read_fasta(FRAT1)
cleanFXN = seq_read_fasta(FXN)

gene_names = ["U5", "ADA", "FRAT1", "FXN"]
gene_sequences = [cleanU5, cleanADA, cleanFRAT1, cleanFXN]

print("EX 6:")
for i in range(len(gene_names)):
    reverse = seq_reverse(gene_sequences[i], 20)
    print(f"Gene {gene_names[i]}:")
    print(f"Fragment: {gene_sequences[i][0:20]}")
    print(f"Reverse: {reverse}")
    print()
