from collections import defaultdict
import re

def word_count(filename):
    word_counts = defaultdict(int)
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())  # Extraction des mots en minuscule
            for word in words:
                word_counts[word] += 1
    
    return word_counts

def print_word_counts(word_counts):
    for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")

if __name__ == "__main__":
    filename = "Senegal.txt"  # Remplacez par le nom de votre fichier texte
    counts = word_count(filename)
    print_word_counts(counts)