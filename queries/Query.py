"""This model represents a Query in MongoDB"""

import json  # Used to turn the value (dict) to json
import zlib  # Used to compute json to an Adler-32 checksum of data

from pymodm import MongoModel, fields


def generate_id(value):
    """Generation is done through 3 steps:
        - Convert dict query to json
        - Compute json to Adler32 checksum (int)
        - Format checksum to hex for final PK id and return it
    """
    data = json.dumps(value, indent=2).encode('utf-8')
    checksum = zlib.adler32(data)
    return format(checksum, 'x')


class Query(MongoModel):
    """MongoDB model for Query

    Takes the query (dict) as parameter and generates its id based on the query
    """
    id = fields.CharField(primary_key=True)
    value = fields.CharField(required=True)

    def __init__(self, value=None):
        """Constructor for Query MongoModel, generates PK id based on value (query)

        Fields are then saved to the MongoModel
        """
        id = generate_id(value)
        super(Query, self).__init__(id=id, value=value)
