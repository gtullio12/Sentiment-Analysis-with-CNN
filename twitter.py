from keras.preprocessing.text import Tokenizer

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

vocab_filename = 'vocab.txt'
doc = load_doc(vocab_filename)
vocab = doc.split()
# Get list of cleaned tweets
data_filename = 'reviews.txt'
doc = load_doc(data_filename)
tweets = doc.split('\n')

# Create tokenizer
tokenizer = create_tokenizer(tweets)
# Encode data
Xtrain = tokenizer.texts_to_matrix(tweets, mode='binary')
