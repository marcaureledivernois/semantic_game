# Guess the secret word !

Play the game [here](https://share.streamlit.io/marcaureledivernois/semantic_game/app.py). The goal of the game is to guess a secret word. To do so,
propose any word and see how close you are from the secret word. The higher the score you get, the closer
you are to the secret word. When you score high, it means your proposed word is either easily
interchangeable with the secret word, or that it is often associated with the secret word.

## Examples

Let's say the secret word is "raising". Words that will score low are for instance "increasing" (synonym), "money" 
(often associated with "raising") or "reducing" (antonym). Antonyms are
also scoring low because they are close semantically ! However, words such as "magically", "fruitcake" or "cyclop" will score high
because they do not really have a link with "raising".