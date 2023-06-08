from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import nltk
import re

nltk.download('wordnet')
nltk.download('stopwords')

# Generated the same way as extended_dataset, but with the article_text added
csv_file = "Resources/extended_dataset_full.csv"

data = pd.read_csv(csv_file)

# Preprocess the data
data['article_text'] = data['article_text'].astype(str)  # Convert to string if not already
data['article_text'] = data['article_text'].str.lower()  # Convert to lowercase

# Initialize lemmatizer and stopwords
lemmatizer = nltk.WordNetLemmatizer()
stopwords_set = set(stopwords.words('english'))

# Create a dictionary to store the word frequencies for each topic
topic_data = {}

# Define a pattern to remove unwanted characters and patterns
pattern = r'\b[A-Za-z]+\b'

# Iterate over each topic
topics = data['topic'].unique()
for topic in topics:
    # Filter the data for the current topic
    topic_articles = data[data['topic'] == topic]

    # Concatenate the text from all articles for the current topic
    topic_text = ' '.join(topic_articles['article_text'])

    # Remove unwanted characters and patterns
    cleaned_text = re.findall(pattern, topic_text)

    # Lemmatize the tokens and filter out stopwords
    filtered_words = [lemmatizer.lemmatize(token) for token in cleaned_text if token not in stopwords_set]

    # Generate word frequencies for the topic
    word_freq = pd.Series(filtered_words).value_counts().to_dict()

    # Store the word frequencies in the dictionary
    topic_data[topic] = word_freq


# Create word clouds and save as images
for topic, words in topic_data.items():
    # Create a WordCloud object
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(words)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.set_title(f'Most Used Words - {topic}')
    ax.axis('off')

    # Save the WordCloud as an image
    image_path = f'wordcloud_{topic}.png'  # Change the filename as desired
    plt.savefig(image_path, bbox_inches='tight', dpi=300)
    plt.close()