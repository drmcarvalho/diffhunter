import simplejson as json
from flask import Flask, jsonify, request
from diffhunterfunctions import compare_database, try_connect, determine_value_inconsistency


api = Flask(__name__)


def error_body():
    target_uri = request.form.getlist("target_uri_left", None)
    origin_uri = request.form.get("origin_uri_right", None)
    if not target_uri:
        return jsonify(error={"message": "Invalid URI"}), 400
    if not origin_uri:
        return jsonify(error={"message": "Invalid URI"}), 400        
    if not try_connect(origin_uri):
        return jsonify(error={"message": "Could not connect to origin database"}), 400
    for target in target_uri:
        if not try_connect(target):
            return jsonify(error={"message": "Could not connect to target database"}), 400
    return False


@api.route("/diffhunter/inconsistency", methods=['POST'])
def inconsistency():
    error = error_body()
    if error:
        return error

    target_uri = request.form.get("target_uri_left")
    origin_uri = request.form.get("origin_uri_right")
    compare_result = compare_database(origin_uri, target_uri)
    inconsistency_value = determine_value_inconsistency(compare_result.errors)
    return jsonify(result={'inconsistency_value': json.dumps(inconsistency_value, use_decimal=True)})


@api.route("/diffhunter/inconsistency_with_multiple_databases")
def inconsistency_with_multiple_databases():
    pass


@api.route("/diffhunter/diff_database", methods=['post'])
def diff_database():    
    error = error_body()
    if error:
        return error
    target_uri = request.form.getlist("target_uri_left")
    origin_uri = request.form.get("origin_uri_right")
    result = {}
    result["diff_list"] = []
    for target in target_uri:
        compare_result = compare_database(origin_uri, target)
        result["diff_list"].append({"diff": compare_result.errors, "match": compare_result.is_match})
    return jsonify(result=result)    
