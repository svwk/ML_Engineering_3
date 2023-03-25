import pytest

from unittest.mock import Mock

from utils import Utils


def test_generate_text_with_exception():
    generator = Utils()
    generator_mock = Mock(side_effect=Exception)
    generator.generator = generator_mock

    a = generator.generate_text("", 1)
    assert "Message" in a.keys()
    assert a.get("Message").startswith('Parameters are not valid')


def test_wrong_length():
    generator = Utils()
    generator_mock = Mock(side_effect=Exception)
    generator.generator = generator_mock

    a = generator.generate_text("", -1)
    assert "Message" in a.keys()
    assert a.get("Message").startswith('Length is not valid')


@pytest.mark.parametrize(
    ('text', 'text_len', 'expected'),
    [("", 100, "Ok"),
     ("Ok", 50, "Ok")]
)
def test_generate_text_with_mock(text, text_len, expected):
    generator = Utils()
    v = [{'generated_text': expected}, ]
    generator_mock = Mock(return_value=v)
    generator.generator = generator_mock

    assert generator.generate_text(text, text_len) == {
        'generated_text': expected
    }
    generator_mock.assert_called_once_with(text, max_length=text_len)


@pytest.mark.parametrize(
    ('x', 'y', 'summa'),
    [(1, 2, 3),
     (4, 5, 9)]
)
def test_add(x, y, summa):
    generator = Utils()
    assert generator.add(x, y) == summa
