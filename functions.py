import re
from typing import Generator, Iterable, List, Union


def filter_query(param: str, data: Union[Generator, List[str]]):
    return filter(lambda x: param in x, data)


def map_query(param: str, data: Iterable[str]):
    return map(lambda x: x.split(' ')[int(param)], data)


def unique_query(data: Iterable[str], *args, **kwargs):
    return set(data)


def sorted_query(param: str, data: Iterable[str]):
    return sorted(data, reverse=param == 'desc')


def limit_query(param: str, data: Iterable[str]):
    return list(data)[:int(param)]


def regex_query(param: str, data: Iterable[str]):
    return filter(lambda row: re.compile(rf'{str(param)}').search(row), data)
