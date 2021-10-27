#!/usr/bin/env python3
import csv
import argparse


def main():
    parser = argparse.ArgumentParser(prog='CSV Generator', description='Generates template CSV\'s for ftuv2 training sets.')
    parser.add_argument('-o', '--output',
                        dest='output',
                        type=str,
                        default='./data.csv',
                        help='Output CSV file.')
    parser.add_argument('rows',
                        type=int,
                        help='Number of rows to create.')
    args = parser.parse_args()

    with open(args.output, 'w+') as file:
    	writer = csv.writer(file)

    	writer.writerow(['frame-number', 'mode'])
    	for i in range(0, args.rows + 1):
    		writer.writerow([str(i), ''])

if __name__ == '__main__':
    main()
