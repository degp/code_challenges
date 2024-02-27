"""
This module contains unit tests for the CalorieCounter class in the calorie_counter module.
To run these tests, use the command: python -m unittest test.py
Advent of Code 2022 - Day 1 optimized solution in Python.
"""

import itertools
import heapq
import os


class CalorieCounter:
    """
    A class used to count calories from a file.

    ...

    Attributes
    ----------
    file_path : str
        a formatted string to print out the file_path
    calories_sum : list
        a list of sums of calorie groups

    Methods
    -------
    read_and_process():
        Reads the file and processes the calorie data.
    max_group_sum():
        Returns the maximum sum of calorie groups.
    sum_of_largest_three():
        Returns the sum of the three largest calorie groups.
    """

    def __init__(self, file_path: str) -> None:
        """
        Constructs all the necessary attributes for the CalorieCounter object.

        Parameters
        ----------
            file_path : str
                file path of the calorie data
        """
        self.file_path = file_path
        self.calories_sum: list[int] = []

    def read_and_process(self) -> None:
        """
        Reads the file and processes the calorie data.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        with open(self.file_path, "r", encoding="utf-8") as file:
            calories = [int(line) if line.strip() else "" for line in file]

            self.calories_sum = [
                sum(x for x in group if isinstance(x, int))
                for is_empty, group in itertools.groupby(calories, lambda x: x == "")
                if not is_empty
            ]

    def max_group_sum(self) -> int | None:
        """
        Returns the maximum sum of calorie groups.

        Returns
        -------
        int | None
            The maximum sum of calorie groups or None if there are no groups.
        """
        return max(self.calories_sum) if self.calories_sum else None

    def sum_of_largest_three(self) -> int | None:
        """
        Returns the sum of the three largest calorie groups.

        Returns
        -------
        int | None
            The sum of the three largest calorie groups or None if there are less than three groups.
        """
        return sum(heapq.nlargest(3, self.calories_sum)) if self.calories_sum else None
