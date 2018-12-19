# Function that finds and records positions of a motif within a dna string
def motif_finder(dna, motif):
    motifs = []
    initial_length = len(dna)
    find = dna.find(motif)
    dna = dna[(find + 1):]
    motifs.append(find + 1)
    while dna.find(motif) >= 0:
        find = dna.find(motif)
        new_length = len(dna)
        dna = dna[(find + 1):]
        motifs.append(find + 1 + (initial_length - new_length))
    return motifs

print(*motif_finder("GATATATGCATATACTT", "ATAT"), sep = " ")
