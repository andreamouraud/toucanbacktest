"""This controller is used to manage Query in MongoDB"""

from .Query import Query


def delete(query):
    """Deletes the Query from MongoDB

    Takes the Query or its id (str) as parameter:
    If parameter is a query, deletes it straight away
    If it is an ID, deletes it if found
    """
    if not isinstance(query, Query):
        query = read(query)
    if query:
        query.delete()


def create(query):
    """Create and saves the new Query to MongoDB without duplicating

    Takes the query (dict) as parameter
    """
    Query(query).save()


def read(id):
    """Returns the Query matching the id specified, None if not found

    Takes the id (str) as parameter
    """
    try:
        return Query.objects.get({'_id': id})
    except Query.DoesNotExist:
        return None


def find_all_ids():
    """ Returns all the Query ids stored in MongoDB """
    return [query.id for query in list(Query.objects.only("_id"))]


def create_queries_from_dict(obj):
    """Recursively loop through dict and create queries found

         - If 'query' key is found: create Query associated to value
         - If value is a dict, recursively loop through it
         - If value is a list, loop through all dicts to perform same actions
    """
    for k, v in obj.items():
        if k == 'query':  # Query to save
            create(v)
        elif isinstance(v, dict):  # Dict inside dict
            obj[k] = create_queries_from_dict(v)
        elif isinstance(v, list):  # List of dict
            for d in v:
                if isinstance(d, dict):
                    d[k] = create_queries_from_dict(d)
    return obj
