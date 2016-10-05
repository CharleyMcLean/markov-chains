import sys
import random
from random import choice


def open_and_read_file(file_path):

    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    poem_string = open(file_path).read()


    return poem_string


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
  
    for word in text_string:
        words = text_string.split()

    n_gram = int(raw_input("What size n-gram would you like to use? >"))

    #Looping over the text and making dictionary of tuples and lists
    for i in range(len(words) - n_gram):
        #  
        if tuple(words[i:i + n_gram]) not in chains:
            chains[tuple(words[i:i + n_gram])] = [words[i + n_gram]]
        else:
            chains[tuple(words[i:i + n_gram])].append(words[i + n_gram])

    # Checking the last two words.  If not in dictionary, a
    if tuple(words[-n_gram:]) not in chains:
        chains[tuple(words[-n_gram:])] = [None]
    else:
        chains[tuple(words[-n_gram:])].append(None)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text_list = []

    generated_key = random.choice(chains.keys())
    text_list.extend(list(generated_key))
    first_word, second_word = generated_key[0], generated_key[1]
    next_word = random.choice(chains[generated_key])
    

    while next_word:
        text_list.append(next_word)

        first_word = second_word
        second_word = next_word
        
        next_pair = (first_word, second_word)

        next_word = random.choice(chains[next_pair])

    print " ".join(text_list)



input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)
