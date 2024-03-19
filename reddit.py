import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize Reddit instance
reddit = praw.Reddit(client_id='5EF2hKP57If-VyElfHs6EA',
                     client_secret='PTwRADax545OhEuPJeGl5EWcoXEUbA',
                     user_agent='MyRedditApp/1.0 by Jayasurya')


# Function to analyze sentiment of a comment
def analyze_sentiment(comment):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(comment)
    # Classify sentiment based on compound score
    if sentiment_score['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'


# Function to fetch comments from a Reddit post and categorize them
def reddit_post_analyzer():
    post_url = input("Enter the URL of the Reddit post: ")
    submission = reddit.submission(url=post_url)
    submission.comments.replace_more(limit=None)
    positive_comments = []
    negative_comments = []
    neutral_comments = []

    for comment in submission.comments.list():
        sentiment = analyze_sentiment(comment.body)
        if sentiment == 'Positive':
            positive_comments.append(comment.body)
        elif sentiment == 'Negative':
            negative_comments.append(comment.body)
        else:
            neutral_comments.append(comment.body)

    # Print results
    print("Positive Comments:")
    print('\n'.join(positive_comments))
    print("\nNegative Comments:")
    print('\n'.join(negative_comments))
    print("\nNeutral Comments:")
    print('\n'.join(neutral_comments))


# Example usage
if __name__ == "__main__":
    reddit_post_analyzer()
