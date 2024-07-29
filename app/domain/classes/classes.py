from domain.classes.base import BaseCharClass

ASSASSIN_HP_MODIF = 0.25
ADVENTURER_ATK_MODIF = 0.5
CRAFTSMAN_DEF_MODIF = 1


class Frog(BaseCharClass):
    def __init__(self, frog: BaseCharClass = None):
        super().__init__()
        if frog is not None:
            self.stats = frog.stats

    def set_hp(self, new_hp: int) -> None:
        self.stats['health'] = new_hp

    def get_atk(self) -> int:
        return self.stats['attack']

    def get_def(self) -> int:
        return self.stats['defence']

    def get_hp(self) -> int:
        return self.stats['health']


class Assassin(BaseCharClass):
    def __init__(self, frog: BaseCharClass):
        self.stats = frog.stats
        self.extra_hp = 0

    def set_hp(self, new_hp: int) -> None:
        self.stats['health'] = new_hp // (1 + ASSASSIN_HP_MODIF)
        self.extra_hp = new_hp % (1 + ASSASSIN_HP_MODIF)

    def get_atk(self) -> int:
        return self.stats['attack']

    def get_def(self) -> int:
        return self.stats['defence']

    def get_hp(self) -> int:
        return round(self.stats['health'] *
                     (1 + ASSASSIN_HP_MODIF) +
                     self.extra_hp)


class Adventurer(BaseCharClass):
    def __init__(self, frog: BaseCharClass):
        self.stats = frog.stats

    def set_hp(self, new_hp: int) -> None:
        self.stats['health'] = new_hp

    def get_atk(self) -> int:
        return round(self.stats['attack'] * (1 + ADVENTURER_ATK_MODIF))

    def get_def(self) -> int:
        return self.stats['defence']

    def get_hp(self) -> int:
        return self.stats['health']


class Craftsman(BaseCharClass):
    def __init__(self, frog: BaseCharClass):
        self.stats = frog.stats

    def set_hp(self, new_hp: int) -> None:
        self.stats['health'] = new_hp

    def get_atk(self) -> int:
        return self.stats['attack']

    def get_def(self) -> int:
        return round(self.stats['defence'] * (1 + CRAFTSMAN_DEF_MODIF))

    def get_hp(self) -> int:
        return self.stats['health']
