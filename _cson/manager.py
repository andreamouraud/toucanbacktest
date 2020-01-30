import cson
from speg import ParseError

from queries.controller import create_queries_from_dict


def create_queries_from_cson_file(filename):
    """Read CSON file and creates queries from it"""
    try:
        with open(filename, 'rb') as data:
            obj = cson.load(data)
            create_queries_from_dict(obj)
            return True, "Success"
    except FileNotFoundError:
        return False, f"File {filename} not found"
    except ParseError:
        return False, f"File {filename} is invalid"
