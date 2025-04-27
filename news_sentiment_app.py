import os
import re
import nltk
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from newsapi import NewsApiClient

# Ensure stopwords are downloaded
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

# Streamlit page config
st.set_page_config(page_title="News Sentiment Analyzer", page_icon="📰", layout="centered")

# Sidebar
st.sidebar.title("📰 News Sentiment Analyzer")
st.sidebar.markdown("Select a country and enter a keyword below to fetch recent news and analyze its sentiment!")

# Main title
st.title("📈 News Headlines Sentiment Analysis")

# Country selection
country_options = {
    "United States": "us",
    "India": "in",
    "United Kingdom": "gb",
    "Australia": "au",
    "Canada": "ca",
    "Germany": "de",
    "France": "fr",
    "Japan": "jp",
    "Russia": "ru",
    "China": "cn"
}
country_name = st.selectbox("Select country for news:", list(country_options.keys()), index=1)
country_code = country_options[country_name]

# User input for topic
query = st.text_input("Enter a topic to search for news:", "stockmarket")

# Initialize NewsAPI client
API_KEY = os.getenv('NEWSAPI_KEY', '87648bcbb57c41ccbdc3e069ddef3cda')
newsapi = NewsApiClient(api_key=API_KEY)

# Cache fetching headlines for performance
@st.cache_data
def load_headlines(country_code, query):
    response = newsapi.get_top_headlines(country=country_code, q=query, page_size=100)
    return response.get('articles', [])

if st.button("Fetch and Analyze"):
    with st.spinner("Fetching news and analyzing sentiment..."):
        # Fetch articles
        articles = load_headlines(country_code, query)
        if not articles:
            st.warning("No articles found for this topic in the selected country.")
            st.stop()

        # Extract headlines
        headlines = [a['title'] for a in articles if a.get('title')]

        # Display fetched headlines for verification
        st.subheader(f"Fetched Headlines (Total: {len(headlines)})")
        for headline in headlines[:10]:  # Show first 10 articles
            st.write(headline)

        # Clean text
        def clean_text(text):
            text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
            text = re.sub(r'\d+', '', text)  # Remove numbers
            words = text.lower().split()  # Split text into words and convert to lowercase
            return ' '.join([w for w in words if w not in stop_words])  # Remove stopwords

        # Sentiment analysis
        analyzer = SentimentIntensityAnalyzer()
        cleaned = [clean_text(headline) for headline in headlines]  # Clean headlines
        scores = [analyzer.polarity_scores(text)['compound'] for text in cleaned]

        def label(score):
            return 'Positive' if score >= 0.05 else 'Negative' if score <= -0.05 else 'Neutral'
        labels = [label(s) for s in scores]

        # Create DataFrame
        df = pd.DataFrame({'Headline': headlines, 'Sentiment': labels, 'Score': scores})

        # Display results
        st.subheader(f"🗞️ {len(df)} Headlines & Their Sentiments")
        st.dataframe(df, use_container_width=True)

        # Download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download as CSV", csv, "headline_sentiments.csv", "text/csv")

        # Bar chart
        st.subheader("📊 Sentiment Distribution (Bar Chart)")
        counts = df['Sentiment'].value_counts()
        fig, ax = plt.subplots()
        colors = ['green' if s=='Positive' else 'red' if s=='Negative' else 'gray' for s in counts.index]
        counts.plot(kind='bar', color=colors, ax=ax)
        ax.set_xlabel('Sentiment')
        ax.set_ylabel('Count')
        for i, v in enumerate(counts):
            ax.text(i, v, f"{v} ({v/len(df)*100:.1f}%)", ha='center', va='bottom')
        st.pyplot(fig)

        # Pie chart
        st.subheader("📈 Sentiment Distribution (Pie Chart)")
        fig2, ax2 = plt.subplots()
        counts.plot(kind='pie', autopct='%1.1f%%', labels=counts.index, colors=colors, startangle=140, ax=ax2)
        ax2.set_ylabel('')
        st.pyplot(fig2)

        # Histogram of compound scores
        st.subheader("📈 Compound Score Distribution")
        fig3, ax3 = plt.subplots()
        ax3.hist(df['Score'], bins=20)
        ax3.set_xlabel('Compound Score')
        ax3.set_ylabel('Frequency')
        st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by **Manas Prabhu**")