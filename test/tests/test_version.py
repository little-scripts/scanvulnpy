"""
This Version
"""

import pytest
from scanvulnpy.scanvulnpy import __version__


class TestVersionFile:
    """Test cases for version file attributes."""

    @pytest.mark.smoke
    def test_version_attributes(self):
        """Check if version file attributes match expected values."""
        version = __version__

        assert version.__title__ == 'scanvulnpy', 'Title mismatch in version file'
        assert version.__author__ == 'little-scripts developers', 'Author mismatch in version file'
        assert version.__license__ == 'Apache 2.0', 'License mismatch in version file'
        assert version.__uri__ == 'https://github.com/little-scripts/scanvulnpy', 'URI mismatch in version file'
