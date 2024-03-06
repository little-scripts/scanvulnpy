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
from datetime import datetime


class Logger:
    """Controller class for Logger."""

    def __init__(self) -> None:
        pass

    def info(self, message) -> None:
        """docstring
        """
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)
        logger.info("%s: %s", current_date, message)

    def warning(self, message) -> None:
        """docstring
        """
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.WARNING)
        logger.warning("%s: %s", current_date, message)

    def error(self, message) -> None:
        """docstring
        """
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.ERROR)
        logger.error("%s: %s", current_date, message)
