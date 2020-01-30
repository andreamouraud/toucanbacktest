import json

from flask import jsonify, request, Blueprint, abort

from queries.controller import find_all_ids, read

queries_api = Blueprint('queries_api', __name__)


@queries_api.route("/queries", methods=['GET'])
def get_all_queries():
    """Returns all queries ids stored in MongoDB"""
    return jsonify(find_all_ids())


@queries_api.route("/query/<id>", methods=['POST'])
def get_query(id):
    """Returns the query for the given id"""
    query = read(id)
    if not query:
        abort(404)
    query = query.value.replace("'", '"')
    if request.data:
        filters = json.loads(str(request.data, encoding='utf-8'))
        for v in filters.items():  # Loop through every filter and replace by value asked
            query = query.replace('{{ ' + v[0] + ' }}', v[1])
    return query
