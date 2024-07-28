import random
import asyncio
from domain.classes.classes import Frog, Assassin, Adventurer, Craftsman
from enum import IntEnum


class ResultOfButtle(IntEnum):
    LOSE = 0,
    WIN = 1


def __deal_damage_oponent(frog: Frog, oponent: Frog) -> None:
    frog_atk = frog.get_atk()
    dmg = random.randint(round(frog_atk / 2), frog_atk)
    resist = random.randint(0, oponent.get_def())

    if dmg - resist > 0:
        oponent.set_hp(oponent.get_hp() - (dmg - resist))
        return 1

    return 0


async def battleTwoFrogs(frog: Frog, oponent: Frog) -> int:
    while frog.get_hp() > 0 and oponent.get_hp() > 0:
        __deal_damage_oponent(frog, oponent)
        __deal_damage_oponent(oponent, frog)

    # imitation of server connection for update
    await asyncio.sleep(0.001)

    if frog.get_hp() <= 0:
        return ResultOfButtle.WIN
    else:
        return ResultOfButtle.LOSE


async def battle100Times():
    totle_wins_first_frog = 0

    for _ in range(100):
        frog1 = Frog()
        frog2 = Frog()
        Class1 = random.choice([Adventurer, Assassin, Craftsman])
        Class2 = random.choice([Adventurer, Assassin, Craftsman])
        totle_wins_first_frog += await battleTwoFrogs(Class1(frog1),
                                                      Class2(frog2))

    return [totle_wins_first_frog, 100 - totle_wins_first_frog]
