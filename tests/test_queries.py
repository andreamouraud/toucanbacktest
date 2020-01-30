import json

from queries.Query import generate_id
from queries.controller import create


def test_queries(client):
    """Test /queries route returns a list"""
    res = client.get('/queries')

    # Test call works
    assert res.status_code == 200

    # Test it returns a list correctly
    assert isinstance(res.json, list)


def test_new_query(client):
    """Test added queries to MongoDB are then retrievable"""
    res = client.get('/queries')
    qid = generate_id({'domain': 'test', 'key': 'value'})

    # Test generated query is not in list
    assert qid not in res.json

    # Add a query test to MongoDB
    create({'domain': 'test', 'key': 'value'})

    # Check new query is in list
    res = client.get('/queries')
    assert qid in res.json


def test_query(client):
    """Test the data retrieved is the expected one"""
    qid = generate_id({'domain': 'test', 'key': 'value'})
    res = client.post('/query/' + qid)

    # Test call works
    assert res.status_code == 200

    # Test data is the expected one
    data = json.loads(str(res.data, encoding='utf-8'))
    assert isinstance(data, dict)
    assert data['domain'] == 'test'

