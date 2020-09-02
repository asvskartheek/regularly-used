import unittest
from unittest import TestCase

from vocab import Vocabulary
from collections import OrderedDict
import glob
import os


class TestVocab(unittest.TestCase):
    def test_add_tokens(self):
        """
		Test tokens are getting added
		"""
        data = ['a', 'b', 'c', 'c', 'c', 'd']
        expected_result = OrderedDict([('<unk>', float('inf')), ('a', 1), ('b', 1), ('c', 3), ('d', 1)])

        v = Vocabulary()
        v.add_tokens(data)
        result = v.tokens
        self.assertEqual(result, expected_result)

    def test_truncate_vocab(self):
        """
		Test truncation of vocabulary
		"""
        data = ['a', 'b', 'c', 'c', 'c', 'd']
        expected_result = OrderedDict([('<unk>', float('inf')), ('c', 3), ('a', 1), ('b', 1)])

        v = Vocabulary()
        v.add_tokens(data)
        v.truncate_vocab(4)
        result = v.tokens

        self.assertEqual(result, expected_result)

    def test_loading_vocab(self):
        """
		Test Vocab saving
		"""
        data = ['a', 'b', 'c', 'c', 'c', 'd']
        expected_tokens = OrderedDict([('<unk>', float('inf')), ('a', 1), ('b', 1), ('c', 3), ('d', 1)])
        expected_vocab_size = 5
        expected_max_vocab_size = 20_000

        v = Vocabulary()
        v.add_tokens(data)
        # save vocab
        file = v.save()
        # load
        v = Vocabulary.load(file)

        # remove temp files
        files = glob.glob('./*.pkl')
        for f in files:
            os.remove(f)

        self.assertDictEqual(v.tokens, expected_tokens)
        self.assertEqual(v.vocab_size, expected_vocab_size)
        self.assertEqual(v.max_vocab_size, expected_max_vocab_size)


if __name__ == '__main__':
    unittest.main()
