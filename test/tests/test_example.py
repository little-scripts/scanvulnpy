"""
This is Pytest Exemple
"""

import pytest
from scanvulnpy.scanvulnpy import __version__


class TestExemple():
    """ Docstring
    """
    @pytest.mark.smoke
    def test_version_file(self):
        """
        Test version file
        """
        expected_title = __version__.__title__
        expected_author = __version__.__author__
        expected_license = __version__.__license__
        expected_uri = __version__.__uri__
        assert expected_title == 'scanvulnpy'
        assert expected_author == 'little-scripts developers'
        assert expected_license == 'Apache 2.0'
        assert expected_uri == 'https://github.com/little-scripts/scanvulnpy'

