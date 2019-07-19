def is_max(reference, value):
    return value > reference


def is_min(reference, value):
    return value < reference


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False