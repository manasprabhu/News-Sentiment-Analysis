import requests

API_KEY = '87648bcbb57c41ccbdc3e069ddef3cda'
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'

print("▶ Starting NewsAPI test")
print("Request URL:", url)

response = requests.get(url)
print("→ Status code:", response.status_code)

try:
    data = response.json()
except Exception as e:
    print("‼ JSON decode error:", e)
    raise

# Show top-level keys so we know what came back
print("Keys in response JSON:", list(data.keys()))

total = data.get('totalResults', None)
print("TotalResults field:", total)

articles = data.get('articles', [])
print("Number of articles in 'articles' list:", len(articles))

# If there are any, print the first few titles
for i, art in enumerate(articles[:5], start=1):
    print(f"{i}. {art.get('title')}")