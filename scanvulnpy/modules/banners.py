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
# https://patorjk.com/software/taag/

"""
Module banner

"""


from platform import system
from os import get_terminal_size
from rich.align import Align
from rich.panel import Panel
from rich.text import Text


def get_terminal_width() -> int:
    """docstring
    """
    try:
        width, _ = get_terminal_size()
    except OSError:
        width = 80

    if system().lower() == "windows":
        width -= 1

    return width

def print_banner(console, author, version) -> None:
    """docstring
    """
    width = get_terminal_width()
    height = 7
    large = """\

    A simple wrapper to scan vulnerability PyPI Packages,
    the data provided by https://osv.dev

"""

    banner = """\

    A simple wrapper to scan vulnerability PyPI Packages,
    the data provided by https://osv.dev

"""

    if width < 90:
        banner = banner
        height = 7

    panel = Panel(
        Align(
            Text(banner, justify="center", style="blue"),
            vertical="middle",
            align="center",
        ),
        width=width,
        height=height,
        subtitle=f"By:{author} | Version:{version}",
    )
    console.print(panel)
    console.print('')
