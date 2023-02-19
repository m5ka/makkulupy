from typing import Any, Dict, List, Union
import orjson
import requests
from dateutil import parser
from datetime import datetime

from .exceptions import BadResponseException, MalformedResponseException
from .models.batch import Batch, BatchSet
from .models.word import Word, WordSet


def _parse_int(object: Union[int, str, None]) -> Union[int, None]:
    """
    Returns an int if the object is an int or string.
    Otherwise returns None.
    """
    if object == None:
        return None
    if type(object) == int:
        return object
    if type(object) == str:
        return int(object)
    return None


def _parse_date(object: Union[str, None]) -> Union[datetime, None]:
    """
    Returns a parsed datetime if the object is a string.
    Otherwise returns None.
    """
    if object and type(object) == str:
        return parser.parse(object)
    return None


def _parse_string(object: Union[str, None]) -> Union[str, None]:
    """
    Returns the given object if it is a non-empty string.
    Otherwise returns None.
    """
    if object and type(object) == str and len(object):
        return object
    return None


def _parse_word_set(objects: List[Any]) -> List[Word]:
    """
    Returns a list of Word objects from a list of
    dictionaries containing word data.
    """
    if not objects:
        return []
    results = []
    for word_object in objects:
        word = Word(
            id=_parse_int(word_object.get("id", None)),
            headword=_parse_string(word_object.get("headword", None)),
            slug=_parse_string(word_object.get("slug", None)),
            pos=_parse_string(word_object.get("pos", None)),
            cls=_parse_string(word_object.get("cls", None)),
            definition=_parse_string(word_object.get("definition", None)),
            etymology=_parse_string(word_object.get("etymology", None)),
            notes=_parse_string(word_object.get("notes", None)),
            url=_parse_string(word_object.get("url", None)),
        )
        results.append(word)
    return results


def _parse_batch_set(objects: List[Any]) -> List[Batch]:
    """
    Returns a list of Batch objects from a list of
    dictionaries containing batch data.
    """
    if not objects:
        return []
    results = []
    for batch_object in objects:
        batch = Batch(
            id=_parse_int(batch_object.get("id", None)),
            name=_parse_string(batch_object.get("name", None)),
            description=_parse_string(batch_object.get("description", None)),
            submitted=_parse_string(batch_object.get("submitted", None)),
            submitted_at=_parse_date(batch_object.get("submitted_at", None)),
            discussion_count=_parse_int(batch_object.get("discussion_count", None)),
            passed=_parse_string(batch_object.get("passed", None)),
            passed_at=_parse_date(batch_object.get("passed_at", None)),
            voting_from=_parse_date(batch_object.get("voting_from", None)),
            voting_hours=_parse_int(batch_object.get("voting_hours", None)),
            url=_parse_string(batch_object.get("url", None)),
            words=_parse_word_set(batch_object.get("word_set", None)),
        )
        results.append(batch)
    return results


def get_words(**params: Dict[str, Any]) -> WordSet:
    """
    Returns a WordSet from the makkulu API based on a
    dictionary of parameters sent to the API.
    """
    response = requests.get("https://lang.kulupu.li/api/words/", params=params)
    if not response.status_code == 200:
        raise BadResponseException("The server responded with a non-OK response code.")
    try:
        object = orjson.loads(response.content)
    except orjson.JSONDecodeError as ex:
        raise MalformedResponseException from ex
    return WordSet(
        count=_parse_int(object.get("count", 0)),
        words=_parse_word_set(object.get("results", None)),
    )


def get_batches(**params: Dict[str, Any]) -> BatchSet:
    """
    Returns a BatchSet from the makkulu API based on a
    dictionary of parameters sent to the API.
    """
    response = requests.get("https://lang.kulupu.li/api/batches/", params=params)
    if not response.status_code == 200:
        raise BadResponseException("The server responded with a non-OK response code.")
    try:
        object = orjson.loads(response.content)
    except orjson.JSONDecodeError as ex:
        raise MalformedResponseException from ex
    return BatchSet(
        count=_parse_int(object.get("count", 0)),
        batches=_parse_batch_set(object.get("results", None)),
    )
