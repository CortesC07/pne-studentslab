from pathlib import Path
from P00.Seq0 import seq_complement, seq_read_fasta

U5 = "../S04/sequences/U5.txt"
ADA = "../S04/sequences/ADA.txt"
FRAT1 = "../S04/sequences/FRAT1.txt"
FXN = "../S04/sequences/FXN.txt"

# Leer y limpiar FASTA
cleanU5 = seq_read_fasta(Path(U5).read_text())
cleanADA = seq_read_fasta(Path(ADA).read_text())
cleanFRAT1 = seq_read_fasta(Path(FRAT1).read_text())
cleanFXN = seq_read_fasta(Path(FXN).read_text())

gene_names = ["U5", "ADA", "FRAT1", "FXN"]
gene_sequences = [cleanU5, cleanADA, cleanFRAT1, cleanFXN]

print("------| Exercise 7 |------")
for i in range(len(gene_names)):
    comp = seq_complement(gene_sequences[i], 20)
    print(f"Gene {gene_names[i]}:")
    print(f"Frag: {gene_sequences[i][0:20]}")
    print(f"Comp: {comp}")
    print()
