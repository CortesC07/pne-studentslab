from pathlib import Path
from P00.Seq0 import seq_read_fasta

FILENAME = "../S04/sequences/U5.txt"

raw = Path(FILENAME).read_text()
clean = seq_read_fasta(raw)
first20 = clean[:20]

print("DNA File: U5.txt")
print("first 20 bases:")
print(first20)
