from Client0 import Client
from P01.Seq1 import Seq

FRAT1 = "../sequences/FRAT1.txt"

s = Seq()
PRACTICE = 2
EXERCISE = 6
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.124.179"

c1 = Client(IP, 8080)
c2 = Client(IP, 8081)

print(c1)
print(c2)

sequence = str(s.read_fasta(FRAT1))
print(f"Gene FRAT1: {sequence[:80]}...")

for i in range(10):
    fragment = sequence[i*10:(i+1)*10]
    print(f"Fragment {i+1}: {fragment}")

    if (i+1) % 2 == 1:
        response = c1.talk(fragment)
    else:
        response = c2.talk(fragment)

    print(f"Response: {response}")