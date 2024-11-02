#!/usr/bin/env python3
"""Utils Test"""
import unittest
import utils
import parameterized
from unittest.mock import patch, Mock

class TestAcessNestedMap(unittest.TestCase):
    '''
    '''
    @parameterized.parameterized.expand([
        ({"a": 1}, ("a",), 1), # nested_map , path,  expected
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        '''
        '''
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)
    
    @parameterized.parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''
        '''
        with self.assertRaises(KeyError) as error_handler:
            utils.access_nested_map(nested_map, path)
        self.assertEqual(str(error_handler.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    '''
    '''
    
    @parameterized.parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io",{"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url,  test_payload, mock_get):
        '''
        '''
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = utils.get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)

class TestClass:
    def a_method(self):
        return 42
    
    @utils.memoize
    def a_property(self):
        return self.a_method()


class TestMemoize(unittest.TestCase):
    '''
    Testing Memoization.
    '''
    def test_memoize(self):
        instance = TestClass()

        with patch.object(instance, 'a_method', return_value=42) as mock_method:
            result1 = instance.a_property
            result2 = instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()
            ''''''