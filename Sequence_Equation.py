#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@author: paco
"""
def permutationEquation(p):
    # OBTENGO LOS INDICES DE LOS VALORES ASCENDENTES EN P,
    # ES DECIR, BUSCO PRIMERO EL INDICE DE "1" EN P, LUEGO
    # BUSCO EL INDICE DE "2" EN P, Y ASI SUCESIVAMENTE.
    gen = [p.index(i) + 1 for i in range(1,len(p) + 1)]
    # CONSTRUYO OTRO GENERADOR, POR CADA ELEMENTO EN GEN
    # BUSCO EL INDICE DEL ELEMENTO EN GEN PERO EN P, ES 
    # DECIR, BUSCO EL INDICE DEL PRIMER ELEMENTO DE GEN
    # EN P
    gen_ = [p.index(i) + 1 for i in gen]
    print(gen_)
    return

p=[2, 3, 1]
permutationEquation(p)
p=[4, 3, 5, 1, 2]
permutationEquation(p)



