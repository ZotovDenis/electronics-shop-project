import pytest

from src.keyboard import KeyBoard


@pytest.fixture
def keyboard():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_str(keyboard):
    assert str(keyboard) == "Dark Project KD87A"


def test_language(keyboard):
    assert str(keyboard.language) == "EN"


def test_change_lang(keyboard):
    assert str(keyboard.language) == "EN"
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "RU"
