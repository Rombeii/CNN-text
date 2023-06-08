from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class SVMUtil:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        # Best Parameters: {'C': 1, 'class_weight': None, 'gamma': 0.1, 'kernel': 'linear'}
        self.svm = SVC(C=1, class_weight=None, gamma=0.1, kernel='linear')

    def clean_text(self, text):
        # Convert to lowercase
        text = text.lower()

        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)

        # Tokenize the text
        tokens = nltk.word_tokenize(text)

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]

        # Lemmatize the words
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]

        # Join the tokens back into a single string
        cleaned_text = ' '.join(tokens)

        return cleaned_text

    def initialize(self, X, y):
        # Clean the text data
        X = X.apply(self.clean_text)

        # Convert text data into numerical features
        X_train = self.vectorizer.fit_transform(X)

        # Train the SVM classifier
        self.svm.fit(X_train, y)

    def initialize_with_grid_search(self, X, y):
        # Clean the text data
        X = X.apply(self.clean_text)

        # Convert text data into numerical features
        X = self.vectorizer.fit_transform(X)

        # Define the parameter grid for grid search
        param_grid = {
            'C': [0.1, 1, 10],
            'kernel': ['linear', 'rbf'],
            'gamma': [0.1, 0.01, 0.001],
            'class_weight': [None, 'balanced']
        }

        # Perform grid search
        grid_search = GridSearchCV(self.svm, param_grid, cv=5)
        grid_search.fit(X, y)

        # Set the best estimator as the trained SVM model
        self.svm = grid_search.best_estimator_

        # Print the best parameters and best score
        print("Best Parameters: ", grid_search.best_params_)
        print("Best Score: ", grid_search.best_score_)

    def predict(self, text):
        # Clean the text data
        cleaned_text = self.clean_text(text)

        # Convert text data into numerical features
        X = self.vectorizer.transform([cleaned_text])

        # Make predictions using the trained SVM model
        predictions = self.svm.predict(X)

        return predictions[0]
