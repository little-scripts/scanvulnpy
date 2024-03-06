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

# Run as module: python -m scanvulnpy

"""
A simple scan vulnerability PyPI Packages, the data provided by https://osv.dev
"""

try:
    import os
    import sys
    from .modules.utils import Utils
    from .modules.scanner import Scanner
    from .modules.banners import print_banner
    from .modules.cmd import cmd_options, get_options
    from .__version__ import (
        __author__,
        __copyright__,
        __description__,
        __license__,
        __title__,
        __version__,
    )
except ModuleNotFoundError as e:
    print("Mandatory dependencies are missing:", e)
    print("Install: python -m pip install --upgrade -r requirements.txt")
    sys.exit(1)


if not Utils.check_platform:
    print("\nThe script doesn't support your platform for the moment !\nFeel free to report issues: https://github.com/little-scripts/scanvulnpy/issues")
    sys.exit(0)

if __name__ == '__main__':

    try:

        config = cmd_options()
        console = get_options()
        print_banner(console, __author__, __version__)
        packages = Utils(config).get_requirements()
        count_vuln, count_ok, list_packages_vuln, list_packages_ok = Scanner(config).run(packages)
        Scanner(config).log_final(count_vuln, count_ok, list_packages_vuln, list_packages_ok)

    except Exception as e:
        print("Exception:", e)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Interrupt script...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
