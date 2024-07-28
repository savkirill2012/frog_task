from abc import ABC, abstractmethod

BASE_FROG_ATK = 15
BASE_FROG_HP = 150
BASE_FROG_DEF = 5


class BaseCharClass(ABC):
    def __init__(self) -> None:
        self.stats = {
            'attack': BASE_FROG_ATK,
            'defence': BASE_FROG_DEF,
            'health': BASE_FROG_HP
        }

    @abstractmethod
    def set_hp(self, new_hp: int) -> None:
        pass

    @abstractmethod
    def get_atk(self) -> int:
        pass

    @abstractmethod
    def get_def(self) -> int:
        pass

    @abstractmethod
    def get_hp(self) -> int:
        pass
