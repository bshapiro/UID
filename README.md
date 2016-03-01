This repository contains the modeling code for ongoing research in computational cognitive linguistics regarding the hypothesis of Uniform Information Density theory and its impact on the evolution of an artificial language. 

uid.py: contains functions for instantiating an ngram, a word order, and then calculating the IDU (information density uniformity) of that word order given the language specified in data/events_artificial.txt.

basic.py: basic text/language writing/reading functionalities.

config.py: config parameters for the system.

trigram.py: contains the implementation of the trigram used for calculating the information density uniformity of any given sentence.

generate_language.py and generate_words.py each contain methods for generating an artificial language based on a set of events (contained in data/events.txt). Generate_words simply uses a cvc paradigm to convert english words to artificial pseudowords and generate_language uses the mapping provided by generate_words to spit out the entire language rewritten. 
