import pytest


@pytest.mark.usefixtures("initialize_driver")
class BaseTest:
    """Базовый тестовый класс"""
    pass
