"""
Test Platform
"""

import pytest
from ...scanvulnpy.modules.utils import Utils


@pytest.mark.smoke
class TestCheckPlatform:
    """
    Test check_platform method for different platforms.
    """

    def test_check_platform_windows(self, utils):
        """ Test check_platform method for Windows platform. """
        utils.platform_os = 'nt'
        assert utils.check_platform() == Utils.is_platform_windows()

    def test_check_platform_linux(self, utils):
        """ Test check_platform method for Linux platform. """
        utils.platform_os = 'posix'
        assert utils.check_platform() == Utils.is_platform_linux()

    def test_check_platform_unsupported(self, utils):
        """ Test check_platform method for an unsupported platform. """
        utils.platform_os = 'mac'
        assert utils.check_platform() is False
