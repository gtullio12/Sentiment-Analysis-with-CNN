import tweepy as tw
from collections import Counter
import re
import string
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

consumer_key = 'KnUlN9kEQ7gJdDiVp8oNE1Wg2'
consumer_secret = 'mRtOVvdiZIzqwdxebqo47WmOBGBvWjIwtZvufDU2E84vlm5QV4'
access_token = '1027293645676769280-2heVzKV4eDN7LDv0Udtk8VkE8Ubj9m'
access_token_secret = '6RdwPKQbgIX75EcsI3eovdsqhtomqUgsHWo4Lwa1lOwnM'

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

# Create a file with one cleaned tweet on each line.
def add_tweets_to_file(tweets, filename):
    # Remove newlines in each tweet
    tweets = [tweet.replace('\n','') for tweet in tweets]
    # Clean each tweet
    cleaned_tweets = [clean_tweets(tweet) for tweet in tweets]
    # Combine all tweets to a document, where each tweet is seperated by newline
    reviews = [' '.join(tweet) for tweet in cleaned_tweets]
    print('Number of tweets: %d ' %len(reviews))
    save_list(reviews, filename)
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


# Authenticate with Twitter
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "#crypto -filter:retweets"
date_since = "2018-11-16"
num_of_tweets = 100

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(num_of_tweets)

#[print('\n\n\n', tweet.text) for tweet in tweets]
words = [tweet.text for tweet in tweets]

# Save reviews for later use. 
reviews_filename = 'reviews.txt'
add_tweets_to_file(words, reviews_filename)

# Create a vocabulary
vocab = Counter()
# Add tokens to vocab with their occurence
add_tweets_to_vocab(words,vocab)

min_occurence = 2
tokens = [k for k,c in vocab.items() if c >= min_occurence]
vocab_filename = 'vocab.txt'
save_list(tokens, vocab_filename)

print('Size of vocab: %d ' % len(vocab.items()))


