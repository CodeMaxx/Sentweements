import nltk


class Analyzer:
    """Implements sentiment analysis."""

    positive_words = []  # Stores positive words
    negative_words = []  # Store negative words

    def __init__(self, positives="positive-words.txt", negatives="negative-words.txt"):
        """Initialize Analyzer."""
        # Initialises class variables
        for line in open(positives):
            li = line.strip()
            if not li.startswith(";"):
                Analyzer.positive_words.append(li)

        for line in open(negatives):
            li = line.strip()
            if not li.startswith(";"):
                Analyzer.negative_words.append(li)

    # noinspection PyMethodMayBeStatic
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # Positive score if text is positive, negative if negative else zero

        words = text.split(" ")
        score = 0

        for word in words:
            if word.lower() in Analyzer.positive_words:
                score += 1
            elif word.lower() in Analyzer.negative_words:
                score -= 1

        return score
