import pytest

from app import main

app = main()

@pytest.fixture()
def client():
    with app.test_client() as c:
        yield c
