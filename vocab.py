from collections import OrderedDict
from itertools import islice
import pickle


class Vocabulary:

    def __init__(self, max_vocab_size=20_000, unk_token='<unk>'):
        self.max_vocab_size = max_vocab_size
        self.unk_token = unk_token
        # UNK token is set to inf to have it not removed during truncate
        self.tokens = OrderedDict([(self.unk_token, float('inf'))])
        self.vocab_size = 1

    def add_token(self, token):
        if token not in self.tokens:
            self.vocab_size += 1
            self.tokens[token] = 0
        self.tokens[token] += 1
        return None

    def add_tokens(self, tokens):
        for token in tokens:
            self.add_token(token)

        return None

    def truncate_vocab(self, max_vocab_size):
        self.max_vocab_size = max_vocab_size
        if self.vocab_size <= self.max_vocab_size:
            print('Truncation Not Required')
        else:
            self.tokens = {k: v for k, v in sorted(self.tokens.items(), key=lambda item: item[1], reverse=True)}
            self.tokens = OrderedDict(islice(self.tokens.items(), 0, self.max_vocab_size))

        return None

    def build_vocabulary(self):
        # TODO
        pass

    def save(self, file='vocab.pkl'):
        with open(file, 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

        print('Saved to {}'.format(file))
        return file

    @staticmethod
    def load(file):
        with open(file, 'rb') as f:
            obj = pickle.load(f)

        print('Loaded from {}'.format(file))
        return obj
