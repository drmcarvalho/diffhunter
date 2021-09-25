from flask import Flask, jsonify, request
from diffhunterfunctions import compare_database


def invalid_parameters():
    return {"mensagem": "parametros invalidos"}


app = Flask(__name__)


@app.route("/diffhunter/inconsistency")
def inconsistency():
    pass


@app.route("/diffhunter/inconsistency_with_multiple_databases")
def inconsistency_with_multiple_databases():
    pass


@app.route("/diffhunter/diff_database")
def diff_database():
    body = request.get_json()
    if not body:
        return jsonify(error=invalid_parameters()), 400

    compare_result = compare_database(
        body["origin"]["uri"], body["target"]["uri"], body["ignores"]
    )
    return jsonify(
        response={"diff": compare_result.errors, "match": compare_result.is_match}
    )


@app.route("/diffhunter/diff_with_multiple_databases")
def diff_with_multiple_databases():
    body = request.get_json()
    if not body:
        return jsonify(error=invalid_parameters()), 400
    result = {}
    result["diffs"] = []
    origin_database = body["origin"]["database_name"]
    targets = body["target"]["databases"]
    uri_origin = body["origin"]["uri"]
    uri_target = body["target"]["uri"]
    for target in targets:
        compare_result = compare_database(uri_origin, uri_target, body["ignores"])
        result["result"].append(
            {"diff": compare_result.errors, "match": compare_result.is_match}
        )
    return jsonify(response=result)
