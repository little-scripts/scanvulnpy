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
Module logger
"""

import logging


class Logger:
    """Controller class for Logger."""

    def __init__(self) -> None:
        pass

    def info(self, message) -> None:
        """
        Logs an info message.

        Parameters
        ----------
        message : str
            The info message to log.
        """
        # Configure the logger
        logger = logging.getLogger(__name__)
        logging.basicConfig(
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.INFO,
        )

        # Log the info message with timestamp
        logger.info("%s",message)

    def warning(self, message) -> None:
        """
        Logs an warning message.

        Parameters
        ----------
        message : str
            The warning message to log.
        """
        # Configure the logger
        logger = logging.getLogger(__name__)
        logging.basicConfig(
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.WARNING,
        )

        # Log the warning message with timestamp
        logger.warning("%s",message)

    def error(self, message) -> None:
        """
        Logs an error message.

        Parameters
        ----------
        message : str
            The error message to log.
        """
        # Configure the logger
        logger = logging.getLogger(__name__)
        logging.basicConfig(
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.ERROR,
        )

        # Log the warning message with timestamp
        logger.error("%s",message)
