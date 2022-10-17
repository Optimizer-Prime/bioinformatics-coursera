def PatternCount(text, pattern):
    """Counts all overlapping instances of the given pattern in the given text."""
    text_len = len(text)
    patt_len = len(pattern)
    count = 0
    for i in range(0, text_len-patt_len+1):
        if text[i:i+patt_len] == pattern:
            count = count + 1
    return count
