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
        """Test the get_requirements method with a file path and freeze set to False."""
        # Create a fictitious requirements file for the test
        requirements_file = tmp_path / "requirements.txt"
        requirements_file.write_text("package1\npackage2\npackage3\n")

        # Call the get_requirements method with a file path and freeze set to False
        packages, nb_packages = utils.get_requirements(str(requirements_file), freeze=False)

        # Check that the method returns the correct packages
        assert packages == ["package1", "package2", "package3"]
        assert nb_packages == 3

    def test_get_requirements_without_path_and_freeze(self, utils, monkeypatch):
        """Test the get_requirements method without a file path and freeze set to True."""

        # Simulate the execution of 'pip freeze' to generate the list of packages
        def mock_pip_freeze(cmd):
            return "packageA\npackageB\npackageC\n"

        # Use io.StringIO to simulate reading a file
        mock_output = io.StringIO(mock_pip_freeze(""))

        # Replace os.popen with mock_output
        monkeypatch.setattr(os, "popen", lambda cmd: mock_output)

        # Call the get_requirements method without a file path and freeze set to True
        packages, nb_packages = utils.get_requirements(path=None, freeze=True)

        # Check that the method returns the correct packages
        assert packages == ["packageA", "packageB", "packageC"]
        assert nb_packages == 3

    def test_get_requirements_without_path_and_no_freeze(self, utils, monkeypatch):
        """Test the get_requirements method without a file path and freeze set to False."""
        # Call the get_requirements method without a file path and freeze set to False
        packages, nb_packages = utils.get_requirements(path=None, freeze=False)

        # Check that the method returns the correct packages
        assert packages is None
        assert nb_packages == 0

