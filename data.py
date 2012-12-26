from random import choice

cvc = ['ver', 'var', 'van', 'ven',
    'ter', 'tar', 'tan', 'ten',
    'com', 'con', 'can', 'cor',
    'don', 'din', 'dan', 'dar',
    'par', 'por',
    'lor', 'lar', 'lan'
    'mar', 'mor', 'mer',
    'gor', 'gon', 'gar', 'gan',
    'bar', 'ban', 'ber', 'ben',
    'far', 'fer', 'fen',
    'war', 'wan', 'wer']
cv = ['har', 'han',
     'her', 'di', 'ha', 'to',
    'lo', 'dro', 'no', 'na',
    'ma', 'mo', 'be', 'tro', 'tra',
    'bra', 'bro', 'bre', 'pro', 'pra', 'pre',
    'pri', 'stro', 'stra',
    'cra', 'cro']
word_final_cvc = ['ted', 'but', 'cut',
    'bot', 'bat', 'art', 'mort', 'nort', 'tack', 'nack', 'nock'
    'ton', 'tom', 'nert', 'dast', 'pust']

hard_sounds = ['t', 'd', 'p', 'c']
middle_consonants = ['r', 's', 'l', 'n', 'm']
begin_consonants = ['sh', 'b', 'g', 'f', 'c', 'w', 'y', 'v', 'ch', 'st', 'str', 'tr', 'pl', 'br', 'pr', 'fr', 'gr', 'dr', 'sp']
vowels = ['a', 'a', 'a', 'o', 'o', 'i', 'e', 'e', 'e', 'u']
end_consonants = ['d', 't', 'rt', 'st', 'ck', 'nt', 'nd', 'ld', 'rd', 'tch', 'rm', 'rn', 'sh']


def generate_generic_syllable(begin):
    c_one = None
    if begin == True:
        c_one = choice(hard_sounds + middle_consonants + begin_consonants)
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
