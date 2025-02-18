#!/usr/bin/env python3
import sys
import re

# Lecture ligne par ligne depuis l'entrée standard
for line in sys.stdin:
    line = line.strip().lower()  # Mise en minuscule
    words = re.findall(r'\b\w+\b', line)  # Extraction des mots
    for word in words:
        print(f"{word}\t1")  # Format "mot \t 1"
