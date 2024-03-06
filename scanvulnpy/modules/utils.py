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
import platform
import tempfile
from .logger import Logger


class Utils:
    """Controller class for Scanner."""

    def __init__(self, config) -> None:
        self.config=config
        self.platform_os = os.name

    def is_platform_windows(self):
        """
        Checking if the running platform is windows.

        Returns
        -------
        bool
            ["win32", "cygwin"] if the running platform is windows.
        """
        if platform.system().lower() == 'windows':
            return True


    def is_platform_linux(self):
        """
        Checking if the running platform is linux.

        Returns
        -------
        bool
            linux if the running platform is linux.
        """
        if platform.system().lower() == 'linux':
            return True


    def is_platform_mac(self):
        """
        Checking if the running platform is mac.

        Returns
        -------
        bool
            darwin if the running platform is mac.
        """
        return sys.platform == 'darwin'


    def is_platform_arm(self):
        """
        Checking if the running platform use ARM architecture.

        Returns
        -------
        bool
            True if the running platform uses ARM architecture.
        """
        is_platform = platform.machine() in ("arm64", "aarch64") or platform.machine().startswith(
            "armv"
        )
        return is_platform


    def check_platform(self):
        """
        Checking running platform.

        Returns
        -------
        bool
            True if the running platform available.
        """
        platform_os = os.name
        if platform_os == 'nt':
            return Utils.is_platform_windows
        elif platform_os == 'posix':
            return Utils.is_platform_linux
        elif platform_os == 'posix':
            return Utils.is_platform_mac
        else:
            return False

    def get_requirements(self):
        """get_requirements"""

        path_requirements = self.config.requirements
        # If no requirements file, freeze PyPI packages on local environnement
        if not self.config.requirements and self.config.freeze:
            tmp_dir = tempfile.gettempdir()
            if os.path.exists(tmp_dir):
                if self.platform_os == 'nt':
                    path_requirements = tmp_dir + '\\requirements.txt'
                elif self.platform_os == 'posix':
                    path_requirements = tmp_dir + '/requirements.txt'
            cmd = f'pip freeze > {path_requirements}'
            os.system(cmd)

        Logger.info(self, f"Get packages requirements: {path_requirements}") # type: ignore

        with open(path_requirements, "r", encoding="utf-8") as file:
            packages = file.readlines()
        file.close()

        return packages
