from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

text = "The man is here. He is a teacher. He is thoughtful. Do you know him?"

sentences = sent_tokenize(text)

print(sentences)

words = [word_tokenize(sentence) for sentence in sentences]

print(words)

# ['The man is here.', 'He is a teacher.', 'He is thoughtful.', 'Do you know him?']
# [['The', 'man', 'is', 'here', '.'], ['He', 'is', 'a', 'teacher', '.'], ['He', 'is', 'thoughtful', '.'], ['Do', 'you', 'know', 'him', '?']]


