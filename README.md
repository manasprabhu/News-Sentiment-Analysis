# NewsSentimentAnalyzer

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-latest-orange)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A **Streamlit** web application that performs real-time sentiment analysis on news headlines. It classifies headlines into **Positive**, **Neutral**, and **Negative**, giving insights into public opinion and media trends.

---

## 🧭 Table of Contents

- [✨ Features](#-features)
- [🛠 Tech Stack](#-tech-stack)
- [🎯 Installation](#-installation)
- [🚀 Usage](#-usage)
- [📈 Screenshots](#-screenshots)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [❤️ Acknowledgments](#-acknowledgments)

---

## ✨ Features

- **Country & Topic Selection**: Fetch top headlines by country and keyword via NewsAPI
- **Text Preprocessing**: Punctuation & number stripping, stopword removal using NLTK
- **Sentiment Analysis**: VADER-based scoring and classification
- **Interactive Visualizations**: Bar chart, pie chart, and histogram of sentiment distribution
- **Export Results**: Download analysis as a CSV for offline use
- **Cached Requests**: Faster repeat queries with Streamlit caching

---

## 🛠 Tech Stack

- **Python 3.8+**
- **Streamlit** – for building the interactive web UI
- **NLTK** & **VADER** – for NLP preprocessing and sentiment scoring
- **Pandas** – data manipulation
- **Matplotlib** – visualization
- **newsapi-python** – fetching news from NewsAPI

---

## 🎯 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/manasprabhu/HeadlineSentimentAnalysis.git
   cd HeadlineSentimentAnalysis
   ```
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set your NewsAPI key**
   - Create a file named `.env` in the project root
   - Add the following line:
     ```text
     NEWSAPI_KEY=YOUR_API_KEY_HERE
     ```

---

## 🚀 Usage

1. **Run the Streamlit app**
   ```bash
   streamlit run news_sentiment_app.py
   ```
2. **Open your browser** at `http://localhost:8501`
3. **Select a country** and **enter a topic**, then click **Fetch and Analyze**
4. **View** the headlines, sentiment results, and interactive charts

---

## 📈 Screenshots

![Screenshot 1](assets/Screenshot%202025-04-27%20204724.png)
![Screenshot 2](assets/Screenshot%202025-04-27%20205122.png)
![Screenshot 3](assets/Screenshot%202025-04-27%20205150.png)
![Screenshot 4](assets/Screenshot%202025-04-27%20205220.png)
![Screenshot 5](assets/Screenshot%202025-04-27%20205235.png)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## ❤️ Acknowledgments

- [NewsAPI](https://newsapi.org/) for the headlines API
- [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment) library
- [Streamlit](https://streamlit.io/) for the UI framework
