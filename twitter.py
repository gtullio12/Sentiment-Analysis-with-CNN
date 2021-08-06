def load_doc(filename):
    doc = open(filename, 'r')
    text = doc.read()
    doc.close()
    return text

vocab_filename = 'vocab.txt'
doc = load_doc(vocab_filename)
vocab = doc.split()
print(vocab)
