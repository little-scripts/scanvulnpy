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
Module scanner
"""

import re
import requests
from .logger import Logger


class Scanner:
    """Controller class for Scanner."""

    def __init__(self, config) -> None:
        self.config=config

    def set_payload(self, package):
        """set_payload"""
        try:
            package = package.strip().split('==')
            version = package[1].strip()
            package = package[0]
            payload = {"version": f"{version}", "package": {"name": f"{package}", "ecosystem": "PyPI"}}
        except Exception:
            package = package[0]
            version = None
            payload = {"package": {"name": f"{package}", "ecosystem": "PyPI"}}
        return payload, version

    def log_run(self, response, package, version, count_vuln, count_ok, list_packages_vuln, list_packages_ok):
        """log_run"""
        if response.text != '{}':
            count_vuln +=1
            list_packages_vuln.append(package)
            if version:
                Logger.warning(self, f"Vulnerability in package: {package} | {response.text}") # type: ignore
            else:
                Logger.warning(self, f"Vulnerabilitys in package: {package} | But we can't find a version in your requirements ! To be sure your version is not vulnerable, recheck with version in requirements(e.g request==2.31.0).") # type: ignore
        elif response.text == '{}' and response.status_code == 200:
            count_ok +=1
            list_packages_ok.append(package)
            Logger.info(self, f"Scan package: {package}") # type: ignore
        return count_ok, count_vuln, list_packages_vuln, list_packages_ok

    def log_final(self, count_vuln, count_ok, list_packages_vuln, list_packages_ok):
        """log_run"""
        total_packages = count_ok + count_vuln
        total_vulns = total_packages - count_ok
        if count_vuln == 0:
            Logger.info(self, f"Total packages: {total_packages}") # type: ignore
            Logger.info(self, f"Package(s) vulnerable: {total_vulns}") # type: ignore
            Logger.info(self, f"List packages scanned: {list_packages_ok} ") # type: ignore
        else:
            Logger.info(self, f"Total packages: {total_packages}") # type: ignore
            Logger.info(self, f"{count_ok} Package(s) ok: {list_packages_ok} ") # type: ignore
            Logger.warning(self, f"{total_vulns} Package(s) vulnerable:: {list_packages_vuln} ") # type: ignore

    def run(self, packages):
        """main"""
        url='https://api.osv.dev/v1/query'
        count_ok = 0
        count_vuln = 0
        list_packages_ok = []
        list_packages_vuln = []
        Logger.info(self, "Start scan vulnerability PyPI packages.") # type: ignore
        Logger.info(self, "In progress, this may take few seconds...") # type: ignore
        for package in packages:
            package = package.strip()
            if re.match('.*[a-z0-9].*', package):
                payload, version = Scanner(self.config).set_payload(package)
                response = requests.post(url, json=payload, headers={'content-type': 'application/json'}, timeout=10)
                count_ok, count_vuln, list_packages_vuln, list_packages_ok = Scanner(self.config).log_run(response, package, version, count_vuln, count_ok, list_packages_vuln, list_packages_ok)
        return count_vuln, count_ok, list_packages_vuln, list_packages_ok
