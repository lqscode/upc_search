#!/usr/bin/python

import csv
import re
import string

upclist = {}
#boxidlist = []
orderlist = []

cnt = 0
with open('ifd.csv','r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        upc = row[0].replace('"','').lstrip('0')
        boxid = row[2]
        #print("UPC: " + upc + " INSIDE " + "BOXID: " + boxid)
        if upc in upclist:
            upclist[upc].append(boxid)
            
        else:
            upclist[upc] = [boxid]
            
        #boxidlist.append(boxid)
        #cnt+=1

#print upclist    
#cnt = 0            
with open('orders-small.txt', 'r') as o:
    for line in o:
        upc = line.split('-',1)[0].replace('"', '').lstrip('0').strip()
        try:
            upc1 = line.split('-',1)[1].replace('"', '').lstrip('0').strip()
        except:
            upc1 = None
        #upc = line.replace('"', '').lstrip('0')
        #print upc
        #print 'UPC:' + upc
        
        #try:
        #    upc = [long(s) for s in upc.split('-') if s.isdigit()][0]
        #except:   
        #    upc = line.replace('"', '')  
        
        if upc in upclist:
            
            print(upc + " : BOX " + str(set(upclist[upc]))).replace('set(','').replace(')','')

        elif upc1 in upclist:
            print(upc1 + " : BOX " + str(set(upclist[upc1]))).replace('set(','').replace(')','')

