import pytest
from military_call.app import create_app

@pytest.fixture(scope="module")
def app():
    """
        Instance of Main Flask app
    """
    return create_app()


## para chamar pytest tests/ --fixtures
