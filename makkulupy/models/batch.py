from typing import List, Union
from datetime import datetime

from .word import Word


class Batch:
    """Represents a Batch from the makkulu API.

    Attributes:
        id: An integer uniquely identifying the Batch.
        name: The name of the Batch.
        description: The description of the Batch.
        submitted:
            A boolean indicating whether the Batch has been submitted to
            the oven.
        submitted_at:
            A datetime object representing when the Batch was submitted,
            if ``submitted`` is True.
        discussion_count:
            The number of active discussions flagged on the Batch.
        passed:
            A boolean indicating whether the Batch has finished baking.
        passed_at:
            A datetime object representing when the Batch finished baking,
            if ``passed`` is True.
        voting_from:
            A datetime object representing the time from which the deadline
            for the Batch passing should be calculated.
        voting_hours:
            An integer representing the number of hours the Batch should
            spend in the oven before finishing baking.
        url: The URL of the Batch on the makkulu website.
        words: A list of Word objects that the Batch contains.
    """

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
    """Represents the result from a call to the makkulu API that contains a
    list of batches.

    Attributes:
        count:
            The full number of results the request found, regardless of how
            many batches were returned in this BatchSet.
        batches:
            A list of Batch objects that were returned from the makkulu API.

    Examples:
        Check if this BatchSet is only a subset of the results found by the
        API.

        >>> batch_set.count > len(batch_set)
    """

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
