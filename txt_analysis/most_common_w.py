import re
from collections import Counter
import matplotlib.pyplot as plt

def mc_words(doc, N):


# Markdown-Datei einlesen
    with open(doc, 'r', encoding='utf-8') as file:
        content = file.read()

    # Markdown in reinen Text konvertieren
    # Hier könnte eine erweiterte Verarbeitung erfolgen, um Markdown-spezifische Syntax zu entfernen
    text = re.sub(r'[#*`]', '', content)  # Entfernt Markdown-Symbole

    # Text in Wörter aufteilen
    words = re.findall(r'\b\w+\b', text.lower())  # Findet alle Wörter und konvertiert sie in Kleinbuchstaben

    # Grundlegende Textanalyse
    word_count = len(words)
    unique_word_count = len(set(words))
    word_frequencies = Counter(words)

    print(f'Gesamtanzahl der Wörter: {word_count}')
    print(f'Anzahl eindeutiger Wörter: {unique_word_count}')

    # Die 10 häufigsten Wörter
    common_words = word_frequencies.most_common(N)
    print('Die 10 häufigsten Wörter:')
    for word, freq in common_words:
        print(f'{word}: {freq}')

    # Ergebnisse visualisieren
    words, frequencies = zip(*common_words)
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies)
    plt.xlabel('Wörter')
    plt.ylabel('Häufigkeit')
    plt.title('Die ' + str(N) + ' häufigsten Wörter in doc1.md')
    plt.show()

