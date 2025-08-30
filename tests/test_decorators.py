import pytest

from src.decorators import my_function, new_func


def test_decorator(capsys):
    my_function()
    captured = capsys.readouterr()
    assert captured.out == ""


@pytest.mark.parametrize("arg_1, arg_2, expected", [(1, 2, -1), (79, 60, 19), ("None", "None", None), ({}, [], None)])
def test_for_console_output(arg_1, arg_2, expected):
    assert new_func(arg_1, arg_2) == expected