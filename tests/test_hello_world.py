from unittest.mock import MagicMock

import pytest

from hello_world.hello_world import print_hello_world


def test_hello_world(monkeypatch: pytest.MonkeyPatch) -> None:
    print_mock = MagicMock()
    monkeypatch.setattr("builtins.print", print_mock)
    print_hello_world()
    print_mock.assert_called_with("Hello world!")
