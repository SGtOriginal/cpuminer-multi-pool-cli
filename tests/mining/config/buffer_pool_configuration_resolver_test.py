import unittest

from mining.pool.config.pool_config import PoolConfiguration
from mining.pool.config.pool_config_resolver import BufferPoolConfigurationResolver


class BufferPoolConfigurationResolverTestCase(unittest.TestCase):

    def test_resolve_all_pool_configs_0(self):
        buffered_pool_configs = []
        pool_config_resolver = BufferPoolConfigurationResolver(buffered_pool_configs)

        actual_pool_configs = pool_config_resolver.resolve_all()

        self.assertListEqual(buffered_pool_configs, actual_pool_configs)

    def test_resolve_all_pool_configs_1(self):
        pool_config = PoolConfiguration('ignored')
        buffered_pool_configs = [pool_config]
        pool_config_resolver = BufferPoolConfigurationResolver(buffered_pool_configs)

        actual_pool_configs = pool_config_resolver.resolve_all()

        self.assertListEqual(buffered_pool_configs, actual_pool_configs)

    def test_resolve_all_pool_configs_n(self):
        pool_config_1 = PoolConfiguration('ignored1')
        pool_config_2 = PoolConfiguration('ignored2')
        buffered_pool_configs = [pool_config_1, pool_config_2]
        pool_config_resolver = BufferPoolConfigurationResolver(buffered_pool_configs)

        actual_pool_configs = pool_config_resolver.resolve_all()

        self.assertListEqual(buffered_pool_configs, actual_pool_configs)


if __name__ == '__main__':
    unittest.main()
