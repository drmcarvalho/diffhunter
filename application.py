from flask import Flask, jsonify, request
from diffhunterfunctions import compare_database
from jsonschema import Draft7Validator
from jsonschema.exceptions import best_match
import body_scheme


def validate_schema(schema, instance):
    return best_match(Draft7Validator(schema).iter_errors(instance))


app = Flask(__name__)


@app.route("/diffhunter/inconsistency")
def inconsistency():
    pass


@app.route("/diffhunter/inconsistency_with_multiple_databases")
def inconsistency_with_multiple_databases():
    pass


@app.route("/diffhunter/diff_database")
def diff_database():
    target_uri = request.form.get("target_uri", None)
    origin_uri = request.form.get("origin_uri", None)
    if not target_uri:
        return jsonify(error={"message": "Invalid URI"})
    if not origin_uri:
        return jsonify(error={"message": "Invalid URI"})
    compare_result = compare_database(origin_uri, target_uri)
    return jsonify(response={"diff": compare_result.errors,"match": compare_result.is_match})


@app.route("/diffhunter/diff_with_multiple_databases")
def diff_with_multiple_databases():
    origin_uri = request.form.get("origin_uri", None)
    target_uri_list = request.form.getlist("target_uri_list")
    result = {}
    result["diff_list"] = []
    for target_uri in target_uri_list:
        compare_result = compare_database(origin_uri, target_uri)
        result["diff_list"].append({"diff": compare_result.errors, "match": compare_result.is_match})
    return jsonify(response=result)
