import body_scheme
from application import validate_schema
from jsonschema import Draft7Validator


# def test_scheme_diff_database():
#     v = validate_schema(body_scheme.scheme_diff_database, {"o": 55})
#     print(v)
#     assert validate_schema(
#         body_scheme.scheme_diff_database,
#         {
#             "origin": {"uri": "string de conexao"},
#             "target": {"uri": "string de conexao"},
#         },
#     )

v = Draft7Validator(body_scheme.scheme_diff_database)
errors = sorted(v.iter_errors({"o": 55}), key=lambda e: e.path)

if errors:
    for error in errors:
        print(error)