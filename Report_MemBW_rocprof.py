#!/usr/bin/python3

#
# Description: Read a CSV file from rocprof and then report memory bandwidth for kernels
#
# Bug reports & feature requests: Please reach out to JaeHyuk Kwack (jkwack@anl.gov)
#

# Importing Libraries
from __future__ import division
import os, sys, getopt
import csv

def get_args(argv):
    if len(sys.argv) < 2:
        print ('Report_MemBW_rocprof.py -i <input csv file>')
        sys.exit(2)
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print ('Report_MemBW_rocprof.py -i <input csv file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('Report_MemBW_rocprof.py -i <input csv file>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            csvfilename = arg
    print ('Input CSV filename = {0}\n '.format(csvfilename))
    return csvfilename

if __name__ == "__main__":
    csvfilename = get_args(sys.argv[1:])
    with open(csvfilename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        FetchSize = { }
        WriteSize = { }
        TimeDurationNs = { }  
        for row in reader:
            if row['KernelName'] in FetchSize:
                FetchSize[ row['KernelName'] ]  += int(row['FetchSize'])
                WriteSize[ row['KernelName'] ]  += int(row['WriteSize'])
                TimeDurationNs[ row['KernelName'] ]  += int(row['EndNs'])-int(row['BeginNs'])
            else:
                FetchSize[ row['KernelName'] ]  = int(row['FetchSize'])
                WriteSize[ row['KernelName'] ]  = int(row['WriteSize'])
                TimeDurationNs[ row['KernelName'] ]  = int(row['EndNs'])-int(row['BeginNs'])
        MemBWinGBs = { }
        for kernel in FetchSize:
            MemBWinGBs[kernel] = ( FetchSize[kernel] + WriteSize[kernel] ) / TimeDurationNs[kernel] * 1024
        # Print out the accumulated data per kernel
        for kernel in MemBWinGBs:
            print('Kernel name: {0}\n ---------- Memory Bandwidth (GB/s): {1}\n'.format(kernel,MemBWinGBs[kernel]))


