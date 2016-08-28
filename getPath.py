import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Compile a pyret program.')
parser.add_argument('file', type=str, help='input pyret file')
parser.add_argument('-o', '--output', dest='output', default='pyret.out', help='pyret output executable name')

args = parser.parse_args()

print("input file:", args.file)
print("output file:", args.output)

infile = Path(args.file)
print(infile.resolve())
