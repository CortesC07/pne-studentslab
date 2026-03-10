from Client0 import Client
from P01.Seq1 import Seq

U5 = "../sequences/U5.txt"
ADA = "../sequences/ADA.txt"
FRAT1 = "../sequences/FRAT1.txt"

s = Seq()

genes = {"U5": U5, "ADA": ADA, "FRAT1": FRAT1}

PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.124.179"
PORT = 8080

c = Client(IP, PORT)

for gene_name, gene_fasta in genes.items():
    print(f"Sending the {gene_name} Gene to the server...")
    sequence = str(s.read_fasta(gene_fasta))
    response = c.talk(sequence)
    print(f"Response: {response}")