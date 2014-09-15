#!/usr/bin/env python

'''sum_ifile.py: gets summary of an IFile'''

__author__ = 'Slamet Pramono'
__copyright__ = '(c)2014, PT Hero Supermarket Tbk'
__credits__ = ['Slamet Pramono', ]
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'Slamet Pramono'
__email__ = 'slamet_pramono@hero.co.id'
__status__ = 'Production'


import sys


def sum_ifile(filepath):
    '''open an ifile and load every loading number and po number into dictionary
    and also put the total qty of each PO number
    '''

    data = {}
    for line in file(filepath, 'r'):
        loadno = line[0:7]
        pono = line[18:45]
        qty = float(line[120:129].strip())

        if loadno not in data:
            data[loadno] = {}

        if pono not in data[loadno]:
            data[loadno][pono] = 0.0

        data[loadno][pono] += qty

    return data


def display_info(data):
    for loadno in data:
        print 'LOAD NO: {:s}'.format(loadno)
        totqty = 0
        totpo = 0

        for po in data[loadno]:
            qty = data[loadno][po]
            totqty += qty
            totpo += 1
            print '  PO NO: {:s} {:>13.3f}'.format(po, qty)

        print 'SUM ALL: {:d} PO\tTotal QTY: {:3.3f}'.format(totpo, totqty)

    print 'TOTAL PO IN FILE: {:d}'.format(totpo)


if __name__ == '__main__':
    for fl in sys.argv[1:]:
        display_info(sum_ifile(fl))
