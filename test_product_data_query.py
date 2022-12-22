import unittest
import product_data_query

class TestProductDataQuery(unittest.TestCase):
    product_data_query = product_data_query.ProductDataQuery()
    _console = "test_console"
    
    def test_get_params(self):
        print("\nStart get_params test")

        self.product_data_query.set_console(self._console)
        params = self.product_data_query.get_params()
        self.assertEqual(
            params["cursor"],
            0
        )

        self.assertEqual(
            params["format"],
            "json"
        )

    def test_set_cursor(self):
        print("\nStart set_cursor")

        self.product_data_query.set_cursor(100)
        self.assertEqual(
            self.product_data_query.get_cursor(),
            100
        )

    def test_set_console(self):
        print("\nStart set_console test")

        self.product_data_query.set_console(self._console)

    def test_get_console(self):
        print("\nStart get_console test")

        self.product_data_query.set_console(self._console)

        self.assertEqual(
            self.product_data_query.get_console(),
            self._console
        )

    def test_get_endpoint(self):
        print("\nStart get_endpoint test")

        self.product_data_query.set_console(self._console)

        self.assertEqual(
            self.product_data_query.get_endpoint(),
            f"{self.product_data_query._base_url}/{self._console}"
        )

    def test_append_product_data(self):
        print("\nStart append_product_data test")

        self.product_data_query.append_product_data(['test'])

        product_data = self.product_data_query.get_product_data()

        self.assertEqual(
            product_data,
            ['test']
        )




if __name__ == '__main__':
    unittest.main()
