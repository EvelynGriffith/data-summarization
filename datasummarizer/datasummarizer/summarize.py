# Add the required docstring to the module
"""Summarize the data through a compute mean function."""

# add an import for all of the required type annotations
from typing import float
from typing import List

# Add a suitable docstring for the compute_mean function

def compute_mean(numbers: List[float]) -> float:
    """Compute the mean for a list called numbers which contains floats."""
    # sum the list of the numbers
    Sum = sum(numbers)
    # determine the length of the list of numbers
    Size = len(numbers)
    # as long as the computation will not be an
    # undefined division by zero, compute the mean
    for i in numbers:
        if i in numbers is not 0:
            mean = Sum/Size
            return mean
    # https://stackoverflow.com/questions/58400652/average-returning-a-value-even-when-list-is-empty
    # if the list was empty, then return a mean that is "not a number"
        else:
            if i is not None:
                return "The mean is not a number."
    # https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values
