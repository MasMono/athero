#!/c/python27/python.exe

"""storinfo.py: Find Store Description from TS Database"""

__author__ = "Slamet Pramono"
__copyright__ = "(c) 2014, PT Hero Supermarket Tbk"
__credits__ = ["Slamet Pramono", ]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Slamet Pramono"
__email__ = "slamet_pramono@hero.co.id"
__status__ = "Production"


import pymssql
import sys
import re


def find_storinfo(store_name):
    con = pymssql.connect('rose', 'devteam', '2011-r05e', 'POM')
    cur = con.cursor()


    sql = '''
        select store_code, store_shortdesc, store_longdesc
        from store
        where is_store = 1
    '''

    if re.match('[0-9]+', store_name):
        sql = sql + ' and store_code = %s '
        cur.execute(sql, (store_name))
    else:
        sql = sql + ' and (store_longdesc like %s or store_shortdesc=%s) '
        cur.execute(sql, ('%{:s}%'.format(store_name),
            '{:s}'.format(store_name.upper().strip())))

    for row in cur.fetchall():
        print ('{:s}\t{:s}\t{:s}'.format(row[0], row[1], row[2]))


def show_help():
    print 'usage: storinfo.py store_name'


if __name__ == '__main__':
    if len(sys.argv) < 2:
        show_help()
        sys.exit(-69)

    store_name = '%'.join(sys.argv[1:])
    print 'finding {:s}\n'.format(store_name)
    find_storinfo(store_name)
