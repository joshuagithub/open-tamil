# -*- coding: utf-8 -*-
# 
# (C) முத்தையா அண்ணாமலை 2013
# 
# N-gram language model for Tamil letters

import tamil

from corpus import Corpus

class Letters:
    def __init__(self,filename):
        self.letter = dict();
        self.letter.update(zip( tamil.utf8.tamil_letters,
                                map(lambda x : 0, tamil.utf8.tamil_letters) ) )
        self.corpus = Corpus( filename )

    def __unicode__( self ):
        op = u""
        for lett,freq in self.letter.items():
            op = op + u"%s => %d\n"%(lett,freq)
        print max(self.letter.values())
        return op

class Unigram(Letters):
    def frequency_model( self ):
        """ build a letter frequency model for Tamil letters from a corpus """
        # use a generator in corpus
        for next_letter in self.corpus.next_tamil_letter():
            # update frequency from corpus
            self.letter[next_letter] = self.letter[next_letter] + 1
    
class Bigram(Unigram):
    def language_model(self):
        """ builds a Tamil bigram letter model """
        pass