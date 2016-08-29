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

sourcefile = fileCommonDirectory / args.file
outfile = fileCommonDirectory / args.output

pyretRoot = "/pyret-lang/"

if args.debug:
    print("abs input file:", str(sourcefile))
    print("abs output file:", str(outfile))
    print("input file exists?", sourcefile.exists())
    print("output file exists?", outfile.exists())

call(["node", pyretRoot + "build/phase0/pyret.jarr",
      "--build-runnable", args.file,
      "--outfile", args.output,
      "--builtin-js-dir", pyretRoot + "src/js/trove/",
      "--builtin-arr-dir", pyretRoot + "src/arr/trove",
      "--require-config", pyretRoot + "src/scripts/standalone-configA.json"
      ])
