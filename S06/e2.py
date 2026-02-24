class Seq:
    def __init__(self, strbases):
        valid_bases = {"A", "C", "G", "T"}
        upper = strbases.upper()

        if all(base in valid_bases for base in upper):
            print("New sequence created!")
            self.strbases = upper
        else:
            print("ERROR!!")
            self.strbases = "ERROR"

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seq_list):
    for i, seq in enumerate(seq_list):
        print(f"Sequence {i}: (Length: {seq.len()}) {seq}")


# Programa principal de prueba
if __name__ == "__main__":
    seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
    print_seqs(seq_list)
