import pytest

from src.decorators import log, func


def test_log(capsys):
    func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == 'my_function ok\n'