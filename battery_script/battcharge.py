#!/usr/bin/env python
# coding=UTF-8

import math, subprocess, sys, os

battCommand= "acpi -b"
p = subprocess.Popen(battCommand.split(), stdout=subprocess.PIPE)
output = p.communicate()[0]

str = output.decode("utf-8")
charge = int(str[str.find(",")+2:str.find('%')])

#o_max = [l for l in output.splitlines() if 'MaxCapacity' in l][0]
#o_cur = [l for l in output.splitlines() if 'CurrentCapacity' in l][0]

#b_max = float(o_max.rpartition('=')[-1].strip())
#b_cur = float(o_cur.rpartition('=')[-1].strip())

#charge_threshold = int(math.ceil(10 * charge))

# Output

total_slots, slots = 10, []
filled = int(math.ceil(charge / 10.0)) * u'▸'
empty = (total_slots - len(filled)) * u'▹'

out = (filled + empty).encode('utf-8')

GRAY="\[\033[1;30m\]"
LIGHT_GRAY="\[\033[0;37m\]"
YELLOW="\033[1;33m"
LIGHT_CYAN="\[\033[1;36m\]"
NO_COLOUR="\[\033[0m\]"

color_green = "%{\033[1;32m%}"
#color_yellow = "%{$fg_no_bold[yellow]%}"
color_yellow = "%{\033[1;33m%}"
color_red = "%{\033[1;31m%}"
color_reset = "%{\033[0m%}"
color_out = (
    color_green if len(filled) > 6
    else color_yellow if len(filled) > 4
    else color_red
)

out = color_out + out.decode('utf-8') + color_reset
#out = CYAN + out.decode('utf-8') + color_reset
sys.stdout.write(out)
