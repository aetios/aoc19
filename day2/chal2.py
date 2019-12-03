#!/usr/bin/env python3

import sys
sys.path.append('../')
import intcode_interpreter.interpret as intcode
init_mem = intcode.load(sys.argv[1])


for i in range(0,100):
    for j in range(0,100):
        pmem = init_mem[:]
        pmem[1] = i
        pmem[2] = j
        intcode.run(pmem)
        if pmem[0] == 19690720:
            print(100*i+j)
            sys.exit()
