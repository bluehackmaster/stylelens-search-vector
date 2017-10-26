# coding: utf-8

"""
    stylelens-search-vector

    This is a API document for Vector search on bl-search-faiss\"

    OpenAPI spec version: 0.0.1
    Contact: bluehackmaster@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import stylelens_search_vector
from stylelens_search_vector.rest import ApiException
from stylelens_search_vector.apis.search_api import SearchApi


class TestSearchApi(unittest.TestCase):
    """ SearchApi unit test stubs """

    def setUp(self):
        self.api = stylelens_search_vector.apis.search_api.SearchApi()

    def tearDown(self):
        pass

    def test_search_vector(self):
        """
        Test case for search_vector

        Query to search vector
        """
        pass


if __name__ == '__main__':
    unittest.main()
