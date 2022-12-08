#From chapter 17

import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(text) #findall returna list with all non-overlapping matches of the regular expression as a list of strings.

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self) -> str:
        return'Sentence(%s)'% reprlib.repr(self.text) #reprlib.repr is a utility function to generate abbreviated string representaion of data structures that can be very large.