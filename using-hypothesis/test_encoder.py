import encoder
from hypothesis import given, example
from hypothesis.strategies import text


@given(text())
@example('')
def test_decode_inverts_encode(s):
    assert encoder.decode(encoder.encode(s)) == s
