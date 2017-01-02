def toJadenCase(string):
    return_value = []
    value = string.split()
    for data in value:
        return_value.append(data.capitalize())
    return_value = " ".join(return_value)
    return return_value