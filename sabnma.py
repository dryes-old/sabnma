#!/usr/bin/python2

## argv[n] - all passed as strings.
## 1	The final directory of the job (full path)
## 2	The original name of the NZB file
## 3	Clean version of the job name (no path info and ".nzb" removed)
## 4	Indexer's report number (if supported)
## 5	User-defined category
## 6	Group that the NZB was posted in e.g. alt.binaries.x
## 7	Status of post processing. 0 = OK, 1=failed verification, 2=failed unpack, 3=1+21

from pynma import PyNMA
from pprint import pprint
import os,sys

def main(argv, apikey):
    p = PyNMA()
    p.addkey(apikey)

    message = argv[3] + ' [' + argv[5] + ']'
   
    status = ''
    if argv[7] == '0':
    	status = 'Complete'
    elif argv[7] == '1':
    	status = 'Failed Verification'
    elif argv[7] == '2':
    	status = 'Failed Unpack'
    elif argv[7] == '3':
       	status = 'Failed Unpack + Verification'
    else:
    	status = 'Failed'
    
    res = p.push('SABnzbd+', message, status)
    pprint(res)
    
if __name__ == '__main__':
	## https://www.notifymyandroid.com/account.jsp
	apikey = 'setme - retain quotes'
	main(sys.argv, apikey)
