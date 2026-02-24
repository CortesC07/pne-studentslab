class Seq:
    def __init__(self, bases):
        print("New sequence created!")
        self.bases = bases

    def __len__(self):
        return len(self.bases)

    def __str__(self):
        return self.bases
