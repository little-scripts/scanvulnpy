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
Scanner vulnerability PyPI Packages, the data provided by https://osv.dev
"""

import sys
import os
from .modules.utils import Utils
from .modules.scanner import VulnerabilityScanner
from .modules.banners import print_banner
from .modules.cmd import cmd_options
from .modules.loggers import Logger
from .__version__ import (
    __author__,
    __version__,
)


def main():
    """
    Scanner vulnerability PyPI Packages.
    """
    if not Utils.check_platform:
        print("\nThe script doesn't support your platform for the moment !\nFeel free to report issues: "
              "https://github.com/little-scripts/scanvulnpy/issues")
        sys.exit(0)
    else:
        print_banner(__author__, __version__)

    # Setup (Instantiate Object)
    options = cmd_options()
    utils = Utils()
    scandal = VulnerabilityScanner()
    logger = Logger()

    # Get packages
    logger.info("Get PyPI packages, this may take few seconds...")
    packages, nb_packages = utils.get_requirements(options.requirements, options.freeze)
    if not packages:
        sys.exit(1)

    # Initialize counters and lists to store results
    count_non_vulnerable = int(0)
    count_vulnerability = int(0)
    list_packages_non_vulnerable = []
    list_packages_vulnerable = []

    # Log start of the Scan
    logger.info(f"Scan vulnerability on {nb_packages} PyPI packages")

    # Iterate over packages and Scan each one
    for package in packages:
        package = package.strip()
        if package != '':
            
            # Set payload and header for request the API endpoint
            payload, version = utils.set_payload(package)
            user_agent = utils.set_random_user_agent()
            header = utils.set_headers(user_agent)

            # If payload send POST request to the API endpoint
            if payload:
                response = scandal.request_api_osv(payload, header)

                # Log the Scan results and update counters and lists
                (nb_packages, count_non_vulnerable, count_vulnerability, list_packages_vulnerable,
                 list_packages_non_vulnerable) = scandal.result_scan(
                    nb_packages, options.verbose, response, payload, package, version, count_vulnerability,
                    count_non_vulnerable, list_packages_vulnerable, list_packages_non_vulnerable)

    # Log the final results based on the number of vulnerabilities found
    scandal.final_results(count_non_vulnerable, count_vulnerability, list_packages_vulnerable,
                          list_packages_non_vulnerable)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Exception:", e)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Interrupt script...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
