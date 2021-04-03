import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

sw = set(stopwords.words('english'))
ss = SnowballStemmer('english')

def getCleanReview(review):
    review = review.lower()
    
    tokens = word_tokenize(review)
    useful_words = [w for w in tokens if w not in sw]
    stemmed_words = [ss.stem(w) for w in useful_words]

    return ' '.join(stemmed_words)

