nltk.download('wordnet')

wordnet_lemmatizer = WordNetLemmatizer()

words_lemmatized = [wordnet_lemmatizer.lemmatize(w) for w in words]

print(words)

print("****************************************************************")

print(words_lemmatized)

"""

['rolling', 'stone', 'gathers', 'moss', 'last', 'saw', '13']
****************************************************************
['rolling', 'stone', 'gather', 'moss', 'last', 'saw', '13']

"""
