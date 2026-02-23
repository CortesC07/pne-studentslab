from P00.Seq0 import seq_count_base, seq_printer_4, seq_read_fasta

U5 = "../sequences/U5.txt"
ADA = "../sequences/ADA.txt"
FRAT1 = "../sequences/FRAT1.txt"
FXN = "../sequences/FXN.txt"

geneU5 = seq_read_fasta(U5)
geneADA = seq_read_fasta(ADA)
geneFRAT1 = seq_read_fasta(FRAT1)
geneFXN = seq_read_fasta(FXN)

resultsU5 = seq_count_base(geneU5)
resultsADA = seq_count_base(geneADA)
resultsFRAT1 = seq_count_base(geneFRAT1)
resultsFXN = seq_count_base(geneFXN)

print("EX 4:")
gene_names = ["U5", "ADA", "FRAT1", "FXN"]
results = [resultsU5, resultsADA, resultsFRAT1, resultsFXN]

for i in range(len(gene_names)):
    print(f"Gene {gene_names[i]}:")
    seq_printer_4(results[i])
    print()
