#!/usr/bin/env python
# coding: utf-8
import os
import sys
import argparse
from pprint import pprint
from . import filter_trace, analysis


class CmdLine(object):

    @staticmethod
    def parse_args():

        parser = argparse.ArgumentParser(
            prog="cx10wd_ana",
            description="Analyzer for various SPI traces we dumped using Saleae board"
        )

        parser.add_argument("trace", type=str)
        parser.add_argument("transfer_len", type=int)

        return parser.parse_args()

    @classmethod
    def main(cls):
        args = cls.parse_args()
        trace_file = os.path.abspath(args.trace)
        transfer_len = int(args.transfer_len)

        data = filter_trace(trace_file)
        print "Analyzing..."
        analysis(data, transfer_len)
        print "Done"


def main():
    sys.exit(CmdLine.main())

if __name__ == '__main__':
    main()
