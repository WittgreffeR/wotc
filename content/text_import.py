from os import path
from typing import TextIO


root = path.dirname(path.dirname(__file__)) #Where the main script is located - the wotc folder


def read_file(relative_location: str) -> str:
    with open(path.join(root,relative_location), "r") as file:
        return file.read()
