from pathlib import Path
from P00.Seq0 import seq_len, seq_read_fasta

U5 = "../S04/sequences/U5.txt"
ADA = "../S04/sequences/ADA.txt"
FRAT1 = "../S04/sequences/FRAT1.txt"
FXN = "../S04/sequences/FXN.txt"


geneU5 = seq_read_fasta(Path(U5).read_text())
geneADA = seq_read_fasta(Path(ADA).read_text())
geneFRAT1 = seq_read_fasta(Path(FRAT1).read_text())
geneFXN = seq_read_fasta(Path(FXN).read_text())

print("-----| Exercise 3 |------")
print("Gene U5 -> Length:", seq_len(geneU5))
print("Gene ADA -> Length:", seq_len(geneADA))
print("Gene FRAT1 -> Length:", seq_len(geneFRAT1))
print("Gene FXN -> Length:", seq_len(geneFXN))
