def invert(dct, key, data):
    if isinstance(dct.get(data), (tuple, list, set)):
        dct.get(data).append(key)
    else:
        dct[data] = [key]


def inv(source_dict):
    res = {}
    if len(source_dict) == 0:
        return None
    for x in source_dict.keys():
        invert(res, x, source_dict.get(x))
    return res
