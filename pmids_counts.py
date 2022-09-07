#!/usr/bin/env python3
'''
This script prepared agregate data on a set of PMID, summarizing how many papers were cited from each journal.
'''

import os
import sys
import argparse
import re
import tempfile
from time import sleep
import datetime
from datetime import timedelta
import numpy as np

def init():
    '''
    Initialization method to get command line parameters.
    '''
    parser = argparse.ArgumentParser(
        description='This script compares PMIDs.')

    parser.add_argument('-p', '--pmids', required=True,
                        help='input file.')
    parser.add_argument('-j', '--journals', required=True,
                        help='input file.')
    
    options = parser.parse_args()
    return options

if __name__ == '__main__':

    args = init()

    p2j = {}
    j2p = {}
    jtotal = {}

    with open(args.journals, 'r') as f:
        for line in f:
            # print(line)
            pmid, d1, d2, d3, journal = line.rstrip().split('\t')
            p2j[pmid] = journal


    # cat agile.pmids.csv | tr , '\n' | tr ';' '\n' | tr  ' ' '\n' | grep -vE "^$" | sort -n > agile.all.citations
    with open(args.pmids, 'r') as f:
        for line in f: 
            pmid = line.rstrip()
            journal = p2j[pmid]
            if journal not in jtotal:
                jtotal[journal] = 1
            else:
                jtotal[journal] += 1
            if journal not in j2p:
                j2p[journal] = {}
            if pmid not in j2p[journal]:
                j2p[journal][pmid] = 1
            else:
                j2p[journal][pmid] += 1
            
    for j in sorted(j2p):
        pcount = 0
        counts = []
        for p in j2p[j]:
            pcount += 1
            counts.append(int(j2p[j][p]))
        print('\t'.join([j, str(jtotal[j]), str(pcount), str(np.min(counts)), str(round(np.mean(counts), 4)), str(np.max(counts))]))
        # print(j, jtotal[j], pcount, counts)


    
