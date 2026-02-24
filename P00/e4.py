from pathlib import Path
from P00.Seq0 import seq_count_base, seq_printer_4, seq_read_fasta

U5 = "../S04/sequences/U5.txt"
ADA = "../S04/sequences/ADA.txt"
FRAT1 = "../S04/sequences/FRAT1.txt"
FXN = "../S04/sequences/FXN.txt"


geneU5 = seq_read_fasta(Path(U5).read_text())
geneADA = seq_read_fasta(Path(ADA).read_text())
geneFRAT1 = seq_read_fasta(Path(FRAT1).read_text())
geneFXN = seq_read_fasta(Path(FXN).read_text())


resultsU5 = seq_count_base(geneU5)
resultsADA = seq_count_base(geneADA)
resultsFRAT1 = seq_count_base(geneFRAT1)
resultsFXN = seq_count_base(geneFXN)

print("------| Exercise 4 |------")
gene_names = ["U5", "ADA", "FRAT1", "FXN"]
results = [resultsU5, resultsADA, resultsFRAT1, resultsFXN]

for i in range(len(gene_names)):
    print(f"Gene {gene_names[i]}:")
    seq_printer_4(results[i])
    print()
