#!/usr/bin/env python3
#input is path to file with mass numbers

import sys
import math
#read input file 

filepath = sys.argv[1]

with open(filepath) as f:
    mass_values = f.readlines()

total_fuel_req = 0

for mass in mass_values:
    total_fuel_req += (math.floor(int(mass)/3)-2)

print('the total fuel requirement is:' + str(total_fuel_req))
