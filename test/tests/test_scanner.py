"""
Test Scanner
"""

import pytest
import requests
import requests_mock  # Import requests_mock to mock HTTP requests


@pytest.mark.smoke
class TestScanner:
    """
    Test Scanner
    """

    def test_request_api_osv_success(self, scanner):
        """Test case for successful API request."""
        # Define test data
        payload = ({'key': 'value'}, '1.0.0')
        headers = {'Content-Type': 'application/json'}

        # Use requests_mock to simulate the POST request response
        with requests_mock.Mocker() as mock:
            # Configure the mock to return a successful response
            mock.post(scanner.url, json={'status': 'success'}, headers=headers)

            # Call the method under test with the test data
            response = scanner.request_api_osv(payload=payload, header=headers)

            # Verify that the response matches the expected result
            assert response.status_code == 200

    def test_request_api_osv_timeout(self, scanner):
        """Test case for API request timeout."""
        # Define test data
        payload = ({'key': 'value'}, '1.0.0')
        headers = {'Content-Type': 'application/json'}

        # Use requests_mock to simulate a timeout exception
        with requests_mock.Mocker() as mock:
            # Configure the mock to raise a timeout exception
            mock.post(scanner.url, exc=requests.exceptions.Timeout)

            # Call the method under test with the test data and capture the exception
            with pytest.raises(requests.exceptions.Timeout):
                scanner.request_api_osv(payload=payload, header=headers)
