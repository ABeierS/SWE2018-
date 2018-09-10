from rle import rle_encoder
from rle import rle_decoder

def test_simpel():
	assert rle_encoder("lllppp") == "l3p3"

def test_simple_t():
	txt_in = "bbbbkkk"
	txt_out = "b4k3"
	assert rle_encoder(txt_in) == txt_out
	assert rle_decoder(txt_out) == txt_in

def test_advanced_t():
	txt_in = "bbbbkkk555"
	txt_out = "b4k353"
	assert rle_encoder(txt_in) == txt_out
	assert rle_decoder(txt_out) == txt_in
	