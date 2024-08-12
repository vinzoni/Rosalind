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

def reverse_complement(dnaString):
    ''' Ex. 3: Complementing a strand of DNA and Reverting '''
    reverseDNAString = dnaString[::-1]
    complementDNA = []
    for nuc in reverseDNAString:
        if nuc == 'A':
            complementDNA.append('T')
        elif nuc == 'T':
            complementDNA.append('A')
        elif nuc == 'C':
            complementDNA.append('G')
        elif nuc == 'G':
            complementDNA.append('C')
    return ''.join(complementDNA)

def finding_motifs_locations(dnaString, motif):
    ''' Ex. 10: Finding a Motif in DNA '''
    locations = []
    
    for i in range(len(dnaString)-len(motif)):
        if dnaString[i:i+len(motif)] == motif:
            locations.append(i+1)
            
    return locations

def read_fast_file(filename):

    with open(filename, "r") as f:
        lines = f.read().splitlines()
        
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

def permutations(dataset):

    result = []
    if len(dataset) == 2:
        result.append(dataset)
        result.append(dataset[::-1])
    else:
        for d in dataset:
            perms = []
            prefix = [d]
            suffix = [x for x in dataset]
            suffix.remove(d)
            perms += permutations(suffix)
            for p in perms:
                result.append(prefix + p)
    return result
