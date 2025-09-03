import spacy
from textblob import TextBlob
import re


def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"





text1 = "I'm extremely happy with your service!"
text2 = "The service is okay, nothing special."
text3 = "I am really angry and frustrated."

print("Analysing..")

print(analyze_sentiment(text1))  # Output: Positive
print(analyze_sentiment(text2))  # Output: Neutral
print(analyze_sentiment(text3))  # Output: Negative
