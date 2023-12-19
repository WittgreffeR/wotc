from typing import Any, Iterable

from .serialisers import file_to_list, line_to_dict, dict_to_class
from ...text_import import read_file


def read_file_as_list(relative_location: str) -> Iterable[str]:
    return file_to_list(read_file(relative_location))


def read_file_as_classes(relative_location: str, cls: Any) -> Iterable[Any]:
    output = []

    for line in read_file_as_list(relative_location):
        output.append(dict_to_class(line_to_dict(line), cls))
    
    return output
