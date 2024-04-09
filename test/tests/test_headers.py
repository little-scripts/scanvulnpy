"""
This Headers
"""

import pytest
from ...scanvulnpy.modules.utils import Utils


@pytest.mark.smoke
class TestHeaders:
    """Test cases for version file attributes."""

    @pytest.mark.parametrize("user_agent", ["Mozilla/5.0", "Chrome/95.0.4638.69", "Safari/537.36"])
    def test_set_headers(self, utils, user_agent):
        headers = utils.set_headers(user_agent)
        assert 'User-Agent' in headers
        assert headers['User-Agent'] == user_agent
        assert 'content-type' in headers
        assert headers['content-type'] == 'application/json'
        assert 'Accept' in headers
        assert headers['Accept'] == 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        assert 'Accept-Language' in headers
        assert headers['Accept-Language'] == 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3'
        assert 'Accept-Encoding' in headers
        assert headers['Accept-Encoding'] == 'gzip, deflate, br'
        assert 'Connection' in headers
        assert headers['Connection'] == 'keep-alive'
        assert 'Upgrade-Insecure-Requests' in headers
        assert headers['Upgrade-Insecure-Requests'] == '1'
        assert 'Pragma' in headers
        assert headers['Pragma'] == 'no-cache'
        assert 'Cache-Control' in headers
        assert headers['Cache-Control'] == 'no-cache'
