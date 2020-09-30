import nltk
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.BFL import has_symbol

nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
min_confidence = 0.7
result = {'pos': 0, 'neg': 0, 'neu': 0}


def analyze_post(post):
    # Initializing a dictionary to keep tally of results
    score = analyzer.polarity_scores(post.selftext)
    if score['compound'] > min_confidence:
        print("long", score['compound'], post.title)
        result['pos'] += 1
    elif score['compound'] < -min_confidence:
        print("short", score['compound'], post.title)
        result['neg'] += 1
    else:
        print("neutral", score['compound'], post.title)
        result['neu'] += 1

    post.comments.replace_more(limit=10)
    for comment in post.comments.list():
        score = analyzer.polarity_scores(comment.body)
        if score['compound'] > min_confidence:
            result['pos'] += 1
        elif score['compound'] < -min_confidence:
            result['neg'] += 1
        else:
            result['neu'] += 1


def get_sentiment():
    print("\n%s" % result)
    pos_confidence = result['pos']/result['neg']
    return("Overall sentiment is %s" % "long" if pos_confidence > min_confidence else "short" if pos_confidence < (1-min_confidence) else "neutral")
