from models import read_file
from config import artificial_events, events
from random import choice

hard_sounds = ['t', 'd', 'p', 'c']
middle_consonants = ['r', 'l', 'n', 'm']
begin_consonants = ['t', 'd', 'p', 'sh', 'th', 'b', 'g', 'f', 'c', 'w', 'y', 'v', 'ch', 'st', 'str', 'tr', 'pl', 'br', 'pr', 'fr', 'gr', 'dr', 'sp']
vowels = ['a', 'a', 'a', 'o', 'o', 'i', 'e', 'e', 'u']
end_consonants = ['ss', 'rt', 'st', 'ck', 'nt', 'nd', 'ld', 'rd', 'tch', 'rm', 'rn', 'sh']


def generate_generic_syllable(begin):
    c_one = None
    if begin == True:
        c_one = choice(middle_consonants + begin_consonants)
    else:
        c_one = choice(hard_sounds)
    v = choice(vowels)
    c_middle = choice(middle_consonants)
    c_none = ""
    c_two = choice([c_middle, c_middle, c_none])  # make a final c 2/3 likely
    return c_one + v + c_two


def generate_ending_syllable():
    c_one = choice(hard_sounds)
    v = choice(vowels)
    c_two = choice(end_consonants)
    return c_one + v + c_two


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


def generate_random_word():
    length = 2
    word = ""
    if length == 1:
        word = generate_ending_syllable()
    if length == 2:
        word = generate_generic_syllable(begin=True)
        word += generate_ending_syllable()
    if length == 3:
        word = generate_generic_syllable(begin=True)
        word += generate_generic_syllable(begin=False)
        word += generate_ending_syllable()
    print word
    return word

if __name__ == "__main__":
    words = read_file(events)
    if generate_language(words) == True:
        print "Successfully wrote new language."
    else:
        print "Error in writing new language."
