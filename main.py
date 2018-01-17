from Preprocessor import Preprocessor
from Wordcounter import Wordcounter

def main():
    file = "input/cv000_tok-11609.txt"
    pp = Preprocessor(file)
    tokens = pp.preprocess()
    wc = Wordcounter(tokens)
    counts = wc.count()
    print(counts)
    

if __name__ == '__main__':
    main()