from typing import List, Union


class Word:
    def __init__(
        self,
        *,
        id: Union[int, None] = None,
        headword: Union[str, None] = None,
        slug: Union[str, None] = None,
        pos: Union[str, None] = None,
        cls: Union[str, None] = None,
        definition: Union[str, None] = None,
        etymology: Union[str, None] = None,
        notes: Union[str, None] = None,
        url: Union[str, None] = None,
    ):
        self.id = id
        self.headword = headword
        self.slug = slug
        self.pos = pos
        self.cls = cls
        self.definition = definition
        self.etymology = etymology
        self.notes = notes
        self.url = url


class WordSet:
    def __init__(
        self,
        *,
        count: int = 0,
        words: List[Word] = None,
    ):
        self.count: int = count
        self.words: List[Word] = words
        self._len_words = len(self.words)

    def __iter__(self):
        return iter(self.words)

    def __next__(self):
        return next(self.words)

    def __getitem__(self, n):
        return self.words[n]

    def __len__(self):
        return self._len_words
