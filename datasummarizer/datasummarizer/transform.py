# Add the required docstring to the module
"""Perform the transform_string_to_number_list function."""

# TODO: Add an import for all of the required type annotations

# Add a suitable docstring for the transform_string_to_number_list function


def transform_string_to_number_list(data_text: str) -> List[float]:
    """Transform a string called data_text into a number to store into a list as a float."""
    # create an empty list of values called data_number_list
    data_number_list = []
    # iterate through the data_text using the splitlines function
    for line in data_text.splitlines():
    # convert every one of the text-based values to a floating-point value
        List = data_number_list.append(float(line))
    # return the list of floating-point values that represent the
    # values that were converted from a string to a float
    return List
