from collections import Counter
import math


class TrigramModel:

    def __init__(self, language):
        trigrams = self.get_trigrams(language)
        bigrams = self.get_bigrams(language)
        self.trigram_counts = self.get_trigram_counts(trigrams)
        self.bigram_counts = self.get_bigram_counts(bigrams)

    def get_trigrams(self, language):
        language_length = len(language)
        trigrams = []
        for index in range(2, language_length):
            word = language[index]
            if word != '.':
                trigrams.append(language[index - 2:index + 1])
        return trigrams

    def get_bigrams(self, language):
        language_length = len(language)
        bigrams = []
        for index in range(1, language_length):
            word = language[index]
            last_word = language[index - 1]
            if word != '.' or last_word == '.':
                bigrams.append(language[index - 1:index + 1])
        return bigrams

    def get_trigram_counts(self, trigrams):
        trigram_counts = Counter()
        for trigram in trigrams:
            hashable_sentence = ' '.join(trigram)
            trigram_counts[hashable_sentence] += 1
        return trigram_counts

    def get_bigram_counts(self, bigrams):
        bigram_counts = Counter()
        for bigram in bigrams:
            hashable_sentence = ' '.join(bigram)
            bigram_counts[hashable_sentence] += 1
        return bigram_counts

    def prob(self, word, context):
        index = context.index(word)
        context = context[index - 2:index + 1]
        trigram = ' '.join(context)
        bigram = ' '.join(context[0:2])
        prob = float(self.trigram_counts[trigram]) / float(self.bigram_counts[bigram])
        return prob

    def log_prob(self, word, context):
        prob = self.prob(word, context)
        log_prob = -1 * math.log(prob, 2)
        return log_prob
