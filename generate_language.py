from config import events, artificial_events, artificial_words
from random import choice
from basic import read_file


def generate_language(words, pseudowords):
    dictionary = {}
    for subset in words:
        for word in subset:
            if dictionary.get(word) == None:
                pseudoword = choice(pseudowords)
                pseudowords.remove(pseudoword)
                dictionary[word] = pseudoword
    return reassemble_language(words, dictionary)


def reassemble_language(words, dictionary):
    new_language = open(artificial_events, "w")
    for i in range(0, len(words[0])):
        line = ""
        for j in range(0, len(words)):
            line += dictionary[words[j][i]] + ","
        line = line[:-1] + "\n"
        new_language.write(line)
    new_language.close()
    return True


if __name__ == "__main__":
    pseudowords = [item[:-1] for item in open(artificial_words).readlines()]
    words = read_file(events)
    if generate_language(words, pseudowords) == True:
        print "Successfully wrote new language."
        print open(artificial_events).read()
    else:
        print "Error in writing new language."
