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


"""
Module Utils
"""

import sys
import os
from .loggers import Logger
logger = Logger()

class Utils:
    """Controller class for Utils."""

    def __init__(self) -> None:
        self.platform_os = os.name

    def __repr__(self):
        return f"__repr__ Utils: [platform_os={self.platform_os}]"

    @staticmethod
    def is_platform_windows():
        """
        Check if the platform is Windows.

        Returns
        -------
        bool
            True if the platform is Windows, False otherwise.
        """
        return os.name == 'nt'

    @staticmethod
    def is_platform_linux():
        """
        Check if the platform is Linux.

        Returns
        -------
        bool
            True if the platform is Linux, False otherwise.
        """
        return os.name == 'posix'

    @staticmethod
    def is_platform_mac():
        """
        Check if the platform is macOS.

        Returns
        -------
        bool
            True if the platform is macOS, False otherwise.
        """
        return os.name == 'posix' and os.uname().sysname == 'Darwin'

    def check_platform(self):
        """
        Checking running platform.

        Returns
        -------
        bool
            True if the running platform available.
        """
        if self.platform_os == 'nt':
            return Utils.is_platform_windows
        elif self.platform_os == 'posix':
            return Utils.is_platform_linux()
        else:
            return False

    def get_requirements(self, path:str = None, freeze:bool = False):
        """
        Retrieves the list of packages from the requirements file.

        Args:
            path (str): Path to requirements file.
            freeze (bool): pip freeze local requirements.

        Returns:
            list: List of package names and versions.
        """
        # Get the path to the requirements file from the configuration
        path_requirements = path

        # If no requirements file specified and freezing packages is enabled
        if not path_requirements and freeze:

            logger.info("Pip freeze local PyPI packages")
            # Use 'pip freeze' command to generate requirements list with installed packages
            cmd = 'pip freeze'
            output = os.popen(cmd).read()
            packages = output.split('\n')

        elif path_requirements and not freeze:

            logger.info(f"Get PyPI packages from requirements: {path_requirements}")
            # Read the requirements file and return the list of packages
            try:
                with open(path_requirements, "r", encoding="utf-8") as file:
                    packages = file.readlines()
            except Exception as e:
                logger.error(f"{e} ! Please check the path you send !")
                sys.exit(1)

        else:
            packages = None

        nb_packages = len(packages)

        return packages, nb_packages
