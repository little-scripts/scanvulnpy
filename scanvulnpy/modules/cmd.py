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
from rich.console import Console


def cmd_options():
    """ Get options
    """
    description = "A simple wrapper to Scan vulnerability PyPI Packages, the data provided by https://osv.dev"

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
        action="store",
        default=False,
        required=False,
        help="path requirements (e.g. -r <path>)",
    )

    parser.add_argument(
        "-v",
        dest="verbose",
        default=True,
        required=False,
        help="verbose (e.g. -v False)",
    )

    parser.add_argument(
        "-nc",
        dest="no_color",
        default=False,
        required=False,
        action="store_true",
        help="Disable colors.",
    )

    options = parser.parse_args()
    return options

def get_options():
    """ Get options
    """
    cmd = cmd_options()
    if cmd.no_color:
        console = Console(record=True, color_system=None)
    else:
        console = Console(record=True, color_system="truecolor")
    return console
