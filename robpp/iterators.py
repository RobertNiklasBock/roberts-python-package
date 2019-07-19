def idxrange(listlike):
    """
    Returns an iterator, that consists of tuples in the form of
    (index, element).

    Keyword arguments:
    listlike -- a list, tuple or similar object that can be iterated over
    """

    assert hasattr(arg, "__getitem__") or hasattr(arg, "__iter__"),
    "Argument is not list-like"

    return zip(range(len(listlike)), listlike)
