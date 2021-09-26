from flask import Flask, jsonify, request
from diffhunterfunctions import compare_database, try_connect


app = Flask(__name__)


@app.route("/diffhunter/inconsistency")
def inconsistency():
    pass


@app.route("/diffhunter/inconsistency_with_multiple_databases")
def inconsistency_with_multiple_databases():
    pass


@app.route("/diffhunter/diff_database", methods=['post'])
def diff_database():
    target_uri = request.form.get("target_uri_left", None)
    origin_uri = request.form.get("origin_uri_right", None)
    if not target_uri:
        return jsonify(error={"message": "Invalid URI"}), 400
    if not origin_uri:
        return jsonify(error={"message": "Invalid URI"}), 400
    if not try_connect(target_uri):
        return jsonify(error={"message": "Could not connect to target database"}), 400
    if not try_connect(origin_uri):
        return jsonify(error={"message": "Could not connect to origin database"}), 400        
    compare_result = compare_database(origin_uri, target_uri)
    return jsonify(result={"diff": compare_result.errors,"match": compare_result.is_match}), 200


@app.route("/diffhunter/diff_with_multiple_databases")
def diff_with_multiple_databases():
    origin_uri = request.form.get("origin_uri", None)
    target_uri_list = request.form.getlist("target_uri", None)
    if not target_uri_list:
        return jsonify(error={"message": "Invalid URI"}), 400
    if not origin_uri:
        return jsonify(error={"message": "Invalid list URI"}), 400
    result = {}
    result["diff_list"] = []
    for target_uri in target_uri_list:
        compare_result = compare_database(origin_uri, target_uri)
        result["diff_list"].append({"diff": compare_result.errors, "match": compare_result.is_match})
    return jsonify(result=result)


with app.test_request_context():
    l = request.form.getlist('lista', None)
    print(l)


@app.route('/test', methods=['post'])
def test():
    l = request.form.getlist('lista', None)
    print(l)
    return jsonify(test='test') 
