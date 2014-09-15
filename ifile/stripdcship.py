#!/usr/bin/env python


"""stripdcship.py: extract only specified Loading Number from entire dscoship file"""

__author__ = "Slamet Pramono"
__copyright__ = "(c) 2014, PT Hero Supermarket Tbk"
__credits__ = ["Slamet Pramono", ]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Slamet Pramono"
__email__ = "slamet_pramono@hero.co.id"
__status__ = "Production"


import sys

if len(sys.argv) < 3:
    print 'usage: stripdcship [dcship.filename] [invoice_number]\n'
    sys.exit(-69)

filename = sys.argv[1]

invoice_nums = ['B' + x for x in sys.argv[2:]]

total_lines = {}

with file(filename, 'r') as f:
    with file(filename[:-4] + '_R' + '_'.join(sys.argv[2:]) + '.dscoship.dat', 'w') as w:
        should_write = False
        for ln in f.readlines():
            if len(ln) < 300:
                cur_inv = ln[85:94]
                if cur_inv in invoice_nums:
                    should_write = True
                else:
                    should_write = False

            if should_write:
                if cur_inv not in total_lines:
                    total_lines[cur_inv] = {}
                    total_lines[cur_inv]['lines'] = 0
                    total_lines[cur_inv]['qty'] = 0
                    total_lines[cur_inv]['po'] = 0

                #total_lines[cur_inv] = total_lines[cur_inv] + (0 if len(ln) < 300 else 1)
                if len(ln) > 300:
                    total_lines[cur_inv]['lines'] += 1
                    qty = float(ln[53:63]) / 100.0
                    total_lines[cur_inv]['qty'] += qty
                else:
                    total_lines[cur_inv]['po'] += 1


                w.write(ln)

for k in total_lines:
    print '{:s}: lines = {:d}, qty = {:5.2f}, po = {:d}'.format(
            k, total_lines[k]['lines'],total_lines[k]['qty'], total_lines[k]['po'])
