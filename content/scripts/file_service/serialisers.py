from typing import Any, Iterable
from json import loads


def file_to_list(file: str) -> Iterable[str]:
    return file.split("\n")


def line_to_dict(line: str) -> "dict[str, Any]":
    return loads(line)


# Here using Values as a generic class for type hinting; cls can be any class
def dict_to_class(dict: dict, cls: Any) -> Any:    
    return cls(**dict)
