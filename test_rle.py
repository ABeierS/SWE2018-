from rle import rle_encoder

def test_simple():
    assert rle_encoder("bbbkkka") == "b3k3a1"
def test_advanced():
    assert rle_encoder("ffffiiiiiaaa") == "f4i5a3"
def test_numbers():
    assert rle_encoder("11777599") == "12735192"
def test_moreNumbers():
    assert rle_encoder("1111111111111166") == "11462"
