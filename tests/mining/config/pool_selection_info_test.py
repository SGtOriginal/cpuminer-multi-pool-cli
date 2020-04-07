import unittest

from mining.pool.config.pool_config import PoolConfiguration
from mining.pool.config.pool_selection_info import PoolSelectionInfo
from mining.pool.config.pool_user_config import PoolUserConfiguration


class PoolSelectionInfoTestCase(unittest.TestCase):

    def test_matches_pool_config_same_case(self):
        pool_config = PoolConfiguration('foo')

        pool_selection_info = PoolSelectionInfo('foo', 'ignored', 'ignored')

        self.assertTrue(pool_selection_info.matches_pool_configuration(pool_config))

    def test_matches_pool_config_not_same_case(self):
        pool_config = PoolConfiguration('Foo')

        pool_selection_info = PoolSelectionInfo('foo', 'ignored', 'ignored')

        self.assertTrue(pool_selection_info.matches_pool_configuration(pool_config))

    def test_not_matches_pool_config(self):
        pool_config = PoolConfiguration('bar')

        pool_selection_info = PoolSelectionInfo('foo', 'ignored', 'ignored')

        self.assertFalse(pool_selection_info.matches_pool_configuration(pool_config))

    def test_matches_pool_user_config_same_case(self):
        pool_user_config = PoolUserConfiguration('foo', 'ignored', 'ignored')

        pool_selection_info = PoolSelectionInfo('foo', 'ignored', 'ignored')

        self.assertTrue(pool_selection_info.matches_pool_configuration(pool_user_config))

    def test_matches_pool_user_config_not_same_case(self):
        pool_user_config = PoolUserConfiguration('Foo', 'ignored', 'ignored')

        pool_selection_info = PoolSelectionInfo('foo', 'ignored', 'ignored')

        self.assertTrue(pool_selection_info.matches_pool_configuration(pool_user_config))

    def test_not_matches_pool_user_config(self):
        pool_user_config = PoolUserConfiguration('bar', 'ignored', 'ignored')

        pool_selection_info = PoolSelectionInfo('foo', 'ignored', 'ignored')

        self.assertFalse(pool_selection_info.matches_pool_configuration(pool_user_config))


if __name__ == '__main__':
    unittest.main()
