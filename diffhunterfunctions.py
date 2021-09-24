from sqlalchemydiff.comparer import compare


def to_uri(user, password, database, host, port, client_name, driver_name=None):    
    if driver_name:
        return f'{client_name}+{driver_name}://{user}:{password}@{host}/{database}'
    return f'{client_name}://{user}:{password}@{host}/{database}'


def compare_database(uri_origin, url_target, ignores=None):
    return compare(uri_origin, url_target, ignores=ignores)
