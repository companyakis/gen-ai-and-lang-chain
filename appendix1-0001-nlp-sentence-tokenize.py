from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')

sentences = [
    "Out of sight, out of mind...",
    "A barking dog never bites!",
    "A rolling stone gathers no moss!.."
]


tokens = [sent_tokenize(i) for i in sentences]

print(tokens[0])
print(tokens[1])
print(tokens[2])

# ['Out of sight, out of mind...']
# ['A barking dog never bites!']
# ['A rolling stone gathers no moss!..']
