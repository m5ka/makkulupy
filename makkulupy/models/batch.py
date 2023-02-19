from typing import List, Union
from datetime import datetime

from .word import Word


class Batch:
    def __init__(
        self,
        *,
        id: Union[int, None] = None,
        name: Union[str, None] = None,
        description: Union[str, None] = None,
        submitted: Union[bool, None] = None,
        submitted_at: Union[datetime, None] = None,
        discussion_count: Union[int, None] = None,
        passed: Union[bool, None] = None,
        passed_at: Union[datetime, None] = None,
        voting_from: Union[datetime, None] = None,
        voting_hours: Union[int, None] = None,
        url: Union[str, None] = None,
        words: List[Word] = [],
    ):
        self.id = id
        self.name = name
        self.description = description
        self.submitted = submitted
        self.submitted_at = submitted_at
        self.discussion_count = discussion_count
        self.passed = passed
        self.passed_at = passed_at
        self.voting_from = voting_from
        self.voting_hours = voting_hours
        self.url = url
        self.words = words
        self._len_words = len(words)

    def __len__(self):
        return self._len_words


class BatchSet:
    def __init__(
        self,
        *,
        count: int = 0,
        batches: List[Batch] = None,
    ):
        self.count = count
        self.batches = batches
        self._len_batches = len(self.batches)

    def __iter__(self):
        return iter(self.batches)

    def __next__(self):
        return next(self.batches)

    def __getitem__(self, n):
        return self.batches[n]

    def __len__(self):
        return self._len_batches
