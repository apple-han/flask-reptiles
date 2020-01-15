import random


def generate_code():
    slice = []
    for i in range(10):
        slice.append(str(i))
    return "".join(random.sample(slice, 6))
