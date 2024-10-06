from twttr import shorten

def test_shorten():
    assert shorten("hussain") == "hssn"
    assert shorten("hussain ,akram") == "hssn ,krm"
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("hello00") == "hll00"
    assert shorten("public") == "pblc"
    assert shorten("HELLO.") == "HLL."
    assert shorten("PUBLIC") == "PBLC"
    assert shorten("PUBLI'C") == "PBL'C"

