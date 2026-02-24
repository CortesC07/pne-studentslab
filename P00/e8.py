from pathlib import Path
from P00.Seq0 import base_count, frequency, seq_read_fasta

U5 = "../S04/sequences/U5.txt"
ADA = "../S04/sequences/ADA.txt"
FRAT1 = "../S04/sequences/FRAT1.txt"
FXN = "../S04/sequences/FXN.txt"


cleanU5 = seq_read_fasta(Path(U5).read_text())
cleanADA = seq_read_fasta(Path(ADA).read_text())
cleanFRAT1 = seq_read_fasta(Path(FRAT1).read_text())
cleanFXN = seq_read_fasta(Path(FXN).read_text())

gene_names = ["U5", "ADA", "FRAT1", "FXN"]
gene_sequences = [cleanU5, cleanADA, cleanFRAT1, cleanFXN]

print("------| Exercise 8 |------")
for i in range(len(gene_names)):
    most_repeated = frequency(base_count(gene_sequences[i]))
    print(f"Gene {gene_names[i]}: Most frequent Base: {most_repeated}")
