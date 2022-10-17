def FrequencyTable(text, k):
    """Returns dictionary with the frequency counts of each overlapping k-mer."""
    freqMap = {}
    n = len(text)
    for i in range(0, n-k):
        pattern = text[i:i+k]
        if pattern not in freqMap:
            freqMap[pattern] = 1
        else:
            freqMap[pattern] = freqMap[pattern] + 1
    return freqMap


def MaxMap(freqMap):
    """Returns max frequency from dictionary of k-mer frequencies."""
    max_value = max(freqMap.values())  # should work even if values negative, in current state probably doesn't
    return max_value


def BetterFrequentWords(text, k):
    """Returns the most frequent patterns of length k-mer."""
    frequentPatterns = []
    freqMap = FrequencyTable(text, k)
    max_value = MaxMap(freqMap)
    for pattern in freqMap:
        if freqMap[pattern] == max_value:
            frequentPatterns.append(pattern)
    return frequentPatterns
