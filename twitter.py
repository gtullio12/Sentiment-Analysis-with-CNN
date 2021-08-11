from keras.preprocessing.text import Tokenizer
from nltk.corpus import stopwords
import nltk
import string
import re
nltk.download('stopwords')
from keras.preprocessing.text import Tokenizer
from keras.utils.vis_utils import plot_model
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from nltk.corpus.reader.knbc import test
from nltk.util import pad_sequence
from numpy import array
from keras.models import load_model

# Fit a tokenizer
def create_tokenizer(lines):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)
    return tokenizer

def load_doc(filename):
    doc = open(filename, 'r')
    text = doc.read()
    doc.close()
    return text

def clean_tweets(tweets, vocab):
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
    # Filter out non vocab words
    tokens = [word for word in tokens if word in vocab]
    return tokens

# Define CNN
def define_model(vocab_size, max_length):
    model = Sequential()
    model.add(Embedding(vocab_size, 100, input_length=max_length))
    model.add(Conv1D(filters=32, kernel_size=8, activation= 'relu' ))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # compile network
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # summarize defined model
    model.summary()
    plot_model(model, to_file='model.png', show_shapes=True)
    return model

# classify a review as negative or positive
def predict_sentiment(tweet, vocab, tokenizer, max_length, model):
    # clean review
    line = clean_tweets(tweet, vocab)
    # encode and pad review
    padded = encode_tweets(tokenizer, max_length, [line])
    # predict sentiment
    yhat = model.predict(padded, verbose=0)
    print('yhat: ', yhat)
    # retrieve predicted percentage and label
    percent_pos = yhat[0,0]
    if round(percent_pos) == 0:
        return (1-percent_pos), 'NEGATIVE'
    return percent_pos, 'POSITIVE'

# Integer encode and pad each tweet
def encode_tweets(tokenizer, max_length, tweets):
    # Integer encode each tweet
    encoded = tokenizer.texts_to_sequences(tweets)
    # Pad sequences
    padded = pad_sequences(encoded,maxlen=max_length,padding='post')
    return padded

vocab_filename = 'vocab.txt'
doc = load_doc(vocab_filename)
vocab = doc.split()
# Get list of cleaned tweets
data_filename = 'reviews.txt'
doc = load_doc(data_filename)
tweets = doc.split('\n')
train_tweets, test_tweets = tweets[:-100], tweets[-100:]
print('Amount of test tweets: %d' % len(test_tweets))
print('Amount of train tweets: %d' % len(train_tweets))

# Grab the classification for each tweet saved in classify.txt
classify_doc = load_doc('classify.txt')
classifications = classify_doc.split()
# Turn strings into integers
classifications = array([int(c) for c in classifications])
train_classifications, test_classifications = classifications[:-100], classifications[-100:]
print('train classification size: %d' % len(train_classifications))
print('test classification size: %d' % len(test_classifications))

# Create tokenizer
tokenizer = create_tokenizer(tweets)
# Get size of vocab for CNN
vocab_size = len(tokenizer.word_index) + 1
# Get max tweet size
max_tweet_length = max([len(tweet.split()) for tweet in tweets])
print('Max tweet size(by words): %d' % max_tweet_length)

# Encode data
Xtrain = encode_tweets(tokenizer, max_tweet_length, train_tweets)
Xtest = encode_tweets(tokenizer, max_tweet_length, test_tweets)
print('Xtrain: ', Xtrain)
print('Xtest: ', Xtest)

# Define the model
#model = define_model(vocab_size, max_tweet_length)
# Fit the model
#model.fit(Xtrain, train_classifications, epochs=10, verbose=2)
# Save the model
#model.save('model.h5')

# evaluate model on training dataset
model = load_model('model.h5')
_, acc = model.evaluate(Xtrain, train_classifications, verbose=0)
print('Train Accuracy: %.2f '% (acc*100))
# evaluate model on test dataset
_, acc = model.evaluate(Xtest, test_classifications, verbose = 0)
print('Test Accuracy: %.2f ' % (acc*100))

# Manual testing
text = 'I think Gamestop will definitley go up!! #Gamestop'
percent, sentiment = predict_sentiment(text, vocab, tokenizer, max_tweet_length, model)
print('Review: [%s]\nSentiment: %s (%.3f%%) ' % (text, sentiment, percent*100))

text = 'I think Gamestop will definitley go down!! #gme #fail'
percent, sentiment = predict_sentiment(text, vocab, tokenizer, max_tweet_length, model)
print('Review: [%s]\nSentiment: %s (%.3f%%) ' % (text, sentiment, percent*100))

text = 'GME has potential. Event y occured so there is a good chance it will go up #gme #success'
percent, sentiment = predict_sentiment(text, vocab, tokenizer, max_tweet_length, model)
print('Review: [%s]\nSentiment: %s (%.3f%%) ' % (text, sentiment, percent*100))