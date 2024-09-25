porter_stemmer = PorterStemmer()

words_stemmed = [porter_stemmer.stem(w) for w in words]

print(words)

print("****************************************************************")

print(words_stemmed)

"""
['rolling', 'stone', 'gathers', 'moss', 'last', 'saw', '13']
****************************************************************
['roll', 'stone', 'gather', 'moss', 'last', 'saw', '13']
"""
