def data_reverse(data):
    dataCopy = data[:]
    result = []

    while dataCopy:
        result.extend(dataCopy[-8:])
        dataCopy = dataCopy[:-8]

    return result