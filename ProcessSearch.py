

import csv
import glob
import logging
import os

import pandas as pd
import time
import sys

from pathlib import Path



sourcePath =''
processPath =  ''
processFile = ''
destinationPath = ''
processlist = []
destfile = ''
ictr =0

nFound = 0
boolFoundProcess = 'F'
def main():

    iCtr = 0
    start = time.perf_counter()
    if not os.path.exists(processPath):
        smsg = "The path " + sourcePath + " does not exist"
        logging.error(smsg)
        print('not found')

    # Verify path exists and traverse using glob
    else:
        with open(processFile, 'r', encoding='utf-8') as f:
            infile = csv.reader(f)
            for lines in infile:
                nameProcess = lines[0]


                for file in Path(sourcePath).glob('tm1server*'):
                    #print(file)

                    fg = open(file, 'r', encoding='utf-8')
                    boolFoundProcess = 'F'
                    infiles = csv.reader(fg)
                    for line in infiles:
                        if(len(line) > 0):

                            nFound = line[0].find(nameProcess)



                            if(nFound != -1):
                                boolFoundProcess = 'Has Been Found'
                                print(nameProcess)
                                processlist.append([nameProcess, 'T'])

                                iCtr = 1
                                break
                            else:
                                iCtr = 0

                    if(iCtr == 1):
                        break






    if iCtr > 0:
        print(' Storing File...to', destfile, ' \n')
        process = pd.DataFrame(processlist)
        process.columns = ["Process Name", "Found"]
        process.to_csv(destfile, index=False)
    else:
        print("No Transactions Found\n")


if __name__ == '__main__':

    processFile = sys.argv[1]
    processPath = sys.argv[2]
    sourcePath = sys.argv[3]
    destinationPath = sys.argv[4]
    destfile = os.path.join(destinationPath, 'ProcessSearch.csv')
    main()