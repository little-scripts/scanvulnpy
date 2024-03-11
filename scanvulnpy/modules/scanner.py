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
Module Scanner
"""

import sys
import re

try:
    import requests
except ModuleNotFoundError as e:
    print("Mandatory dependencies are missing:", e)
    print("Install: python -m pip install --upgrade <module-named>")
    sys.exit(1)

from .loggers import Logger
logger = Logger()

class Scanner:
    """Controller class for Scanner."""

    def __init__(self):
        pass

    def __repr__(self):
        return "__repr__ Scanner: None"

    @staticmethod
    def set_payload(package:str = None) -> None :
        """
        Sets the payload for a given package.

        Args:
            package (str): The name and version of the package.

        Returns:
            tuple: A tuple containing the payload and the package version.
        """
        package = package.strip()
        # Check if the package name contains alphanumeric characters
        if re.match('.*[a-z0-9].*', package):
            # If version is specified
            if re.match('.*==.*', package):
                # Retrieves the package name and version
                package = package.strip().split('==')
                package_name = package[0]
                version = package[1]
                # Creates the payload with the package name, version, and ecosystem (PyPI)
                payload = {"version": f"{version}", "package": {"name": f"{package_name}", "ecosystem": "PyPI"}}
            elif re.match('.*>=.*', package):
                payload = None
                version = None
                logger.error(f"{package} ! Retry with a specific version(e.g., request==2.31.0) in your requirements.")
            elif re.match('.*<=.*', package):
                payload = None
                version = None
                logger.error(f"{package} ! Retry with a specific version(e.g., request==2.31.0) in your requirements.")
            else:
                # If no version is specified
                package = package.strip().split()
                package = package[0]
                version = None
                # Creates the payload with the package name, and ecosystem (PyPI)
                payload = {"package": {"name": f"{package}", "ecosystem": "PyPI"}}

        return payload, version

    @staticmethod
    def request_api_osv_dev(payload:tuple = None) -> None :
        """
        Request API endpoint for the given packages.

        Args:
            tuple: A tuple containing the payload and the package version.

        Returns:
            json: A json response containing vulnerable and non-vulnerable packages.
        """
        # API endpoint for vulnerability Scanning
        url = 'https://api.osv.dev/v1/query'
        header = {'content-type': 'application/json'}
        response = requests.post(url, json=payload, headers=header, timeout=10)
        return response

    @staticmethod
    def log_result_request(verbose, response, payload, package, version, count_vulnerability, count_non_vulnerable, list_packages_vulnerable, list_packages_non_vulnerable):
        """
        Logs the result of Scanning a single package.

        Args:
            verbose (str): verbose vulnerability.
            response (Response): HTTP response object from the vulnerability Scan.
            package (str): Name of the package being Scanned.
            version (str): Version of the package being Scanned (if available).
            count_vulnerability (int): Number of vulnerable packages.
            count_non_vulnerable (int): Number of non-vulnerable packages.
            list_packages_vulnerable (list): List of vulnerable packages.
            list_packages_non_vulnerable (list): List of non-vulnerable packages.

        Returns:
            tuple: A tuple containing updated counts of vulnerable and non-vulnerable packages,
            and updated lists of vulnerable and non-vulnerable packages.
        """
        # Check if the response contains vulnerability information
        if response.text != '{}':
            count_vulnerability += 1
            list_packages_vulnerable.append(package.strip())
            # Log vulnerability details
            if version:
                if verbose == 'vulns':
                    logger.warning(response.text)
                else:
                    logger.warning(payload)
            else:
                logger.warning(f"{payload}...We can't determinate if your version is affected. Retry with a specific version(e.g., request==2.31.0) in your requirements.")
        # If no vulnerabilities found and response is successful
        elif response.text == '{}' and response.status_code == 200:
            count_non_vulnerable += 1
            list_packages_non_vulnerable.append(package.strip())
            logger.info(f'Scan: {payload}')

        return count_non_vulnerable, count_vulnerability, list_packages_vulnerable, list_packages_non_vulnerable

    @staticmethod
    def final_results(count_non_vulnerable, count_vulnerability, list_packages_vulnerable, list_packages_non_vulnerable):
        """
        Logs the result of Scanning a single package.

        Args:
            count_vulnerability (int): Number of vulnerable packages.
            count_non_vulnerable (int): Number of non-vulnerable packages.
            list_packages_vulnerable (list): List of vulnerable packages.
            list_packages_non_vulnerable (list): List of non-vulnerable packages.

        Returns:
            tuple: A tuple containing counts of vulnerable and non-vulnerable packages,
            and updated lists of vulnerable and non-vulnerable packages.
        """

        # Calculate total packages and total vulnerabilities
        total_packages = count_non_vulnerable + count_vulnerability
        total_vulnerabilities = total_packages - count_non_vulnerable

        logger.info("----------------- Results ----------------------")
        if count_vulnerability == 0:
            # Log if no vulnerabilities found
            logger.info(f"{total_packages} Package(s) scanned")
            logger.info(f"{total_vulnerabilities} Package(s) vulnerable")
            logger.info(f"Package(s) non-vulnerable: {list_packages_non_vulnerable}")
        else:
            # Log if vulnerabilities found
            logger.info(f"{total_packages} Package(s) scanned")
            logger.info(f"{count_non_vulnerable} Package(s) non-vulnerable: {list_packages_non_vulnerable}")
            logger.warning(f"{total_vulnerabilities} Package(s) vulnerable: {list_packages_vulnerable}")

        return count_non_vulnerable, count_vulnerability, list_packages_vulnerable, list_packages_non_vulnerable

    def run(self, packages:list = None, verbose:str = None) -> None :
        """
        Runs the vulnerability Scan for the given packages.

        Args:
            packages (list): List of PyPI packages to Scan.
            verbose (str): verbose vulnerability.

        Returns:
            list: List of vulnerable packages.
        """
        # Log start of the Scan
        logger.info("Scan vulnerability PyPI packages, this may take few seconds...")

        # Initialize counters and lists to store results
        count_non_vulnerable = 0
        count_vulnerability = 0
        list_packages_non_vulnerable = []
        list_packages_vulnerable = []

        # Iterate over packages and Scan each one
        for package in packages:
            # Set payload for the package
            payload, version = Scanner().set_payload(package)
            # If payload send POST request to the API endpoint
            if payload:
                response = Scanner().request_api_osv_dev(payload)
                # Log the Scan results and update counters and lists
                count_non_vulnerable, count_vulnerability, list_packages_vulnerable, list_packages_non_vulnerable = Scanner().log_result_request(verbose, response, payload, package, version, count_vulnerability, count_non_vulnerable, list_packages_vulnerable, list_packages_non_vulnerable)
        # Log the final results based on the number of vulnerabilities found
        count_non_vulnerable, count_vulnerability, list_packages_vulnerable, list_packages_non_vulnerable = Scanner().final_results(count_non_vulnerable, count_vulnerability, list_packages_vulnerable, list_packages_non_vulnerable)

        return count_non_vulnerable, count_vulnerability, list_packages_non_vulnerable, list_packages_vulnerable