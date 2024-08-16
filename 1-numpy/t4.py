import os
import typing

import numpy as np

def print_array(arr: np.array, message: str = None):
    if message:
        print(message)
    print(arr)


def create_array():
    return np.random.randint(low=0, high=100, size=(10, 10), dtype="int8")


def save_array(
    arr: np.array,
    file_format: typing.Literal["csv", "txt", "npy", "npz"],
    file_path: str = None,
) -> str:
    if file_path is None:
        file_path = os.path.join(os.getcwd(), f"array.{file_format}")
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if file_format == "csv":
        np.savetxt(file_path, arr, delimiter=",", fmt="%s")
    elif file_format == "txt":
        np.savetxt(file_path, arr, fmt="%s")
    elif file_format == "npy":
        np.save(file_path, arr)
    elif file_format == "npz":
        np.savez(file_path, arr)
    else:
        raise ValueError(f"Invalid format {file_format}!")

    return file_path


def load_array_from_file(file_path: str) -> np.array:
    file_format = os.path.splitext(file_path)[1].lower().replace(".", "")

    if file_format == "csv":
        return np.loadtxt(file_path, delimiter=",")
    elif file_format == "txt":
        return np.loadtxt(file_path)
    elif file_format == "npy":
        return np.load(file_path)
    elif file_format == "npz":
        npz_file = np.load(file_path)
        return npz_file[npz_file.files[0]]
    else:
        raise ValueError(f"Invalid format {file_format}!")


def sum_array(arr: np.array, axis: int = None) -> np.floating:
    return np.sum(arr, axis=axis)


def mean_array_value(arr: np.array, axis: int = None) -> np.floating:
    return np.mean(arr, axis=axis)


def median_array_value(arr: np.array, axis: int = None) -> np.floating:
    return np.median(arr, axis=axis)


def std_array_value(arr: np.array, axis: int = None) -> np.floating:
    return np.std(arr, axis=axis)


def aggregate(
    arr: np.array,
    agg_function: typing.Callable[[np.array, int], np.array],
    axis: int,
) -> list[np.array]:
    return agg_function(arr, axis)


if __name__ == "__main__":
    initial_array = create_array()
    print_array(initial_array, message="Created array:")

    folder_for_files = os.path.join(os.getcwd(), "1-numpy/files")
    os.makedirs(folder_for_files, exist_ok=True)

    files_formats = {"txt", "csv", "npy", "npz"}
    save_files_paths = [
        save_array(
            arr=initial_array,
            file_format=file_format,
            file_path=os.path.join(folder_for_files, f"array.{file_format}"),
        )
        for file_format in files_formats
    ]

    print(f"Saved array to files: {save_files_paths}")

    for file_format in files_formats:
        loaded_array = load_array_from_file(
            os.path.join(folder_for_files, f"array.{file_format}")
        )
        assert loaded_array.shape == (10, 10)
        print_array(arr=loaded_array, message=f"Loaded array using {file_format=}")

    print_array(sum_array(initial_array), "Sum:")
    print_array(mean_array_value(initial_array), "Mean:")
    print_array(median_array_value(initial_array), "Median:")
    print_array(std_array_value(initial_array), "SD:")

    print_array(
        aggregate(initial_array, sum_array, axis=0),
        message="Sum by axis 0:",
    )
    print_array(
        aggregate(initial_array, mean_array_value, axis=0),
        message="Mean by axis 0:",
    )
    print_array(
        aggregate(initial_array, median_array_value, axis=0),
        message="Median by axis 0:",
    )
    print_array(
        aggregate(initial_array, std_array_value, axis=0),
        message="StdDev by axis 0:",
    )
