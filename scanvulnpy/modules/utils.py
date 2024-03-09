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

import os


class Utils:
    """Controller class for Utils."""

    def __init__(self, config) -> None:
        self.config=config
        self.platform_os = os.name

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

    def get_requirements(self):
        """
        Retrieves the list of packages from the requirements file.

        Returns:
            list: List of package names and versions.
        """
        # Get the path to the requirements file from the configuration
        path_requirements = self.config.requirements
        # If no requirements file specified and freezing packages is enabled
        if not path_requirements and self.config.freeze:
            # Use 'pip freeze' command to generate requirements list with installed packages
            cmd = 'pip freeze'
            output = os.popen(cmd).read()
            packages = output.split('\n')
        else:
            # Read the requirements file and return the list of packages
            with open(path_requirements, "r", encoding="utf-8") as file:
                packages = file.readlines()

        return packages
