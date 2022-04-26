import numpy as np
import pandas as pd
from scipy.spatial import distance
import streamlit as st

words = []
with open('words.txt', "r", encoding='utf8') as fp:
    for index, word in enumerate(fp):
        words.append(word.strip('\n'))

with open('embeddings_matrix.npy', 'rb') as f:
    embeddings_matrix = np.load(f, allow_pickle=True)

st.title('Guess the secret word !')
st.write('Play the game . The goal of the game is to guess a secret word. To do so, '
         'propose any word and see how close you are from the secret word. The lower the score you get, the closer '
         'you are to the secret word. When you score low, it means your proposed word is either easily '
         'interchangeable with the secret word, or that it is often associated with the secret word.')


seed = 1
import random

random.seed(seed)
target_index = random.randint(0, embeddings_matrix.shape[0])
target_word = words[target_index]
target_embedding = embeddings_matrix[target_index]

distances = [distance.cosine(target_embedding, vec) for vec in embeddings_matrix]
distances = np.array([[int(i), dist] for i, dist in zip(range(len(distances)), distances)])
distances = distances[distances[:, 1].argsort()]
distances = np.c_[distances, [words[int(distances[i, 0])] for i in range(len(distances))]]


@st.cache(allow_output_mutation=True)
def store_inputs():
    return []


proposed_word = st.text_input('Enter your proposed word')

if proposed_word:
    if proposed_word in words:
        rank = np.where(distances[:,2]==proposed_word)[0][0]
        distance = distances[rank,1][0]
        st.write(proposed_word ,'is', distance,'unit away from the target word ! It is the',rank ,'closest word !')
        store_inputs().append({'Proposed Word': proposed_word,'Score': distance,'Rank' : rank})

        if rank == 0:
            st.write('**Congratulations !! You found the secret word !**')
            st.write('It is', target_word)
    else:
        st.write('I dont know this word :( Please select another one')


st.table(pd.DataFrame(store_inputs()).sort_values(by='Rank'))

