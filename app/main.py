from domain.events.battle import battle100Times
import asyncio


def main():
    return asyncio.run(battle100Times())


if __name__ == '__main__':
    win_stat = main()
    print(f'first frog wins: {win_stat[0]}/100')
    print(f'second frog wins: {win_stat[1]}/100')
