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

    lines = open(filename, "r").read().splitlines()
    genome_dict = {}
    current_id = ""
    current_genome = ""
    for l in lines:
        if l[0] == ">":
            if len(current_genome) > 0:
                (fast_id, data) = (current_id, current_genome)
                genome_dict[fast_id] = data
            current_id = l[1:]
            current_genome = ""
        else:
            current_genome += l
    (fast_id, data) = (current_id, current_genome)
    genome_dict[fast_id] = data
    
    return genome_dict
