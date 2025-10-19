from collections import defaultdict
import numpy as np


class MarkovText(object):
    # Exercise 1
    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    def get_term_dict(self):
        # Split the corpus into tokens
        tokens = self.corpus.split()

        # Create dictionary where each word maps to list of following words
        term_dict = defaultdict(list)

        # Loop through tokens to populate dictionary
        for i in range(len(tokens) - 1):
            current_word = tokens[i]
            next_word = tokens[i + 1]
            term_dict[current_word].append(next_word)

        # Save dictionary to the object
        self.term_dict = term_dict

        # Return dictionary
        return self.term_dict

    def generate(self, seed_term=None, term_count=15):
        # This will be used in Exercise 2
        return None

    
    # Exercise 2
    def generate(self, seed_term=None, term_count=15):
        """Generate a sequence of words using the Markov chain model."""

        # Make sure the transition dictionary exists
        if self.term_dict is None:
            raise ValueError("Please build the term dictionary first using get_term_dict().")

        # If no seed word is given, choose one randomly
        if seed_term is None:
            current_word = np.random.choice(list(self.term_dict.keys()))
        else:
            # If the provided seed isn't in our dictionary, raise an error
            if seed_term not in self.term_dict:
                raise ValueError(f"Seed term '{seed_term}' not found in corpus.")
            current_word = seed_term

        # Start building the generated sentence
        generated_words = [current_word]

        # Loop to generate the rest of the words
        for _ in range(term_count - 1):
            # If the current word has no next word, restart randomly
            if current_word not in self.term_dict or len(self.term_dict[current_word]) == 0:
                current_word = np.random.choice(list(self.term_dict.keys()))

            # Choose a random next word from the list of possible next words
            next_word = np.random.choice(self.term_dict[current_word])

            # Append it to our growing sentence
            generated_words.append(next_word)

            # Move to the next word
            current_word = next_word

        # Join all words into one string
        return ' '.join(generated_words)
