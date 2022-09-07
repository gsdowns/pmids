#!/bin/bash
# This syntax is specific to the layout of the JSON files produced by Watson for Genomics
grep -iE “PubmedID|evidence|PMID”  ../TST15/TST15_Watson_DOWN_874/UHN-TST15-0*.json  | cut -f 3 -d : | tr -d '"' | sort -u > tst15.pmids
