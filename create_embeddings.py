import numpy as np
import pandas as pd
import requests
import numpy as np

def load_glove_embeddings(embeddings_file, word_index):
    """Load embeddings from a file."""
    embeddings = {}
    with open(embeddings_file, "r", encoding='utf8') as fp:
        for index, line in enumerate(fp):
            values = line.split()
            word = values[0]
            if word in word_index:
                embedding = np.asarray(values[1:], dtype='float32')
                embeddings[word] = embedding
    return embeddings

# Create embeddings (pretrained from GloVe as initialization)
EMBEDDING_DIM = 50
embeddings_file = 'glove.6B.{0}d.txt'.format(EMBEDDING_DIM)

url = 'https://raw.githubusercontent.com/dolph/dictionary/master/popular.txt'
common_words = requests.get(url).content.decode("utf-8").split('\n')

glove_embeddings = load_glove_embeddings(embeddings_file=embeddings_file, word_index=common_words)

from sklearn.manifold import TSNE

keys = ['dog','cat','paprika','job','tweet','phone','adjust','telephone']
X = np.array([glove_embeddings.get(w).tolist() for w in keys])
X_embedded = TSNE(n_components=2, learning_rate='auto', init='random').fit_transform(X)

words = []
embeddings_matrix = []
for k,v in glove_embeddings.items():
    words.append(k)
    embeddings_matrix.append(v)

embeddings_matrix = np.array(embeddings_matrix)

np.savetxt("words.txt", words, delimiter=" ", newline="\n", fmt="%s")
with open('embeddings_matrix.npy', 'wb') as f:
    np.save(f, embeddings_matrix)
