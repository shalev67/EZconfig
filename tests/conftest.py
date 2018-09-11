import pytest


@pytest.fixture
def config():
    from ezcfg import ezcfg
    del ezcfg
    from ezcfg.config import EZConfig
    return EZConfig()
