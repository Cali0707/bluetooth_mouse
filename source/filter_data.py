from scipy import signal


def initialize_filter():
    """Initializes a butterworth filter."""
    b, a = signal.butter(3, 0.05)
    zi = signal.lfilter_zi(b, a)
    return b, a, zi


def filter_data(datapoint, a, b, z):
    """Passes data into a low pass filter and returns filter state and the filtered data"""
    result, z = signal.lfilter(b, a, [datapoint], zi=z)
    return result, z


if __name__ == '__main__':
    b, a, zi = initialize_filter()
    l = [b, a, zi]
    print(l)
