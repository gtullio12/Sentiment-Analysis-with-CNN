import tweepy as tw
from nltk.corpus import stopwords
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
import re
import string
nltk.download('stopwords')
nltk.download('vader_lexicon')

consumer_key = 'KnUlN9kEQ7gJdDiVp8oNE1Wg2'
consumer_secret = 'mRtOVvdiZIzqwdxebqo47WmOBGBvWjIwtZvufDU2E84vlm5QV4'
access_token = '1027293645676769280-2heVzKV4eDN7LDv0Udtk8VkE8Ubj9m'
access_token_secret = '6RdwPKQbgIX75EcsI3eovdsqhtomqUgsHWo4Lwa1lOwnM'
auth = tw.OAuthHandler(consumer_key, consumer_secret) # Pass in Consumer key and secret for authentication by API
auth.set_access_token(access_token, access_token_secret) # Pass in Access key and secret for authentication by API
api = tw.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True) # Sleeps when API limit is reached
sid = SentimentIntensityAnalyzer()

def clean_tweets(tweets):
    tokens = tweets.split()
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    # remove punctuation from each word
    tokens = [re_punc.sub('', w) for w in tokens]
    # remove remaining tokens that are not alphabetic
    tokens = [word for word in tokens if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    # filter out short tokens
    tokens = [word for word in tokens if len(word) > 1]
    # Make lower case
    tokens = [word.lower() for word in tokens]
    # Remove RT and URL links from tokens
    tokens = [word for word in tokens if word != 'rt' and 'http' not in word]
    return tokens

# -1 = Negative tweet. 1 = Positive tweet. 0 = Neutral tweet
def classify_tweet(tweet):
    ss = sid.polarity_scores(tweet)
    neg_score = ss['neg']
    pos_score = ss['pos']
    neu_score = ss['neu']
    if neg_score > pos_score and neg_score > neu_score:
        return -1
    elif pos_score > neg_score and pos_score > neu_score:
        return 1
    else:
        return 0

# Create a file with one cleaned tweet on each line.
def add_tweets_to_file(tweets, filename):
    # Remove newlines in each tweet
    tweets = [tweet.replace('\n','') for tweet in tweets]
    # Clean each tweet
    cleaned_tweets = [clean_tweets(tweet) for tweet in tweets]
    # Combine all tweets to a document, where each tweet is seperated by newline
    tokens = [' '.join(tweet) for tweet in cleaned_tweets]
    # Classify tweet as positive or negative 
    classifications = [classify_tweet(token) for token in tokens]
    classifications = [str(classify) for classify in classifications] 
    save_list(classifications, 'classify.txt')
    save_list(tokens, filename)
    return None

def save_list(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()

def add_tweets_to_vocab(tweets, vocab):
    words = ' '.join(tweets)
    tokens = clean_tweets(words)
    vocab.update(tokens)

# Define the search term and the date_since date as variables
search_words = '#crypto OR \" crypto will \" OR \" crypto wont \" OR \" crypto won\'t \" OR \" crypto can \" OR \" crypto is \" OR \" crypto isnt \" -filter:links AND -filter:retweets'

num_of_tweets = 20000

words = []

# Collect tweets
for i in tw.Cursor(api.search,
              q=search_words,
              since = '2021-01-01', 
              until = '2021-08-08', 
              since_id = None,
              lang="en",
              tweet_mode = "extended").items(num_of_tweets):
              words.append(i.full_text)

#print('\n\n\n',words)
print('Amount of tweets: %d ' % len(words))
#[print('\n\n\n', tweet.text) for tweet in tweets]
#words = [tweet.text for tweet in tweets]

# Save reviews for later use. 
reviews_filename = 'reviews.txt'
add_tweets_to_file(words, reviews_filename)

# Create a vocabulary
vocab = Counter()
# Add tokens to vocab with their occurence
add_tweets_to_vocab(words,vocab)
# Filter out unique words.
min_occurence = 2
tokens = [k for k,c in vocab.items() if c >= min_occurence]
# Save vocab to file.
vocab_filename = 'vocab.txt'
save_list(tokens, vocab_filename)

print('Size of vocab: %d ' % len(vocab.items()))


