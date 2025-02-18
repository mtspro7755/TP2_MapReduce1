#!/usr/bin/env python3
import sys
from collections import defaultdict

word_counts = defaultdict(int)

# Lecture de l'entrée standard
for line in sys.stdin:
    word, count = line.strip().split("\t")
    word_counts[word] += int(count)

# Affichage des résultats triés par fréquence
for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}\t{count}")
