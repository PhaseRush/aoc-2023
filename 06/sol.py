import math
import time
from typing import List

from tqdm import tqdm

with open('input.txt') as f:
    lines = f.read().splitlines()
    race = (61709066, 643118413621041)

    ways = []

    total_time = int(race[0])
    record_dist = int(race[1])

    curr_ways = 0

    start = time.process_time_ns()
    for charge_time in range(total_time):
        move_time = total_time - charge_time
        speed = charge_time
        dist = speed * move_time
        if dist > record_dist:
            curr_ways += 1

    print((time.process_time_ns() - start)/10e6, " ms")

    print(curr_ways)