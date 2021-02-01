# User-facing CLI

import sys
import argparse

from football import Season


def main():
    rawdatafile_help = 'a file containing a season\'s match results'

    parser = argparse.ArgumentParser(description='Analyze a season\'s worth of premier league results')
    parser.add_argument('rawdatafile', help=rawdatafile_help)

    namespace = parser.parse_args()

    season = Season.Season(namespace.rawdatafile)
    print('- A Premier League season\'s data -\n')
    print('Team with the lowest goal differential:')
    print(season.getmingoaldiffteam())


if __name__ == '__main__':
    sys.exit(main())
