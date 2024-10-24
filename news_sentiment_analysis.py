import os
import requests
import re
import nltk
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

# Download NLTK stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Fetching news headlines from NewsAPI
API_KEY = os.getenv('87648bcbb57c41ccbdc3e069ddef3cda')  # Ensure to set this environment variable
URL = f'https://newsapi.org/v2/everything?q=stockmarket&apiKey=87648bcbb57c41ccbdc3e069ddef3cda'

# Fetch news data with error handling
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to fetch data from NewsAPI") 
    exit()

news_data = response.json()
articles = news_data['articles']
headlines = [article['title'] for article in articles]

# Function to clean text
def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)      # Remove numbers
    words = text.lower().split()
    return ' '.join([word for word in words if word not in stop_words])

cleaned_headlines = [clean_text(headline) for headline in headlines]

# Sentiment Analysis using VADER
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment = analyzer.polarity_scores(text)
    return sentiment['compound']  # Compound score as overall sentiment

headline_sentiments = [analyze_sentiment(headline) for headline in cleaned_headlines]

# Classify sentiment based on compound score
def sentiment_label(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

headline_labels = [sentiment_label(score) for score in headline_sentiments]

# Display the results in a DataFrame
df = pd.DataFrame({
    'Headline': headlines,
    'Sentiment': headline_labels
})

print(df)

# Save the DataFrame to a CSV file
df.to_csv('headline_sentiments.csv', index=False)

# Visualize the sentiment distribution
sentiment_counts = df['Sentiment'].value_counts()
ax = sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
plt.title('News Headlines Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Count')

# Add percentage labels on top of the bars
for index, value in enumerate(sentiment_counts):
    plt.text(index, value, f"{value} ({(value/len(df)*100):.1f}%)", ha='center')

plt.show()