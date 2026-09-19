import re

import pytest

from app.utils import generate_short_code


@pytest.mark.parametrize("length", [6, 7, 10, 20])
def test_generate_short_code_length(length):
    assert len(generate_short_code(length)) == length

def test_generate_short_code_only_base62():
    short_code = generate_short_code()
    assert re.fullmatch("[A-Za-z0-9]+", short_code)

def test_generate_short_code_different_returns():
    short_code_one = generate_short_code()
    short_code_two = generate_short_code()
    assert short_code_one != short_code_two