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

def dna_to_rna_transcription(dnaString):
    return dnaString.replace('T', 'U')

def rna_to_protein_translation(rnaString):
    ''' Ex. 9: Translating RNA into Protein '''
    
    RNA_codon_table = {
        "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
        "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
        "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
        "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
        "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
        "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
        "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
        "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
        "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
        "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
        "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
        "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
        "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
        "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
        "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
        "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G", 
    }

    proteinString = ""
    codon = ""    
    for nuc in rnaString:
        codon += nuc
        
        if len(codon) == 3:
            protein = RNA_codon_table[codon]
            
            if protein == "Stop":
                break
            
            proteinString += RNA_codon_table[codon]
            codon = ""
            
    return proteinString

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

def combinations(alphabetString, wordlen):

    # "A B C" --> [ 'A', 'B', 'C',]
    alphabet = alphabetString.split(" ")

    result = []
    
    if wordlen == 2:
        for c1 in alphabet:
            for c2 in alphabet:
                result.append(f'{c1}{c2}')
    else:
        for c1 in alphabet:
            subwords = combinations(alphabetString, wordlen-1)
            for sw in subwords:
                result.append(f'{c1}{sw}')
    return result
