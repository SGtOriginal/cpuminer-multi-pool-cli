import unittest

from mining.pool.config.pool_user_config import PoolUserConfiguration
from mining.pool.config.pool_user_config_resolver import BufferPoolUserConfigurationResolver


class BufferPoolUserConfigurationResolverTestCase(unittest.TestCase):

    def test_resolve_all_pool_user_configs_0(self):
        buffered_pool_user_configs = []
        pool_user_config_resolver = BufferPoolUserConfigurationResolver(buffered_pool_user_configs)

        actual_user_pool_configs = pool_user_config_resolver.resolve_all()

        self.assertListEqual(buffered_pool_user_configs, actual_user_pool_configs)

    def test_resolve_all_pool_user_configs_1(self):
        pool_user_config = PoolUserConfiguration('foo', 'ignored', 'ignored')
        buffered_pool_user_configs = [pool_user_config]
        pool_user_config_resolver = BufferPoolUserConfigurationResolver(buffered_pool_user_configs)

        actual_user_pool_configs = pool_user_config_resolver.resolve_all()

        self.assertListEqual(buffered_pool_user_configs, actual_user_pool_configs)

    def test_resolve_all_pool_user_configs_n(self):
        pool_user_config_1 = PoolUserConfiguration('foo1', 'ignored', 'ignored')
        pool_user_config_2 = PoolUserConfiguration('foo2', 'ignored', 'ignored')
        buffered_pool_user_configs = [pool_user_config_1, pool_user_config_2]
        pool_user_config_resolver = BufferPoolUserConfigurationResolver(buffered_pool_user_configs)

        actual_user_pool_configs = pool_user_config_resolver.resolve_all()

        self.assertListEqual(buffered_pool_user_configs, actual_user_pool_configs)


if __name__ == '__main__':
    unittest.main()
