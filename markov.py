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


def make_chains(text_string, n_gram=2):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    
    words = text_string.split()

    

    #Looping over the text and making dictionary of tuples and lists
    for i in range(len(words) - n_gram):
        n_gram_key = tuple(words[i:i + n_gram])
        n_gram_value = words[i + n_gram]
        if n_gram_key not in chains:
            chains[n_gram_key] = [n_gram_value]
        else:
            chains[n_gram_key].append(n_gram_value)

    # Checking the last two words.  If not in dictionary, a
    if tuple(words[-n_gram:]) not in chains:
        chains[tuple(words[-n_gram:])] = [None]
    else:
        chains[tuple(words[-n_gram:])].append(None)

    return chains


def make_text(chains, n_gram=2):
    """Takes dictionary of markov chains; returns random text."""

    text_list = []

    #try putting this block into while loop

    generated_key = random.choice(chains.keys())

    while True:
        if generated_key[0].istitle():
            text_list.extend(list(generated_key))
            # print text_list
            break
        else:
            generated_key = random.choice(chains.keys())
            # print generated_key

    
    previous_words = generated_key[-(n_gram-1):]
    next_word = random.choice(chains[generated_key])


    while next_word:
        if next_word[-1] in [".", "?", "!"]:
            text_list.append(next_word)
            break
        text_list.append(next_word)
        next_group = tuple(text_list[-n_gram:])
        next_word = random.choice(chains[next_group])

    print " ".join(text_list)



input_path = sys.argv[1]

n_gram = int(raw_input("What size n-gram would you like to use? > "))

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n_gram)

# print chains

# Produce random text
random_text = make_text(chains, n_gram)
