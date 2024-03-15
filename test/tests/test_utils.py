"""
Test Utils
"""

import pytest
from scanvulnpy.scanvulnpy.modules.utils import Utils


@pytest.mark.smoke
class TestPlatform():
    """ Docstring
    """

    def test_check_platform_windows(self, utils):
        """ Test de la méthode check_platform pour le cas où la plate-forme est Windows
        """
        utils.platform_os = 'nt'
        assert utils.check_platform() == Utils.is_platform_windows()

    def test_check_platform_linux(self, utils):
        """ Test de la méthode check_platform pour le cas où la plate-forme est Linux
        """
        utils.platform_os = 'posix'
        assert utils.check_platform() == Utils.is_platform_linux()

    def test_check_platform_unsupported(self, utils):
        """ Test de la méthode check_platform pour une plate-forme non prise en charge
        """
        utils.platform_os = 'mac'
        assert utils.check_platform() == False