from flask import Flask, jsonify, request
from diffhunterfunctions import compare_database


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
        return jsonify(error={"mensagem": "parametros invalidos"}), 400

    result = compare_database(body["origin"]["uri"], body["target"]["uri"], body['ignores'])
    return jsonify(response={"diff": result.errors, "match": result.is_match})


@app.route("/diffhunter/diff_with_multiple_databases")
def diff_with_multiple_databases():
    pass
