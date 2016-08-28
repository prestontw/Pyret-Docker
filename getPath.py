#!/usr/bin/env python3

import argparse
from pathlib import Path
from subprocess import call

parser = argparse.ArgumentParser(description='Compile a pyret program.')
parser.add_argument('file', type=str, help='input pyret file')
parser.add_argument('-o', '--output', dest='output', default='pyret.out', help='pyret output executable name')

args = parser.parse_args()

print("input file:", args.file)
print("output file:", args.output)

infile = Path(args.file)
infileAbsPath = infile.resolve()
print(infileAbsPath)
print(infileAbsPath.parent)

call(["node", "build/phas0/pyret.jarr",\
      "--build-runnable", infileAbsPath,\
      "--outfile", infileAbsPath.parent / args.output,\
      "--builtin-js-dir", "src/js/trove/",\
      "--builtin-arr-dir", "src/arr/trove",\
      "--require-config", "src/scripts/standalone-configA.json"\
      ])
