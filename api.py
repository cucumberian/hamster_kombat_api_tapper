import os
import random
import time
import sys

import requests

from schema.tap import Tap
from schema.tap_response import TapResponse

tap_url = "https://api.hamsterkombatgame.io/clicker/tap"

bearer = os.environ["HAMSTER_AUTH_TOKEN"]

count = int(sys.argv[1]) if (len(sys.argv) > 1) else 1


def make_tap(count: int, availableTaps: int, bearer: str):
    header = {"Authorization": f"Bearer {bearer}"}
    tap = Tap(count=count, availableTaps=availableTaps)
    response = requests.post(tap_url, headers=header, json=tap.model_dump())
    json = response.json()
    tap_response = TapResponse.model_validate(json)
    return tap_response


taps_to_make = count or random.randint(1, 10)
print(f"Making {taps_to_make} taps")
tap_response = make_tap(
    count=taps_to_make,
    availableTaps=random.randint(0, 5),
    bearer=bearer,
)
print(tap_response)

total_coins = tap_response.clickerUser.totalCoins
balance_coins = tap_response.clickerUser.balanceCoins
available_taps = tap_response.clickerUser.availableTaps
max_taps = tap_response.clickerUser.maxTaps
earn_per_tap = tap_response.clickerUser.earnPerTap


i = 0
while True:
    time.sleep(1)
    available_taps += 3
    taps_to_tap = available_taps // earn_per_tap
    taps_count = random.randint(0, taps_to_tap)
    tap_response = make_tap(
        count=taps_count,
        availableTaps=available_taps - taps_count * earn_per_tap,
        bearer=bearer,
    )
    total_coins = tap_response.clickerUser.totalCoins
    balance_coins = tap_response.clickerUser.balanceCoins
    available_taps = tap_response.clickerUser.availableTaps
    earn_per_tap = tap_response.clickerUser.earnPerTap
    max_taps = tap_response.clickerUser.maxTaps

    if not (i % 10):
        print(f"B: {int(balance_coins)} | E: {available_taps} / {max_taps}")
        i = 0
    i += 1
