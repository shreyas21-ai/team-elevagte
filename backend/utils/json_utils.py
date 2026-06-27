from datetime import date, datetime, time
from decimal import Decimal


def serialize_value(value):
    if isinstance(value, (date, datetime, time)):
        return value.isoformat()

    if isinstance(value, Decimal):
        return float(value)

    return value


def serialize_row(row):
    return {key: serialize_value(value) for key, value in row.items()}


def serialize_rows(rows):
    return [serialize_row(row) for row in rows]
