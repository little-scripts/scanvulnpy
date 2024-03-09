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
Module logger
"""

import sys
try:
    from datetime import datetime
    from rich.console import Console
    console = Console()
except ModuleNotFoundError as e:
    print("Mandatory dependencies are missing:", e)
    print("Install: python -m pip install --upgrade <module-named>")
    sys.exit(1)

class Logger:
    """Controller class for Level."""

    def __init__(self):
        """Init Class Level."""

    def info(self, message):
        """docstring
        """
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
        console.print("{} | {}INFO{} | {}".format( current_date, "[bold grey]", "[/bold grey]", message), highlight=False, overflow="ignore", crop=False)

    def success(self, message):
        """docstring
        """
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
        console.print("{} | {}SUCCESS{} | {}".format( current_date, "[bold green]", "[/bold green]", message), highlight=False, overflow="ignore", crop=False)

    def debug(self, message):
        """docstring
        """
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
        console.print("{} | {}DEBUG{} | {}".format( current_date, "[bold yellow]", "[/bold yellow]", message), highlight=False, overflow="ignore", crop=False)

    def warning(self, message):
        """docstring
        """
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
        console.print("{} | {}WARN{} | {}".format( current_date, "[bold orange3]", "[/bold orange3]", message), highlight=False, overflow="ignore", crop=False)

    def error(self, message):
        """docstring
        """
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
        console.print("{} | {}ERROR{} | {}".format( current_date, "[bold red]", "[/bold red]", message), highlight=False, overflow="ignore", crop=False)
