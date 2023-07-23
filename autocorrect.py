import nltk
from nltk.corpus import words
from difflib import get_close_matches

nltk.download('words')
word_list = words.words()

def auto_correct(input_word):
    input_word = input_word.lower()
    
    # Check if the input word is in the dictionary
    if input_word in word_list:
        return f"{input_word.capitalize()} is spelled correctly."
    
    # Find the nearest word in the dictionary using Levenshtein distance
    closest_word = get_close_matches(input_word, word_list, n=1, cutoff=0.8)
    
    if closest_word:
        return f"Did you mean: {closest_word[0].capitalize()}?"
    else:
        return "Sorry, the word is not in the dictionary."

# Test cases
word_to_correct = "computerrr"
print(auto_correct(word_to_correct))

word_to_correct = "butter"
print(auto_correct(word_to_correct))

word_to_correct = "jamme"
print(auto_correct(word_to_correct))

word_to_correct = "progrmer"
print(auto_correct(word_to_correct))


