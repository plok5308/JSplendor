from abc import ABC, abstractmethod
from typing import List

class GameComponent(ABC):
    def __init__(self, name: str, development_cards: List, noble_cards: List, coins: List, verbose: bool) -> None:
        self.name = name
        self.development_cards = development_cards
        self.noble_cards = noble_cards
        self.coins = coins
        self.verbose = verbose

    @abstractmethod
    def print_status(self, object_name=None):
        pass

