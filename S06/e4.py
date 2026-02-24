from seq import Seq
import termcolor

def generate_seqs(pattern, number):
    seq_list = []
    for i in range(1, number + 1):
        new_seq = Seq(pattern * i)
        seq_list.append(new_seq)
    return seq_list


def print_seqs(seq_list, color):
    for i, seq in enumerate(seq_list):
        text = f"Sequence {i}: (Length: {len(seq)}) {seq}"
        print(colored(text, color))


# Programa principal
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print(colored("List 1:", "blue"))
print_seqs(seq_list1, "blue")

print()
print(colored("List 2:", "green"))
print_seqs(seq_list2, "green")
