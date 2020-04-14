import unittest

from mining.currency import Currency
from mining.pool.config.pool_config import PoolConfiguration, PoolCurrencyConfiguration, PoolHashAlgorithmConfiguration, \
    PoolConnectionConfiguration
from mining.pool.config.pool_connection_info_resolver import resolve_connection_info


class PoolConnectionInfoResolverTestCase(unittest.TestCase):

    pool_config = PoolConfiguration('pool1', [
        PoolCurrencyConfiguration(Currency('currency1', 'c1'), []),
        PoolCurrencyConfiguration(Currency('currency2', 'c2'), [
            PoolHashAlgorithmConfiguration('algo1', []),
            PoolHashAlgorithmConfiguration('algo2', [
                PoolConnectionConfiguration(1, 'base_url_1', 4201),
                PoolConnectionConfiguration(2, 'base_url_2', 4202),
                PoolConnectionConfiguration(None, 'base_url_3', 4203)
            ])
        ])
    ])

    def test_resolve_pool_connection_info_from_pool_config_currency_name(self):
        pool_connection_info = resolve_connection_info(self.pool_config, 'currency2', 'algo2', 2)

        self.assertEqual('pool1', pool_connection_info.pool_name)
        self.assertEqual('base_url_2', pool_connection_info.base_url)
        self.assertEqual(4202, pool_connection_info.port)

    def test_resolve_pool_connection_info_from_pool_config_currency_symbol(self):
        pool_connection_info = resolve_connection_info(self.pool_config, 'c2', 'algo2', 2)

        self.assertEqual('pool1', pool_connection_info.pool_name)
        self.assertEqual('base_url_2', pool_connection_info.base_url)
        self.assertEqual(4202, pool_connection_info.port)

    def test_resolve_pool_connection_info_from_pool_config_unknown_currency(self):
        pool_connection_info = resolve_connection_info(self.pool_config, 'c42', 'algo2', 2)

        self.assertIsNone(pool_connection_info)

    def test_resolve_pool_connection_info_from_pool_config_unknown_hash_algorithm(self):
        pool_connection_info = resolve_connection_info(self.pool_config, 'c2', 'algo42', 2)

        self.assertIsNone(pool_connection_info)

    def test_resolve_pool_connection_info_from_pool_config_c_not_none_a_not_none_d_none(self):
        # first difficulty == None else any first if not empty
        pool_connection_info = resolve_connection_info(self.pool_config, 'c2', 'algo2', None)

        self.assertEqual('pool1', pool_connection_info.pool_name)
        self.assertEqual('base_url_3', pool_connection_info.base_url)
        self.assertEqual(4203, pool_connection_info.port)

    def test_resolve_pool_connection_info_from_pool_config_c_none_a_not_none_d_not_none(self):
        pool_connection_info = resolve_connection_info(self.pool_config, None, 'algo2', 2)

        self.assertEqual('pool1', pool_connection_info.pool_name)
        self.assertEqual('base_url_2', pool_connection_info.base_url)
        self.assertEqual(4202, pool_connection_info.port)

    def test_resolve_pool_connection_info_from_pool_config_c_not_none_a_none_d_none(self):
        pool_connection_info = resolve_connection_info(self.pool_config, 'c2', None, None)

        self.assertEqual('pool1', pool_connection_info.pool_name)
        self.assertEqual('base_url_3', pool_connection_info.base_url)
        self.assertEqual(4203, pool_connection_info.port)

    def test_resolve_pool_connection_info_from_pool_config_c_none_a_not_none_d_none(self):
        pool_connection_info = resolve_connection_info(self.pool_config, None, 'algo2', None)

        self.assertEqual('pool1', pool_connection_info.pool_name)
        self.assertEqual('base_url_3', pool_connection_info.base_url)
        self.assertEqual(4203, pool_connection_info.port)

    def test_resolve_pool_connection_info_from_pool_config_c_none_a_none_d_none(self):
        # for each: any first if not empty
        pool_connection_info = resolve_connection_info(self.pool_config, None, None, None)

        self.assertEqual('pool1', pool_connection_info.pool_name)
        self.assertEqual('base_url_3', pool_connection_info.base_url)
        self.assertEqual(4203, pool_connection_info.port)


if __name__ == '__main__':
    unittest.main()
