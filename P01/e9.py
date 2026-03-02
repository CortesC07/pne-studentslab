from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")

s = Seq()  # Null sequence
s.read_fasta("../S04/sequences/U5.txt")   # <- OJO: dos puntos y barra

print(f"Sequence : (Length: {s.len()}) {s.strbases[:60]}...")
print(f"  Bases: {s.count()}")
print(f"  Rev:   {s.reverse()[:60]}...")
print(f"  Comp:  {s.complement()[:60]}...")
