"""
Test Payload
"""


import pytest
from ...scanvulnpy.modules.utils import Utils


@pytest.mark.smoke
class TestSetPayload:
    """
    Test Set Payload
    """

    def test_set_payload_valid_package_with_version(self, scanner):
        """Test the set_payload method with a valid package with version."""
        package = "requests==2.26.0"
        payload, version = scanner.set_payload(package)
        assert payload == {"version": "2.26.0", "package": {"name": "requests", "ecosystem": "PyPI"}}
        assert version == "2.26.0"

    def test_set_payload_valid_package_without_version(self, scanner):
        """Test the set_payload method with a valid package without version."""
        package = "requests"
        payload, version = scanner.set_payload(package)
        assert payload == {"package": {"name": "requests", "ecosystem": "PyPI"}}
        assert version is None

    def test_set_payload_invalid_inf_version_format(self, scanner):
        """Test the set_payload method with an invalid version format (<=)."""
        package = "requests<=2.26.0"
        payload, version = scanner.set_payload(package)
        assert payload is None
        assert version is None

    def test_set_payload_invalid_sup_version_format(self, scanner):
        """Test the set_payload method with an invalid version format (>=)."""
        package = "requests>=2.26.0"
        payload, version = scanner.set_payload(package)
        assert payload is None
        assert version is None

    def test_set_payload_package_without_alphanumeric_characters(self, scanner):
        """Test the set_payload method without alphanumeric characters."""
        package = "!@#$%^&*()_+"
        payload, version = scanner.set_payload(package)
        assert payload is None
        assert version is None

    def test_set_payload_package_with_empty_string(self, scanner):
        """Test the set_payload method with an empty string."""
        package = ""
        payload, version = scanner.set_payload(package)
        assert payload is None
        assert version is None
