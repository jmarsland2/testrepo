from collections import defaultdict

def better_frequent_words(text, k):
    freqmap = defaultdict(int)
    n = len(text)
    
    # Create frequency map for initial window
    for i in range (n - k + 1):
        pattern = text[i:i+k]
        freqmap[pattern] += 1
    
    # Find Max frequency
    max_value = max(freqmap.values(), default=0)
    
    # Return patterns with max frequency
    return [pattern for pattern, count in freqmap.items() if count == max_value]

def clump_finder(text, k, L, t):
    clump = set()
    n = len(text)
    
    # iterate over all windows of Length L
    for i in range(n - L + 1):
        window = text[i:i + L]
        # frequent kmers
        frequent_patterns = better_frequent_words(window,k)
        
        # check if kmer appears t times
        for pattern in frequent_patterns:
            count = window.count(pattern)
            if count >= t:
                clump.add(pattern)
    return list(clump)

file = open("data.1.txt", "r") 
text = str(file.read())
file.close()

print(*clump_finder(text, 10, 100, 4), sep=' ')
        