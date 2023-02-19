from typing import List, Union


class Word:
    """Represents a Word from the makkulu API.

    Attributes:
        id: An integer uniquely identifying the Word.
        headword:
            A string representation of the Word as it appears in the
            makkulu dictionary.
        slug:
            The URL-friendly representation of the headword that is used
            to generate the Word's URL.
        pos: A string representing the Word's part of speech.
        cls: A string representing the Word's class.
        definition: The definition of the Word.
        etymology: The etymology of the Word.
        notes: Any notes attached to the Word.
        url: The URL of the Word on the makkulu website.
    """

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
    """Represents the result of a call to the makkulu API that contains a
    list of Words.

    Attributes:
        count:
            The full number of results the request found, regardless of how
            many Words were returned in this WordSet.
        words:
            A list of Word objects that were returned from the makkulu API.

    Examples:
        Check if this WordSet is only a subset of the results found by the
        API.

        >>> word_set.count > len(word_set)
    """

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
