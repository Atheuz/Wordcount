from lib import Preprocessor
from lib import Wordcounter
import unittest
import tests.test_basic

def main():
    """Entry point into project.

    Runs test suite first, and then applies a flow to the provided input file finally outputting the counts that we want.
    """
    suite = unittest.TestLoader().loadTestsFromModule(tests.test_basic)
    unittest.TextTestRunner(verbosity=3).run(suite)

    file = "input/cv000_tok-11609.txt"
    corpus = open(file, encoding='utf8').read()
    pp = Preprocessor()
    tokens = pp.preprocess(corpus)
    wc = Wordcounter(tokens)
    counts = wc.count()

    print(counts)

if __name__ == '__main__':
    main()