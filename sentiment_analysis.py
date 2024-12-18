from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    - sentiment (str): Positive, Neutral, or Negative.
    """
    if not text.strip():
        return "Neutral"  # Handle empty or whitespace-only text

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    # Classify sentiment based on polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

# Example usage
if __name__ == "__main__":
    sample_texts = [
        "I love this app!",
        "This is okay, nothing special.",
        "I hate how this works!",
        "Just an average experience."
    ]

    for text in sample_texts:
        print(f"Text: {text} => Sentiment: {analyze_sentiment(text)}")