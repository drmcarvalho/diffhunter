from sqlalchemydiff.comparer import compare
from decimal import Decimal
import math
import sqlalchemy as sql
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


def compare_database(uri_origin, uri_target, ignores=None):
    return compare(uri_origin, uri_target, ignores=ignores)

def calculate_value_inconsistency(total_diff=0):
    return Decimal(total_diff / 100 / math.e)

def determine_value_inconsistency(diff):
    pass

def try_connect(uri):
    try:
        database = sql.create_engine(uri)
        database.connect()
        database.execute('select 1;')
        return True
    except OperationalError:
        return False
