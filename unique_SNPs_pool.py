#!/usr/bin/env python
import sys

mut_file = open(sys.argv[1], 'r')
wt_file = open(sys.argv[2], 'r')


mut = []
mut_set =set()
for line in mut_file:
    mut = line.strip().split('\t')
    if line.startswith('#'):
        pass
    else:
        temp_tuple = (mut[0],mut[1])
        #print temp_tuple
        mut_set.add(temp_tuple)
        #print DTY22_set

wt = []
wt_set =set()
for line in wt_file:
    wt = line.strip().split('\t')
    if line.startswith('#'):
        pass
    else:
        temp_tuple = (wt[0],wt[1])
        wt_set.add(temp_tuple)
        #print DTY47_set


unique_snps = mut_set.difference(wt_set)
print unique_snps



open(sys.argv[3]+'.txt', 'w').write('\n'.join('%s''\t''%s' % x for x in unique_snps))



