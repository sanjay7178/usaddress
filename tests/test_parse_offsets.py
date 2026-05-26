from usaddress import parse


def test_parse_offsets_single_address():
    address = "123 Main St."
    parsed = parse(address)

    assert [token for token, _, _, _ in parsed] == ["123", "Main", "St."]
    for token, _, start, end in parsed:
        assert address[start:end] == token


def test_parse_offsets_multiple_addresses():
    address = "123 Main St.; 500 Oak St."
    parsed = parse(address)

    tokens = [token for token, _, _, _ in parsed]
    assert tokens[:3] == ["123", "Main", "St."]
    assert "500" in tokens

    for token, _, start, end in parsed:
        assert address[start:end] == token

    token_500 = next(item for item in parsed if item[0] == "500")
    assert token_500[2] == address.index("500")
