from vocab import Vocabulary

class Numericalizer:

	def __init__(self, vocabulary:Vocabulary, unk=True):
		self.vocabulary = vocabulary
		self.tokens = list(vocabulary.tokens)
		self.unk = unk


	def token_to_idx(self, token):
		# TODO: Handle when unk is not True
		if token not in self.tokens:
			if self.unk:
				return self.tokens.index(self.vocabulary.unk_token)
			else:
				raise KeyError('{} not in the vocabulary'.format(token))
		return self.tokens.index(token)


	def idx_to_token(self, idx):
		if idx >= self.vocabulary.vocab_size:
			raise KeyError('{} is out of range {}'.format(idx, self.vocabulary.max_vocab_size))
		else:
			return list(self.vocabulary.tokens)[idx]