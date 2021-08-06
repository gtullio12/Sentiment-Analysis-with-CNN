import os
import tweepy as tw
import pandas as pd
from collections import Counter
from nltk.corpus.reader.chasen import test
from numpy import array
from keras.preprocessing.text import Tokenizer
import re
import string
from nltk.corpus import stopwords
from os import listdir
import nltk
from numpy.lib.function_base import percentile
nltk.download('stopwords')
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.vis_utils import plot_model
from pandas import DataFrame
from matplotlib import pyplot

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
    # Remove duplicate tweets
    reviews = list(set(reviews))
    save_list(reviews, filename)
    return None

def save_list(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()

# Authenticate with Twitter
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "#moviereview"
date_since = "2018-11-16"
num_of_tweets = 50

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(num_of_tweets)

words = [tweet.text for tweet in tweets]

# Save reviews for later use. 
reviews_filename = 'reviews.txt'
add_tweets_to_file(words, reviews_filename)

# Create a vocabulary
words = ' '.join(words)
tokens = clean_tweets(words)
vocab = Counter()
# Add tokens to vocab with their occurence
vocab.update(tokens)
min_occurence = 2
tokens = [k for k,c in vocab.items() if c >= min_occurence]
vocab_filename = 'vocab.txt'
save_list(tokens, vocab_filename)


