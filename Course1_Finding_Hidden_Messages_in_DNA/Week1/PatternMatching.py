def PatternMatching(genome, pattern):
    """Returns all zero-based indicies for matching overlapping pattern in genome."""
    # determine length of input genome and pattern
    genome_len = len(genome)
    patt_len = len(pattern)

    # create empty list to store zero-based indexes of matching patterns in genome
    genome_idx = []

    # find all overlapping matches and add index to list
    for idx in range(0, genome_len-patt_len+1):
        if genome[idx:idx+patt_len] == pattern:
            genome_idx.append(idx)

    # use * to unpack list into individual values
    unpacked = print(*genome_idx)

    return unpacked
