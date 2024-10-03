from sklearn.feature_extraction.text import CountVectorizer

samples = [
    "A rolling stone gathers no moss",
    "Out of sight, out of mind",
    "A barking dog never bites"
]

count_vectorizer = CountVectorizer(binary = True) # 0 or 1

one_hot_matrix = count_vectorizer.fit_transform(samples)

print(one_hot_matrix.toarray())

print(".........................")

print(count_vectorizer.vocabulary_)

"""
[[0 0 0 1 0 1 0 1 0 0 1 0 1]
 [0 0 0 0 1 0 0 0 1 1 0 1 0]
 [1 1 1 0 0 0 1 0 0 0 0 0 0]]
.........................
{'rolling': 10, 'stone': 12, 'gathers': 3, 'no': 7, 'moss': 5, 'out': 9, 'of': 8, 'sight': 11, 'mind': 4, 'barking': 0, 'dog': 2, 'never': 6, 'bites': 1}

"""
