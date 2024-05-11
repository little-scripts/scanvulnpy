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
Module ScannerVulnerability
"""

import sys

try:
    import requests
    import os
    import re
    from typing import Optional, Tuple
    from dataclasses import dataclass
except ModuleNotFoundError as e:
    print("Mandatory dependencies are missing:", e)
    print("Install: python -m pip install --upgrade <module-named>")
    sys.exit(1)

from .loggers import Logger


@dataclass
class ScannerVulnerability:
    """Controller class for ScannerVulnerability."""

    logger = Logger()
    url = 'https://api.osv.dev/v1/query'  # API endpoint for vulnerability Scanning

    def store_result(self, nb_packages: int = None, verbose: str = None,
                     response: str = None, payload: dict = None, package: str = None, version: str = None,
                     count_vulnerability: int = None, count_non_vulnerable: int = None,
                     list_packages_vulnerable: list = None, list_packages_non_vulnerable: list = None):
        """
        Logs the result of Scanning a single package.

        Args:
            nb_packages (int): Number of packages.
            verbose (str): verbose vulnerability.
            response (Response): HTTP response object from the vulnerability Scan.
            payload (dict): Dictionary payload.
            package (str): Name of the package being Scanned.
            version (str): Version of the package being Scanned (if available).
            count_vulnerability (int): Number of vulnerable packages.
            count_non_vulnerable (int): Number of non-vulnerable packages.
            list_packages_vulnerable (list): List of vulnerable packages.
            list_packages_non_vulnerable (list): List of non-vulnerable packages

        Returns:
            tuple: A tuple containing updated counts of vulnerable and non-vulnerable packages,
            and updated lists of vulnerable and non-vulnerable packages.
        """
        if verbose == 'package':
            # Check if the response contains vulnerability information
            if response.text != '{}':
                count_vulnerability += 1
                list_packages_vulnerable.append(f"{package.strip()}: {response.text}")
                # Log vulnerability details
                if version:
                    self.logger.warning(f'Scan {payload}')
                else:
                    self.logger.warning(
                        f"Scan {payload}...We can't determinate if your version is affected. Retry with a specific "
                        f"version(e.g., request==2.31.0) in your requirements.")
            # If no vulnerabilities found and response is successful
            elif response.text == '{}' and response.status_code == 200:
                count_non_vulnerable += 1
                list_packages_non_vulnerable.append(package.strip())
                self.logger.info(f'Scan {payload}')
        else:
            # Check if the response contains vulnerability information
            if response.text != '{}':
                count_vulnerability += 1
                list_packages_vulnerable.append(package.strip())
            # If no vulnerabilities found and response is successful
            elif response.text == '{}' and response.status_code == 200:
                count_non_vulnerable += 1
                list_packages_non_vulnerable.append(package.strip())

        return (nb_packages, count_non_vulnerable, count_vulnerability, list_packages_vulnerable,
                list_packages_non_vulnerable)

    def display_results(self, count_non_vulnerable: int = None, count_vulnerability: int = None,
                        list_packages_vulnerable: list = None,
                        list_packages_non_vulnerable: list = None):
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

    def request_api_osv(self, payload: tuple = None, header: dict = None):
        """
        Request API endpoint for the given packages.
    
        Args:
            payload: A tuple containing the payload and the package version.
            header: A dict containing the header.
    
        Returns:
            json: response.
        """
        return requests.post(self.url, json=payload, headers=header, timeout=10)

    def get_requirements(self, path: str = False):
        """
        Retrieves the list of packages from the requirements file.

        Args:
            path (str): Path to requirements file.

        Returns:
            list: List of package names and versions.
        """
        # If no requirements file specified and freezing packages is enabled
        if path is False:
            freeze = True
            # Use 'pip freeze' command to generate requirements list with installed packages
            cmd = 'pip freeze'
            output = os.popen(cmd).read()
            packages = output.split('\n')
            packages.remove(packages[-1])
            nb_packages = len(packages)
            return packages, nb_packages

        elif path is not False:
            freeze = False
            # Read the requirements file and return the list of packages
            try:
                with open(path, "r", encoding="utf-8") as file:
                    packages = file.readlines()
                    # Filter empty line
                    filtered_packages = [x.strip() for x in packages if x.strip() != '' and '\n' in x]
                    nb_packages = len(filtered_packages)
                return filtered_packages, nb_packages

            except Exception as e:
                self.logger.error(f"{e} ! Please check the path you send !")
                return None, False
        else:
            return None, False

    def set_payload(self, package: str = None) -> Tuple[Optional[dict], Optional[str]]:
        """
        Sets the payload for a given package.

        Args:
            package (str): The name and version of the package.

        Returns:
            tuple: A tuple containing the payload and the package version.
        """
        payload = None
        version = None

        if package and re.match(r'^[a-zA-Z0-9_.-]+(?:==[0-9]+(?:\.[0-9]+)*(?:\.\w+)?)?$', package):
            if '==' in package:
                package_name, version = package.split('==')
                payload = {"version": version, "package": {"name": package_name, "ecosystem": "PyPI"}}
            elif '>=' in package or '<=' in package:
                self.logger.error(
                    f"{package}! Retry with a specific version (e.g., request==2.31.0) in your requirements.")
            else:
                package_name = package.split()[0]
                payload = {"package": {"name": package_name, "ecosystem": "PyPI"}}
        else:
            self.logger.error(f"Invalid package format: {package} Retry with a valid package name.")

        return payload, version
