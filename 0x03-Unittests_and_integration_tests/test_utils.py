#!/usr/bin/env python3
"""
Tests utils.
"""
import unittest
from parameterized import parameterized  # Ensure this is installed
from utils import access_nested_map  # Import the function you are testing


class TestAccessNestedMap(unittest.TestCase):
    """Test the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function with parameterized inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
