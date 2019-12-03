#!/usr/bin/env python3

def load(path):
    with open(path) as f:
        pmem = f.read().split(',') #program memory
        pmem = [int(i) for i in pmem]
    return pmem

def run(pmem):
    #------- the opcodes
    def nop(*args):
        pass

    def op_add(pmem, ip):
        # adds values pointed by [ip + 1], [ip + 2], stores in location [ip + 3]
        pmem[pmem[ip + 3]] = pmem[pmem[ip + 1]] + pmem[pmem[ip + 2]]
        return

    def op_mult(pmem, ip):
        # multiplies values pointed by [ip + 1], [ip + 2], stores in location [ip + 3]
        pmem[pmem[ip + 3]] = pmem[pmem[ip + 1]] * pmem[pmem[ip + 2]]
        return
    #-------------

    op = 0
    ip = 0 # instruction pointer

    ops=[nop, op_add, op_mult]

    while True:
        #read opcode at pc
        op = pmem[ip]
        if op == 99:
            break
        else:
            ops[op](pmem, ip)
        ip += 4 # likely to change. might be able to return this 
        
    return pmem
