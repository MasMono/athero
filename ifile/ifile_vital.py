#!/c/Python27/python.exe

import zipfile
import glob
import os
import shutil
import sys


def find_ifile(store_skt, load_num):
    zip_path = os.path.join(r'z:/', store_skt, r'transfer', r'bos')
    zip_archive = os.path.join(zip_path, 'archive')

    for fname in glob.glob(os.path.join(zip_path, '*I*.ZIP')):
        print 'checking file: {:s}'.format(fname)
        find_loadnum(fname, store_skt, load_num)

    for fname in glob.glob(os.path.join(zip_archive, '*I*.ZIP')):
        print 'checking file: {:s}'.format(fname)
        find_loadnum(fname, store_skt, load_num)


def find_loadnum(zipfile_name, store_skt, load_num):
    copy_file = False
    with zipfile.ZipFile(zipfile_name) as z:
        for num in load_num:
            ifile_name = 'I{:s}.{:s}'.format(num, store_skt)
            if ifile_name.upper() in z.namelist():
                copy_file = True

    if copy_file:
        shutil.copy(zipfile_name, 'ifile/')


if __name__ == '__main__':
    if sys.argv.count<2:
        print 'usage: python find_ifile skt load_num'
        sys.exit()

    store, load_num = sys.argv[1], sys.argv[2:]
    print 'finding ifile for {:s} with load number: {:s}'.format(store, load_num)
    find_ifile(store, load_num)

