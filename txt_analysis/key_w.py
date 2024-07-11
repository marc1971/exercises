import re
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
import numpy as np

# Markdown-Datei einlesen
# laguage is either 'english' or 'german'

def key_words(doc, language, N):

    list_kw = []
    # Laden der deutschen Stoppwörter
    if language == 'german':
        nltk.download('stopwords')
        sw = stopwords.words('german')
    else:
        sw = 'english'

    # Markdown-Datei einlesen
    with open(doc, 'r', encoding='utf-8') as file:
        content = file.read()

    # Markdown in reinen Text konvertieren
    new_content = re.sub(r'[#*`]', '', content)  # Entfernt Markdown-Symbole
    text = re.sub(r'\d+', '', new_content)  # Entfernt der Zahlen

    # TF-IDF Vektorizer initialisieren
    vectorizer = TfidfVectorizer(stop_words=sw)

    # TF-IDF Matrix erstellen
    tfidf_matrix = vectorizer.fit_transform([text])

    # Wörter und deren TF-IDF-Werte extrahieren
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray()[0]

    # Wörter und ihre TF-IDF-Werte sortieren
    sorted_items = sorted(zip(tfidf_scores, feature_names), reverse=True)

    # Die wichtigsten Keywords auswählen (z.B. Top 10)
    top_n = N
    top_keywords = sorted_items[:top_n]

    # Ergebnisse anzeigen
    print('Die wichtigsten ' +str(N)+ ' Keywords sind:')
    for score, word in top_keywords:
        print(f'{word}: {score:.4f}')
        rounded_score = round(score, 3)
        list_kw.append((word, f'{rounded_score:.4f}'))

    return list_kw

if __name__ == "__main__":
# Paths to the input PDF and output Markdown file
    doc = r'C:\Users\COPE_Eyer_Marc\Documents\Projects\git_tasks\txt_analysis\docs\doc1.md'
    N = 10
    language = 'german'
    
    # Convert PDF to Markdown
    print(key_words(doc, language, N))
    