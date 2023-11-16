#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
#
# © Copyright 2023 GSI Helmholtzzentrum für Schwerionenforschung
#
# This software is distributed under
# the terms of the GNU General Public Licence version 3 (GPL Version 3),
# copied verbatim in the file "LICENCE".

import argparse
import logging
import sys
import os
import re

DEFAULT_OUTPUT_SEPERATOR = '|'

def init_arg_parser():

    parser = argparse.ArgumentParser(description='pygrep')

    parser.add_argument('-f',
                        '--file',
                        dest='file',
                        type=str,
                        required=True,
                        help='Input file')

    parser.add_argument('-r',
                        '--regex',
                        dest='regex',
                        type=str,
                        required=True,
                        help='Regular expression string')

    parser.add_argument('-s',
                        '--sep',
                        dest='seperator',
                        type=str,
                        required=False,
                        help=f"Output seperator for captured groups (default: '{DEFAULT_OUTPUT_SEPERATOR}')",
                        default=DEFAULT_OUTPUT_SEPERATOR)

    parser.add_argument('-D',
                        '--debug',
                        dest='enable_debug',
                        required=False,
                        action='store_true',
                        help='Enable debug.')


    return parser.parse_args()

def init_logging(enable_debug):

    if enable_debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s: %(message)s")

def main():

    try:

        args = init_arg_parser()

        init_logging(args.enable_debug)

        logging.debug('Started')

        seperator = args.seperator

        regex = rf"{args.regex}"

        pattern = re.compile(regex)

        if not os.path.isfile(args.file):
            raise FileNotFoundError(f"File not found: {args.file}")

        with open(args.file, 'r', encoding='utf-8') as file_handle:

            for line in file_handle.readlines():

                match = pattern.search(line)

                if match:

                    output = ''

                    matched_groups = match.groups()
                    len_matched_groups = len(matched_groups)

                    if len_matched_groups == 1:
                        output = matched_groups[0]

                    elif len_matched_groups > 1:

                        output += matched_groups[0]

                        for i in range(1, len_matched_groups):
                            output += seperator + matched_groups[i]

                    else:
                        output = match.group(0)

                    print(output)

        logging.debug('Finished')

    except Exception as err:

        _, _, exc_tb = sys.exc_info()
        filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        # TODO: Add exception type
        logging.error(f"Exception in {filename} (line: {exc_tb.tb_lineno}): {err}")

if __name__ == '__main__':
    main()
