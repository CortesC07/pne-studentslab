# P01/Seq1.py

class Seq:
    def __init__(self, strbases=None):
        if strbases is None:
            print("NULL sequence created")
            self.strbases = "NULL"
            return

        valid_bases = {'A', 'C', 'T', 'G'}
        if all(base in valid_bases for base in strbases):
            print("New sequence created!")
            self.strbases = strbases
            return

        print("INVALID sequence!")
        self.strbases = "ERROR"

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases in ("NULL", "ERROR"):
            return 0
        return len(self.strbases)

    def count_base(self, base):
        if self.strbases in ("NULL", "ERROR"):
            return 0
        return self.strbases.count(base)

    def count(self):
        if self.strbases in ("NULL", "ERROR"):
            return {'A': 0, 'T': 0, 'C': 0, 'G': 0}

        return {
            'A': self.count_base('A'),
            'T': self.count_base('T'),
            'C': self.count_base('C'),
            'G': self.count_base('G')
        }

    def reverse(self):
        if self.strbases in ("NULL", "ERROR"):
            return self.strbases
        return self.strbases[::-1]

    def complement(self):
        if self.strbases in ("NULL", "ERROR"):
            return self.strbases

        comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return "".join(comp[b] for b in self.strbases)

    def read_fasta(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        seq = ""
        for line in lines:
            if line.startswith(">"):
                continue
            seq += line.strip()

        valid_bases = {'A', 'C', 'T', 'G'}

        if all(base in valid_bases for base in seq):
            self.strbases = seq
        else:
            self.strbases = "ERROR"
