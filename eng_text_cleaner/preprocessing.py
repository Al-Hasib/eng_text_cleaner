import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
 

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')


class TextCleaner:
    '''Class for cleaning Text'''
    def __init__(self, currency_symbols = r'[\$\£\€\¥\₹\¢\₽\₩\₪]', stop_words=None, lemmatizer=None):
        self.currency_symbols = currency_symbols
        
        if stop_words is None:
            self.stop_words = set(stopwords.words('english'))
        else:
            self.stop_words = stop_words
        
        if lemmatizer is None:
            self.lemmatizer = WordNetLemmatizer()
        else:
            self.lemmatizer = lemmatizer


    
    def remove_emoji(self, text):
        '''remove any kind of emojis in the text'''
        emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)
    

    def remove_punctuation(self,text):

        return text.translate(str.maketrans('', '', string.punctuation))
    

    def remove_html_tags(self, text):
        '''
        args:
            text: text with html tags
        returns:
            text: text without html tags
        '''
        return re.compile('<.*?>').sub('', text)
    
    def remove_url(self, text):
        '''remove the url link from text'''
        url_pattern = re.compile(r'http[s]?://\S+')
        
        return url_pattern.sub('', text)
    

    def remove_not_word_digit_underscore(self, text):
        '''Remove all the characters that is not word, digits, underscore and whitespace'''
        return re.sub(r'[^\w\s]', '', text)


    def remove_digits(self, text):
        '''removing numbers from text'''
        return re.sub(r'\d', ' ', text)
    
    def spell_correction(self, text):
        '''Correction the spelling if needed'''
        from textblob import TextBlob
        blob = TextBlob(text)
        return blob.correct()


    def removing_stopwords(self, text):
        '''remove stopwords if not needed in the further works'''
        return ' '.join(word for word in text.split() if word not in self.stop_words)
    

    def stemmer(self,text):
        '''perform porter stemmer on text'''
        from nltk.stem import PorterStemmer
        nltk.download('punkt')
        stemmer = PorterStemmer()
        return ' '.join(stemmer.stem(word) for word in text.split())

    
    
    def lemmatize_text(self, text):
        '''lemmatize the word into root format'''
        return ' '.join(self.lemmatizer.lemmatize(word) for word in text.split())


    # Functions for cleaning text
    def clean_text(self, text):
        '''
        Clean the text by removing punctuations, html tag, underscore, 
        whitespaces, numbers, stopwords.
        Lemmatize the words in root format.
        '''
        text = text.lower()
        text = re.sub(self.currency_symbols, 'currency', text)
        text = self.remove_punctuation(text)
        text = re.compile('<.*?>').sub('', text)
        text = text.replace('_', '')
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\d', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        text = ' '.join(word for word in text.split() if word not in self.stop_words)
        text = ' '.join(self.lemmatizer.lemmatize(word) for word in text.split())
        
        return text