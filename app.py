import numpy as np

words = []
with open('words.txt', "r", encoding='utf8') as fp:
    for index, word in enumerate(fp):
        words.append(word.strip('\n'))

with open('embeddings_matrix.npy', 'rb') as f:
    embeddings_matrix = np.load(f, allow_pickle=True)

seed = 1
import random
random.seed(seed)
target_index = random.randint(0,embeddings_matrix.shape[0])
target_word = words[target_index]
target_embedding = embeddings_matrix[target_index]

from scipy.spatial import distance
distances = [distance.cosine(target_embedding, vec) for vec in embeddings_matrix]
distances = np.array([[int(i),dist] for i,dist in zip(range(len(distances)),distances)])
distances = distances[distances[:, 1].argsort()]
distances =  np.c_[ distances, [words[int(distances[i,0])] for i in range(len(distances))]]

