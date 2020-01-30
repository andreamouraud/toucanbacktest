from _cson.manager import create_queries_from_cson_file


def test_valid_cson(client):
    """Test fetching queries on a valid cson file"""
    assert create_queries_from_cson_file('config.cson')[0]


def test_invalid_cson(client):
    """Test fetching queries on a invalid cson file"""
    assert not create_queries_from_cson_file('invalid_config.cson')[0]



