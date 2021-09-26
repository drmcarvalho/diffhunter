import diffhunterfunctions
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

# v = Draft7Validator(body_scheme.scheme_diff_database)
# errors = sorted(v.iter_errors({"o": 55}), key=lambda e: e.path)

# if errors:
#     for error in errors:
#         print(error)


diff = {
    "result": {
        "diff": {
            "enums": {},
            "tables": {},
            "tables_data": {
                "pessoa": {
                    "columns": {
                        "diff": [
                            {
                                "key": "nome",
                                "left": {
                                    "comment": None,
                                    "default": None,
                                    "name": "nome",
                                    "nullable": True,
                                    "type": "VARCHAR(200)"
                                },
                                "right": {
                                    "comment": None,
                                    "default": None,
                                    "name": "nome",
                                    "nullable": True,
                                    "type": "VARCHAR(100)"
                                }
                            }
                        ],
                        "left_only": [
                            {
                                "comment": None,
                                "default": None,
                                "name": "email",
                                "nullable": True,
                                "type": "VARCHAR(50)"
                            }
                        ]
                    },
                    "indexes": {
                        "left_only": [
                            {
                                "column_names": [
                                    "nome"
                                ],
                                "name": "nome",
                                "unique": False
                            }
                        ]
                    }
                }
            },
            "uris": {
                "left": "mysql+pymysql://root:@localhost/diffhuntermock2",
                "right": "mysql+pymysql://root:@localhost/diffhuntermock1"
            }
        },
        "match": False
    }
}

print(diffhunterfunctions.calculate_value_inconsistency(690))
