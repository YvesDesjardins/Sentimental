import nltk
import os, sys
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from utils.BFL import has_symbol

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()
min_confidence = 0.7
min_data_points = 15
result = {'pos': 0, 'neg': 0, 'neu': 0}
symbols = {}
regex_filter = r'([$()])+'

# todo: this file really needs a refactor/rewrite
def analyze_post(post):
    # Initializing a dictionary to keep tally of results
    score = analyzer.polarity_scores(post.selftext)
    if score['compound'] > min_confidence:
        print("long", score['compound'], post.title)
        result['pos'] += 1
        __parse_symbols(post.selftext, 'pos')
    elif score['compound'] < -min_confidence:
        print("short", score['compound'], post.title)
        result['neg'] += 1
        __parse_symbols(post.selftext, 'neg')
    else:
        print("neutral", score['compound'], post.title)
        result['neu'] += 1
        __parse_symbols(post.selftext, 'neu')

    post.comments.replace_more(limit=10)

    for comment in post.comments.list():
        score = analyzer.polarity_scores(comment.body)
        if score['compound'] > min_confidence:
            result['pos'] += 1
            __parse_symbols(comment.body, 'pos')
        elif score['compound'] < -min_confidence:
            result['neg'] += 1
            __parse_symbols(comment.body, 'neg')
        else:
            result['neu'] += 1
            __parse_symbols(comment.body, 'neu')

def get_sentiment():
    print("\n%s" % result)
    pos_confidence = result['pos']/result['pos']+result['neg']
    return("Overall sentiment is %s" % "long" if pos_confidence > min_confidence else "short" if pos_confidence < (1-min_confidence) else "neutral")

def get_sentiment_symbols():
    parsed_results = []
    for symb, stats in symbols.items():
        pos = stats['pos']
        neg = stats['neg']
        neu = stats['neu']
        sum_data_points = pos + neg + neu
        pos_confidence = (pos if pos > 0 else 1)/((pos if pos > 0 else 1)+(neg if neg > 0 else 1))

        if sum_data_points > min_data_points:
          parsed_results.append('%(symbol)s: %(sentiment)s from %(total)s datapoints (%(pos)s positive/ %(neg)s negative)' % {
            'symbol': symb,
            'sentiment': "long" if pos_confidence > min_confidence else "short" if pos_confidence < (1-min_confidence) else "neutral",
            'total': sum_data_points,
            'pos': pos,
            'neg': neg
            })
    return '\n'.join(parsed_results)

def __parse_symbols(string, change):
    words = string.split(' ')
    for word in words:
        filtered_word = re.sub(regex_filter, '', word)
        if has_symbol(filtered_word):
            if not filtered_word in symbols:
                symbols[filtered_word] = {'pos': 0, 'neg': 0, 'neu': 0}
            if change == 'pos':
              symbols[filtered_word]['pos'] += 1
            elif change == 'neg':
              symbols[filtered_word]['neg'] += 1
            else:
              symbols[filtered_word]['neu'] += 1
