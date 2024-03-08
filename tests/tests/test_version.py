# -*- coding: utf-8 -*-
""" Docstring
"""

import pytest
from scanvulnpy.scanvulnpy import __version__


class TestFrameworkRF():
    """ Docstring
    """

    @pytest.mark.smoke
    def test_title(self):
        """ Docstring
        """
        expected = __version__.__title__
        assert expected == 'scanvulnpy' # type: ignore
