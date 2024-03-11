# -*- coding: utf-8 -*-
#
# Copyright 2024 little-scripts
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Module cmd

"""

import argparse

def cmd_options():
    """
    Returns the options send by user in command-line.

    Returns:
        Options: freeze, requirements, verbose, no_color.
    """

    description = "A simple wrapper to scan vulnerability PyPI Packages, the data provided by https://osv.dev"

    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "-f",
        dest="freeze",
        default=True,
        required=False,
        help="enable by default, disable if '-r <path>' is setting",
    )

    parser.add_argument(
        "-r",
        dest="requirements",
        default=False,
        required=False,
        help="path requirements(e.g. -r <path>)",
    )

    parser.add_argument(
        "--verbose",
        dest="verbose",
        default=False,
        required=False,
        help="verbose details vulns(e.g. --verbose vulns)",
    )

    options = parser.parse_args()

    if options.requirements is not False:
        options.freeze = False

    return options
