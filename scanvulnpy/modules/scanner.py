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
Module VulnerabilityScanner
"""

import sys
import re

try:
    import requests
    from fake_useragent import UserAgent
except ModuleNotFoundError as e:
    print("Mandatory dependencies are missing:", e)
    print("Install: python -m pip install --upgrade <module-named>")
    sys.exit(1)

from .loggers import Logger


class VulnerabilityScanner:
    """Controller class for VulnerabilityScanner."""

    def __init__(self):
        self.logger = Logger()

    def __repr__(self):
        return "__repr__ Scanner: [logger={self.logger}]"

    @staticmethod
    def get_random_user_agent():
        """
        Sets random user agent.

        Returns:
            str: user agent.
        """
        user_agent = UserAgent()
        return user_agent.random

    @staticmethod
    def set_headers(user_agent):
        """
        Sets headers.

        Args:
            user_agent (str): A user agent.

        Returns:
            dict: headers.
        """

        headers = {
            'User-Agent': '{}'.format(user_agent),
            'content-type': 'application/json',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            }
        return headers

    def set_payload(self, package: str = None) -> tuple:
        """
        Sets the payload for a given package.

        Args:
            package (str): The name and version of the package.

        Returns:
            tuple: A tuple containing the payload and the package version.
        """
        package = package.strip()

        if re.match('.*[a-z0-9].*', package):
            if '==' in package:
                package_name, version = package.split('==')
                payload = {"version": version, "package": {"name": package_name, "ecosystem": "PyPI"}}
            elif '>=' in package or '<=' in package:
                payload = None
                version = None
                self.logger.error(f"{package} ! Retry with a specific version (e.g., request==2.31.0) in your requirements.")
            else:
                package_name = package.split()[0]
                version = None
                payload = {"package": {"name": package_name, "ecosystem": "PyPI"}}
        else:
            payload = None
            version = None
            self.logger.error(f"Invalid package format: {package}. Retry with a valid package name.")

        return payload, version

    def request_api_osv_dev(self, payload:tuple = None, header:dict = None) -> None :
        """
        Request API endpoint for the given packages.

        Args:
            tuple: A tuple containing the payload and the package version.
            dict: A dict containing the header.

        Returns:
            json: A json response containing vulnerable and non-vulnerable packages.
        """
        # API endpoint for vulnerability Scanning
        url = 'https://api.osv.dev/v1/query'
        response = requests.post(url, json=payload, headers=header, timeout=10)
        return response

    def log_result_request(self, nb_packages: int, verbose: str, response: str, payload: dict, package: str, version: str, count_vulnerability: int, count_non_vulnerable: int, list_packages_vulnerable: list, list_packages_non_vulnerable: list) -> tuple:
        """
        Logs the result of Scanning a single package.

        Args:
            nb_packages (int): Number of packages.
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
                    self.logger.warning(f'Scan {nb_packages}: {response.text}')
                else:
                    self.logger.warning(f'Scan {nb_packages}: {payload}')
            else:
                self.logger.warning(f"Scan {nb_packages}: {payload}...We can't determinate if your version is affected. Retry with a specific version(e.g., request==2.31.0) in your requirements.")
        # If no vulnerabilities found and response is successful
        elif response.text == '{}' and response.status_code == 200:
            count_non_vulnerable += 1
            list_packages_non_vulnerable.append(package.strip())
            self.logger.info(f'Scan {nb_packages}: {payload}')

        nb_packages -= 1

        return nb_packages, count_non_vulnerable, count_vulnerability, list_packages_vulnerable, list_packages_non_vulnerable

    def final_results(self, count_non_vulnerable, count_vulnerability, list_packages_vulnerable, list_packages_non_vulnerable):
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

        self.logger.info("----------------- Results ----------------------")
        if count_vulnerability == 0:
            # Log if no vulnerabilities found
            self.logger.info(f"{total_packages} Package(s) scanned")
            self.logger.info(f"{total_vulnerabilities} Package(s) vulnerable")
            self.logger.info(f"Package(s) non-vulnerable: {list_packages_non_vulnerable}")
        else:
            # Log if vulnerabilities found
            self.logger.info(f"{total_packages} Package(s) scanned")
            self.logger.info(f"{count_non_vulnerable} Package(s) non-vulnerable: {list_packages_non_vulnerable}")
            self.logger.warning(f"{total_vulnerabilities} Package(s) vulnerable: {list_packages_vulnerable}")

        return count_non_vulnerable, count_vulnerability, list_packages_vulnerable, list_packages_non_vulnerable

    def run(self, packages:list = None, nb_packages:int = None, verbose:str = None) -> None :
        """
        Runs the vulnerability Scan for the given packages.

        Args:
            packages (list): List of PyPI packages to Scan.
            verbose (str): verbose vulnerability.

        Returns:
            list: List of vulnerable packages.
        """
        # Log start of the Scan
        self.logger.info(f"Scan vulnerability on {nb_packages} PyPI packages, this may take few seconds...")

        # Initialize counters and lists to store results
        count_non_vulnerable = int(0)
        count_vulnerability = int(0)
        list_packages_non_vulnerable = []
        list_packages_vulnerable = []

        # Instantiate Objects
        scanvuln = VulnerabilityScanner()

        # Iterate over packages and Scan each one
        for package in packages:
            # Set payload for the package
            payload, version = scanvuln.set_payload(package)
            # If payload send POST request to the API endpoint
            if payload:
                user_agent = scanvuln.get_random_user_agent()
                header = scanvuln.set_headers(user_agent)
                response = scanvuln.request_api_osv_dev(payload, header)
                # Log the Scan results and update counters and lists
                nb_packages, count_non_vulnerable, count_vulnerability, list_packages_vulnerable, list_packages_non_vulnerable = scanvuln.log_result_request(nb_packages, verbose, response, payload, package, version, count_vulnerability, count_non_vulnerable, list_packages_vulnerable, list_packages_non_vulnerable)

        # Log the final results based on the number of vulnerabilities found
        count_non_vulnerable, count_vulnerability, list_packages_vulnerable, list_packages_non_vulnerable = scanvuln.final_results(count_non_vulnerable, count_vulnerability, list_packages_vulnerable, list_packages_non_vulnerable)

        return count_non_vulnerable, count_vulnerability, list_packages_non_vulnerable, list_packages_vulnerable