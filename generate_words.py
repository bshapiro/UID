from random import choice

hard_sounds = ['t', 'd', 'p', 'c']
middle_consonants = ['r', 'l', 'n', 'm']
begin_consonants = ['t', 's', 'd', 'p', 'sh', 'th', 'b', 'g', 'f', 'c', 'w', 'y', 'v', 'ch', 'st', 'str', 'tr', 'pl', 'br', 'pr', 'fr', 'gr', 'dr', 'sp']
vowels = ['a', 'a', 'a', 'a', 'o', 'o', 'oo', 'i', 'i', 'e', 'e', 'e', 'u']
end_consonants = ['k', 'b', 'p', 't', 'm', 'p', 'rt', 'st', 'ck', 'nt', 'nd', 'ld', 'rd']
end_only = ['te', 'ss', 'se', 'tch', 'sh']
global end_true
end_true = False


def generate_generic_syllable(begin):
    global end_true
    c_one = None
    if begin == True:
        c_one = choice(middle_consonants + begin_consonants + hard_sounds)
    else:
        c_one = choice(hard_sounds)
    v = choice(vowels)
    c_middle = choice(middle_consonants)
    c_none = ""
    c_end = choice(end_consonants)
    c_two = choice([c_middle, c_none, c_end])  # make a final c 1/2 likely
    if c_two in end_consonants:
        end_true = True
    return c_one + v + c_two


def generate_ending_syllable():
    global end_true
    c_one = choice(hard_sounds)
    if end_true:
        c_one = choice([""])
        end_true = False
    v = choice(vowels)
    c_two = choice(end_consonants + end_only)
    return c_one + v + c_two


def generate_words():
    for i in range(0, 20):
        print generate_random_word()


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
    return word

if __name__ == "__main__":
    generate_words()
