from seq import Seq

def generate_seqs(pattern, number):
    seq_list = []
    for i in range(1, number + 1):
        new_seq = Seq(pattern * i)
        seq_list.append(new_seq)
    return seq_list


def print_seqs(seq_list):
    for i, seq in enumerate(seq_list):
        print(f"Sequence {i}: (Length: {len(seq)}) {seq}")


# Programa principal
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
