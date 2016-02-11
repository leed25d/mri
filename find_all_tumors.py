import argparse
import os
import re
import sys
sys.setrecursionlimit(10000)

from mri_lib.tumor_finder import TumorFinder


def main():
    parser = argparse.ArgumentParser(prog='find_tumor',
                                     description='Tumor search.')
    parser.add_argument('--inputdir', nargs=1, help='input directory')
    parser.add_argument('--outputfile', nargs=1, help='output (csv) file')
    args = parser.parse_args()
    with open(args.outputfile[0], 'w') as csv_out:
        csv_out.write("Filename,Has Tumor,Rows,Columns\n")
        dir_path = args.inputdir[0]
        for in_file in os.listdir(dir_path):
            if not re.search(r'\.in$', in_file):
                continue
            fullpath = "%s/%s" % (dir_path, in_file)
            line = "%s,%s\n" % (in_file, TumorFinder(fullpath).process_image())
            csv_out.write(line)

if __name__ == "__main__":
    main()
