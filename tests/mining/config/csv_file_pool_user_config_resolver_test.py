import unittest

from mining.pool.config.pool_user_config import PoolUserConfiguration
from mining.pool.config.pool_user_config_resolver import CsvFilePoolUserConfigurationResolver


class CsvFilePoolUserConfigurationResolverTestCase(unittest.TestCase):

    def test_resolve_all_pool_user_configs_empty(self):
        pool_user_config_resolver = CsvFilePoolUserConfigurationResolver(
            'sample_files/sample_pool_user_config_empty.csv')

        actual_user_pool_configs = pool_user_config_resolver.resolve_all()

        self.assertListEqual([], actual_user_pool_configs)

    def test_resolve_all_pool_user_configs_0(self):
        pool_user_config_resolver = CsvFilePoolUserConfigurationResolver('sample_files/sample_pool_user_config_0.csv')

        actual_user_pool_configs = pool_user_config_resolver.resolve_all()

        self.assertListEqual([], actual_user_pool_configs)

    def test_resolve_all_pool_user_configs_1(self):
        pool_user_config_resolver = CsvFilePoolUserConfigurationResolver('sample_files/sample_pool_user_config_1.csv')

        actual_user_pool_configs = pool_user_config_resolver.resolve_all()

        self.assertListEqual([PoolUserConfiguration('foo', 'ignored', 'ignored')], actual_user_pool_configs)

    def test_resolve_all_pool_user_configs_n(self):
        pool_user_config_resolver = CsvFilePoolUserConfigurationResolver('sample_files/sample_pool_user_config_n.csv')

        actual_user_pool_configs = pool_user_config_resolver.resolve_all()

        self.assertListEqual([
            PoolUserConfiguration('foo1', 'ignored', 'ignored'),
            PoolUserConfiguration('foo2', 'ignored', 'ignored')
        ], actual_user_pool_configs)

    def test_resolve_all_pool_user_configs(self):
        pool_user_config_resolver = CsvFilePoolUserConfigurationResolver('sample_files/sample_pool_user_config.csv')

        actual_user_pool_configs = pool_user_config_resolver.resolve_all()

        self.assertListEqual([
            PoolUserConfiguration('pool1', 'ignored', 'ignored'),
            PoolUserConfiguration('pool2', 'ignored', 'ignored')
        ], actual_user_pool_configs)
        self.assertEqual('user1', actual_user_pool_configs[0].username)
        self.assertEqual('pass1', actual_user_pool_configs[0].password)
        self.assertEqual('user2', actual_user_pool_configs[1].username)
        self.assertEqual('pass2', actual_user_pool_configs[1].password)


if __name__ == '__main__':
    unittest.main()
