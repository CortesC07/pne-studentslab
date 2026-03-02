from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")

genes = {
    "U5": "../S04/sequences/U5.txt",
    "ADA": "../S04/sequences/ADA.txt",
    "FRAT1": "../S04/sequences/FRAT1.txt",
    "FXN": "../S04/sequences/FXN.txt",
    "RNU6_269P": "../S04/sequences/RNU6_269P.txt"
}

for gene, filepath in genes.items():
    s = Seq()                     # Null sequence
    s.read_fasta(filepath)        # Load FASTA file

    counts = s.count()            # Dictionary of bases
    most_frequent = max(counts, key=counts.get)

    print(f"Gene {gene}: Most frequent Base: {most_frequent}")
