# Parse float


def parse_float(string):
    try:
        return float(string)
    except (ValueError, TypeError) as e:
        return None
