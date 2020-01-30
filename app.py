import os
from sys import stderr

import pytest
from flask import Flask
from pymodm import connect

from queries.Query import Query
from queries.api import queries_api
from _cson.manager import create_queries_from_cson_file

MONGO_URI = "mongodb://localhost:27017/backtechtest"
CSON = "config.cson"


def main():
    """App entry point

            - Starts MongoDB connection
            - Load queries from config file
            - Run server
        """
    # Register connection to MongoDB
    mongo_uri = os.getenv('mongo_uri', MONGO_URI)
    connect(mongo_uri)

    # Run Flask dev server
    app = Flask(__name__)
    app.register_blueprint(queries_api)
    app.run()
    return app


if __name__ == "__main__":
    main()

    # Create queries from .cson file, log to stderr if any error
    cson = os.getenv('cson', CSON)

    ret = create_queries_from_cson_file(cson)
    if not ret[0]:
        print(ret[1], file=stderr)

