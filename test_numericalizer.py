import unittest
from vocab import Vocabulary
from numericalizer import Numericalizer

class TestNumericalizer(unittest.TestCase):

	def test_indexer(self):
		data = ['a', 'b', 'c', 'c', 'c', 'd']
		v = Vocabulary()
		v.add_tokens(data)
		n = Numericalizer(v)
		expected_results = [0, 1, 2, 3, 4]
		
		self.assertEqual(n.token_to_idx(v.unk_token), expected_results[0])
		self.assertEqual(n.token_to_idx('a'), expected_results[1])
		self.assertEqual(n.token_to_idx('b'), expected_results[2])
		self.assertEqual(n.token_to_idx('c'), expected_results[3])
		self.assertEqual(n.token_to_idx('d'), expected_results[4])
		self.assertEqual(n.token_to_idx('boo'), expected_results[0])


	def test_rev_indexer(self):
		data = ['a', 'b', 'c', 'c', 'c', 'd']
		v = Vocabulary()
		v.add_tokens(data)
		n = Numericalizer(v)

		expected_results = [v.unk_token, 'a', 'b', 'c', 'd']

		self.assertEqual(n.idx_to_token(0), expected_results[0])
		self.assertEqual(n.idx_to_token(1), expected_results[1])
		self.assertEqual(n.idx_to_token(2), expected_results[2])
		self.assertEqual(n.idx_to_token(3), expected_results[3])
		self.assertEqual(n.idx_to_token(4), expected_results[4])
		with self.assertRaises(KeyError):
			n.idx_to_token(5)

	def test_token_error(self):
		data = ['a', 'b', 'c', 'c', 'c', 'd']
		v = Vocabulary()
		v.add_tokens(data)
		n = Numericalizer(v,unk=False)

		with self.assertRaises(KeyError):
			n.token_to_idx('hahaha')


if __name__ == '__main__':
	unittest.main()