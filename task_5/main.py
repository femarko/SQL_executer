from enum import unique


def func(numbers_list: list[int | float]) -> dict[str, list[int |float]]:
    unique_numbers = set(numbers_list)
    return {
        "unic_numbers_qwantity": len(unique_numbers),
        "second_grate": sorted(unique_numbers, reverse=True)[1],
        "numbers_devided_by_3": [number for number in numbers_list if number % 3 == 0]
    }

if __name__ == "__main__":
    print(func([10, 20, 30, 40, 50, 30, 20]))
    print(func([8, -20, 1, -7, 0, 1000, -2]))