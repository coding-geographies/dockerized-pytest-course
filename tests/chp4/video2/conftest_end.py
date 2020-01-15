"""
This file is for walkthrough purposes only
Normally, conftest.py file should be located directly under the "tests/" folder


Note:
Fixtures with @pytest.fixture(scope="session", autouse=True) must remain in this file
"""
pytest_plugins = [
   "tests.fixtures.cities",
   "tests.fixtures.data_processing",
]
