import unittest
from lib import Preprocessor
from lib import Wordcounter

class TestPreprocessing(unittest.TestCase):

    def test_remove_punctuation(self):
        """Test preprocessor removal of punctuation from a series of strings."""
        pp = Preprocessor()
        map = {'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~': '', # All are removed
               'abc.def': 'abcdef', # One character is removed
               '!!!! test !!!!': ' test ', # Spaces are retained.
               'test': 'test', # Nothing is removed
               '':'' # Empty.
            }

        for k,v in map.items():
            self.assertEqual(pp.remove_punctuation(k),v)

    def test_remove_stopwords(self):
        """Test removal of stopwords.

        Not implemented as it is out of scope."""
        self.assertTrue(True)  # Always return True as this is out of scope.

    def test_stem(self):
        """Test stemming.

        Not implemented as it is out of scope."""
        self.assertTrue(True) # Always return True as this is out of scope.

    def test_to_lowercase(self):
        """Test preprocessor lowercase conversion method from lists of tokens. """
        pp = Preprocessor()
        map = [(['ABC'], ['abc']), # SImple
               (['test'], ['test']), # Nothing done
               (['!!!! aBc !!!!'], ['!!!! abc !!!!']), # Special text
               ([], []) # Empty
            ]

        for k,v in map:
            self.assertListEqual(pp.to_lowercase(k),v)

    def test_tokenize(self):
        """Test preprocessor tokenization, going from str -> list<str>. """

        pp = Preprocessor()
        map = {'abcdefg': ['abcdefg'], # Simple.
               'test test test test test': ['test', 'test', 'test', 'test', 'test'], # Multiple words
               '!!!! aBc !!!!': ['!!!!', 'aBc','!!!!'], # Special text
               '': [] # Empty
            }

        for k,v in map.items():
            self.assertListEqual(pp.tokenize(k),v)

class TestWordcounter(unittest.TestCase):
    
    def test_count(self):
        """Test wordcounter count method, case 1 where there is only one word."""
        tokens = ['test', 'test', 'test', 'test', 'test']
        wc = Wordcounter(tokens)
        self.assertEqual(wc.count(), [('test', 5)])

    def test_count2(self):
        """Test wordcounter count method, case 2 where there are different words."""
        tokens = ['test', 'test', 'test', 'test', 'test', 'abc', 'abc', 'def', 'abc', 'def', 'abc']
        wc = Wordcounter(tokens)
        self.assertEqual(wc.count(), [('test', 5), ('abc', 4), ('def', 2)])

    def test_count3(self):
        """Test wordcounter count method, case 3 where there are no words."""
        tokens = []
        wc = Wordcounter(tokens)
        self.assertEqual(wc.count(), [])

    def test_big(self):
        """Test wordcounter count method, case 4 where we have two identical files except for the fact that:
        
        e has been replaced with æ
        o has been replaced with o
        a has been replaced with å. 

        This should provide the same counts.
        """
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