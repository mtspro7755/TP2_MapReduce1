# TP2 - MapReduce 

Ce projet implémente un programme MapReduce pour compter les mots dans un texte.

📂 Structure du projet
- `wordcount.py` : Script principal pour exécuter MapReduce
- `mapper.py` : Fonction de mappage (extrait et émet les mots)
- `reducer.py` : Fonction de réduction (compte les occurrences)

 Exécution
**1. Exécution locale avec Python**
```bash
cat senegal.txt | python3 mapper.py | sort | python3 reducer.py



