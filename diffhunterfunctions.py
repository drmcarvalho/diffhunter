from sqlalchemydiff.comparer import compare
from decimal import Decimal
import math

def compare_database(uri_origin, uri_target, ignores=None):
    return compare(uri_origin, uri_target, ignores=ignores)

def calculate_value_inconsistency(total_diff=0):
    return Decimal(total_diff / 100 / math.e)

def determine_value_inconsistency(diff):
    pass