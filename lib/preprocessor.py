import string
import re
import nltk
from nltk.corpus import stopwords


class Preprocessor(object):
    def __init__(self):
        pass
        
    def remove_punctuation(self, text):
        """Remove punctuation in a string.

        input: Input text string from which punctuation should be removed.
        output: Output text string from which punctuation has been removed.

        Punctuation defined as string.punctuation, that is: !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~   
        """
        punctuation_filter = re.compile(r'([%s])+' % re.escape(string.punctuation), re.UNICODE) # Use this to remove all punctuation defined in !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
        stripped = punctuation_filter.sub("", text)
        return stripped

    def remove_stopwords(self, tokens):
        """Removes stopwords in a string.

        input: Input list of tokens from which stopwords should be removed.
        output: text_removed_s : Output list of tokens which punctuation has been removed.
        
        In a real scenario you would also remove stopwords, I.E very common words such as "and, i, to, a, be and so on.."
        The list of stopwords can either be determined from a preconstructed list based on the language(i.e. English) or constructed based on the corpus itself.
        For the purposes of this exercise this is left out."""

        stop_words = set(stopwords.words('english'))
        stopwords_tokens = [token for token in tokens if token not in stop_words]
        return stopwords_tokens

    def to_lowercase(self, tokens):
        """Converts tokens to lowercase.

        input: Input list of tokens that should be converted to lowercase.
        output: Output list of tokens converted to lowercase.
        """

        lowercased_tokens = [x.lower() for x in tokens]
        return lowercased_tokens

    def stem(self, tokens):
        """Stems the tokens to their base form.
    
        input: Input list of tokens to be stemmed.
        output: Output list of stemmed tokens.

        This would also be necessary in a real scenario, but for the purposes of this exercise it has been left out.   
        """
        stemmer = nltk.stem.snowball.EnglishStemmer() 
        stemmed_tokens = [stemmer.stem(x) for x in tokens]
        return stemmed_tokens

    def tokenize(self, text):
        """Tokenize a string, i.e create a list of words(tokens).
    
        input: Input text string that should be tokenized.
        output: Output list of tokens.

        Creates a list of tokens split on 
        """
    
        tokens = []
        split_text = text.split()
        return split_text
            
    def preprocess(self, input):
        text = self.remove_punctuation(input)
        tokens = self.tokenize(text)
        tokens = self.to_lowercase(tokens)
        #tokens = self.remove_stopwords(tokens)
        #tokens = self.stem(tokens)
        return tokens