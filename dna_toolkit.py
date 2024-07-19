#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:25:11 2024

@author: vinzoni
"""

def gc_content(dnaString):
    count = 0;
    for nuc in dnaString.upper():
        if nuc == 'G':
            count +=1
        if nuc == 'C':
            count +=1

    return (count / len(dnaString)) * 100

def read_fast_file(filename):
    text = open(filename, "r").read().splitlines()
    genome_dict = {}
    for idx in range(0, len(text)-1, 2):
        (fast_id, data, score) = (text[idx][1:], text[idx+1], gc_content(text[idx+1]))
        genome_dict[fast_id] = (data, score)