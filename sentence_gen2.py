import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text):
        self.text = text #No need to create a word list

    def __repr__(self) -> str:
        return f'Sentence({reprlib.repr(self.text)}'

    def __iter__(self):
        for match in RE_WORD.finditer(self.text): #finditer builds an iterator over the matches of RE_WORD on self.text, yielding MatchObject
            yield match.group()
            #mathc.group() extracts the matched text from the MatchObject instance
