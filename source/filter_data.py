from scipy import signal


def initialize_filter():
    b, a = signal.butter(3, 0.05)
    zi = signal.lfilter_zi(b, a)
    # print(zi)
    return b, a, zi


def filter_data(datapoint, a, b, z):
    result, z = signal.lfilter(b, a, [datapoint], zi=z)
    return result, z


if __name__ == '__main__':
    b, a, zi = initialize_filter()
    l = [b, a, zi]
    print(l)
