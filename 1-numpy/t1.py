import numpy as np

def print_array(arr: np.array, message: str | None = None):
    if message:
        print(message)
    print(arr)

def array_creation_1() -> np.array:
    return np.arange(start=1, stop=11, dtype="int8")


def array_creation_2() -> np.array:
    return np.arange(start=1, stop=10).reshape((3, 3))


def array_indexing_and_slicing_1():
    return array_creation_1()[2]


def array_indexing_and_slicing_2():
    return array_creation_2()[:2, :2]


def basic_arithmetic_1():
    print(array_creation_1() + 5)


def basic_arithmetic_2():
    print(array_creation_2() * 2)


if __name__ == "__main__":
    array_1 = array_creation_1()
    array_2 = array_creation_2()

    print_array(array_1)
    print_array(array_1)

    print_array(array_indexing_and_slicing_1(), message="Third element of 1dim array:")
    print_array(array_indexing_and_slicing_2(), message="First two rows and columns of the 2dim array:")

    basic_arithmetic_1()
    basic_arithmetic_2()