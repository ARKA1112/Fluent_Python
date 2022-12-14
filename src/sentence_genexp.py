import re
import reprlib

RE_WORD = re.compile(r'\W+')

class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self) -> str:
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        return (match.group()  for match in RE_WORD.finditer(self.text))