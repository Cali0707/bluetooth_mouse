def decode_bytes(arr):
    values = []
    values.append(int.from_bytes(arr[0:3], byteorder='big'))
    values.append(int.from_bytes(arr[4:7], byteorder='big'))
    values.append(int.from_bytes(arr[8:11], byteorder='big'))
    return values
