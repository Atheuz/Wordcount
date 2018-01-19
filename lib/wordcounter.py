import collections
import pandas as pd

class Wordcounter(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.count_dict = {}

    def count(self):
        """Returns a list of tokens and their associated count.

        Output: A list of tokens and their associated count, sorted by count.

        Manual implementation"""
        for token in self.tokens:
            if token not in self.count_dict:
                self.count_dict[token] = 0
            self.count_dict[token] += 1
        
        counts = self.count_dict.items()
        val = sorted(counts, key=lambda x: x[1], reverse=True)
        return val

    def count_counter(self):
        """Returns a list of tokens and their associated count.

        Output: A list of tokens and their associated count, sorted by count.
        
        Uses collections.Counter.
        """
        counts = list(collections.Counter(self.tokens).items())
        val = sorted(counts, key=lambda x: x[1], reverse=True)
        return val

    def count_pd(self):
        """Returns a list of tokens and their associated count.

        Output: A list of tokens and their associated count, sorted by count.
        
        Uses pandas
        """
        df = pd.DataFrame(self.tokens, columns = ['Word'])
        counts = df.apply(pd.value_counts).reset_index()
        counts.columns = ['Word','Count']
        count_lst = [tuple(x) for x in counts.to_records(index=False)]
        return count_lst
        
        