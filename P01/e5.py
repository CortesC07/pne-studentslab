from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

seqs = [
    Seq(),
    Seq("ACTGA"),
    Seq("Invalid sequence")
]

for i, s in enumerate(seqs):
    print(f"Sequence {i}: (Length: {s.len()}) {s}")
    print(f"  A: {s.count_base('A')},   C: {s.count_base('C')},   T: {s.count_base('T')},   G: {s.count_base('G')}")
