from dataclasses import dataclass

@dataclass
class Volume:
    name: str


@dataclass
class Weight:
    name: str


class Measures:
    volumes = []
    weights = []


@dataclass
class Recipe:
    ...