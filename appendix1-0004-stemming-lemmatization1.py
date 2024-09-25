from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
nltk.download('stopwords')

eng_stop_words = set(stopwords.words("english"))

print(eng_stop_words)

"""
{'they', 'between', 'that', 'wasn', 's', 'shouldn', 'below', 'too', 'm', 'ain', 'themselves', 'such', 'did', 'same', 'doesn',
'o', 'are', 'weren', 'some', 'whom', 'above', 'am', 'any', 'most', 'hadn', 'being', 'my', 'have', 'into', 'after', 'over', 'further', 
'your', 'there', 'yourselves', 'he', 'down', 'and', 'on', 'yourself', "that'll", "needn't", 'off', 'was', "wasn't", 'not', 'will', 'y', 
'at', 'be', "don't", "didn't", "doesn't", 'nor', 'its', 'himself', 'their', 'should', "weren't", 'where', 'no', 'been', 'me', "hasn't", 
'them', 'these', 'those', 'haven', 'yours', 'mightn', 'couldn', "you're", 'own', 'each', 'before', 'which', 'only', 'how', 'few', 'this', 
'ours', 'is', 'a', 'both', "hadn't", "isn't", 'what', "mustn't", 'our', 'for', "you've", 'than', 'didn', 'to', 'has', 'when', 'won', 'herself', 
"wouldn't", 'she', 'shan', 't', 'now', 'having', 'if', 'as', 'ma', 'his', 'isn', 'just', 'who', 'why', 'but', 'until', 'needn', 'hasn', 'other', 
'can', 'up', 'then', "aren't", 'hers', 'had', 'i', 'more', "she's", 'out', "couldn't", 'itself', 'while', 'very', 'aren', 'it', "shouldn't", 'so', 
'under', 'about', 'myself', 'in', "mightn't", "it's", 'him', 'you', 'against', 'during', 'don', "you'll", 'an', 'were', 'or', "shan't", 'here', 
'does', 're', 'll', 'mustn', 'theirs', 'ourselves', "you'd", 'because', 'her', 'from', 'again', "haven't", 'the', "should've", 've', 'we', 'doing', 
'do', 'by', 'once', 'wouldn', 'all', 'with', "won't", 'of', 'through', 'd'}

"""
