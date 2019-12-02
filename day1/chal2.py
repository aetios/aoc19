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
    fuel_req_this_module = (math.floor(int(mass)/3)-2)
    
    total_fuel_weight = fuel_req_this_module
    
    
    while fuel_req_this_module >= 0:
        fuel_req_this_module = (math.floor(fuel_req_this_module/3)-2)
        if fuel_req_this_module <= 0:
            break
        total_fuel_weight += fuel_req_this_module

    total_fuel_req += total_fuel_weight





print('the total fuel requirement is:' + str(total_fuel_req))
