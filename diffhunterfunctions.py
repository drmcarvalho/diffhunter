from sqlalchemydiff.comparer import compare


def compare_database(uri_origin, uri_target, ignores=None):
    return compare(uri_origin, uri_target, ignores=ignores)
