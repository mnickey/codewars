def box_capacity(length, width, height):
    length_converted = int((length * 12) / 16)
    width_converted = int((width * 12) / 16)
    height_converted = int((height * 12) / 16)
    return int(length_converted * width_converted * height_converted)
