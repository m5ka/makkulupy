from unittest.mock import patch
from ward import raises, test

from .. import (
    BadResponseException,
    get_words,
    MalformedResponseException,
    Word,
    WordSet,
)


@test("raises exception on api error")
def _():
    with patch("makkulupy.requests.requests") as mock:
        mock.status_code = 500
        mock.get.return_value = mock
        with raises(BadResponseException):
            get_words()


@test("raises exception on malformed api response")
def _():
    with patch("makkulupy.requests.requests") as mock:
        mock.status_code = 200
        mock.content = "skjh3hr@32n//jr9heswjhlbf.287g2r"
        mock.get.return_value = mock
        with raises(MalformedResponseException):
            get_words()


@test("correctly parses word set")
def _():
    with patch("makkulupy.requests.requests") as mock:
        mock.status_code = 200
        mock.content = (
            '{"count": 3, "next": null, "previous": null, "results": ['
            '{"id": 1, "headword": "jan", "slug": "jan", "pos": "verb", '
            '"cls": "", "definition": "person", "etymology": "chinese", '
            '"notes": "a good word", "url": "https://example.com/word/1/"}, '
            '{"id": 2, "headword": "ona", "slug": "ona", "pos": "noun", '
            '"cls": "ikulu", "definition": "she", "etymology": "polish", '
            '"notes": "", "url": "https://example.com/word/2/"}, {"id": 3, '
            '"headword": "lon", "slug": "lon", "pos": "particle", "cls": "", '
            '"definition": "at, on", "etymology": "", "notes": "a note", '
            '"url": "https://example.com/word/3/"}]}'
        )
        mock.get.return_value = mock
        results = get_words(limit=3)
        mock.get.assert_called_with(
            "https://lang.kulupu.li/api/words/", params={"limit": 3}
        )
        assert type(results) == WordSet
        assert len(results) == 3
        assert type(results[0]) == Word
        assert type(results[0].id) == int
        assert results[0].id == 1
        assert results[0].headword == "jan"
        assert results[0].slug == "jan"
        assert results[0].pos == "verb"
        assert results[0].cls == None
        assert results[0].definition == "person"
        assert results[0].etymology == "chinese"
        assert results[0].notes == "a good word"
        assert results[0].url == "https://example.com/word/1/"
        assert type(results[1]) == Word
        assert type(results[1].id) == int
        assert results[1].id == 2
        assert results[1].headword == "ona"
        assert results[1].notes == None
        assert type(results[2]) == Word
        assert type(results[2].id) == int
        assert results[2].id == 3
        assert results[2].headword == "lon"
