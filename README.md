# DiffHunter

An app with focus on normalization, equalization and database scheme migration for distributed arquitecture or micro services or multiple schemes.

# Requeriments
- [flask](https://github.com/pallets/flask)
- [sqlalchemy-dff](https://github.com/gianchub/sqlalchemy-diff)

Python >= 3.8.5
---

TODO

- Endpoint para calcular o valor de incosistencia
Request:
```http
GET /diffhunter/inconsistency
```

Response:
```json
{
	"inconsistency_value": 20.155 //example
}
```
- Endpoint para retornar a comparação entre duas bases
```json
{
	"origin": {},
	"target": {}
}
```
- Endpoint para comparar uma base modelo com multiplas
```json
{
	"origin": {},
	"targets": []
}
```
