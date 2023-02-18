class Batch:
    def __init__(
        self,
        *,
        name=None,
        description=None,
        submitted=None,
        submitted_at=None,
        discussion_count=None,
        passed=None,
        passed_at=None,
        voting_from=None,
        voting_hours=None,
        words=[],
    ):
        self.name = name
        self.description = description
        self.submitted = submitted
        self.submitted_at = submitted_at
        self.discussion_count = discussion_count
        self.passed = passed
        self.passed_at = passed_at
        self.voting_from = voting_from
        self.voting_hours = voting_hours
        self.words = words
        self._len_words = len(words)

    def __len__(self):
        return self._len_words


class BatchSet:
    def __init__(
        self,
        *,
        count=0,
        batches=None,
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
