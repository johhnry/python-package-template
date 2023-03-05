from typing import Self


class Builder:
    def __init__(self, initial: str) -> None:
        self.content = initial

    def add(self, other: str) -> Self:
        self.content += " " + other
        return self

    def __str__(self) -> str:
        return self.content
