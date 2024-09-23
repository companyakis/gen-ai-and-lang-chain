import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')

info_file = "info.txt"

with open(
    info_file,
    "r",
    encoding = "utf-8"
) as file:
    w_text = file.read()
    
splitted = w_text.split(".")

print(splitted[0])
print(splitted[1])

tokens = [word_tokenize(s) for s in splitted]

print(tokens)

# Any understanding of what is ahead must start with an acknowledgment of the extraordinary resilience of Trump as a political figure
#  He’s transformed the Republican Party in his image and built an unassailable grip on the GOP’s base as the nominee in a third straight election

# [['Any', 'understanding', 'of', 'what', 'is', 'ahead', 'must', 'start', 'with', 'an', 'acknowledgment', 'of', 'the', 'extraordinary', 'resilience', 'of', 'Trump', 'as', 'a', 'political', 'figure'], 
#  ['He', '’', 's', 'transformed', 'the', 'Republican', 'Party', 'in', 'his', 'image', 'and', 'built', 'an', 'unassailable', 'grip', 'on', 'the', 'GOP', '’', 's', 'base', 'as', 'the', 'nominee', 'in', 'a', 'third', 'straight', 'election'], []]
