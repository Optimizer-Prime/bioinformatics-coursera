def ReverseComplement(strand):
    """Returns the reverse complement of any DNA strand (ACTG)."""
    # dict of complementary letters
    nucleotides = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # convert input strand to uppercase
    strand = strand.upper()

    # add each nucleotide to list
    reverse_comp = []

    # compare input letters to dict, add complementary pair to list
    for letter in strand:
        for key, val in nucleotides.items():
            if letter == key:
                reverse_comp.append(val)


    # reverse the sequence so it will actually be reverse complement
    reverse_comp.reverse()

    # combine all nucleotides into one string
    final_reverse_comp = "".join(reverse_comp)

    return final_reverse_comp
