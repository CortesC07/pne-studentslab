from Seq1 import Seq

print("-----| Practice 1, Exercise 7 |------")

seqs = [
    Seq(),
    Seq("ACTGA"),
    Seq("Invalid sequence")
]

for i, s in enumerate(seqs):
    print(f"Sequence {i}: (Length: {s.len()}) {s}")
    print(f"  Bases: {s.count()}")
    print(f"  Rev:   {s.reverse()}")
