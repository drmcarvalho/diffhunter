import diffhunterfunctions

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

diff_empty = {
    "result": {
        "diff": {},
        "match": True
    }
}

print(len(diff_empty['result']['diff'].keys()))
print(len(diff['result']['diff'].keys()))

print(diffhunterfunctions.calculate_value_inconsistency(5))
