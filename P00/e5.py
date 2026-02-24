from pathlib import Path
from P00.Seq0 import seq_count, seq_read_fasta

U5 = "../S04/sequences/U5.txt"
ADA = "../S04/sequences/ADA.txt"
FRAT1 = "../S04/sequences/FRAT1.txt"
FXN = "../S04/sequences/FXN.txt"

# Leer y limpiar FASTA
geneU5 = seq_read_fasta(Path(U5).read_text())
geneADA = seq_read_fasta(Path(ADA).read_text())
geneFRAT1 = seq_read_fasta(Path(FRAT1).read_text())
geneFXN = seq_read_fasta(Path(FXN).read_text())

gene_names = ["U5", "ADA", "FRAT1", "FXN"]
gene_sequences = [geneU5, geneADA, geneFRAT1, geneFXN]

print("------| Exercise 5 |------")
for i in range(len(gene_names)):
    counts = seq_count(gene_sequences[i])
    print(f"Gene {gene_names[i]}: {counts}")
