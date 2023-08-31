def reverse_complement(sequence_input: str):
    COMPLEMENT_TABLE = {
        "A": "T",
        "G": "C",
        "C": "G",
        "T": "A",
    }
    dna_seq = sequence_input.strip()
    complement_seq: list = []
    for nucleotide in dna_seq:
        if nucleotide in COMPLEMENT_TABLE.keys():
            complement_seq.append(COMPLEMENT_TABLE[nucleotide])
    reverse_complement = "".join(complement_seq)[::-1]
    return reverse_complement


def sequence_manipulation(sequence_input: str, seq_orientation: str):
    if seq_orientation == "forward":
        first_forward_motif = "aaac"
        second_forward_motif = "a"
        modified_sequence = first_forward_motif + sequence_input + second_forward_motif
        return modified_sequence
    elif seq_orientation == "reverse":
        first_reverse_motif = "agcatt"
        reverse_complement_sequence = reverse_complement(sequence_input)
        modified_sequence = first_reverse_motif + reverse_complement_sequence
        return modified_sequence
