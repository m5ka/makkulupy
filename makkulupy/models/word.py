class Word:
    def __init__(
        self,
        *,
        headword=None,
        pos=None,
        cls=None,
        definition=None,
        etymology=None,
        notes=None,
    ):
        self.headword = headword
        self.pos = pos
        self.cls = cls
        self.definition = definition
        self.etymology = etymology
        self.notes = notes


class WordSet:
    def __init__(
        self,
        *,
        count=0,
        words=None,
    ):
        self.count = count
        self.words = words
        self._len_words = len(self.words)

    def __iter__(self):
        return iter(self.words)

    def __next__(self):
        return next(self.words)

    def __getitem__(self, n):
        return self.words[n]

    def __len__(self):
        return self._len_words
