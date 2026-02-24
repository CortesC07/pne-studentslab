class Seq:
    def __init__(self, strbases):
        valid_bases = {"A", "C", "G", "T"}
        upper = strbases.upper()

        # Comprobación de validez
        if all(base in valid_bases for base in upper):
            print("New sequence created!")
            self.strbases = upper
        else:
            print("ERROR!!")
            self.strbases = "ERROR"

    def __str__(self):
        return self.strbases


# Programa principal de prueba
if __name__ == "__main__":
    s1 = Seq("ACCTGC")
    s2 = Seq("Hello? Am I a valid sequence?")

    print(f"Sequence 1: {s1}")
    print(f"Sequence 2: {s2}")
