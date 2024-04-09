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
from fake_useragent import UserAgent
from .loggers import Logger


class Utils:
    """Controller class for Utils."""

    def __init__(self) -> None:
        self.platform_os = os.name
        self.logger = Logger()

    def __repr__(self):
        return f"__repr__ Utils: [platform_os={self.platform_os}, logger={self.logger}]"

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
        return os.name == 'posix' and platform.system() == 'Darwin'

    @staticmethod
    def set_random_user_agent():
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

    def check_platform(self):
        """
        Checking running platform.

        Returns
        -------
        bool
            True if the running platform available.
        """
        if self.platform_os == 'nt':
            return Utils.is_platform_windows()
        elif self.platform_os == 'posix':
            return Utils.is_platform_linux()
        else:
            return False

    def progress_bar(self, count: int = None, total: int = None, status: str = ''):
        """
        Progress bar.

        Args:
            count (int): count package.
            total (int): total package.
            status (str): status message.

        Returns:
            None
        """
        bar_len = 100
        filled_len = int(round(bar_len * count / float(total)))
        percents = round(100.0 * count / float(total), 1)
        bar = '■' * filled_len + ' ' * (bar_len - filled_len)
        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()
