from config_reader import validate_font_size

def test_validate_font_size():
    # Test valid font sizes
    assert validate_font_size("8") == 8
    assert validate_font_size("16") == 16
    assert validate_font_size("32") == 32

    # Test invalid font sizes (too small)
    assert validate_font_size("7") is None

    # Test invalid font sizes (too large)
    assert validate_font_size("33") is None

    # Test non-integer input
    assert validate_font_size("abc") is None
    assert validate_font_size("12.5") is None

