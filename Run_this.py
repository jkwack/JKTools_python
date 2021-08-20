#!/usr/bin/python3
#
# Description: Read a CSV file using Read_CSV.py
#
#         written by JaeHyuk Kwack (jkwack@anl.gov)
#                    Performance Engineering Group
#                    Leadership Computing Facility
#                    Argonne National Laboratory
#                    (630) 252-6515, jkwack@anl.gov
# ------------------------------------------------------------------------------------------------------------------

# Importing Libraries
from __future__ import division
import os, sys, getopt
#from Read_CSV import myCSV

def get_args(argv):
  csvfile = ''
  if len(sys.argv) < 2:
    print ('Run_this.py -i <input csv file>')
    sys.exit(2)
  try:
    opts, args = getopt.getopt(argv,"hi:",["ifile="])
  except getopt.GetoptError:
    print ('Run_this.py -i <input csv file>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print ('Run_this.py -i <input csv file>')
      sys.exit()
    elif opt in ("-i", "--ifile"):
      csvfile = arg
  print ('Input CSV filename = ', csvfile)

if __name__ == "__main__":
  get_args(sys.argv[1:])


