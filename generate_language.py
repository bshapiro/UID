from models import read_file
from models import generate_random_word
from config import artificial_events, events


def generate_language(words):
    dictionary = {}
    for subset in words:
        for word in subset:
            if dictionary.get(word) == None:
                dictionary[word] = generate_random_word()
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
    words = read_file(events)
    if generate_language(words) == True:
        print "Successfully wrote new language."
    else:
        print "Error in writing new language."
