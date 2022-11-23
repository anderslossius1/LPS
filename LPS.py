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
    startTime = time.time()
    lps = 0
    IN = takeinput()
    endTime = time.time()
    lugs = 0
    # pase data and count number of valid strings "lug "
    for i in range(len(IN)-3):
        if IN[i:i+4] == 'lug ':
            lugs += 1
    lps = lugs/(endTime-startTime)
    output = "Your LPS is: " + str(lps/numSec)
    print(lps, numSec)

    return output


playLPS(1000)
