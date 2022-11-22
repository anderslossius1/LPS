#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:47:06 2022


@author: alossius
"""

import time

def takeinput(): return input("Type here: ")

def playLPS(numSec):
    time.sleep(0.5)
    print('\n-------------- WELCOME TO THE LPS --------------\n')
    time.sleep(1.2)
    print('Please ensure your seatbelts are securely fashioned!\n')
    time.sleep(1.4)
    print('Ready...\n')
    time.sleep(1)
    print('Set...\n')
    time.sleep(1)
    print('GO !! \n\n')
    t_end = time.time() + numSec
    lps = 0
    while time.time() < t_end:
        t = takeinput()
        if t == 'lug':
            lps += 1 
    output = "Your LPS is: " + str(lps/numSec)
    print(lps, numSec)

    return output







