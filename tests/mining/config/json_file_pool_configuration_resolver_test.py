import unittest

from mining.currency import Currency
from mining.pool.config.pool_config import PoolConfiguration, PoolCurrencyConfiguration, PoolHashAlgorithmConfiguration, \
    PoolConnectionConfiguration
from mining.pool.config.pool_config_resolver import JsonFilePoolConfigurationResolver


class JsonFilePoolConfigurationResolverTestCase(unittest.TestCase):

    def test_resolve_all_pool_configs_empty(self):
        pool_config_resolver = JsonFilePoolConfigurationResolver('sample_files/sample_pool_config_empty.json')

        actual_pool_configs = pool_config_resolver.resolve_all()

        self.assertListEqual([], actual_pool_configs)

    def test_resolve_all_pool_configs_0(self):
        pool_config_resolver = JsonFilePoolConfigurationResolver('sample_files/sample_pool_config_0.json')

        actual_pool_configs = pool_config_resolver.resolve_all()

        self.assertListEqual([], actual_pool_configs)

    def test_resolve_all_pool_configs_1(self):
        pool_config_resolver = JsonFilePoolConfigurationResolver('sample_files/sample_pool_config_1.json')

        actual_pool_configs = pool_config_resolver.resolve_all()

        self.assertListEqual([PoolConfiguration('foo')], actual_pool_configs)

    def test_resolve_all_pool_configs_n(self):
        pool_config_resolver = JsonFilePoolConfigurationResolver('sample_files/sample_pool_config_n.json')

        actual_pool_configs = pool_config_resolver.resolve_all()

        self.assertListEqual([PoolConfiguration('foo1'), PoolConfiguration('foo2')], actual_pool_configs)

    def test_resolve_all_pool_configs(self):
        pool_config_resolver = JsonFilePoolConfigurationResolver('sample_files/sample_pool_config.json')

        actual_pool_configs = pool_config_resolver.resolve_all()

        pool_config_1 = PoolConfiguration('pool1')
        pool_config_2 = PoolConfiguration('pool2')
        pool_config_3 = PoolConfiguration('pool3')
        self.assertListEqual([
            pool_config_1,
            pool_config_2,
            pool_config_3
        ], actual_pool_configs)
        currency_config_1 = PoolCurrencyConfiguration(Currency('currency1', 'c1'))
        currency_config_2 = PoolCurrencyConfiguration(Currency('currency2', 'c2'))
        currency_config_3 = PoolCurrencyConfiguration(Currency('currency3', 'c3'))
        self.assertListEqual([
            currency_config_1,
            currency_config_2,
            currency_config_3
        ], actual_pool_configs[0].currency_configs)
        hash_algorithm_config_1 = PoolHashAlgorithmConfiguration('algo1')
        hash_algorithm_config_2 = PoolHashAlgorithmConfiguration('algo2')
        hash_algorithm_config_3 = PoolHashAlgorithmConfiguration('algo3')
        self.assertListEqual([
            hash_algorithm_config_1,
            hash_algorithm_config_2,
            hash_algorithm_config_3
        ], actual_pool_configs[0].currency_configs[0].hash_algorithm_configs)
        connection_config_1 = PoolConnectionConfiguration(1, 'pool.1', 4201)
        connection_config_2 = PoolConnectionConfiguration(2, 'pool.1', 4202)
        connection_config_3 = PoolConnectionConfiguration(3, 'pool.1', 4203)
        self.assertListEqual([
            connection_config_1,
            connection_config_2,
            connection_config_3
        ], actual_pool_configs[0].currency_configs[0].hash_algorithm_configs[0].connection_configs)


if __name__ == '__main__':
    unittest.main()
