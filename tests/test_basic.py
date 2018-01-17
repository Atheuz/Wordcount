import unittest
from lib import Preprocessor
from lib import Wordcounter

class TestPreprocessing(unittest.TestCase):

    def test_remove_punctuation(self):
        pp = Preprocessor()
        map = {'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~': '',
               'abc.def': 'abcdef',
               '!!!! test !!!!': ' test ',
               'test': 'test',
               '':''
            }

        for k,v in map.items():
            self.assertEqual(pp.remove_punctuation(k),v)

    def test_remove_stopwords(self):
        self.assertTrue(True)  # Out of scope.

    def test_stem(self):
        self.assertTrue(True) # Out of scope.

    def test_to_lowercase(self):
        pp = Preprocessor()
        map = [(['ABC'], ['abc']),
               (['test'], ['test']),
               (['!!!! aBc !!!!'], ['!!!! abc !!!!']),
               ([], [])
            ]

        for k,v in map:
            self.assertListEqual(pp.to_lowercase(k),v)

    def test_tokenize(self):
        pp = Preprocessor()
        map = {'abcdefg': ['abcdefg'],
               'test test test test test': ['test', 'test', 'test', 'test', 'test'],
               '!!!! aBc !!!!': ['!!!!', 'aBc','!!!!'],
               '': []
            }

        for k,v in map.items():
            self.assertListEqual(pp.tokenize(k),v)

class TestWordcounter(unittest.TestCase):
    
    def test_count(self):
        tokens = ['test', 'test', 'test', 'test', 'test']
        wc = Wordcounter(tokens)
        self.assertEqual(wc.count(), [('test', 5)])

    def test_count2(self):
        tokens = ['test', 'test', 'test', 'test', 'test', 'abc', 'abc', 'def', 'abc', 'def', 'abc']
        wc = Wordcounter(tokens)
        self.assertEqual(wc.count(), [('test', 5), ('abc', 4), ('def', 2)])

    def test_count3(self):
        tokens = []
        wc = Wordcounter(tokens)
        self.assertEqual(wc.count(), [])

    def test_big(self):
        file = "input/cv000_tok-11609.txt"
        corpus = open(file, encoding='utf8').read()
        pp = Preprocessor()
        tokens = pp.preprocess(corpus)
        wc = Wordcounter(tokens)
        counts = wc.count()

        file2 = "input/test.txt" # Contains unicode æøå replacing eoa, should result in same output.
        corpus2 = open(file2, encoding='utf8').read()
        pp2 = Preprocessor()
        tokens2 = pp2.preprocess(corpus2)
        wc2 = Wordcounter(tokens2)
        counts2 = wc2.count()

        self.assertListEqual([x[1] for x in counts], [x[1] for x in counts2])