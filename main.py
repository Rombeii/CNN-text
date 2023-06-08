import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from RegexUtil import RegexUtil
from SVMUtil import SVMUtil
from SentimentUtil import SentimentUtil

if __name__ == '__main__':
    dataset = pd.read_csv('Resources/cnn_dailymail/train.csv')
    article_texts = dataset['article']
    article_summaries = dataset['highlights']

    extended_data = []

    # Load the dataset
    bbc_dataset = pd.read_csv('Resources/bbc.csv')

    # Separate features (news) and labels (type)
    X = bbc_dataset['news']
    y = bbc_dataset['type']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    svm_util = SVMUtil()
    svm_util.initialize(X_train, y_train)
    # svm_util.initialize_with_grid_search(X_train, y_train)

    # Printing out classification_report
    predictions = [svm_util.predict(text) for text in X_test]
    report = classification_report(y_test, predictions)
    print(report)

    sentimentUtil = SentimentUtil()

    for article_text in article_texts:
        city, state, country = RegexUtil.get_location_from_text(article_text)
        publisher = RegexUtil.get_publisher_from_text(article_text)
        publication_date = RegexUtil.get_date_from_text_with_regex(article_text, r"PUBLISHED:\s*\.\s*(.*?)\s*\.\s*\|")
        date_updated = RegexUtil.get_date_from_text_with_regex(article_text, r"UPDATED:\s*\.\s*(.*?)\s*\.")
        topic_prediction = svm_util.predict(article_text)
        sentiment_score, sentiment_label = sentimentUtil.analyze_sentiments(article_text)

        print("Article text:", article_text)
        print("City:", city)
        print("State:", state)
        print("Country:", country)
        print("Publisher:", publisher)
        print("Publish date:", publication_date)
        print("Update date:", date_updated)
        print("Predicted topic:", topic_prediction)
        print("Sentiment score:", sentiment_score)
        print("Sentiment label:", sentiment_label)
        print()

        extended_data.append({'city': city,
                              'state': state,
                              'country': country,
                              'publisher': publisher,
                              'publication_date': publication_date,
                              'date_updated': date_updated,
                              'topic': topic_prediction,
                              'sentiment_score': sentiment_score,
                              'sentiment_label': sentiment_label})

    extended_dataset = pd.DataFrame(extended_data)
    extended_dataset.to_csv('extended_dataset.csv', index=False)