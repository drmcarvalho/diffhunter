# DiffHunter

An app with focus on normalization, equalization and database scheme migration for distributed arquitecture, micro services or multiple schemes.

# Requirements
- [flask](https://github.com/pallets/flask)
- [sqlalchemy-dff](https://github.com/gianchub/sqlalchemy-diff)
- [PyMySQL](https://pypi.org/project/PyMySQL/)
- [pymssql](https://pypi.org/project/pymssql/)
- Python >= 3.8.5


# TODO

- [ ] Endpoint for calculating the inconsistency value
- [x] Endpoint for returning the comparison between two databases
- [ ] Endpoint for returning the comparison between mutiple databases
- [ ] Endpoint for differences in Tables
- [ ] Endpoint for differences in Primary Keys for a common table
- [ ] Endpoint for differences in Foreign Keys for a common table
- [ ] Endpoint for differences in Indexes for a common table
- [ ] Endpoint for differences in Columns for a common table
- [ ] Swagger for documentantion the API
