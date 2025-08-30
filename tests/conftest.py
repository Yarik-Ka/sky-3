import pytest


@pytest.fixture
def fixture_for_mask() -> list:
    return ["1234567890123456", "12345678901234567890", "!@#$%^&*()", "", [12, 13, 14], (12,), {}, False, "Visa"]


@pytest.fixture
def fixture_for_date() -> list:
    return ["3034-12-07", "!@#$", "Тысяча сто пятый год, 31 июля", "9889-34-67", "12.07.2025"]
@pytest.fixture
def universal_fixture() -> list:
    return ["1234567890123456", "12345678901234567890", "!@#$%^&*()", "", [12, 13, 14], (12,), {}, False, "Visa"]
