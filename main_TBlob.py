from textblob import TextBlob

# Example text
text = "I love programming. It's so much fun and rewarding!"
blob = TextBlob(text)
sentiment = blob.sentiment
print(f"Sentiment: {sentiment}")
print(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")