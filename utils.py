import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_input(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    
    tokens = nltk.word_tokenize(text)
    
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    return ' '.join(filtered_tokens)
