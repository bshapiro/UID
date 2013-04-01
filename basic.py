from config import artificial_events
from uid import generate_ngram, estimate_language_idu


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
    words = read_file(artificial_events)
    orders = ["svao", "svoa", "vsao", "vsoa", "aovs", "oavs", "saov", "soav", "voas", "vaos", "aosv", "oasv"]

    for order in orders:
        ngram, language = generate_ngram(order, words)
        language_idu = estimate_language_idu(ngram, language)
        print order.upper(), ": ", str(language_idu)
