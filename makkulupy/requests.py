import orjson, requests

from .exceptions import BadResponseException, MalformedResponseException
from .models.batch import Batch, BatchSet
from .models.word import Word, WordSet


def _parse_word_set(objects):
    if not objects:
        return []
    results = []
    for word_object in objects:
        word = Word(
            headword=word_object.get("headword", None),
            pos=word_object.get("pos", None),
            cls=word_object.get("cls", None),
            definition=word_object.get("definition", None),
            etymology=word_object.get("etymology", None),
            notes=word_object.get("notes", None),
        )
        results.append(word)
    return results


def _parse_batch_set(objects):
    if not objects:
        return []
    results = []
    for batch_object in objects:
        batch = Batch(
            name=batch_object.get("name", None),
            description=batch_object.get("description", None),
            submitted=batch_object.get("submitted", None),
            submitted_at=batch_object.get("submitted_at", None),
            discussion_count=batch_object.get("discussion_count", None),
            passed=batch_object.get("passed", None),
            passed_at=batch_object.get("passed_at", None),
            voting_from=batch_object.get("voting_from", None),
            voting_hours=batch_object.get("voting_hours", None),
            words=_parse_word_set(batch_object.get("word_set", None)),
        )
        results.append(batch)
    return results


def get_words(*, search=None, headword=None, pos=None, cls=None, page=1):
    response = requests.get(
        "https://lang.kulupu.li/api/words/",
        params={
            "search": search,
            "headword": headword,
            "pos": pos,
            "cls": cls,
            "page": page,
        },
    )
    if not response.status_code == 200:
        return BadResponseException("The server responded with a non-OK response code.")
    try:
        object = orjson.loads(response.content)
    except orjson.JSONDecodeError as ex:
        raise MalformedResponseException from ex
    return WordSet(
        count=object.get("count", 0),
        words=_parse_word_set(object.get("results", None)),
    )


def get_batches(*, search=None, name=None, passed=None):
    response = requests.get(
        "https://lang.kulupu.li/api/batches/",
        params={
            "search": search,
            "name": name,
            "passed": passed,
        },
    )
    if not response.status_code == 200:
        return BadResponseException("The server responded with a non-OK response code.")
    try:
        object = orjson.loads(response.content)
    except orjson.JSONDecodeError as ex:
        raise MalformedResponseException from ex
    return BatchSet(
        count=object.get("count", 0),
        batches=_parse_batch_set(object.get("results", None)),
    )
