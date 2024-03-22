"""
This Loger
"""

import pytest
from scanvulnpy.scanvulnpy.modules.loggers import Logger


class TestLogger:
    """Test cases for Logger."""

    @pytest.mark.smoke
    def test_logger_info(self, logger, capsys):
        logger.info("This is a test message.")
        captured = capsys.readouterr()
        assert captured.out.startswith("2024")  # Check years
        assert "INFO" in captured.out
        assert "This is a test message." in captured.out

    @pytest.mark.smoke
    def test_logger_success(self, logger, capsys):
        logger.success("This is a test message.")
        captured = capsys.readouterr()
        assert captured.out.startswith("2024")  # Check years
        assert "SUCCESS" in captured.out
        assert "This is a test message." in captured.out

    @pytest.mark.smoke
    def test_logger_debug(self, logger, capsys):
        logger.debug("This is a test message.")
        captured = capsys.readouterr()
        assert captured.out.startswith("2024")  # Check years
        assert "DEBUG" in captured.out
        assert "This is a test message." in captured.out

    @pytest.mark.smoke
    def test_logger_warning(self, logger, capsys):
        logger.warning("This is a test message.")
        captured = capsys.readouterr()
        assert captured.out.startswith("2024")  # Check years
        assert "WARN" in captured.out
        assert "This is a test message." in captured.out

    @pytest.mark.smoke
    def test_logger_error(self, logger, capsys):
        logger.error("This is a test message.")
        captured = capsys.readouterr()
        assert captured.out.startswith("2024")  # Check years
        assert "ERROR" in captured.out
        assert "This is a test message." in captured.out
