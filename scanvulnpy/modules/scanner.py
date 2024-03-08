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
try:
    import re
    import requests
except ModuleNotFoundError as e:
    print("Mandatory dependencies are missing:", e)
    print("Install: python -m pip install --upgrade <module-named>")
    sys.exit(1)

from .loggers import Level

class Scanner:
    """Controller class for Scanner."""

    def __init__(self, config) -> None:
        self.config=config

    def set_payload(self, package):
        """
        Sets the payload for a given package.

        Args:
            package (str): The name and version of the package.

        Returns:
            tuple: A tuple containing the payload and the package version.
        """
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
            Level.error(self, f"{package} ! Retry with a specific version(e.g., request==2.31.0) in your requirements.") # type: ignore
        elif re.match('.*<=.*', package):
            payload = None
            version = None
            Level.error(self, f"{package} ! Retry with a specific version(e.g., request==2.31.0) in your requirements.") # type: ignore
        else:
            # If no version is specified
            package = package.strip().split()
            package = package[0]
            version = None
            # Creates the payload with the package name, and ecosystem (PyPI)
            payload = {"package": {"name": f"{package}", "ecosystem": "PyPI"}}

        return payload, version

    def log_result(self, response, payload, package, version, count_vuln, count_ok, list_packages_vuln, list_packages_ok):
        """
        Logs the result of Scanning a single package.

        Args:
            response (Response): HTTP response object from the vulnerability Scan.
            package (str): Name of the package being Scanned.
            version (str): Version of the package being Scanned (if available).
            count_vuln (int): Number of vulnerable packages.
            count_ok (int): Number of non-vulnerable packages.
            list_packages_vuln (list): List of vulnerable packages.
            list_packages_ok (list): List of non-vulnerable packages.

        Returns:
            tuple: A tuple containing updated counts of vulnerable and non-vulnerable packages,
            and updated lists of vulnerable and non-vulnerable packages.
        """
        # Check if the response contains vulnerability information
        if response.text != '{}':
            count_vuln += 1
            list_packages_vuln.append(package)
            # Log vulnerability details
            if version:
                Level.warning(self, payload) # type: ignore
            else:
                Level.warning(self, f"{payload}...We can't determinate if your version is affected. Retry with a specific version(e.g., request==2.31.0) in your requirements.") # type: ignore
        # If no vulnerabilities found and response is successful
        elif response.text == '{}' and response.status_code == 200:
            count_ok += 1
            list_packages_ok.append(package)
            Level.info(self, f'Scan: {payload}') # type: ignore

        return count_ok, count_vuln, list_packages_vuln, list_packages_ok

    def log_final(self, count_vuln, count_ok, list_packages_vuln, list_packages_ok):
        """
        Logs the final results of the vulnerability Scan.

        Args:
            count_vuln (int): Number of vulnerable packages.
            count_ok (int): Number of non-vulnerable packages.
            list_packages_vuln (list): List of vulnerable packages.
            list_packages_ok (list): List of non-vulnerable packages.
        """
        # Calculate total packages and total vulnerabilities
        total_packages = count_ok + count_vuln
        total_vulns = total_packages - count_ok

        # Log the final results based on the number of vulnerabilities found
        if count_vuln == 0:
            # Log if no vulnerabilities found
            Level.info(self, f"{total_packages} Package(s) scanned") # type: ignore
            Level.info(self, f"{total_vulns} Package(s) vulnerable") # type: ignore
            Level.info(self, f"Package(s) non-vulnerable: {list_packages_ok}") # type: ignore
        else:
            # Log if vulnerabilities found
            Level.info(self, f"{total_packages} Package(s) scanned") # type: ignore
            Level.info(self, f"{count_ok} Package(s) non-vulnerable: {list_packages_ok}") # type: ignore
            Level.warning(self, f"{total_vulns} Package(s) vulnerable: {list_packages_vuln}") # type: ignore

    def run(self, packages):
        """
        Runs the vulnerability Scan for the given packages.

        Args:
            packages (list): List of PyPI packages to Scan.

        Returns:
            tuple: A tuple containing counts of vulnerable and non-vulnerable packages,
            and lists of vulnerable and non-vulnerable packages.
        """
        # API endpoint for vulnerability Scanning
        url = 'https://api.osv.dev/v1/query'

        # Initialize counters and lists to store results
        count_ok = 0
        count_vuln = 0
        list_packages_ok = []
        list_packages_vuln = []

        # Log start of the Scan
        Level.info(self, "Start Scan vulnerability PyPI packages. The data provided by https://osv.dev") # type: ignore
        Level.info(self, "In progress, this may take few seconds...") # type: ignore

        # Iterate over packages and Scan each one
        for package in packages:
            package = package.strip()
            # Check if the package name contains alphanumeric characters
            if re.match('.*[a-z0-9].*', package):
                # Set payload for the package
                payload, version = Scanner(self.config).set_payload(package)
                # If payload send POST request to the API endpoint
                if payload:
                    response = requests.post(url, json=payload, headers={'content-type': 'application/json'}, timeout=10)
                    # Log the Scan results and update counters and lists
                    count_ok, count_vuln, list_packages_vuln, list_packages_ok = Scanner(self.config).log_result(response, payload, package, version, count_vuln, count_ok, list_packages_vuln, list_packages_ok)

        # Logs the final results of the vulnerability Scan
        Scanner(self.config).log_final(count_vuln, count_ok, list_packages_vuln, list_packages_ok)
