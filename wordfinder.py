"""Word Finder: finds random words from a dictionary."""

import random 



class WordFinder:
    """Class with methods for finding random words from a dictionary
    
    >>> wf = WordFinder("teams.txt")
    6 words read

    >>> wf.random() in ["Panthers", "Cowboys", "Eagles", "Giants", "Rams", "Seahawks"]
    True 

    >>> wf.random() in ["Panthers", "Cowboys", "Eagles", "Giants", "Rams", "Seahawks"]
    True 

    >>> wf.random() in ["Panthers", "Cowboys", "Eagles", "Giants", "Rams", "Seahawks"]
    True 

    """



    def __init__(self, filepath):
        """Read dictionary, extract words into a list, and reports # of items read"""
        self.filepath = filepath 
        self.words = self.create_words_list()
        self.num_words = len(self.words)

        print(f'{self.num_words} words read')
    
    def create_words_list(self):
        """opens file provided by filepath and extract words into a list """

        with open(self.filepath) as file:
            return [line.strip() for line in file]
    
    def random(self):
        """selects a random word from the dictionary"""
        return random.choice(self.words)
     
    

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments

    >>> swf = SpecialWordFinder('new_words.txt')
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True
    """



    def __init__(self, filepath):
        super().__init__(filepath)

    def create_words_list(self):

        with open(self.filepath) as file:
            return [line.strip() for line in file if line.strip() and line[0] != '#']

