import argparse
from mri_lib.tumor_finder import TumorFinder


def main():
    parser = argparse.ArgumentParser(prog='find_tumor',
                                     description='Tumor search.')
    parser.add_argument('--inputfile', nargs=1, help='input file')
    args = parser.parse_args()

    t = TumorFinder(args.inputfile[0])
    print t.process_image()
    ##print t.dump_image()   ##  for testing

if __name__ == "__main__":
    main()
