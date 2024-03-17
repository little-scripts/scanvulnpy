"""
Test Utils
"""

import os
import io
import pytest
from scanvulnpy.scanvulnpy.modules.utils import Utils


@pytest.mark.smoke
class TestPlatform:
    """
    Test Platform
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
        assert utils.check_platform() is False


@pytest.mark.smoke
class TestGetRequirements:
    """
    Test Get Requirements
    """

    def test_get_requirements_with_path_and_no_freeze(self, utils, tmp_path):
        """ Test de la méthode get_requirements avec un chemin de fichier et freeze à False
        """
        # Créez un fichier de requirements fictif pour le test
        requirements_file = tmp_path / "requirements.txt"
        requirements_file.write_text("package1\npackage2\npackage3\n")

        # Appelez la méthode get_requirements avec un chemin de fichier et freeze à False
        packages, nb_packages = utils.get_requirements(str(requirements_file), freeze=False)

        # Vérifiez que la méthode retourne les packages corrects
        assert packages == ["package1", "package2", "package3"]
        assert nb_packages == 3

    def test_get_requirements_without_path_and_freeze(self, utils, monkeypatch):
        """ Test de la méthode get_requirements sans chemin de fichier et freeze à True
        """

        # Simulez l'exécution de 'pip freeze' pour générer la liste des packages
        def mock_pip_freeze(cmd):
            return "packageA\npackageB\npackageC\n"

        # Utilisez io.StringIO pour simuler la lecture d'un fichier
        mock_output = io.StringIO(mock_pip_freeze(""))

        # Remplacez os.popen par le mock_output
        monkeypatch.setattr(os, "popen", lambda cmd: mock_output)

        # Appelez la méthode get_requirements sans chemin de fichier et freeze à True
        packages, nb_packages = utils.get_requirements(path=None, freeze=True)

        # Vérifiez que la méthode retourne les packages corrects
        assert packages == ["packageA", "packageB", "packageC"]
        assert nb_packages == 3

    def test_get_requirements_with_invalid_path(self, utils):
        """ Test de la méthode get_requirements avec un chemin de fichier invalide
        """
        # Appelez la méthode get_requirements avec un chemin de fichier invalide
        packages, nb_packages = utils.get_requirements(path="invalid/path", freeze=False)

        # Vérifiez que la méthode génère une erreur et affiche un message d'erreur approprié
        assert packages is None
        assert nb_packages == 0


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
