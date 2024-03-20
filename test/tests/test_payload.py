"""
Test Payload
"""

import os
import io
import pytest
from scanvulnpy.scanvulnpy.modules.utils import Utils

@pytest.mark.smoke
class TestSetPayload:
    """
    Test Set Payload
    """

    def test_set_payload_valid_package_with_version(self, utils):
        """ Test de la méthode set_payload avec package valide avec version
        """
        package = "requests==2.26.0"
        payload, version = utils.set_payload(package)
        expected_payload = {"version": "2.26.0", "package": {"name": "requests", "ecosystem": "PyPI"}}
        assert payload == expected_payload
        assert version == "2.26.0"

    def test_set_payload_valid_package_without_version(self, utils):
        """ Test de la méthode set_payload avec package valide sans version
        """
        package = "requests"
        payload, version = utils.set_payload(package)
        expected_payload = {"package": {"name": "requests", "ecosystem": "PyPI"}}
        assert payload == expected_payload
        assert version is None

    def test_set_payload_invalid_version_format(self, utils):
        """ Test de la méthode set_payload avec un format de version invalide (<=)
        """
        package = "requests<=2.26.0"
        payload, version = utils.set_payload(package)
        assert payload is None
        assert version is None

    def test_set_payload_package_without_alphanumeric_characters(self, utils):
        """ Test de la méthode set_payload sans caractères alphanumerique
        """
        package = "!@#$%^&*()_+"
        payload, version = utils.set_payload(package)
        assert payload is None
        assert version is None

    def test_set_payload_package_with_invalid_version_format(self, utils):
        """ Test de la méthode set_payload avec un format de version invalide (>=)
        """
        package = "requests>=2.26.0"
        payload, version = utils.set_payload(package)
        assert payload is None
        assert version is None

    def test_set_payload_package_with_empty_string(self, utils):
        """ Test de la méthode set_payload avec une ligne vide
        """
        package = ""
        payload, version = utils.set_payload(package)
        assert payload is None
        assert version is None
