import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--base_url",
        default="https://ya.ru",
        help="domain"
    )

    parser.addoption(
        "--status_code",
        default = 200,
        help="status"
    )

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
