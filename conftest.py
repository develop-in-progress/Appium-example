import pytest


def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='android_emulator_local',
                     help="Choose platform for tests, avaliable: android_emulator_local - be default,"
                          " android_saucelab_emulator, ios_emulator_local, ios_saucelab_emulator")


@pytest.fixture(scope="function")
def platform(request):
    """Use different desired capabilies"""
    platform = request.config.getoption("platform")
    yield platform
