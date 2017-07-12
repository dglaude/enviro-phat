#!/usr/bin/env python

import sys
import time

from envirophat import light


def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()

write("--- Enviro pHAT Monitoring ---")

try:
    while True:
        rgb = light.rgb()

        output = """
Light: {c}
RGB: {r}, {g}, {b} 

""".format(
        c = light.light(),
        r = rgb[0],
        g = rgb[1],
        b = rgb[2]
    )
        output = output.replace("\n","\n\033[K")
        write(output)
        lines = len(output.split("\n"))
        write("\033[{}A".format(lines - 1))

        time.sleep(1)
        
except KeyboardInterrupt:
    pass
