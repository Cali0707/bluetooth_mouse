def accel_to_position(a, dt):
    return float((a * (dt ** 2)) / 2)


if __name__ == '__main__':
    a = 0
    v = 0
    dt = 0.1
    print(accel_to_position(a, dt))
