from P00.Seq0 import seq_len, seq_read_fasta

U5 = "../sequences/U5.txt"
ADA = "../sequences/ADA.txt"
FRAT1 = "../sequences/FRAT1.txt"
FXN = "../sequences/FXN.txt"

geneU5 = seq_read_fasta(U5)
geneADA = seq_read_fasta(ADA)
geneFRAT1 = seq_read_fasta(FRAT1)
geneFXN = seq_read_fasta(FXN)

print("EXERCISE 3:")
print("Gene U5 -> Length:", seq_len(geneU5))
print("Gene ADA -> Length:", seq_len(geneADA))
print("Gene FRAT1 -> Length:", seq_len(geneFRAT1))
print("Gene FXN -> Length:", seq_len(geneFXN))
