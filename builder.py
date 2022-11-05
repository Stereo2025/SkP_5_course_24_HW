from typing import Optional, Iterable, List, Union

from functions import filter_query, map_query, unique_query, sorted_query, limit_query, regex_query

FILE_NAME = 'data/apache_logs.txt'
CMD_TO_FUNCTIONS: dict = {
    'filter': filter_query, 'map': map_query, 'unique': unique_query,
    'sort': sorted_query, 'limit': limit_query, 'regex': regex_query
}


def iter_file(file_name: str) -> Iterable[str]:
    """Генератор для чтения логов"""

    with open(file_name) as file:
        for row in file:
            yield row


def query_builder(cmd: str, value: Union[str, int], data: Optional[Iterable[str]]) -> List:

    if data is None:
        prepared_data = iter_file(FILE_NAME)
    else:
        prepared_data = data
    result = CMD_TO_FUNCTIONS[cmd](param=value, data=prepared_data)
    return list(result)
