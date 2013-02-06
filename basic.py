from trigram import TrigramModel
from config import events


def generate_order_list(order, words):
    periods = ['.' for word in words[0]]
    subjects = words[0]
    verbs = words[1]
    adjectives = words[2]
    objects = words[3]

    if order == "svao":
        order_list = [subjects, verbs, adjectives, objects]
    elif order == "svoa":
        order_list = [subjects, verbs, objects, adjectives]
    elif order == "saov":
        order_list = [subjects, adjectives, objects, verbs]
    elif order == "soav":
        order_list = [subjects, objects, adjectives, verbs]
    elif order == "aosv":
        order_list = [adjectives, objects, subjects, verbs]
    elif order == "oasv":
        order_list = [objects, adjectives, subjects, verbs]
    elif order == "aovs":
        order_list = [adjectives, objects, verbs, subjects]
    elif order == "oavs":
        order_list = [objects, adjectives, verbs, subjects]
    elif order == "vsao":
        order_list = [verbs, subjects, adjectives, objects]
    elif order == "vsoa":
        order_list = [verbs, subjects, objects, adjectives]
    elif order == "vaos":
        order_list = [verbs, adjectives, objects, subjects]
    elif order == "voas":
        order_list = [verbs, objects, adjectives, subjects]

    order_list.insert(0, periods)
    order_list.insert(0, periods)

    return order_list


def generate_ngram(order, words):
    order_list = generate_order_list(order, words)
    language = assemble_language(order_list)
    return TrigramModel(language), order_list


def assemble_language(order_list):
    language = []
    for i in range(0, len(order_list[0])):
        for j in range(0, len(order_list)):
            word = order_list[j][i]
            if word != "":
                language.append(order_list[j][i])
    return language


def estimate_language_idu(ngram, words):
    sentence_idus = []
    for i in range(0, len(words[0])):
        sentence_list = [collection[i] for collection in words if collection[i] != ""]
        word_entropies = []

        for word in sentence_list:
            if word == '.':
                continue
            prob = ngram.prob(word, sentence_list)
            log_prob = ngram.log_prob(word, sentence_list)
            entropy = prob * log_prob
            word_entropies.append(entropy)

        avg_entropy = average(word_entropies)
        distances = [abs(word_entropy - avg_entropy) for word_entropy in word_entropies]
        avg_distance = average(distances)
        if avg_distance != 0:
            sentence_idu = 1 / avg_distance
        else:
            sentence_idu = 9999999999
        sentence_idus.append(sentence_idu)
    language_idu = average(sentence_idus)
    return language_idu


def average(items):
    sum_items = 0
    for item in items:
        sum_items += item
    average = float(sum_items) / float(len(items))
    return average


def read_file(filename):
    f = open(filename)
    subjects = []
    verbs = []
    adjectives = []
    objects = []
    for line in f:

        if line == '\n':
            continue

        items = line.split(',')

        subject = items[0]
        verb = items[1]
        if len(items) > 3:
            adjective = items[2]
            dobject = items[3][:-1]
        else:
            adjective = ''
            dobject = items[2][:-1]

        subjects.append(subject)
        verbs.append(verb)
        adjectives.append(adjective)
        objects.append(dobject)
    f.close()
    words = [subjects, verbs, adjectives, objects]
    return words

if __name__ == "__main__":
    words = read_file(events)
    orders = ["svao", "svoa", "vsao", "vsoa", "aovs", "oavs", "saov", "soav", "voas", "vaos", "aosv", "oasv"]

    for order in orders:
        ngram, language = generate_ngram(order, words)
        language_idu = estimate_language_idu(ngram, language)
        print order, " IDU rating:", str(language_idu)
