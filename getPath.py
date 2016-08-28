#!/usr/bin/env python3

import argparse
from pathlib import Path
from subprocess import call

parser = argparse.ArgumentParser(description='Compile a pyret program.')
parser.add_argument('file', type=str, help='input pyret file')
parser.add_argument('-o', '--output', dest='output', default='pyret.out', help='pyret output executable name')
parser.add_argument('--debug', action="store_true", help='debug compiling script')

args = parser.parse_args()

if args.debug:
    print("input file:", args.file)
    print("output file:", args.output)

infile = Path(args.file)
infileAbsPath = infile.resolve()
fileCommonDirectory = infileAbsPath.parent

infileStr = str(fileCommonDirectory / args.file)
outfileStr = str(fileCommonDirectory / args.output)

if args.debug:
    print("abs input file:", infileStr)
    print("abs output file:", outfileStr)

call(["node", "build/phase0/pyret.jarr",\
      "--build-runnable", str(fileCommonDirectory / args.file),\
      "--outfile", str(fileCommonDirectory / args.output),\
      "--builtin-js-dir", "src/js/trove/",\
      "--builtin-arr-dir", "src/arr/trove",\
      "--require-config", "src/scripts/standalone-configA.json"\
      ])
