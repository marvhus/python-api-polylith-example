data = {
    "a": [1, 2, 3],
    "b": [4, 5, 6],
    "c": [7, 8, 9],
}

# imagine that this calls out to some other API
def retrieve_some_data(key: str) -> None|list:
    if key not in data:
        return None

    return data[key]
