"""
Configuration / Settings pytest
"""

import pytest
from scanvulnpy.scanvulnpy.modules.utils import Utils

# ----------------------------------------------------------------
# Parser
# ----------------------------------------------------------------
def pytest_addoption(parser):
    """
    Parser.
    """
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests (e.g., dev, stage, prod)")


# ----------------------------------------------------------------
# Fixtures
# ----------------------------------------------------------------
@pytest.fixture(scope="session")
def environment(request):
    """
    Fixture environment.
    """
    return request.config.getoption("--env")

@pytest.fixture(scope="function")
def utils():
    """
    Fixture platform.
    """
    return Utils()