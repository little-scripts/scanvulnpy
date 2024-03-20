"""
Test Requirements
"""

import os
import io
import pytest
from scanvulnpy.scanvulnpy.modules.utils import Utils

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
