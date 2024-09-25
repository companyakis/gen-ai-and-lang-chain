nltk.download('punkt')

sample_sentence = "A rolling stone gathers no moss. When I last saw her, he was only 13."

words = word_tokenize(sample_sentence)

print(words)

print("****************************************************************")

words = [w.lower() for w in words if w.isalnum()]

print(words)

print("****************************************************************")

words = [w for w in words if w not in eng_stop_words]

print(words)

"""
['A', 'rolling', 'stone', 'gathers', 'no', 'moss', '.', 'When', 'I', 'last', 'saw', 'her', ',', 'he', 'was', 'only', '13', '.']
****************************************************************
['a', 'rolling', 'stone', 'gathers', 'no', 'moss', 'when', 'i', 'last', 'saw', 'her', 'he', 'was', 'only', '13']
****************************************************************
['rolling', 'stone', 'gathers', 'moss', 'last', 'saw', '13']

"""
