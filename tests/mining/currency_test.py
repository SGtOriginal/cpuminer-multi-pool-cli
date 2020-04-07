import unittest

from mining.currency import Currency


class CurrencyTestCase(unittest.TestCase):

    def test_matches_name_same_case(self):
        currency = Currency('Bitcoin', 'BTC')
        self.assertTrue(currency.matches('Bitcoin'))

    def test_matches_name_not_same_case(self):
        currency = Currency('Bitcoin', 'BTC')
        self.assertTrue(currency.matches('bitcoin'))

    def test_matches_symbol_same_case(self):
        currency = Currency('Bitcoin', 'BTC')
        self.assertTrue(currency.matches('BTC'))

    def test_matches_symbol_not_same_case(self):
        currency = Currency('Bitcoin', 'BTC')
        self.assertTrue(currency.matches('btc'))

    def test_not_matches_name_or_symbol(self):
        currency = Currency('Bitcoin', 'BTC')
        self.assertFalse(currency.matches('Coin'))


if __name__ == '__main__':
    unittest.main()
