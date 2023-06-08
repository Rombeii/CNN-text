import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import string


class SentimentUtil:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        nltk.download('vader_lexicon')  # Download the lexicon for sentiment analysis
        nltk.download('stopwords')  # Download the stopwords

        self.stopwords = set(stopwords.words('english'))
        self.punctuation = set(string.punctuation)

    def analyze_sentiments(self, text):
        sentiment_scores, sentiment_label = self._get_sentiment(text)
        return sentiment_scores, sentiment_label

    def _get_sentiment(self, text):
        text = self._clean_text(text)
        sentiment_scores = self.sia.polarity_scores(text)
        score = sentiment_scores['compound']
        if score >= 0.05:
            label = 'positive'
        elif score <= -0.05:
            label = 'negative'
        else:
            label = 'neutral'
        return score, label

    def _clean_text(self, text):
        text = ''.join([c for c in text if c not in self.punctuation])
        text = text.lower()
        text = ' '.join([word for word in text.split() if word not in self.stopwords])
        return text
