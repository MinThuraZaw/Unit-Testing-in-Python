import pytest
from pytest import raises
from unittest.mock import MagicMock
from LineReader import read_from_file


# def test_can_read_from_file():
#     read_from_file('file')

@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value='test line')
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr('builtins.open', mock_open)
    return mock_open


#test - can call read_from_file
#test - return correct string
def test_return_correct_string(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr('os.path.exists', mock_exists)

    result = read_from_file('testing')
    mock_open.assert_called_once_with('testing', 'r')
    assert result == 'test line'


#test - throw exception when filename doesn't exist
def test_throw_exception_with_bad_file(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr('os.path.exists', mock_exists)

    with raises(Exception):
        result = read_from_file('testing')

