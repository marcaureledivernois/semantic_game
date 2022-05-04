# Guess the secret word !

Play the game [here](https://share.streamlit.io/marcaureledivernois/semantic_game/app.py). The goal of the game is to guess a secret word. To do so,
propose any word and see how close you are from the secret word. 

**The lower the score you get, the closer
you are to the secret word**. When you score low, you did a good job ! It means your proposed word is either easily
interchangeable with the secret word, or that it is often associated with the secret word. Continue in that direction !

## Examples

Let's say the secret word is "raising". Words that will score low are for instance "increasing" (synonym), "money" 
(often associated with "raising") or "reducing" (antonym). Antonyms are
also scoring low because they are close semantically ! However, words such as "magically", "fruitcake" or "cyclop" will score high
because they do not really have a link with "raising".

## Algorithm

For those interested, the game is based on cosine distances between word embeddings. Every word is mapped
on a vector of size (1,*embed_dim*) in such a way that two words that are close should have similar vectors.
Every time a secret word is drawn, the cosine distances between the secret word and all the words in the vocabulary are computed
and sorted. When the player tries to guess a word, the game outputs the cosine distance (which I call score) between the proposed word and the secret word, 
and its rank in the sorted vector of cosine distances. Recursively, the player will find better and better words until the cosine distance is zero, meaning that he has found the secret word.
The game is using pretrained word embeddings from [GloVe](https://nlp.stanford.edu/projects/glove/).