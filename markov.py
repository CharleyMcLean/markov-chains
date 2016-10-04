import sys
import random
from random import choice

file_path = sys.argv[1]




def open_and_read_file(file_path):

    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
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

    
    for i in range(len(words) - 2):
        if (words[i], words[i + 1]) not in chains:
            chains[(words[i], words[i + 1])] = [words[i + 2]]
        else:
            chains[(words[i], words[i + 1])].append(words[i + 2])

    # Checking the last two words.  If not in dictionary, a
    if (words[-2], words[-1]) not in chains:
        chains[(words[-2], words[-1])] = [None]
    else:
        chains[(words[-2], words[-1])].append(None)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text_list = []

    # your code goes here
 
    #text = text + " ".join(random.choice(chains))
    

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
              
    print text_list

    print " ".join(text_list)


    # first_gen_key = random.choice(chains.keys())
    # next_word = random.choice(chains[first_gen_key])
    # first_word, second_word = first_gen_key[0], first_gen_key[1]
    # text = first_word + " " + second_word + " " + next_word


    # print text
    # print first_gen_key
    # print next_word
    # print first_word
    # print second_word
    # return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
