from Client0 import Client
from P01.Seq1 import Seq

FRAT1 = "../sequences/FRAT1.txt"

s = Seq()
PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.124.179"
PORT = 8080

c = Client(IP, PORT)

sequence = str(s.read_fasta(FRAT1))
print(f"Gene FRAT1: {sequence[:60]}...")

for i in range(5):
    fragment = sequence[i*10:(i+1)*10]
    print(f"Fragment {i+1}: {fragment}")
    response = c.talk(fragment)
    print(f"Response: {response}")