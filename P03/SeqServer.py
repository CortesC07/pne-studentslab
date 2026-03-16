# P03/SeqServer.py
import socket
from P01.Seq1 import Seq



SEQUENCES = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"
]


GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

def load_gene(name):
    """Reads a gene file and returns its sequence."""
    filename = f"../Session-04/{name}.txt"
    try:
        with open(filename) as f:
            seq = ""
            for line in f:
                if not line.startswith(">"):
                    seq += line.strip()
            return seq
    except:
        return None


def process_request(msg):
    """Parses and executes commands."""
    parts = msg.strip().split()

    if len(parts) == 0:
        return "ERROR\n"

    cmd = parts[0]

    # -------------------------
    # EXERCISE 1: PING
    # -------------------------
    if cmd == "PING":
        print("PING command!")
        return "OK!\n"

    # -------------------------
    # EXERCISE 2: GET
    # -------------------------
    if cmd == "GET":
        print("GET command!")
        if len(parts) != 2:
            return "ERROR\n"
        try:
            idx = int(parts[1])
            return SEQUENCES[idx] + "\n"
        except:
            return "ERROR\n"

    # -------------------------
    # EXERCISE 3: INFO
    # -------------------------
    if cmd == "INFO":
        print("INFO command!")
        seq = Seq(parts[1])
        info = seq.info()
        return info + "\n"

    # -------------------------
    # EXERCISE 4: COMP
    # -------------------------
    if cmd == "COMP":
        print("COMP command!")
        seq = Seq(parts[1])
        return seq.complement() + "\n"

    # -------------------------
    # EXERCISE 5: REV
    # -------------------------
    if cmd == "REV":
        print("REV command!")
        seq = Seq(parts[1])
        return seq.reverse() + "\n"

    # -------------------------
    # EXERCISE 6: GENE
    # -------------------------
    if cmd == "GENE":
        print("GENE command!")
        if len(parts) != 2:
            return "ERROR\n"
        name = parts[1]
        if name not in GENES:
            return "ERROR\n"
        gene_seq = load_gene(name)
        if gene_seq is None:
            return "ERROR\n"
        return gene_seq + "\n"

    return "ERROR\n"


# -------------------------
# MAIN SERVER LOOP
# -------------------------
IP = "127.0.0.1"
PORT = 8080

print(f"Server running at {IP}:{PORT}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connection from {addr}")

            msg = conn.recv(2048).decode()
            print("Received:", msg.strip())

            response = process_request(msg)
            print("Response:", response.strip())

            conn.sendall(response.encode())
